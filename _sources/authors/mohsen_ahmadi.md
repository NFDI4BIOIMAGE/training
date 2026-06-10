# Mohsen ahmadi (9)
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

## Data stewardship for Bio-Image Research Data Management Support and Training at RDM4mic Meeting 2025

Cornelia Wetzker, Vanessa Fuchs, Jens Wendt, Mohsen Ahmadi, Maximilian E. Müller, Riccardo Massei

Published 2025-10-29

Licensed CC-BY-4.0



Talk at the RDM4mic Meeting 2025 in Münster, Germany, about the importance of Research Data Management (RDM) for microscopy and the role of NFDI4BIOIMAGE in supporting researchers with tools and services for RDM in bioimaging.

Tags: Research Data Management, Include In Dalia

Content type: Slides

[https://zenodo.org/records/17472821](https://zenodo.org/records/17472821)


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

## NFDI4BIOIMAGE Helpdesk Deutschlandkarte

Fuchs, Vanessa Aphaia Fiona, Jens Wendt, Müller, Maximilian E., Cornelia Wetzker, Mohsen Ahmadi, Riccardo Massei

Published 2026-03-12

Licensed CC-BY-4.0



[https://zenodo.org/records/18953151](https://zenodo.org/records/18953151)

[https://doi.org/10.5281/zenodo.18953151](https://doi.org/10.5281/zenodo.18953151)


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

## RDM4mic Meeting 2025 Talks

Cornelia Wetzker, Vanessa Fuchs, Jens Wendt, Mohsen Ahmadi, Maximilian E. Müller, Riccardo Massei, David Schwartz, Joost Willemse, Bettina Hagen, Thomas Zobel, Susanne Kunis, Peter Zentis, Niraj Kandpal, Tom Boissonnet

Published 2026-01-12

Licensed UNKNOWN



Talk Series RDM4mic Meeting 2025 in Münster, Germany about RDM and the role of NFDI4BIOIMAGE in supporting researchers with tools and services for RDM in bioimaging.

Tags: Research Data Management, Include In Dalia

Content type: Video

[https://www.youtube.com/playlist?list=PL2k-L-zWPoR67_02CuEROsYr1nnCNgMcI](https://www.youtube.com/playlist?list=PL2k-L-zWPoR67_02CuEROsYr1nnCNgMcI)


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

## [TiM2025] Hands-on: Creating Bio-image Overviews with OMERO.figure

Cornelia Wetzker, Mohsen Ahmadi, Ksenia Krooß, Jens Wendt, Tom Boissonnet

Published 2026-06-09

Licensed CC-BY-4.0



The slides are part of a hands-on session that demonstrates the usage of OMERO.figure to create overviews of microscopy images and datasets presented at the Workshop Data Stewardship in Microscopy at the Trends in Microscopy 2025.
Usage of the material in self learning:
To be able to follow the hands-on material, find the 3 example datasets of the workshop openly accessible in a public user space of an OMERO instance at the University of M&uuml;nster via this link: https://omero-tim.gerbi-gmb.de/webclient/?show=dataset-25739
Alternatively, open the tool omero.figure in this instance directly (https://omero-tim.gerbi-gmb.de/figure/) and add one of the datasets by providing its id: 105986. (see the slides for details)
Origin of the microscopy dataset:
The datasets originate from a project dealing with fluorescence lifetime imaging microscopy (FLIM) and its possible application to distinguish spectrally overlapping fluorophores based on their lifetimes.&nbsp;The scientific context and further processing of the image datasets are described in the following publication: https://doi.org/10.1111/jmi.70036
The complete bioimage dataset including experimental, microscopy and image analysis metadata can be found on the BioImage Archive: https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD1967

[https://zenodo.org/records/20610539](https://zenodo.org/records/20610539)

[https://doi.org/10.5281/zenodo.20610539](https://doi.org/10.5281/zenodo.20610539)


---

