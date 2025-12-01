// Configuration: sections and their markdown files
const sections = [
  { id: "about", label: "About", file: "content/about.md" },
  { id: "projects", label: "Projects", file: "content/projects.md" },
  { id: "publications", label: "Publications", file: "content/publications.md" },
  { id: "teaching", label: "Teaching", file: "content/teaching.md" },
  { id: "awards", label: "Awards", file: "content/awards.md" }
];

// Inline fallback content so the site still works when opened directly via file://
const inlineMarkdown = {
  about: `# About

I am a **Research Software Engineer, Computer Scientist, and Researcher** based in Exeter, UK. My work sits at the intersection of environmental intelligence, software engineering, and technical education.

I have experience developing data-driven tools (including dashboards and open-source packages), leading and supporting teaching in programming and data science, and collaborating across academia, government, and industry.

You can think of my professional profile as spanning three main strands:

- **Research & Environmental Intelligence**
- **Software Engineering & Tooling**
 - **Teaching, Mentoring & Academic Practice**`,
  teaching: `# Teaching

## Train the Trainer (Jan 2025 – Present)

- Designed and facilitated a five-session programme to upskill technical educators in inclusive pedagogy.  
- Grounded in UDL, Backward Design, ADDIE, Bloom’s Taxonomy, and differentiated instruction.  
- Balanced lectures, workbooks, workshop slides, group activities, and reflective exercises to boost teaching confidence.

## GPU Training (May 2025)

- Hands-on course for researchers covering GPU memory hierarchies, thread models, and OpenMP/CUDA/CuPy workflows.  
- Includes performance analysis labs, CPU-GPU comparisons, and benchmarking exercises with example code.

## Concepts for Efficient Programming (Feb 2023)

- Workshop on computer architecture, algorithm analysis, and practical optimisation (parallelism, search-space reduction).  
- Materials and examples available: berrli/ConceptsForEfficientProgramming.

## Research Supervision (Jan 2023 – Present)

- Supervised projects spanning wildfire modelling, parking capacity prediction, marine species abundance, ocean acidification, renewable energy forecasting, and socio-economic analytics.  
- Outcomes include MSc award recognition and multiple undergraduate research completions.

## Associate Lecturer Contributions (2023)

- Curriculum redesign for COM1012 Data Science Group Project; co-led ECM2434 Group Software Engineering Project with sustainability focus.  
- Provided bespoke teaching activities including imposter syndrome enrichment lectures and efficient programming short courses.`,
  publications: `# Publications

## A framework for scalable ambient air pollution concentration estimation

![Ambient air pollution estimation](https://placehold.co/1200x630/ffffff/1d1d1f?text=Ambient+Air+Pollution+Estimation)

Details forthcoming — add co-authors, venue, and DOI here.

## Machine Learning for Hourly Air Pollution Prediction in England (ML-HAPPE)

![ML-HAPPE](https://placehold.co/1200x630/ffffff/1d1d1f?text=ML-HAPPE)

Details forthcoming — add co-authors, venue, and DOI here.

## Environmental Insights: Democratizing access to ambient air pollution data and predictive analytics with an open-source Python package

![Environmental Insights](https://placehold.co/1200x630/ffffff/1d1d1f?text=Environmental+Insights)

Details forthcoming — add co-authors, venue, and DOI here.

## Estimating annual ambient air pollution using structural properties of road networks

![Road network estimation](https://placehold.co/1200x630/ffffff/1d1d1f?text=Road+Network+Estimation)

Details forthcoming — add co-authors, venue, and DOI here.

## Synthetic Hourly Air Pollution Prediction Averages for England (SynthHAPPE)

![SynthHAPPE](https://placehold.co/1200x630/ffffff/1d1d1f?text=SynthHAPPE)

Details forthcoming — add co-authors, venue, and DOI here.`,
  awards: `# Awards & Honours

- **Netcraft Prize 2016 – First Year Undergraduates**  
- **Peer Assisted Learning Leader – Scheme of the Year (Shortlisted)**  
- **The Bath Award**  
- **Volunteer Recognition Scheme**  
- **Chosen Exemplary Dissertation — Initial Underwater Structure Exploration Planning**`,
  projects: `# Projects

## Projects

### Train the Trainer (Jan 2025 – Present, University of Exeter)

![Train the Trainer](https://placehold.co/1200x630/ffffff/1d1d1f?text=Train+the+Trainer)

- Designed and facilitated a five-session programme to upskill technical educators in inclusive pedagogy.  
- Grounded in UDL, Backward Design, ADDIE, Bloom’s Taxonomy, and differentiated instruction.  
- Balanced lectures, workbooks, workshop slides, group activities, and reflective exercises to boost teaching confidence.

### College of Policing Behavioural Change Dashboards (Aug 2024 – Present, University of Exeter)

![Behavioural change dashboards](images/police_pulse_check.png)

- Delivered five Power BI dashboards for a UKRI-funded initiative tackling sexism and misogyny across three police forces.  
- Built surveys and analytics with role-based anonymity; iterated with pilots, cognitive assessments, and QA reviews.  
- Enabled leadership teams to monitor behavioural interventions and make data-informed decisions.

### Met Office NG-ARCH: LFRic Spectral Gravity Wave Drag Optimisation (Mar 2024 – Present)

![LFRic optimisation](https://placehold.co/1200x630/ffffff/1d1d1f?text=LFRic+Optimisation)

- Led PSyclone-based performance optimisation of the Spectral Gravity Wave Drag kernel (CPU OpenMP and GPU offload).  
- Built automation for job generation, analysis, and verification across Azure (Milan/NVIDIA) and ARCHER2 (Rome).  
- Produced guidance for hybrid MPI/OpenMP and offloaded configurations now informing other LFRic physics components.

### Environmental Insights (Feb 2024 – Present)

![Environmental Insights](https://placehold.co/1200x630/ffffff/1d1d1f?text=Environmental+Insights)

- Open-source Python package for ambient air pollution data access and forecasting with ML models.  
- Aims to democratise air quality data via simple retrieval, visualisation, and analytics for public and policy use.  
- Public repo: berrli/Environmental-Insights.

### GPU Training (May 2025)

![GPU training](https://placehold.co/1200x630/ffffff/1d1d1f?text=GPU+Training)

- Hands-on course for researchers covering GPU memory hierarchies, thread models, and OpenMP/CUDA/CuPy workflows.  
- Includes performance analysis labs, CPU-GPU comparisons, and benchmarking exercises with example code.

### England Ambient Air Pollution Model Output Demo (Mar 2024)

![England air pollution demo](https://placehold.co/1200x630/ffffff/1d1d1f?text=England+Pollution+Demo)

- Interactive demo showcasing outputs from “A Framework for Scalable Ambient Air Pollution Concentration Estimation.”  
- Live at: https://berrli.github.io/England-Ambient-air-Pollution-Model-Dashboard/england_AIUK_2024_air_pollution_demo.html

### Global Ambient Air Pollution Model Output Demo (Mar 2024)

![Global air pollution demo](https://placehold.co/1200x630/ffffff/1d1d1f?text=Global+Pollution+Demo)

- Demonstrates global predictions from “A Data-Driven Supervised Machine Learning Approach to Estimating Global Ambient Air Pollution.”  
- Live at: https://berrli.github.io/Global-Ambient-air-Pollution-Model-Dashboard/global_AIUK_2024_air_pollution_demo.html

### Pilot Study: Indoor Air Quality Model Auditing (Feb 2024)

![Indoor air quality audit](https://placehold.co/1200x630/ffffff/1d1d1f?text=Indoor+Air+Quality+Audit)

- Audited ML models predicting indoor air quality in social housing; combined sensor data with citizen science.  
- Focused on inclusivity, public engagement, and transparent model auditing for vulnerable communities.

### Concepts for Efficient Programming (Feb 2023)

![Efficient programming](https://placehold.co/1200x630/ffffff/1d1d1f?text=Efficient+Programming)

- Workshop on computer architecture, algorithm analysis, and practical optimisation (parallelism, search-space reduction).  
- Materials and examples available: berrli/ConceptsForEfficientProgramming.

### Impact of Extreme Weather on Global Shipping (Jun 2021)

![Shipping resilience](https://placehold.co/1200x630/ffffff/1d1d1f?text=Shipping+Resilience)

- Simulation study of cyclone impacts on shipping routes around Australia; quantified distance and cost increases.  
- Proposed optimisation strategies considering environmental and security trade-offs.

### Heatmapper (Sep 2020)

![Heatmapper](https://placehold.co/1200x630/ffffff/1d1d1f?text=Heatmapper)

- ESA Space App Camp project using Copernicus data to surface hot/cool urban zones for heatwave comfort.  
- Android prototype highlighted microclimate insights for public health applications.

### Initial Underwater Structure Exploration Planning (Sep 2017 – Jun 2018)

![Underwater exploration](https://placehold.co/1200x630/ffffff/1d1d1f?text=Underwater+Exploration)

- Built Blender/Unity simulations with C# plus JavaFX GUI and 3D viewer for photogrammetry point clouds.  
- Produced datasets and visuals for underwater structure planning and review.

### Summary of Research Supervision (Jan 2023 – Present)

![Research supervision](https://placehold.co/1200x630/ffffff/1d1d1f?text=Research+Supervision)

- Supervised projects spanning wildfire modelling, parking capacity prediction, marine species abundance, ocean acidification, renewable energy forecasting, and socio-economic analytics.  
- Outcomes include MSc award recognition and multiple undergraduate research completions.

## Volunteering

### Leadership & Entrepreneurship

- **Bath Launchpad** co-founder and organiser — a 24-hour idea-to-pitch event drawing approximately 150 participants across computer science and business disciplines.  
- **Young Enterprise Ignite** (Assistant Managing Director & Operations Director) — student-run company generating over £5,000 revenue and delivering products to clients such as Virgin Group, JCB, and Wedgwood.`
};

