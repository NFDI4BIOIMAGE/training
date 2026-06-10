# Yi sun (9)
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

## NFDI4BIOIMAGE Interim Progress Report (03/2023 - 02/2026)

Josh Moore, Christian Schmidt, Robert Haase, Jan-Philipp Mallm, Carsten Fortmann-Grote, Thilo Figge, Christian Tischer, Yi Sun, Thomas Zobel, Jens Wendt, Björn Grüning, Susanne Kunis, Markus Blank-Burian, Ami Trivedi, Janina Hanne, von Suchodoletz, Dirk, Michael Scherle, Riccardo Massei, Cornelia Wetzker, Maximilian Müller, Marie Baldenius, Inga Mohr, Vanessa Fuchs, Tobias Gottschall, Michele Bortolomeazzi, Ruman Gerst, Mohsen Ahmadi, Jianxu Chen, Markus Becker, Elisa Ferrando-May, Stefanie Weidtkamp-Peters

Published 2026-06-02

Licensed CC-BY-4.0



Interim Progress Report of the Consortium NFDI4BIOIMAGEPart 1 published at: https://www.dfg.de/en/research-funding/funding-initiative/nfdi/progress-reportsPart 2 published here.
&nbsp;
Biological imaging is a core pillar of modern life science, enabling quantitative insight across scales and disciplines, from molecular biology to medicine. Increasingly, imaging is combined with other data modalities such as genomics and proteomics, positioning bioimaging at the heart of phenomics and integrative research. At the same time, bioimaging experiments are among the largest and most heterogeneous produced in academia, often surpassing terabyte scale. Without shared standards, scalable infrastructure, and coordinated community practices, much of this data risks remaining siloed or non-reusable, limiting its scientific value for the wider research community.&nbsp;NFDI4BIOIMAGE was established to address these challenges by embedding the German bioimaging community within a strong international ecosystem and contributing to long-standing global goals around data acquisition, management, discovery, and publication. Three years into its five-year funding period, NFDI4BIOIMAGE has become a visible and trusted actor in shaping how bioimaging data are standardized, shared, analyzed, and sustained, both nationally and internationally[1]. At its inception, the consortium defined four closely linked objectives, spanning the full bioimaging data lifecycle and aligning national efforts with international developments (Figure 1).
A central objective of NFDI4BIOIMAGE has been to champion open, community-driven standards (Obj. 1) that enable data to be reused across tools, institutions, and scientific domains. The consortium has led the development and international adoption of a Next-Generation File Format (NGFF) through a Request for Comments (RFC) process. This work directly addresses the needs of modern, cloud-scale, and multimodal imaging and has attracted sustained engagement from global partners, including follow-on funding from international sources such as Wellcome and Biohub. NGFF, however, goes beyond a file format, by enabling systematic extension in other ecosystems, like the emerging SpatialData standard for the specific needs of spatially resolved omics. This serves as a blueprint for domain-specific specialization from a shared core standard. In collaboration with the BioImage Archive (BIA) at EBI, the consortium is contributing to interoperable metadata specifications that move bioimaging closer to FAIR Digital Objects (FDOs), or &ldquo;FAIR Image Objects&rdquo; (FAIR-IO). Additional contributions include promotion of REMBI (Recommended Metadata for Biological Images) as a de facto metadata standard, RO-Crate&ndash;based packaging approaches, and expanding our data ambassador model into FAIR data champions who drive community adoption.
To make standards usable in practice, NFDI4BIOIMAGE has invested heavily in scalable, interoperable infrastructure (Obj. 2) supporting both national and international workflows. This includes cloud-ready analysis environments based on Jupyter, object storage, Desktop-as-a-Service (DaaS) and workflow platforms such as Galaxy, enabling reproducible analysis of large imaging datasets across infrastructures. The consortium has supported the migration of major international resources, including the Image Data Resource (IDR), to scalable cloud-based access models and has worked closely with EMBL-EBI to convert BioImage Archive holdings into REMBI-annotated NGFFs, namely OME-Zarr, substantially improving online accessibility and reuse.
At the software level, NFDI4BIOIMAGE has strengthened tools for maximizing reproducible bioimage analysis (Obj. 3), such as Galaxy and JIPipe, adding features including RO-Crate packaging, OME-Zarr support, and OMERO integration to bridge experimental analysis pipelines with FAIR data publication. The BioImage ANalysis Desktop (BAND) has served as a key transitional DaaS platform, bringing users&rsquo; experience closer to their large-scale imaging data in the cloud while maintaining an interactive, reproducible computational environment, which is particularly effective for training and lowering barriers to advanced analysis. The consortium has also engaged with emerging AI ecosystems like Hugging Face, aligning bioimaging workflows with broader developments in machine learning and reproducible research. In parallel, the consortium has supported local data stewardship and storage solutions at multiple German institutions and the operation of federated OMERO services, ensuring national capacity grows in step with international alignment.
A defining strength of NFDI4BIOIMAGE is its emphasis on capacitating researchers through training and data stewardship (Obj. 4). Over the past three years, the consortium has delivered a broad program of training and capacity building, including institutional workshops, national courses, and contributing to major international conferences, and enhanced access to open educational resources for bioimaging RDM. Flagship initiatives such as RDM4mic and I3D:bio have significantly raised awareness and competence around research data management in bioimaging by giving the community a platform to actively engage. NFDI4BIOIMAGE has, furthermore, helped professionalize data stewardship roles through helpdesks and cross-consortia collaboration, supported data submission to the BioImage Archive, and improved discoverability through catalogs of tools, services, and use cases integrated into institutional research structures.
In addition, NFDI4BIOIMAGE contributes actively beyond its consortium. The speaker has chaired the NFDI Konsortialversammlung while members participate broadly in relevant NFDI Sections, notably those focused on metadata (including ontologies, search, and knowledge graphs) and on common infrastructure and data integration. Internationally, consortium members contribute to ISO standardization, provide leadership within the Open Microscopy Environment (OME), and represent bioimaging interests in the European Open Science Cloud (EOSC). Engagement in initiatives such as IO-FAST and foundingGIDE, together with close ties to Global BioImaging, further amplify Germany&rsquo;s visibility in the global imaging landscape. For the final two years of funding, NFDI4BIOIMAGE&rsquo;s priorities include the formal standardization of widely adopted practices for bioimage data, establishment of a national OMERO framework in coordination with de.NBI (underpinned by an MoU), and the development of sustainable operational models for bioimaging data services. While challenges remain, particularly around long-term sustainability and scaling, the consortium has laid a robust foundation. By combining standards, infrastructure, tools, and people, NFDI4BIOIMAGE has positioned Germany as a central contributor to a FAIR, reproducible, globally connected bioimaging ecosystem.



[1] https://youtu.be/7nj2BkRJ8Q0



[https://zenodo.org/records/20509378](https://zenodo.org/records/20509378)

[https://doi.org/10.5281/zenodo.20509378](https://doi.org/10.5281/zenodo.20509378)


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

