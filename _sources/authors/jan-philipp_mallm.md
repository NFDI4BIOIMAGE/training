# Jan-philipp mallm (5)
## Introducing OMERO-vitessce: an OMERO.web plugin for multi-modal data

Michele Bortolomeazzi, Christian Schmidt, Jan-Philipp Mallm

Published 2025-02-07

Licensed CC-BY-4.0



omero-vitessce: an OMERO.web plugin for multi-modal data viewing.
OMERO is the most used research data management system (RDM) in the bioimaging domain, and has been adopted as a centralized RDM solution by several academic and research institutions. A main reason for this is the ability to directly view and annotate images from a web-based interface. However, this feature of OMERO is currently underpowered for the visualization of very large or multimodal datasets. These datasets, are becoming a more and more common foundation for biological and biomedical studies, due to the recent developments in imaging, and sequencing technologies which enabled their application to spatial-omics. In order to begin to provide this multimodal-data capability to OMERO, we developed omero-vitessce (https://github.com/NFDI4BIOIMAGE/omero-vitessce/tree/main), a new OMERO.web plugin for viewing data stored in OMERO with the Vitessce (http://vitessce.io/) multimodal data viewer. omero-vitessce can be installed as an OMERO.web plugin with PiPy (https://pypi.org/project/omero-vitessce/), and allows users to set up interactive visualizations of their images of cells and tissues through interactive plots which are directly linked to the image. This enables the visual exploration of bioimage-analysis results and of multimodal data such as those generated through spatial-omics experiments. The data visualization is highly customizable and can be configured not only through custom configuration files, but also with the graphical interface provided by the plugin, thus making omero-vitessce a highly user-friendly solution for multimodal data viewing. most biological datasets. We plan to extend the interoperability of omero-vitessce with the OME-NGFF and SpatialData file formats to leverage the efficiency of these cloud optimized formats.
The three files in this Zenodo Record are all the same poster saved in different format all with high resolution images.

Tags: Nfdi4Bioimage, Exclude From Dalia

[https://zenodo.org/records/14832855](https://zenodo.org/records/14832855)

[https://doi.org/10.5281/zenodo.14832855](https://doi.org/10.5281/zenodo.14832855)


---

## NFDI4BIOIMAGE Calendar Cover 2025

Anne Rademacher, Alik Huseynov, Michele Bortolomeazzi, Wille, Sina Jasmin, Sabrina Schumacher, Pooja Sant, Denise Keitel, Konstantin Okonechnikov, Ghasemi, David R., Pajtler, Kristian W., Jan-Philipp Mallm, Karsten Rippe

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar Cover 2025.
The image is a visualization showing the integration of multimodal data including a spinning disk confocal image and gene expression data from a spatial transcriptomic experiment on a human medulloblastoma sample. The microscopy image of the tissue with the nuclei in white has been overlayed with the result of the cell segmentation colored according to the assigned cell type (immune cells: red, stromal cells: violet, brain cells: cyan/blue, tumor cells: green). A subset of transcripts for three genes whose expression varies across the different cell types in the tissue have been represented as colored dots (CD4 (immune cells): red, PTCH1 (tumor cells): green, AQP4 (brain cells): blue).
Image Metadata (using REMBI template):




Study




Study description


Comparison of spatial transcriptomics technologies for medulloblastoma cryosection




Study type


Spatial Transcriptomics (Xenium) on medulloblastoma cryosections




Study Component




Imaging method


Xenium and Spinning disk confocal microscopy




Study component description


Datasets with raw and processed data from the study "Comparison of spatial transcriptomics technologies for medulloblastoma cryosections" including Xenium and spinning disk confocal microscopy data




Biosample




Identity


MB266




Biological entity


Human cerebellum from a patient with Medulloblastoma with extensive nodularity




Organism


Homo sapiens




Specimen




Experimental status


Patient sample




Preparation method


10 &micro;m cryosections were acquired using the cryostar NX50 with a cutting temperature of -15 &deg;C. Tissues were section in 10 &micro;m slices and four samples were placed on one Xenium slide. Subsequently, the tissue was fixed with PFA according to the manufacture&acute;s protocol. Tissues were permeabilized with SDS, incubated in 70% ice cold methanol and washed with PBS. Hybridization of the human generic brain panel with 70 add-on genes (Supplementary Dataset 1) was performed at 50&deg;C in a Bio-Rad C1000 touch cycler for 20 hours. Washing, ligation and amplification steps were carried out according to the manufacturer&rsquo;s instructions. ROIs were selected according to the tissue area excluding non-tissue covered tiles. Each transcript was imaged in a bright state five times across 60 cycle-channels (15 cycles x 4 channels). After the run on the Xenium analyzer slides were removed and buffer exchanged with PBS-T for further storage at 4&deg;C.




Signal/contrast mechanism


Fluorescence




Channel 1 &ndash; content


DAPI




Channel 1 &ndash; biological entity


Nuclei (DNA)




Image acquisition




Instrument attributes


Imaging of RNAscope samples and reimaging of Xenium slides by SDCM was conducted on an Andor Dragonfly 505 spinning disk confocal system equipped with a Nikon Ti2-E inverted microscope and a CFI P-Fluor 40X/1.30 oil objective or a Plan Apo 60x/1.40 oil objective. Multicolor images were acquired with the following laser lines 405 nm (DAPI), 488 nm (Alexa 488, eosin), 561 nm (Atto 550), 637 nm (Atto 647) 730nm (Alexa 750).




Image acquisition parameters


Images were recorded at 16-bit depth and with 1024x1024 pixels dimensions (pixel size: 0.217 &micro;m) using an iXon Ultra 888 EM-CCD camera. The region of interest was selected based on the DAPI signal and 50 z-slices were acquired with a step size of 0.4&thinsp;&micro;m (20&thinsp;&micro;m z-range) per field of view (FOV). Tiles were imaged with a 10% overlap to ensure accurate stitching.




Image data




Type


Figure




Format &amp; compression


PNG




Size description


8800x8788+0+0 pixels (Primary image)




Pixel/voxel size description


0.217 &micro;m (Primary image)




Channel information


RGB




Image processing method


Tiles were imaged with a 10% overlap to ensure accurate stitching. Subsequently, a flatfield-correction was conducted based on the DAPI channel and stitching and registration of the tiles was conducted with Fiji. First, SDCM image stacks were subjected to a maximum intensity projection, followed by flat field and chromatic aberration correction using a custom script. Next, image tiles were stitched using the &ldquo;Grid/Collection Stitching&rdquo; plugin. DAPI images from SDCM were registered to MC or Xenium widefield images using &ldquo;Register Virtual Stack Slices&rdquo; with Affine feature extraction model and the Elastic bUnwarpJ splines registration model. In case of further staining, images were transformed via Transform Virtual Stack slices employing the transformation file of the DAPI registration.




Image Correlation




Spatial and temporal alignment


The region of interest was selected based on the DAPI signal and 50 z-slices were acquired with a step size of 0.4 &micro;m (20 &micro;m z-range) per field of view (FOV). Tiles were imaged with a 10% overlap to ensure accurate stitching. Subsequently, a flatfield-correction was conducted based on the DAPI channel and stitching and registration of the tiles was conducted with Fiji (https://github.com/RippeLab/MBEN/tree/main/stitching) (https://github.com/RippeLab/MBEN/tree/main/Registration).




Related images and relationship


MB266-morphology_mip.ome.tif at https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD1093




Analysed data




Analysis result type


Figure




Data used for analysis


MB266-transcripts.csv.gz, MB266-transcripts.csv.gz at https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD1093




Analysis method and details


Most of the analysis and visualization (including tidyverse, data.table, ggridges R packages) was done in R 4.2.2. Raw data were processed using technology-specific corporate pipelines (custom pipeline was used for MC). For each technology Seurat objects of the sample data and analysis results were created using the Seurat (v. 4.3.0) R package (https://github.com/scOpenLab/spatial_analysis/tree/main)




Submitted via NFDI4BIOIMAGE




&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/16979744](https://zenodo.org/records/16979744)

[https://doi.org/10.5281/zenodo.16979744](https://doi.org/10.5281/zenodo.16979744)


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

## The role of Helmholtz Centers in NFDI4BIOIMAGE - A national consortium enhancing FAIR data management for microscopy and bioimage analysis

Riccardo Massei, Christian Schmidt, Michele Bortolomeazzi, Julia Thoennissen, Jan Bumberger, Timo Dickscheid, Jan-Philipp Mallm, Elisa Ferrando-May

Published 2024-06-06

Licensed CC-BY-4.0



Germany&rsquo;s National Research Data Infrastructure (NFDI) aims to establish a sustained, cross-disciplinary research data management (RDM) infrastructure that enables researchers to handle FAIR (findable, accessible, interoperable, reusable) data. While&nbsp;FAIR principles have been&nbsp;adopted by funders, policymakers, and publishers, their practical implementation remains an ongoing effort. In the field of bio-imaging, harmonization of&nbsp;data formats, metadata ontologies, and open data repositories is necessary&nbsp;to achieve FAIR data.&nbsp;The NFDI4BIOIMAGE was established&nbsp;to address these issues and&nbsp;develop tools and best practices to facilitate FAIR microscopy and image analysis data in alignment with international community activities. The&nbsp;consortium operates through its Data Stewards team to provide expertise and direct support to help overcome RDM challenges. The three Helmholtz Centers in NFDI4BIOIMAGE aim to collaborate closely with other centers and initiatives, such as HMC, Helmholtz AI, and HIP. Here we present NFDI4BIOIMAGE&rsquo;s work and its significance for research in Helmholtz and beyond

Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

[https://zenodo.org/records/11501662](https://zenodo.org/records/11501662)

[https://doi.org/10.5281/zenodo.11501662](https://doi.org/10.5281/zenodo.11501662)


---

## [Workshop] Managing FAIR microscopy data at scale for universities and research institutions: an introduction for non-imaging stakeholders

Christian Schmidt, Michele Bortolomeazzi, Ksenia Krooß, Jan-Philipp Mallm, Elisa Ferrando-May, Stefanie Weidtkamp-Peters

Published 2025-03-14

Licensed CC-BY-4.0



These slides were used in a workshop at the 2025 E-Science Tage in Heidelberg.
Workshop Abstract:
Effective Research Data Management (RDM) requires collaboration between infrastructure providers, support units, and domain-specific experts across scientific disciplines. Microscopy, or bioimaging, is a widely used technology at universities and research institutions, generating large, multi-dimensional datasets. Scientists now routinely produce microscopy data using advanced imaging modalities, often through centrally-provided instruments maintained by core facilities.
Bioimaging data management presents unique challenges: files are often large (e.g., 15+ GB for whole slide images), come in various proprietary formats, and are accessed frequently for viewing as well as for complex image processing and analysis workflows. Collaboration between experimenters, clinicians, group leaders, core facility staff, and image analysts adds to the complexity, increasing the risk of data fragmentation and metadata loss.
The DFG-funded project I3D:bio and the consortium NFDI4BIOIMAGE, part of Germany&rsquo;s National Research Data Infrastructure (NFDI), are addressing these challenges by developing solutions and best practices for managing large, complex microscopy datasets. This workshop introduces the challenges of bioimaging RDM to institutional support personnel, including, for example, library staff, IT departments, and data stewards. Participants will explore the bioimaging RDM system OMERO, and apply structured metadata annotation and object-oriented data organization to a simple training dataset. OMERO offers centralized, secure access to data, allowing collaboration and reducing the data fragementation risk. Moreover, participants will experience the benefits of OME-Zarr, a chunked open file format designed for FAIR data sharing and remote access. OME-Zarr enables streaming of large, N-dimensional array-typed data over the Internet without the need to download whole files. An expanding toolbox for leveraging OME-Zarr for bioimaging data renders this file type a promising candidate for a standard file format suitable for use in FAIR Digital Object (FDO) implementations for microscopy data. OME-Zarr has become a pillar for imaging data sharing in two bioimaging-specific data repositories, i.e., the Image Data Resource (IDR) and the BioImage Archive (BIA). The team of Data Stewards from both abovenmentioned projects help researchers and research support staff to manage und publish bioimaging data.
By the end of the workshop, participants will have gained hands-on experience with bioimaging data and will be aware of support resources like the NFDI4BIOIMAGE Help Desk for addressing specific local use cases. Our goal is to promote collaboration across disciplines to effectively manage complex bioimaging data in compliance with the FAIR principles.
&nbsp;









Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

[https://zenodo.org/records/15026373](https://zenodo.org/records/15026373)

[https://doi.org/10.5281/zenodo.15026373](https://doi.org/10.5281/zenodo.15026373)


---

