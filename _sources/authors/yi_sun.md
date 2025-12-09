# Yi sun (8)
## Bioimage ANalysis Desktop Source Code

Yi Sun, Christian Tischer, Jean-Karim Hériché

Published 2025-11-21

Licensed CC-BY-4.0



The BAND platform offers cloud based desktops accessible with a web browser so that you can work on your data from anywhere with an internet connection.
This project is funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under the National Research Data Infrastructure &ndash; NFDI 46/1 &ndash; 501864659

[https://zenodo.org/records/17671971](https://zenodo.org/records/17671971)

[https://doi.org/10.5281/zenodo.17671971](https://doi.org/10.5281/zenodo.17671971)


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

## Development FAIR image analysis workflows and RDM pipelines in Galaxy

Riccardo Massei, Beatriz Serrano-Solano, Anne Fouilloux, Björg Gruening, Yi Sun, Diana Chiang, Matthias Bernt, Leonid Kostrykin

Published 2025-09-10

Licensed CC-BY-4.0



Imaging is crucial across various scientific disciplines, particularly in life sciences, where it plays a key role in studies ranging from single molecules to whole organisms. However, the complexity and sheer volume of image data present significant challenges. Managing and analyzing this data efficiently requires well-defined image processing tools and analysis pipelines that align with the FAIR principles—ensuring they are findable, accessible, interoperable, and reusable across different domains. In the frame of NFDI4BIOIMAGE1 (the National Research Data Infrastructure focusing on bioimaging in Germany), we want to find viable solutions for storing, processing, analyzing, and sharing bioimaging data. In particular, we want to develop solutions to make findable and machine-readable metadata developing analysis pipelines. In scientific research, such pipelines are crucial for maintaining data integrity, supporting reproducibility, and enabling interdisciplinary collaboration. These tools can be used by different users to retrieve images based on specific attributes as well as support quality control by identifying appropriate metadata. Galaxy, an open-source, web-based platform for data-intensive research, offers a solution by enabling the construction of reproducible pipelines for image analysis2. By integrating popular analysis software like CellProfiler and connecting with cloud services such as OMERO and IDR, Galaxy facilitates the seamless access and management of image data. This capability is particularly valuable in bioimaging, where automated pipelines can streamline the handling of complex metadata, ensuring data integrity and fostering interdisciplinary collaboration. This approach not only increases the efficiency of RDM processes in bioimaging but also contributes to the broader scientific community's efforts to embrace FAIR principles, ultimately advancing scientific discovery and innovation. In the present poster, we showed how to integrate RDM processes and tools in Galaxy. We will showcase how Images can be enriched with metadata (i.e. key-value pairs, tags, raw data, regions of interest) and uploaded to a target OME Remote Objects (OMERO) server using a novel set of OMERO tools developed with Galaxy3. Workflows give the possibility to the user to intuitively fetch images from the local server and perform image analysis (i.e. annotation). Furthermore, we will show the potential integration of eletronic lab books such as eLabFTW4, cloud storage systems (i.e. OneData)5 and interactive norebooks (Jupyter Notebooks) 6 in the Galaxy pipeline.

Tags: Nfdi4Bioimage, Exclude From Dalia

[https://zenodo.org/records/17093454](https://zenodo.org/records/17093454)

[https://doi.org/10.5281/zenodo.17093454](https://doi.org/10.5281/zenodo.17093454)


---

## From Cells to Morphological Profiles A FAIR cloud processing pipeline using Galaxy

Cruz C., Arsenio N., Pham, Thanh Huy, Collin Zimmer, Riccardo Massei, Yi Sun, Paul Czodrowski

Published 2025-12-01

Licensed CC-BY-4.0



Galaxy is an online computational platform used by a global community of thousands of scientists for processing of large-scale data.This collective effort includes the development of the Galaxy software framework, the integration of analysis tools and visualizations, and the operation of public servers that provide access to Galaxy through web browsers (usegalaxy.eu). Galaxy increases the FAIRness of data analysis pipelines by&nbsp; providing versioned tools and workflows that can be annotated, shared and published. Furthermore, Galaxy has a dedicated interface for image data analysis&mdash;imaging.usegalaxy.eu&mdash;providing a comprehensive suite of tools and workflows tailored specifically for imaging scientists. Through the implementation of open source CellProfiler tool into the Galaxy framework, we are creating an interactive evaluation environment for the Cell Painting community. This environment can aid the drug discovery process.

[https://zenodo.org/records/17775957](https://zenodo.org/records/17775957)

[https://doi.org/10.5281/zenodo.17775957](https://doi.org/10.5281/zenodo.17775957)


---

## Modular training resources for bioimage analysis

Christian Tischer, Antonio Politi, Tim-Oliver Buchholz, Elnaz Fazeli, Nicola Gritti, Aliaksandr Halavatyi, Gonzalez Tirado, Sebastian, Julian Hennies, Toby Hodges, Arif Khan, Dominik Kutra, Stefania Marcotti, Bugra Oezdemir, Felix Schneider, Martin Schorb, Anniek Stokkermans, Yi Sun, Nima Vakili

Published 2025-01-21

Licensed CC-BY-4.0



The newly developed image data formats course was taught for the first time: https://github.com/NEUBIAS/training-resources/blob/master/courses/2025_01_EMBL_image_data_formats.md

Tags: Exclude From Dalia

[https://zenodo.org/records/14710820](https://zenodo.org/records/14710820)

[https://doi.org/10.5281/zenodo.14710820](https://doi.org/10.5281/zenodo.14710820)


---

## NFDITalk Cloud based image data science

Josh Moore, Yi Sun

Published 2025-06-02

Licensed UNKNOWN



In this talk, we will be discussing OME-ZARR, a cloud-optimized format for scalable bioimage data management, and BARD,  a cloud virtual desktop that provides a seamless way to run resource-intensive applications in the cloud, enabling users to access powerful computing environments from any device with a web browser.

Tags: Bioimage Analysis, OMERO, Exclude From Dalia

Content type: Video

[https://www.youtube.com/watch?v=bzfmE29S270](https://www.youtube.com/watch?v=bzfmE29S270)


---

## [NFDI Tech Talk] Cloud Based Image Science

Josh Moore, Yi Sun

Published 2025-06-02

Licensed CC-BY-4.0



Slides for the NFDI Tech Talk live streamed to https://www.youtube.com/live/bzfmE29S270
See http://nfdi.de/talks for more information.

Tags: Nfdi4Bioimage, Include In Dalia

[https://zenodo.org/records/15575379](https://zenodo.org/records/15575379)

[https://doi.org/10.5281/zenodo.15575379](https://doi.org/10.5281/zenodo.15575379)


---

## training-resources

Christian Tischer, Antonio Politi, Toby Hodges, maulakhan, grinic, bugraoezdemir, Tim-Oliver Buchholz, Elnaz Fazeli, Aliaksandr Halavatyi, Dominik Kutra, Stefania Marcotti, AnniekStok, Felix, jhennies, Severina Klaus, Martin Schorb, Nima Vakili, Sebastian Gonzalez Tirado, Stefan Helfrich, Yi Sun, Ziqiang Huang, Jan Eglinger, Constantin Pape, Joel Lüthi, Matt McCormick, Oane Gros

Published 2020-04-23T07:51:38+00:00

Licensed CC-BY-4.0



Resources for teaching/preparing to teach bioimage analysis

Tags: Bioimageanalysis, Neurobias, Include In Dalia

Content type: Github Repository

[https://github.com/NEUBIAS/training-resources](https://github.com/NEUBIAS/training-resources)


---

