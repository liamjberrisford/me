# Projects

## High Performance Computing 

### Met Office NG-ARCH: LFRic Spectral Gravity Wave Drag Optimisation 

![LFRic optimisation](content/images/ngarch.webp)

As part of the NG-ARCH initiative, I led a comprehensive optimisation of the Spectral Gravity Wave Drag (SGWD) component within the Met Office’s LFRic atmospheric model, using the PSyclone code generation framework. This work focused on applying advanced performance transformations to a Fortran implementation of Spectral Gravity Wave Drag and systematically evaluating both CPU-based (OpenMP) and GPU-based (OpenMP offloading, OpenACC) implementations.

Working within a bespoke optimisation branch, I developed, tested, and refined PSyclone transformation scripts to target compute-intensive loops, using profiling data to identify performance-critical regions. On the CPU side, optimisations included the insertion of fine-grained OpenMP directives, loop collapsing, and parallel region clustering, with performance evaluated across a range of MPI-thread configurations. In parallel, GPU offloading strategies were explored to assess their suitability for future hardware acceleration pathways.

The workflow I implemented enabled high-throughput experimentation across platforms such as Microsoft Azure (Milan CPUs and NVIDIA GPUs) and ARCHER2 (Rome CPUs), supported by automated job generation, analysis pipelines, and verification tooling. A key innovation was a hybrid MPI/OpenMP benchmarking matrix that revealed optimal core utilisation strategies under constrained-node conditions, highlighting the importance of balanced sub-domain sizes, communication cost trade-offs, and thread management overhead.

This work delivered a validated set of performance improvements for the SGWD kernel, alongside robust guidance for hybrid and offloaded configurations in operational LFRic runs. The pipeline and methodology developed are now being extended to other physics components in LFRic, contributing to a broader drive towards performance-portable atmospheric modelling.

### GPU Accelerated openFOAM (gpuFOAM)

![openFOAM Tutorial Test Case Visualisation](content/images/openfoam.png)

As part of the gpuFOAM project, I am responsible for benchmarking C++ code that leverages GPUs via stdpar on a range of HPC platforms (e.g. Isambard-AI) across multiple GPU architectures (e.g. GH200, MI300A).

## Software

### Environmental Insights Python Package

![Environmental Insights](content/images/ei.png)

The package, designed for simplicity and inclusivity, enables users from diverse backgrounds, including academic, governmental, and non-governmental sectors, to retrieve historical air pollution data and utilize machine learning models for forecasting future conditions. It offers dynamic visualizations and analytical tools to enhance user engagement and comprehension of air pollution trends and implications. Environmental Insights aims to lower the barriers to air pollution data access, promoting informed decision-making and encouraging public advocacy for air quality improvements. By offering an open-source, user-friendly platform, the project contributes significantly to the democratization of environmental data, making it a valuable resource for stakeholders aiming to explore and mitigate the effects of air pollution across various sectors.

## Websites 

### Coding for Reproducible Research

![CfRR](content/images/cfrr.png)

[CfRR Homepage](https://coding-for-reproducible-research.github.io/CfRR_Courses/home_page.html)

The Coding for Reproducible Research (CfRR) website is the public-facing home of our coding training programme. It hosts courses and standalone modules on topics such as Python, R, Unix, Git and GitHub, data management, Julia, and high-performance/GPU computing, with content designed to help researchers move from ad-hoc scripts to robust, shareable, and well-documented code. The site is generated as a Jupyter Book, meaning that the notebooks, markdown files, quizzes, and configuration stored are compiled into the pages that learners see online, keeping the teaching material and the deployed site tightly synchronised. The repository behind the website has grown into a substantial collaborative project, with 18 contributors, more than 1,300+ commits, over 300+ pull requests, and 100+ issues, reflecting continuous refinement of examples, exercises, accessibility, and documentation. Development takes place openly via GitHub, where proposed changes are reviewed and tested before automated workflows build and publish updates to the live site. Although the project is community-driven, with input from tutors, researchers, and colleagues from professional services, I have overall responsibility for managing and maintaining the system, including reviewing contributions, coordinating updates, and ensuring the site remains stable, accurate, and aligned with learner needs. As a result, the website serves both as a practical teaching resource for live workshops and self-paced study, and as a transparent record of the ongoing evolution of the CfRR training programme.

### Environmental Insights Interactive

![Environmental Insights Interactive](content/images/ei_interactive.png)

Environmental Insights Interactive is a web application that showcases the capabilities of the environmental-insights Python package by providing an interactive way to explore air pollution data and model outputs. It combines a Python/Flask backend, which runs the air quality models, manages data and generates PDFs, with a React-based frontend that displays maps, charts and other visualisations for users. Together, these components let users query locations, view estimated pollution levels and explore environmental insights through a modern web interface.

## Dashboards 

### College of Policing Behavioural Change Dashboards 

![Example Dashboard used for the Pulse Check Survey](content/images/police_pulse_check.png)

I worked as a Research Software Engineer, a UKRI-funded behavioural change initiative led by the College of Policing, supporting three police forces in England and Wales. The project aimed to help supervisors address sexism and racism within policing culture by running short, monthly “pulse” surveys capturing officers’ and staff’s lived experiences of workplace culture. I led the design and implementation of a suite of Power BI dashboards for supervisors, participating officers and staff, and line managers overseeing monthly action plans, translating thousands of survey responses from over 1,800 personnel into clear, accessible insights. This involved complex DAX development, visual design, and rapid troubleshooting under tight timelines, all while maintaining role-based anonymity within highly non-uniform team structures. I iteratively refined the tools using feedback from pilot studies, cognitive testing, and stakeholder quality assurance to ensure the dashboards were both trusted and practically useful. This work enabled leadership teams to monitor behavioural change interventions, respond quickly to emerging cultural issues, and make data-informed decisions with confidence.
