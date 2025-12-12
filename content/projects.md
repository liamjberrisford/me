# Projects

## High Performance Computing 

### Met Office NG-ARCH: LFRic Spectral Gravity Wave Drag Optimisation 

![LFRic optimisation](_static/images/ngarch.png)

As part of the NG-ARCH initiative, I led a comprehensive performance optimisation of the Spectral Gravity Wave Drag (SGWD) component within the Met Office’s LFRic atmospheric model, using the PSyclone code-generation framework. The work focused on applying and evaluating advanced performance transformations to the Fortran SGWD implementation in a codebase that already employs distributed-memory parallelism via MPI, requiring careful design and validation of hybrid configurations (MPI+OpenMP on CPUs, and exploratory MPI+OpenMP target offloading / MPI+OpenACC approaches for GPUs).

Working within a dedicated optimisation branch, I designed, implemented, and validated PSyclone transformation scripts to target compute-intensive regions, guided by detailed profiling and kernel-level analysis. CPU-focused optimisations included selective insertion of fine-grained OpenMP directives, evaluation of loop-collapsing strategies, and restructuring of parallel regions to minimise thread management overhead while preserving correctness under MPI domain decomposition. Performance was assessed across a wide range of MPI configurations. In parallel, I explored GPU offloading strategies to evaluate their feasibility and limitations for SGWD within hybrid MPI+accelerator execution modes.

I developed a reproducible, high-throughput benchmarking workflow supporting experimentation across multiple HPC platforms, including Microsoft Azure (Milan CPUs and NVIDIA GPUs) and ARCHER2 (Rome CPUs). This workflow integrated automated job generation, performance analysis pipelines, and numerical verification tooling. A key outcome was the construction of a hybrid MPI/OpenMP benchmarking matrix, which exposed optimal core-utilisation strategies under fixed-node constraints and quantified the trade-offs between sub-domain granularity, MPI communication overheads, and OpenMP thread management costs.

This work delivered a validated set of performance improvements for the SGWD kernel, together with practical guidance on effective hybrid parallel configurations for operational LFRic runs. Importantly, the work also fed directly into PSyclone development, resulting in new or enhanced transformation capabilities applicable to other physics kernels. The optimisation pipeline and methodology are now being reused across additional LFRic physics components, supporting a broader programme of performance portability and sustainable numerical weather prediction model development.

### GPU Accelerated openFOAM (gpuFOAM)

![openFOAM Tutorial Test Case Visualisation](_static/images/openfoam.png)

 As part of the gpuFOAM project, I support benchmarking and portability work for a C++ codebase that leverages GPUs via standard parallelism (stdpar) across a range of HPC platforms. My contribution focuses on taking the code from system to system, establishing reliable build and benchmarking workflows, and resolving platform-specific compilation, linking, and runtime issues across heterogeneous hardware and software environments, including systems such as Isambard-AI and multiple GPU architectures (e.g. NVIDIA GH200 and AMD MI300A).

A major element of this work involves identifying and documenting issues that arise from differences in toolchains, linkers, runtime environments, and platform configuration. In practice, this has meant using Spack extensively to create reproducible environments and to manage compiler and dependency variations across sites, while developing a detailed understanding of how architectural differences impact both build feasibility and performance characteristics.

This activity has also resulted in contributions back to platform and vendor teams when issues are traced to compiler or toolchain behaviour rather than project code. One example is an issue observed with NVHPC 24.11 on Grace (AArch64), where the device-link helper (pgacclnk) compiles its internal link stub with small PIC (-fpic) during device link. On AArch64 this can lead to a small GOT and, for large shared libraries such as libOpenFOAM.so, trigger a GOT overflow and final link failure. I documented the behaviour, captured supporting trace evidence showing the injected -fpic flag, and provided a minimal reproducer to assist investigation. Colleagues have reported that alternative SDK configurations using -fPIC internally can avoid the failure, suggesting the outcome is sensitive to NVHPC’s internal defaults or installation-time configuration rather than project build settings.

