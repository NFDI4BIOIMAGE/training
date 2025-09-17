# Mohsen ahmadi (4)
## Bioimaging workflow based on OMERO, eLabFTW, and Adamant for integrating images with multimodal metadata

Mohsen Ahmadi, Robert Wagner, Sander Bekeschus, Becker, Markus M.

Published 2025-07-29

Licensed CC-BY-4.0



This research data management workflow for bioimaging is designed to bridge the gap between image metadata and experimental / process metadata. By linking images and microscopy-related metadata with broader experimental records, the workflow particularly supports the adoption of the FAIR (Findable, Accessible, Interoperable, Reusable) data principles in interdisciplinary fields where bioimaging is used to analyse treated samples requiring multimodal metadata. A Jupyter Notebook guides the user through the metadata level, data handling level, and data processing level and connects various software components in a modular manner. On the metadata level, microscope-specific metadata are captured using the Micro-Meta App and stored as reusable digital assets. Adamant provides a user interface to collect and process schema-based metadata related to the experiment / treatment procedure. Structured imaging and process metadata are attached to the complete experiment description in eLabFTW. On the data handling level, OMERO serves as the central platform for storing and managing microscopy images together with their metadata retrieved from eLabFTW (workflow with ELN) or directly from JSON files (workflow without ELN). On the data processing level, OMERO supports both automated and manual image analysis either directly via the Jupyter Notebook or FIJI. Due to the modularity of the workflow, the integrated tools can be substituted with equivalent systems based on institutional / user requirements. Whether in teaching or research settings, this workflow supports high-throughput, reproducible imaging workflows, ensuring that data, metadata, and analysis steps remain transparent, interoperable, and reusable across diverse bioimage analysis platforms.

Tags: Nfdi4Bioimage, Exclude From Dalia

[https://zenodo.org/records/16561545](https://zenodo.org/records/16561545)

[https://doi.org/10.5281/zenodo.16561545](https://doi.org/10.5281/zenodo.16561545)


---

## Data stewardship and research data management tools for multimodal linking of imaging data in plasma medicine

Mohsen Ahmadi, Robert Wagner, Philipp Mattern, Nick Plathe, Sander Bekeschus, Markus M. Becker, Torsten Stöter, Stefanie Weidtkamp-Peters

Published 2023-11-03

Licensed CC-BY-4.0



A more detailed understanding of the effect of plasmas on biological systems can be fostered by combining data from different imaging modalities, such as optical imaging, fluorescence imaging, and mass spectrometry imaging. This, however, requires the implementation and use of sophisticated research data management (RDM) solutions to incorporate the influence of plasma parameters and treatment procedures as well as the effects of plasma on the treated targets. In order to address this, RDM activities on different levels and from different perspectives are started and brought together within the framework of the NFDI consortium NFDI4BIOIMAGE.

Tags: Include In Dalia

[https://zenodo.org/records/10069368](https://zenodo.org/records/10069368)

[https://doi.org/10.5281/zenodo.10069368](https://doi.org/10.5281/zenodo.10069368)


---

## Linking of Research (Meta-)data in OMERO to Foster FAIR Data in Plasma Science

Robert Wagner, Mohsen Ahmadi, Dagmar Waltemath, Kristina Yordanova, Becker, Markus M.

Published 2025-09-10

Licensed CC-BY-4.0



Applied plasma research involves several disciplines such as physics, medicine and biology to solve application-oriented problems, often generating large and heterogeneous experimental data sets. The descriptions and metadata describing these interdisciplinary scientific investiga-tions is stored in distributed systems (e.g., physical laboratory notebooks or electronic labora-tory notebooks (ELN) like eLabFTW [1]), and the experimental data are either stored locally within the laboratories or on centralized institutional storage systems. As a result, the collected information often has to be tediously assembled for processing into publications. The workflow represented in Figure 1 addresses this suboptimal situation and promotes the combination of the image database OMERO [2], the ELN system eLabFTW, the research data management tool Adamant [3] and Python scripts for handling microscopy images in plasma life science and plasma medicine [4]. This workflow highlights how the developments from the NFDI4BIOIMAGE consortium can be brought into practical applications by addressing the specific demands of plasma science, where domain-specific metadata is essential for effective data interpretation and reuse. It showcases the benefits of FAIR [5] metadata combining do-main-specific requirements with method-specific solutions. Similar to most imaging workflows, image analysis in plasma research requires metadata from several sections of the experiment. Moreover, the plasma-related metadata are essential for the experimental context and must be included in the analysis, e.g. to describe the influence of plasma on the treated sample. Therefore, the metadata schema Plasma-MDS [6] is adapted to collect plasma-related metadata, such as information on the plasma species having a major impact on the treated samples. Alongside Plasma-MDS, the Recommended Metadata for Bio-logical Images (REMBI) standard [7] is used for the biological metadata such as the sample preparation and treatment procedures. The collection of these metadata is realized using Adamant, which enables the beginner-friendly collection of structured metadata. The tool presents JSON schemas in easy-to-read and easy-to-fill HTML forms, enabling metadata validation. Once completed and validated, the metadata are uploaded directly to eLabFTW using Adamant's workflow functionalities. The images from the treated samples are uploaded to OMERO by OMERO.insight and afterwards automatically annotated via Python scripts. These scripts take previously collected metadata from the related eLabFTW experiments and the microscope description metadata collected by the Micro Meta App [8], which are also stored in eLabFTW. The metadata is categorized and annotated according to the various data organizational levels within OMERO, specifically fo-cusing on project and dataset hierarchies, as well as screens that are composed of plates, which in turn contain wells. Screens resemble microwell plates, commonly used in a variety of biological experiments. The hieraic organization of metadata significantly enhances the ease of reusing images and associated metadata for subsequent processing and analysis. By efficiently distributing and reducing large metadata sets to an acceptable level, while simultaneously eliminating redun-dancies, this approach facilitates straightforward analyses with tools like ImageJ [9] and FIJI [10], thanks to the close association of metadata with the images themselves. In summary, one of the application-specific developments within the NFDI4BIOIMAGE consor-tium is presented, which contributes to the adoption of the FAIR principles in laboratory envi-ronments. Further work will address the integration of ontologies for the semantic description of data and metadata.

Tags: Nfdi4Bioimage, Bioimage Analysis, Exclude From Dalia

[https://zenodo.org/records/17092348](https://zenodo.org/records/17092348)

[https://doi.org/10.5281/zenodo.17092348](https://doi.org/10.5281/zenodo.17092348)


---

## Who you gonna call? - Data Stewards to the rescue

Vanessa Aphaia Fiona Fuchs, Jens Wendt, Maximilian Müller, Mohsen Ahmadi, Riccardo Massei, Cornelia Wetzker

Published 2024-03-01

Licensed CC-BY-4.0



The Data Steward Team of the NFDI4BIOIMAGE consortium presents themselves and the services (including the Helpdesk) that we offer.

Tags: Exclude From Dalia

[https://zenodo.org/records/10730424](https://zenodo.org/records/10730424)

[https://doi.org/10.5281/zenodo.10730424](https://doi.org/10.5281/zenodo.10730424)


---