// Utility: very simple Markdown → HTML converter
function formatInline(text) {
  return text
    .replace(
      /!\[([^\]]*)\]\(([^)]+)\)/g,
      '<img src="$2" alt="$1" loading="lazy" class="content-image" data-caption="$1" />'
    )
    .replace(
      /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
      '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>'
    )
    .replace(
      /\[([^\]]+)\]\(((?!https?:\/\/)[^)]+)\)/g,
      '<a href="$2">$1</a>'
    )
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/__(.+?)__/g, "<strong>$1</strong>")
    .replace(/\*(?!\s)(.+?)(?!\s)\*/g, "<em>$1</em>");
}

function simpleMarkdownToHtml(md) {
  const lines = md.split(/\r?\n/);
  let html = "";
  let inList = false;

  const flushList = () => {
    if (inList) {
      html += "</ul>";
      inList = false;
    }
  };

  for (let rawLine of lines) {
    const line = rawLine.trim();

    if (!line) {
      flushList();
      continue;
    }

    // Headings
    if (line.startsWith("### ")) {
      flushList();
      html += `<h3>${formatInline(line.substring(4))}</h3>`;
      continue;
    }
    if (line.startsWith("## ")) {
      flushList();
      html += `<h2>${formatInline(line.substring(3))}</h2>`;
      continue;
    }
    if (line.startsWith("# ")) {
      flushList();
      html += `<h1>${formatInline(line.substring(2))}</h1>`;
      continue;
    }

    if (/^---+$/.test(line)) {
      flushList();
      html += "<hr />";
      continue;
    }

    // Raw HTML passthrough (so you can use <a>, etc.)
    if (line.startsWith("<") && line.endsWith(">")) {
      flushList();
      html += line;
      continue;
    }

    // Lists
    if (line.startsWith("- ")) {
      if (!inList) {
        html += "<ul>";
        inList = true;
      }
      const item = formatInline(line.substring(2));
      html += `<li>${item}</li>`;
      continue;
    }

    // Paragraph
    flushList();
    const text = formatInline(line);

    const imgOnlyMatch = text.trim().match(/^<img\b[^>]*>/i);
    if (imgOnlyMatch) {
      const altMatch = text.match(/alt="([^"]*)"/i);
      const caption = altMatch ? altMatch[1] : "";
      html += `<figure class="content-figure">${text}<figcaption>${caption}</figcaption></figure>`;
    } else {
      html += `<p>${text}</p>`;
    }
  }

  if (inList) {
    html += "</ul>";
  }

  return html;
}