## Software

### Environmental Insights Python Package

![Environmental Insights](_static/images/ei.png)

[Environmental Insights Python Package GitHub Homepage](https://github.com/liamjberrisford/Environmental-Insights)

The package, designed for simplicity and inclusivity, enables users from diverse backgrounds, including academic, governmental, and non-governmental sectors, to retrieve historical air pollution data and utilize machine learning models for forecasting future conditions. It offers dynamic visualizations and analytical tools to enhance user engagement and comprehension of air pollution trends and implications. Environmental Insights aims to lower the barriers to air pollution data access, promoting informed decision-making and encouraging public advocacy for air quality improvements. By offering an open-source, user-friendly platform, the project contributes significantly to the democratization of environmental data, making it a valuable resource for stakeholders aiming to explore and mitigate the effects of air pollution across various sectors.

## Websites 

### Coding for Reproducible Research

![CfRR](_static/images/cfrr.png)

[CfRR Homepage](https://coding-for-reproducible-research.github.io/CfRR_Courses/home_page.html)

The Coding for Reproducible Research (CfRR) website is the public-facing home of our coding training programme. It hosts courses and standalone modules on topics such as Python, R, Unix, Git and GitHub, data management, Julia, and high-performance/GPU computing, with content designed to help researchers move from ad-hoc scripts to robust, shareable, and well-documented code. The site is generated as a Jupyter Book, meaning that the notebooks, markdown files, quizzes, and configuration stored are compiled into the pages that learners see online, keeping the teaching material and the deployed site tightly synchronised. The repository behind the website has grown into a substantial collaborative project, with 18 contributors, more than 1,300+ commits, over 300+ pull requests, and 100+ issues, reflecting continuous refinement of examples, exercises, accessibility, and documentation. Development takes place openly via GitHub, where proposed changes are reviewed and tested before automated workflows build and publish updates to the live site. Although the project is community-driven, with input from tutors, researchers, and colleagues from professional services, I have overall responsibility for managing and maintaining the system, including reviewing contributions, coordinating updates, and ensuring the site remains stable, accurate, and aligned with learner needs. As a result, the website serves both as a practical teaching resource for live workshops and self-paced study, and as a transparent record of the ongoing evolution of the CfRR training programme.

### Environmental Insights Interactive

![Environmental Insights Interactive](_static/images/ei_interactive.png)

[Environmental Insights Interactive GitHub Homepage](https://github.com/liamjberrisford/Environmental-Insights-interactive)

Environmental Insights Interactive is a web application that showcases the capabilities of the environmental-insights Python package by providing an interactive way to explore air pollution data and model outputs. It combines a Python/Flask backend, which runs the air quality models, manages data and generates PDFs, with a React-based frontend that displays maps, charts and other visualisations for users. Together, these components let users query locations, view estimated pollution levels and explore environmental insights through a modern web interface.

## Dashboards 

### College of Policing Behavioural Change Dashboards 

![Example Dashboard used for the Pulse Check Survey](_static/images/police_pulse_check.png)

I worked as a Research Software Engineer, a UKRI-funded behavioural change initiative led by the College of Policing, supporting three police forces in England and Wales. The project aimed to help supervisors address sexism and racism within policing culture by running short, monthly “pulse” surveys capturing officers’ and staff’s lived experiences of workplace culture. I led the design and implementation of a suite of Power BI dashboards for supervisors, participating officers and staff, and line managers overseeing monthly action plans, translating thousands of survey responses from over 1,800 personnel into clear, accessible insights. This involved complex DAX development, visual design, and rapid troubleshooting under tight timelines, all while maintaining role-based anonymity within highly non-uniform team structures. I iteratively refined the tools using feedback from pilot studies, cognitive testing, and stakeholder quality assurance to ensure the dashboards were both trusted and practically useful. This work enabled leadership teams to monitor behavioural change interventions, respond quickly to emerging cultural issues, and make data-informed decisions with confidence.
