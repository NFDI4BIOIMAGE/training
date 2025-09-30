# Recently added (9)
## A Perspective on FAIR and Scalable Access to Large Image Data

Julia Thönnißen, Sarah Oliveira, Alexander Oberstrass, Jan-Oliver Kropp, Xiao Gui, Christian Schiffer, Timo Dickscheid

Published 2025-08-04

Licensed CC-BY-4.0



The rapid development of new imaging technologies across scientific domains–especially high-throughput technologies–results in a growing volume of image datasets in the Tera- to Petabyte scale. Efficient visualization and analysis of such massive image resources is critical but remains challenging due to the sheer size of the data, its continuous growth, and the limitations of conventional software tools to address these problems. Tools for visualization, annotation and analysis of large image data are confronted with the fundamental dilemma of balancing computational efficiency and memory requirements. Many tools are unable to process large datasets due to memory constraints, requiring workarounds like downsampling. On the other hand, solutions that can handle large data efficiently often rely on specialized or even proprietary file formats, limiting interoperability with other software. This reflects diverging requirements: storage favours compression for efficiency, analysis demands fast data access, and visualization requires tiled, multi-resolution representations. Lacking a unified approach for these conflicting needs, the operation of large and dynamically evolving image repositories in practice often requires undesirable data conversions and costly data duplication. In addressing these challenges, the bioimaging community increasingly adheres to the FAIR principles [1] through national and international initiatives [2], [3], [4]. For example, the Open Microscopy Environment (OME) fosters standards such as OME-TIFF [5] and its cloud-native successor OME-NGFF [6]; BioFormats [7] and OMERO [8] facilitate metadata-rich data handling across diverse platforms; and BrAinPI [9] provides web-based visualization of images via Neuroglancer [10]. These tools represent important developments towards more efficient and standardized use of bioimaging data. However, for very large and dynamically growing repositories, it is still not feasible to settle on a single standard for a subset of these tools, in particular in the light of very diverging needs for massively parallel processing on HPC systems. Therefore, converting data to a single target format is often not a practical solution. We propose a concept for a modular image delivery service which acts as a middleware between large image data resources and applications, serving image data from a cloud resource in multiple requested representations on demand. The service allows reading data stored in different input file formats, applying coordinate transformations and filtering operations on-the-fly, and serving the results in a range of different output formats and layouts. Building upon a common framework for reading and transforming data, an extensible set of access points connects the service to client applications: Lightweight REST APIs allow web-based mutli-resolution access (e.g., in common formats such as used in Neuroglancer and OpenSeadragon base viewers); mountable filesystem interfaces enable linking the repository to file-oriented solutions (e.g., OMERO, ImageJ); and programmatic access from customizable software tools (e.g., Napari). To provide compatibility with upcoming image data standards like BIDS [11] and minimize conversion efforts, the service is able to dynamically expose standard-conform views into arbitrarily organized datasets. The proposed approach for reading and transforming data on-the-fly eliminates the need for redundant storage and application-specific conversions of datasets, improving workflow efficiency and sustainability. In summary, we advocate for the development of a flexible and extensible image data service that supports large-scale analysis, dynamic transformations, multi-tool interoperability, and compatibility with community standards for large image datasets. This way it supports the FAIR principles, reduces integration barriers, meets the performance demands of modern imaging research, and still fosters the use of existing community developments.

Tags: Include In Dalia