function setActiveNav(id) {
  const buttons = document.querySelectorAll("#nav-links button");
  buttons.forEach((btn) => {
    if (btn.dataset.sectionId === id) {
      btn.setAttribute("aria-current", "page");
    } else {
      btn.removeAttribute("aria-current");
    }
  });
}

async function loadSection(id) {
  const section = sections.find((s) => s.id === id) || sections[0];
  const contentEl = document.getElementById("content-inner");

  contentEl.innerHTML = `<p class="loading-message">Loading ${section.label.toLowerCase()}…</p>`;

  try {
    const md = await getMarkdownForSection(section);
    const html = simpleMarkdownToHtml(md);
    contentEl.innerHTML = html;
    buildSubNav(section.id);
    setActiveNav(section.id);
    document.title = `Liam Berrisford | ${section.label}`;
  } catch (err) {
    console.error(err);
    contentEl.innerHTML = `<p class="error-message">Sorry, there was a problem loading this section.</p>`;
  }
}

function initNav() {
  const nav = document.getElementById("nav-links");
  sections.forEach((section) => {
    const li = document.createElement("li");
    const button = document.createElement("button");
    button.textContent = section.label;
    button.type = "button";
    button.dataset.sectionId = section.id;
    button.addEventListener("click", () => {
      // Update URL hash for deep-linking
      window.location.hash = section.id;
      loadSection(section.id);
    });
    li.appendChild(button);
    nav.appendChild(li);
  });
}

