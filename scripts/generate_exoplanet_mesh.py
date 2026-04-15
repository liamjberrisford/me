#!/usr/bin/env python3
"""Generate a stylised exoplanet hero asset for the Isambard-3 project.

The site is wired to use these filenames:
- _static/images/exoplanet_mesh.png
- _static/images/exoplanet_mesh.webp
- _static/videos/exoplanet_mesh.mp4
- _static/videos/exoplanet_mesh-h265.mp4

This script rebuilds that asset set from procedurally generated SVG frames using
only the Python standard library plus the locally available `magick` and
`ffmpeg` binaries.
"""

from __future__ import annotations

import argparse
import math
import random
import shutil
import subprocess
import tempfile
from pathlib import Path

WIDTH = 2688
HEIGHT = 672
FPS = 12
FRAMES = 84
PLANET_RADIUS = 248
PLANET_CENTER = (910, 338)
SURFACE_SUBDIVISIONS = 52


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mix(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def mix_rgb(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return (
        int(round(mix(a[0], b[0], t))),
        int(round(mix(a[1], b[1], t))),
        int(round(mix(a[2], b[2], t))),
    )


def smoothstep(edge0: float, edge1: float, x: float) -> float:
    if edge0 == edge1:
        return 0.0
    t = clamp((x - edge0) / (edge1 - edge0))
    return t * t * (3.0 - 2.0 * t)


def scale_rgb(rgb: tuple[int, int, int], factor: float) -> tuple[int, int, int]:
    return tuple(int(round(clamp(channel / 255.0 * factor) * 255.0)) for channel in rgb)


def rgb_hex(rgb: tuple[int, int, int]) -> str:
    return "#%02x%02x%02x" % rgb


def wrap_angle(angle: float) -> float:
    return (angle + math.pi) % (2 * math.pi) - math.pi


def normalize(point: tuple[float, float, float]) -> tuple[float, float, float]:
    x, y, z = point
    mag = math.sqrt(x * x + y * y + z * z)
    return (x / mag, y / mag, z / mag)


def dot(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def rotate_point(
    point: tuple[float, float, float],
    yaw: float,
    pitch: float,
    roll: float,
) -> tuple[float, float, float]:
    x, y, z = point

    cos_yaw = math.cos(yaw)
    sin_yaw = math.sin(yaw)
    x, z = x * cos_yaw + z * sin_yaw, -x * sin_yaw + z * cos_yaw

    cos_pitch = math.cos(pitch)
    sin_pitch = math.sin(pitch)
    y, z = y * cos_pitch - z * sin_pitch, y * sin_pitch + z * cos_pitch

    cos_roll = math.cos(roll)
    sin_roll = math.sin(roll)
    x, y = x * cos_roll - y * sin_roll, x * sin_roll + y * cos_roll

    return (x, y, z)


def project(point: tuple[float, float, float], center_x: float, center_y: float, radius: float) -> tuple[float, float]:
    x, y, _ = point
    return (center_x + x * radius, center_y - y * radius)


def cube_to_sphere(face: str, u: float, v: float) -> tuple[float, float, float]:
    if face == "px":
        point = (1.0, v, -u)
    elif face == "nx":
        point = (-1.0, v, u)
    elif face == "py":
        point = (u, 1.0, -v)
    elif face == "ny":
        point = (u, -1.0, v)
    elif face == "pz":
        point = (u, v, 1.0)
    elif face == "nz":
        point = (-u, v, -1.0)
    else:
        raise ValueError(f"Unknown face {face}")
    return normalize(point)


def cubic_point(
    p0: tuple[float, float],
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    t: float,
) -> tuple[float, float]:
    mt = 1.0 - t
    x = (mt ** 3) * p0[0] + 3 * (mt ** 2) * t * p1[0] + 3 * mt * (t ** 2) * p2[0] + (t ** 3) * p3[0]
    y = (mt ** 3) * p0[1] + 3 * (mt ** 2) * t * p1[1] + 3 * mt * (t ** 2) * p2[1] + (t ** 3) * p3[1]
    return (x, y)


def build_stars(width: int, height: int) -> list[tuple[float, float, float, tuple[int, int, int], float]]:
    rng = random.Random(17)
    stars = []
    for _ in range(220):
        x = rng.uniform(0, width)
        y = rng.uniform(0, height)
        if 610 < x < 1230 and 70 < y < 610 and rng.random() < 0.72:
            continue
        size = rng.uniform(0.55, 2.1)
        color = rng.choice([(176, 227, 255), (252, 224, 192), (211, 240, 255)])
        opacity = rng.uniform(0.18, 0.82)
        stars.append((x, y, size, color, opacity))
    return stars


def earth_components(normal: tuple[float, float, float], phase: float) -> dict[str, float]:
    x, y, z = normal
    lat = math.asin(clamp(y, -1.0, 1.0))
    lon = math.atan2(z, x)
    continent_field = (
        0.58 * math.sin(1.18 * lon + 0.44 * math.sin(2.4 * lat + 0.12 * phase))
        + 0.29 * math.cos(2.36 * lon - 1.55 * lat)
        + 0.18 * math.sin(4.9 * lon + 3.2 * lat + 0.14 * phase)
        + 0.11 * math.cos(7.4 * lon - 5.4 * lat - 0.11 * phase)
    )
    land = smoothstep(0.10, 0.30, continent_field)
    humidity = clamp(
        0.52
        + 0.22 * math.sin(2.2 * lon + 3.3 * lat - 0.22 * phase)
        + 0.17 * math.cos(5.8 * lat)
        + 0.08 * math.sin(7.8 * lon - 1.8 * lat)
    )
    mountain = land * smoothstep(
        0.48,
        0.84,
        0.5
        + 0.5 * math.sin(6.2 * lon - 2.5 * lat + 0.08 * phase)
        + 0.16 * math.cos(9.1 * lon + 3.4 * lat),
    )
    desert_band = smoothstep(0.18, 0.58, math.cos(2.3 * lat) - 0.2 * humidity + 0.08 * math.sin(1.7 * lon))
    desert = land * desert_band * (1.0 - humidity)
    vegetation = land * humidity * (1.0 - smoothstep(0.62, 1.18, abs(lat)))
    ice = smoothstep(0.94, 1.20, abs(lat) + 0.12 * mountain - 0.05 * humidity)

    cloud_field = (
        0.48
        + 0.21 * math.sin(4.2 * lon + 2.6 * lat - 0.34 * phase)
        + 0.15 * math.cos(8.8 * lat)
        + 0.10 * math.sin(10.8 * lon - 4.9 * lat + 0.26 * phase)
        + 0.08 * math.cos(13.0 * lon + 1.8 * lat)
    )
    cloud = smoothstep(0.50, 0.82, cloud_field + 0.16 * ice + 0.08 * humidity)
    coast_distance = abs(continent_field - 0.20)
    shallow = (1.0 - land) * (1.0 - smoothstep(0.03, 0.18, coast_distance))
    ocean_variation = clamp(
        0.45
        + 0.18 * math.sin(3.0 * lon + 0.8 * lat - 0.10 * phase)
        + 0.12 * math.cos(5.3 * lat - 0.3 * lon)
    )

    return {
        "land": land,
        "humidity": humidity,
        "mountain": mountain,
        "desert": desert,
        "vegetation": vegetation,
        "ice": ice,
        "cloud": cloud,
        "shallow": shallow,
        "ocean_variation": ocean_variation,
    }


def build_surface_polygons(phase: float) -> list[tuple[float, str, str, float]]:
    yaw = 0.92 * phase - 0.25
    pitch = -0.37
    roll = 0.08
    center_x, center_y = PLANET_CENTER
    radius = PLANET_RADIUS
    light = normalize((0.86, 0.18, 0.48))

    cells: list[tuple[float, str, str, float]] = []
    subdivisions = SURFACE_SUBDIVISIONS
    faces = ("px", "nx", "py", "ny", "pz", "nz")

    for face in faces:
        for row in range(subdivisions):
            for col in range(subdivisions):
                u0 = -1.0 + 2.0 * col / subdivisions
                u1 = -1.0 + 2.0 * (col + 1) / subdivisions
                v0 = -1.0 + 2.0 * row / subdivisions
                v1 = -1.0 + 2.0 * (row + 1) / subdivisions

                corners = [
                    cube_to_sphere(face, u0, v0),
                    cube_to_sphere(face, u1, v0),
                    cube_to_sphere(face, u1, v1),
                    cube_to_sphere(face, u0, v1),
                ]
                center = normalize(
                    (
                        sum(point[0] for point in corners) / 4.0,
                        sum(point[1] for point in corners) / 4.0,
                        sum(point[2] for point in corners) / 4.0,
                    )
                )
                rotated_center = rotate_point(center, yaw, pitch, roll)
                if rotated_center[2] <= -0.08:
                    continue

                rotated_corners = [rotate_point(point, yaw, pitch, roll) for point in corners]
                projected = [project(point, center_x, center_y, radius) for point in rotated_corners]
                path = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in projected) + " Z"

                surface = earth_components(center, phase)
                diffuse = clamp(dot(rotated_center, light), 0.0, 1.0)
                shade = 0.42 + 0.74 * ((diffuse + 0.18) / 1.18)
                ocean_color = mix_rgb((12, 58, 128), (35, 121, 196), surface["ocean_variation"])
                ocean_color = mix_rgb(ocean_color, (86, 190, 214), 0.55 * surface["shallow"])

                land_color = mix_rgb((72, 116, 54), (44, 88, 40), surface["humidity"])
                land_color = mix_rgb(land_color, (158, 138, 87), 0.80 * surface["desert"])
                land_color = mix_rgb(land_color, (104, 92, 76), 0.75 * surface["mountain"])
                land_color = mix_rgb(land_color, (86, 142, 73), 0.62 * surface["vegetation"])

                color = mix_rgb(ocean_color, land_color, surface["land"])
                color = mix_rgb(color, (255, 251, 245), 0.92 * surface["ice"])
                color = scale_rgb(color, shade)

                ocean_glint = (1.0 - surface["land"]) * clamp((diffuse - 0.55) / 0.45)
                color = mix_rgb(color, (170, 222, 248), 0.18 * ocean_glint)
                color = mix_rgb(color, (244, 248, 252), 0.28 * surface["cloud"] * (0.45 + 0.55 * diffuse))

                rim = (1.0 - clamp(rotated_center[2], 0.0, 1.0)) ** 3 * clamp(diffuse + 0.28)
                color = mix_rgb(color, (98, 201, 255), 0.16 * rim)

                opacity = 0.96 if rotated_center[2] > 0.0 else 0.8 + 0.16 * (rotated_center[2] + 0.12) / 0.12
                cells.append((rotated_center[2], path, rgb_hex(color), opacity))

    cells.sort(key=lambda item: item[0])
    return cells

def build_ribbons(phase: float) -> tuple[list[str], list[str]]:
    return [], []
def render_svg(frame_index: int, total_frames: int, width: int, height: int) -> str:
    phase = 2.0 * math.pi * frame_index / total_frames
    cells = build_surface_polygons(phase)
    ribbons, ribbon_pulses = build_ribbons(phase)
    stars = build_stars(width, height)

    cx, cy = PLANET_CENTER
    radius = PLANET_RADIUS

    surface_markup = [
        f'<path d="{path}" fill="{fill}" opacity="{opacity:.3f}" />' for _, path, fill, opacity in cells
    ]
    star_markup = [
        f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{size:.2f}" fill="{rgb_hex(color)}" opacity="{opacity:.2f}" />'
        for x, y, size, color, opacity in stars
    ]

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#040812" />
  <rect width="100%" height="100%" fill="#09121f" opacity="0.34" />
  <circle cx="250" cy="114" r="240" fill="#1c426d" opacity="0.10" />
  <circle cx="820" cy="340" r="360" fill="#0b5f86" opacity="0.08" />
  {''.join(star_markup)}
  <circle cx="{cx}" cy="{cy}" r="{radius + 30}" fill="#4bc1df" opacity="0.10" />
  <circle cx="{cx}" cy="{cy}" r="{radius + 16}" fill="#4bc1df" opacity="0.12" />
  <circle cx="{cx}" cy="{cy}" r="{radius}" fill="#06121f" />
  <circle cx="{cx}" cy="{cy}" r="{radius - 12}" fill="#12334b" opacity="0.20" />
  <ellipse cx="{cx + 92}" cy="{cy - 92}" rx="146" ry="94" fill="#fff2ca" opacity="0.09" transform="rotate(18 {cx + 92} {cy - 92})" />
  <ellipse cx="{cx + 134}" cy="{cy - 36}" rx="184" ry="112" fill="#6fd8ff" opacity="0.08" transform="rotate(16 {cx + 134} {cy - 36})" />
  <g>
    {''.join(surface_markup)}
    <ellipse cx="{cx + 86}" cy="{cy - 104}" rx="124" ry="74" fill="#fff3db" opacity="0.06" transform="rotate(20 {cx + 86} {cy - 104})" />
    <ellipse cx="{cx + 126}" cy="{cy - 48}" rx="176" ry="96" fill="#d5f4ff" opacity="0.04" transform="rotate(15 {cx + 126} {cy - 48})" />
  </g>
  <circle cx="{cx}" cy="{cy}" r="{radius}" fill="#66dfff" opacity="0.03" />
  <circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="#a7f0ff" stroke-width="1.3" opacity="0.28" />
  <ellipse cx="{cx + 132}" cy="{cy - 126}" rx="136" ry="84" fill="#fff3cc" opacity="0.10" transform="rotate(21 {cx + 132} {cy - 126})" />
  {''.join(ribbons)}
  {''.join(ribbon_pulses)}
</svg>
'''


def ensure_tools() -> None:
    for tool in ("magick", "ffmpeg"):
        if shutil.which(tool) is None:
            raise SystemExit(f"Required tool not found on PATH: {tool}")


def run_command(command: list[str], cwd: Path | None = None) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def build_assets(output_root: Path, width: int, height: int, frames: int, fps: int) -> None:
    ensure_tools()

    image_dir = output_root / "_static" / "images"
    video_dir = output_root / "_static" / "videos"
    image_dir.mkdir(parents=True, exist_ok=True)
    video_dir.mkdir(parents=True, exist_ok=True)

    poster_png = image_dir / "exoplanet_mesh.png"
    poster_webp = image_dir / "exoplanet_mesh.webp"
    video_h264 = video_dir / "exoplanet_mesh.mp4"
    video_h265 = video_dir / "exoplanet_mesh-h265.mp4"
    gif_path = video_dir / "exoplanet_mesh.gif"

    poster_frame = frames // 5

    with tempfile.TemporaryDirectory(prefix="exoplanet_mesh_") as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        svg_dir = temp_dir / "svg"
        png_dir = temp_dir / "png"
        svg_dir.mkdir()
        png_dir.mkdir()

        for frame_index in range(frames):
            svg_path = svg_dir / f"frame_{frame_index:03d}.svg"
            svg_path.write_text(render_svg(frame_index, frames, width, height), encoding="utf-8")

        run_command([
            "magick",
            "mogrify",
            "-format",
            "png",
            "-path",
            str(png_dir),
            *sorted(str(path) for path in svg_dir.glob("*.svg")),
        ])

        shutil.copyfile(png_dir / f"frame_{poster_frame:03d}.png", poster_png)

        run_command([
            "ffmpeg",
            "-y",
            "-framerate",
            str(fps),
            "-i",
            str(png_dir / "frame_%03d.png"),
            "-c:v",
            "libx264",
            "-preset",
            "slow",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-movflags",
            "+faststart",
            str(video_h264),
        ])

        run_command([
            "ffmpeg",
            "-y",
            "-framerate",
            str(fps),
            "-i",
            str(png_dir / "frame_%03d.png"),
            "-c:v",
            "libx265",
            "-preset",
            "medium",
            "-crf",
            "22",
            "-pix_fmt",
            "yuv420p",
            "-tag:v",
            "hvc1",
            "-movflags",
            "+faststart",
            str(video_h265),
        ])

        run_command([
            "ffmpeg",
            "-y",
            "-i",
            str(poster_png),
            "-c:v",
            "libwebp",
            "-q:v",
            "82",
            "-compression_level",
            "6",
            "-preset",
            "photo",
            str(poster_webp),
        ])

        run_command([
            "ffmpeg",
            "-y",
            "-framerate",
            str(fps),
            "-i",
            str(png_dir / "frame_%03d.png"),
            "-vf",
            "fps=12,scale=1344:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4",
            str(gif_path),
        ])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--width", type=int, default=WIDTH)
    parser.add_argument("--height", type=int, default=HEIGHT)
    parser.add_argument("--frames", type=int, default=FRAMES)
    parser.add_argument("--fps", type=int, default=FPS)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_assets(args.output_root, args.width, args.height, args.frames, args.fps)


if __name__ == "__main__":
    main()