[https://zenodo.org/records/16736220](https://zenodo.org/records/16736220)

[https://doi.org/10.5281/zenodo.16736220](https://doi.org/10.5281/zenodo.16736220)


---

## COBA-NIH/2024_Bridging_Imaging_Users_to_Imaging_Analysis_Survey: Survey data with preliminary exploration

Erin Weisbart

Published 2025-09-15

Licensed BSD-3-CLAUSE



Contains the survey data collected through the 2024 Bridging Imaging Users to Imaging Analysis Survey and figures/code from preliminary data exploration of the survey results.

Tags: Exclude From Dalia

[https://zenodo.org/records/17127544](https://zenodo.org/records/17127544)

[https://doi.org/10.5281/zenodo.17127544](https://doi.org/10.5281/zenodo.17127544)


---

## Cloud-Based Virtual Desktops for Reproducible Research

Yi Sun, Christian Tischer, Kelleher, Harry Alexander, Jean-Karim Heriche

Published 2025-09-10

Licensed CC-BY-4.0



Reproducing computing environments become increasingly challenging in research, especially when compute-intensive scientific workflows require specialised software stacks, specialized hardware (e.g. GPUs), and interactive analysis tools. While traditional high-performance computing (HPC) systems offer scalable resources for batch processing, they don't easily support interactive workflows. On the other hand, workstations have fixed resources  and face workflow deployment challenges because conflicts can occur when multiple tools and dependencies are deployed into the same environment. To address these limitations, we present cloud-based virtual desktop platforms, built on the desktop-as-a-service (DaaS) model, using a containerised, cloud-native approach.  Our platforms offer on-demand, customized desktop environments accessible from any web browser, with dynamic allocation of CPU, memory, and GPU resources for efficient utilization of resources. We introduce two types of virtual desktops: BAND, built on top of a Slurm scheduler and BARD, using Kubernetes. In both cases, containerization ensures consistent and reproducible environments across sessions and pre-installed software improves accessibility for researchers. Deployment and system administration are also simplified through the use of orchestration and automation tools.  Our virtual desktop platforms are particularly valuable for bioimage analysis, which requires complex workflows involving high interactivity, multiple software and GPU acceleration. By combining containerization and cloud-native services, BAND and BARD offer a scalable and sustainable model for delivering interactive, reproducible research environments.

Tags: Nfdi4Bioimage, Exclude From Dalia

[https://zenodo.org/records/17092303](https://zenodo.org/records/17092303)

[https://doi.org/10.5281/zenodo.17092303](https://doi.org/10.5281/zenodo.17092303)


---

## Image Analysis in Healthcare - The Current Landscape, Trends, and Collaborative Opportunities

Martin Schätz, Pérez Koldenkova, Vadim

Published 2025-09-09

Licensed CC-BY-4.0



Workshop presentation from XXXIV Foro de Investigaci&oacute;n en Salud 2025.

Tags: Include In Dalia

[https://zenodo.org/records/17080219](https://zenodo.org/records/17080219)

[https://doi.org/10.5281/zenodo.17080219](https://doi.org/10.5281/zenodo.17080219)


---

## PygamePrompts

Lea Kabjesz, Lea Gihlein, Mara Lampert, FPGro

Published 2025-08-12T11:36:36+00:00

Licensed CC-BY-4.0



A collection of workshop materials for exploring prompting techniques by building a Snake game in Cursor.  

Tags: Include In Dalia

Content type: Github Repository

[https://github.com/kaabl/PygamePrompts](https://github.com/kaabl/PygamePrompts)


---

## Reproducible Bio-Image Analysis using Python, Napari, Jupyter and AI

Robert Haase

Published 2025-09-09

Licensed CC-BY-4.0



In this slide deck we learn how to write reproducible bio-image analysis code in Jupyter notebooks. Goal is not just to have code running elsewhere reproducibly, but also enabling others to understand workflows to enable them reproducing the analysis also in their mind and potentially other tools. Additionally we cover how to generate Jupyter notebooks from Napari and using artificial intelligence, namely bia-bob.

Tags: Nfdi4Bioimage, Bioimage Analysis, Include In Dalia

[https://zenodo.org/records/17085991](https://zenodo.org/records/17085991)

[https://doi.org/10.5281/zenodo.17085991](https://doi.org/10.5281/zenodo.17085991)


---

## Research Data Management

Robert Haase

Published 2025-09-22

Licensed CC-BY-4.0



This slides covers aspects of research data management (RDM) and open science such as the RDM life cylce, FAIR principles, sharing data on Zenodo, rights and duties of scientists in the RDM context.

[https://zenodo.org/records/17174207](https://zenodo.org/records/17174207)

[https://doi.org/10.5281/zenodo.17174207](https://doi.org/10.5281/zenodo.17174207)


---

## Test data for Bioformats Issue #4366

Ivo Alxneit

Published 2025-09-22

Licensed CC-BY-4.0



[https://zenodo.org/records/17176730](https://zenodo.org/records/17176730)

[https://doi.org/10.5281/zenodo.17176730](https://doi.org/10.5281/zenodo.17176730)


---

## embo-bia-2025

Kevin Yamauchi

Published 2025-08-18T09:32:20+00:00

Licensed BSD-3-CLAUSE





Tags: Exclude From Dalia

Content type: Github Repository

[https://github.com/kevinyamauchi/embo-bia-2025](https://github.com/kevinyamauchi/embo-bia-2025)


---