function getInitialSectionId() {
  const hash = window.location.hash.replace("#", "").trim();
  if (hash && sections.some((s) => s.id === hash)) {
    return hash;
  }
  return sections[0].id;
}

function canFetchMarkdown() {
  return window.location.protocol === "http:" || window.location.protocol === "https:";
}

function slugify(text) {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

function clearSubNav() {
  const subNav = document.getElementById("sub-nav");
  const list = document.getElementById("sub-nav-links");
  if (list) list.innerHTML = "";
  if (subNav) subNav.setAttribute("hidden", "true");
  const title = document.getElementById("sub-nav-title");
  if (title) title.textContent = "";
  window.__subSegments = null;
}

function setActiveSubNav(id) {
  document.querySelectorAll("#sub-nav-links button").forEach((btn) => {
    if (btn.dataset.targetId === id) {
      btn.setAttribute("aria-current", "page");
    } else {
      btn.removeAttribute("aria-current");
    }
  });
}

function buildSubNav(sectionId) {
  const subNav = document.getElementById("sub-nav");
  const list = document.getElementById("sub-nav-links");
  const title = document.getElementById("sub-nav-title");
  if (!subNav || !list) return;

  list.innerHTML = "";

  const headings = Array.from(document.querySelectorAll("#content-inner h2"));
  const mainHeading = document.querySelector("#content-inner h1");
  if (!headings.length) {
    if (mainHeading) {
      mainHeading.style.display = "";
    }
    subNav.setAttribute("hidden", "true");
    return;
  }

  if (mainHeading) {
    mainHeading.style.display = "none";
  }

  const sectionMeta = sections.find((s) => s.id === sectionId);

  if (title) {
    title.textContent = mainHeading?.textContent || sectionMeta?.label || "";
  }

  const segments = {};

  headings.forEach((h) => {
    if (!h.id) {
      h.id = slugify(`${sectionId}-${h.textContent}`);
    }
    const nodes = [];
    let node = h;
    while (node && node !== null) {
      nodes.push(node);
      node = node.nextElementSibling;
      if (node && node.tagName === "H2") break;
    }
    segments[h.id] = nodes;

    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = h.textContent;
    btn.dataset.targetId = h.id;
    btn.addEventListener("click", () => {
      h.scrollIntoView({ behavior: "smooth", block: "start" });
      showSubSection(h.id);
    });
    li.appendChild(btn);
    list.appendChild(li);
  });

  subNav.removeAttribute("hidden");
  window.__subSegments = segments;
  showSubSection(headings[0].id);
}

function showSubSection(id) {
  const segments = window.__subSegments || {};
  Object.entries(segments).forEach(([segId, nodes]) => {
    nodes.forEach((node) => {
      if (!node) return;
      if (segId === id) {
        if (node.tagName === "H2") {
          node.style.display = "none";
        } else {
          node.style.display = "";
        }
      } else {
        node.style.display = "none";
      }
    });
  });
  setActiveSubNav(id);
}

async function getMarkdownForSection(section) {
  if (canFetchMarkdown()) {
    try {
      const res = await fetch(section.file);
      if (!res.ok) {
        throw new Error(`Could not load ${section.file}`);
      }
      return await res.text();
    } catch (err) {
      console.warn(`Falling back to inline content for ${section.id}`, err);
    }
  }

  if (inlineMarkdown[section.id]) {
    return inlineMarkdown[section.id];
  }

  throw new Error(`No content available for section: ${section.id}`);
}

document.addEventListener("DOMContentLoaded", () => {
  // Year in footer
  const yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  initNav();
  const initialSection = getInitialSectionId();
  loadSection(initialSection);

  if ("serviceWorker" in navigator) {
    navigator.serviceWorker
      .register("/sw.js")
      .catch((err) => console.warn("Service worker registration failed", err));
  }
});

// Handle back/forward navigation with hashes
window.addEventListener("hashchange", () => {
  const id = getInitialSectionId();
  loadSection(id);
});
