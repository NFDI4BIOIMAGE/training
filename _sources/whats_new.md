# Recently added (10)
## A Perspective on FAIR and Scalable Access to Large Image Data

Julia Thönnißen, Sarah Oliveira, Alexander Oberstrass, Jan-Oliver Kropp, Xiao Gui, Christian Schiffer, Timo Dickscheid

Published 2025-08-04

Licensed CC-BY-4.0



The rapid development of new imaging technologies across scientific domains–especially high-throughput technologies–results in a growing volume of image datasets in the Tera- to Petabyte scale. Efficient visualization and analysis of such massive image resources is critical but remains challenging due to the sheer size of the data, its continuous growth, and the limitations of conventional software tools to address these problems. Tools for visualization, annotation and analysis of large image data are confronted with the fundamental dilemma of balancing computational efficiency and memory requirements. Many tools are unable to process large datasets due to memory constraints, requiring workarounds like downsampling. On the other hand, solutions that can handle large data efficiently often rely on specialized or even proprietary file formats, limiting interoperability with other software. This reflects diverging requirements: storage favours compression for efficiency, analysis demands fast data access, and visualization requires tiled, multi-resolution representations. Lacking a unified approach for these conflicting needs, the operation of large and dynamically evolving image repositories in practice often requires undesirable data conversions and costly data duplication. In addressing these challenges, the bioimaging community increasingly adheres to the FAIR principles [1] through national and international initiatives [2], [3], [4]. For example, the Open Microscopy Environment (OME) fosters standards such as OME-TIFF [5] and its cloud-native successor OME-NGFF [6]; BioFormats [7] and OMERO [8] facilitate metadata-rich data handling across diverse platforms; and BrAinPI [9] provides web-based visualization of images via Neuroglancer [10]. These tools represent important developments towards more efficient and standardized use of bioimaging data. However, for very large and dynamically growing repositories, it is still not feasible to settle on a single standard for a subset of these tools, in particular in the light of very diverging needs for massively parallel processing on HPC systems. Therefore, converting data to a single target format is often not a practical solution. We propose a concept for a modular image delivery service which acts as a middleware between large image data resources and applications, serving image data from a cloud resource in multiple requested representations on demand. The service allows reading data stored in different input file formats, applying coordinate transformations and filtering operations on-the-fly, and serving the results in a range of different output formats and layouts. Building upon a common framework for reading and transforming data, an extensible set of access points connects the service to client applications: Lightweight REST APIs allow web-based mutli-resolution access (e.g., in common formats such as used in Neuroglancer and OpenSeadragon base viewers); mountable filesystem interfaces enable linking the repository to file-oriented solutions (e.g., OMERO, ImageJ); and programmatic access from customizable software tools (e.g., Napari). To provide compatibility with upcoming image data standards like BIDS [11] and minimize conversion efforts, the service is able to dynamically expose standard-conform views into arbitrarily organized datasets. The proposed approach for reading and transforming data on-the-fly eliminates the need for redundant storage and application-specific conversions of datasets, improving workflow efficiency and sustainability. In summary, we advocate for the development of a flexible and extensible image data service that supports large-scale analysis, dynamic transformations, multi-tool interoperability, and compatibility with community standards for large image datasets. This way it supports the FAIR principles, reduces integration barriers, meets the performance demands of modern imaging research, and still fosters the use of existing community developments.

[https://zenodo.org/records/16736220](https://zenodo.org/records/16736220)

[https://doi.org/10.5281/zenodo.16736220](https://doi.org/10.5281/zenodo.16736220)


---

## COBA-NIH/2024_Bridging_Imaging_Users_to_Imaging_Analysis_Survey: Survey data with preliminary exploration

Erin Weisbart

Published 2025-09-15

Licensed BSD-3-CLAUSE



Contains the survey data collected through the 2024 Bridging Imaging Users to Imaging Analysis Survey and figures/code from preliminary data exploration of the survey results.

[https://zenodo.org/records/17127544](https://zenodo.org/records/17127544)

[https://doi.org/10.5281/zenodo.17127544](https://doi.org/10.5281/zenodo.17127544)


---

## Cloud-Based Virtual Desktops for Reproducible Research

Yi Sun, Christian Tischer, Kelleher, Harry Alexander, Jean-Karim Heriche

Published 2025-09-10

Licensed CC-BY-4.0



Reproducing computing environments become increasingly challenging in research, especially when compute-intensive scientific workflows require specialised software stacks, specialized hardware (e.g. GPUs), and interactive analysis tools. While traditional high-performance computing (HPC) systems offer scalable resources for batch processing, they don't easily support interactive workflows. On the other hand, workstations have fixed resources  and face workflow deployment challenges because conflicts can occur when multiple tools and dependencies are deployed into the same environment. To address these limitations, we present cloud-based virtual desktop platforms, built on the desktop-as-a-service (DaaS) model, using a containerised, cloud-native approach.  Our platforms offer on-demand, customized desktop environments accessible from any web browser, with dynamic allocation of CPU, memory, and GPU resources for efficient utilization of resources. We introduce two types of virtual desktops: BAND, built on top of a Slurm scheduler and BARD, using Kubernetes. In both cases, containerization ensures consistent and reproducible environments across sessions and pre-installed software improves accessibility for researchers. Deployment and system administration are also simplified through the use of orchestration and automation tools.  Our virtual desktop platforms are particularly valuable for bioimage analysis, which requires complex workflows involving high interactivity, multiple software and GPU acceleration. By combining containerization and cloud-native services, BAND and BARD offer a scalable and sustainable model for delivering interactive, reproducible research environments.

Tags: Nfdi4Bioimage

[https://zenodo.org/records/17092303](https://zenodo.org/records/17092303)

[https://doi.org/10.5281/zenodo.17092303](https://doi.org/10.5281/zenodo.17092303)


---

## Development FAIR image analysis workflows and RDM pipelines in Galaxy

Riccardo Massei, Beatriz Serrano-Solano, Anne Fouilloux, Björg Gruening, Yi Sun, Diana Chiang, Matthias Bernt, Leonid Kostrykin

Published 2025-09-10

Licensed CC-BY-4.0



Imaging is crucial across various scientific disciplines, particularly in life sciences, where it plays a key role in studies ranging from single molecules to whole organisms. However, the complexity and sheer volume of image data present significant challenges. Managing and analyzing this data efficiently requires well-defined image processing tools and analysis pipelines that align with the FAIR principles—ensuring they are findable, accessible, interoperable, and reusable across different domains. In the frame of NFDI4BIOIMAGE1 (the National Research Data Infrastructure focusing on bioimaging in Germany), we want to find viable solutions for storing, processing, analyzing, and sharing bioimaging data. In particular, we want to develop solutions to make findable and machine-readable metadata developing analysis pipelines. In scientific research, such pipelines are crucial for maintaining data integrity, supporting reproducibility, and enabling interdisciplinary collaboration. These tools can be used by different users to retrieve images based on specific attributes as well as support quality control by identifying appropriate metadata. Galaxy, an open-source, web-based platform for data-intensive research, offers a solution by enabling the construction of reproducible pipelines for image analysis2. By integrating popular analysis software like CellProfiler and connecting with cloud services such as OMERO and IDR, Galaxy facilitates the seamless access and management of image data. This capability is particularly valuable in bioimaging, where automated pipelines can streamline the handling of complex metadata, ensuring data integrity and fostering interdisciplinary collaboration. This approach not only increases the efficiency of RDM processes in bioimaging but also contributes to the broader scientific community's efforts to embrace FAIR principles, ultimately advancing scientific discovery and innovation. In the present poster, we showed how to integrate RDM processes and tools in Galaxy. We will showcase how Images can be enriched with metadata (i.e. key-value pairs, tags, raw data, regions of interest) and uploaded to a target OME Remote Objects (OMERO) server using a novel set of OMERO tools developed with Galaxy3. Workflows give the possibility to the user to intuitively fetch images from the local server and perform image analysis (i.e. annotation). Furthermore, we will show the potential integration of eletronic lab books such as eLabFTW4, cloud storage systems (i.e. OneData)5 and interactive norebooks (Jupyter Notebooks) 6 in the Galaxy pipeline.

Tags: Nfdi4Bioimage

[https://zenodo.org/records/17093454](https://zenodo.org/records/17093454)

[https://doi.org/10.5281/zenodo.17093454](https://doi.org/10.5281/zenodo.17093454)


---

## Image Analysis in Healthcare - The Current Landscape, Trends, and Collaborative Opportunities

Martin Schätz, Pérez Koldenkova, Vadim

Published 2025-09-09

Licensed CC-BY-4.0



Workshop presentation from XXXIV Foro de Investigaci&oacute;n en Salud 2025.

[https://zenodo.org/records/17080219](https://zenodo.org/records/17080219)

[https://doi.org/10.5281/zenodo.17080219](https://doi.org/10.5281/zenodo.17080219)


---

## Linking of Research (Meta-)data in OMERO to Foster FAIR Data in Plasma Science

Robert Wagner, Mohsen Ahmadi, Dagmar Waltemath, Kristina Yordanova, Becker, Markus M.

Published 2025-09-10

Licensed CC-BY-4.0



Applied plasma research involves several disciplines such as physics, medicine and biology to solve application-oriented problems, often generating large and heterogeneous experimental data sets. The descriptions and metadata describing these interdisciplinary scientific investiga-tions is stored in distributed systems (e.g., physical laboratory notebooks or electronic labora-tory notebooks (ELN) like eLabFTW [1]), and the experimental data are either stored locally within the laboratories or on centralized institutional storage systems. As a result, the collected information often has to be tediously assembled for processing into publications. The workflow represented in Figure 1 addresses this suboptimal situation and promotes the combination of the image database OMERO [2], the ELN system eLabFTW, the research data management tool Adamant [3] and Python scripts for handling microscopy images in plasma life science and plasma medicine [4]. This workflow highlights how the developments from the NFDI4BIOIMAGE consortium can be brought into practical applications by addressing the specific demands of plasma science, where domain-specific metadata is essential for effective data interpretation and reuse. It showcases the benefits of FAIR [5] metadata combining do-main-specific requirements with method-specific solutions. Similar to most imaging workflows, image analysis in plasma research requires metadata from several sections of the experiment. Moreover, the plasma-related metadata are essential for the experimental context and must be included in the analysis, e.g. to describe the influence of plasma on the treated sample. Therefore, the metadata schema Plasma-MDS [6] is adapted to collect plasma-related metadata, such as information on the plasma species having a major impact on the treated samples. Alongside Plasma-MDS, the Recommended Metadata for Bio-logical Images (REMBI) standard [7] is used for the biological metadata such as the sample preparation and treatment procedures. The collection of these metadata is realized using Adamant, which enables the beginner-friendly collection of structured metadata. The tool presents JSON schemas in easy-to-read and easy-to-fill HTML forms, enabling metadata validation. Once completed and validated, the metadata are uploaded directly to eLabFTW using Adamant's workflow functionalities. The images from the treated samples are uploaded to OMERO by OMERO.insight and afterwards automatically annotated via Python scripts. These scripts take previously collected metadata from the related eLabFTW experiments and the microscope description metadata collected by the Micro Meta App [8], which are also stored in eLabFTW. The metadata is categorized and annotated according to the various data organizational levels within OMERO, specifically fo-cusing on project and dataset hierarchies, as well as screens that are composed of plates, which in turn contain wells. Screens resemble microwell plates, commonly used in a variety of biological experiments. The hieraic organization of metadata significantly enhances the ease of reusing images and associated metadata for subsequent processing and analysis. By efficiently distributing and reducing large metadata sets to an acceptable level, while simultaneously eliminating redun-dancies, this approach facilitates straightforward analyses with tools like ImageJ [9] and FIJI [10], thanks to the close association of metadata with the images themselves. In summary, one of the application-specific developments within the NFDI4BIOIMAGE consor-tium is presented, which contributes to the adoption of the FAIR principles in laboratory envi-ronments. Further work will address the integration of ontologies for the semantic description of data and metadata.

Tags: Nfdi4Bioimage, Bioimage Analysis

[https://zenodo.org/records/17092348](https://zenodo.org/records/17092348)

[https://doi.org/10.5281/zenodo.17092348](https://doi.org/10.5281/zenodo.17092348)


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

[https://zenodo.org/records/16979744](https://zenodo.org/records/16979744)

[https://doi.org/10.5281/zenodo.16979744](https://doi.org/10.5281/zenodo.16979744)


---

## NFDI4BIOIMAGE Calendar January 2025

Lea Miebach, Sander Bekeschus

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar January 2025.
A Heart for Redox Biology: The image of primary bone mesenchymal stromal/stem cells (hBM-MSCs) was captured in a study evaluating the cellular effects of therapeutic oxidation in the context of regenerative medicine. The cells were isolated from an arthroplasty patient cohort in a joint research project between the Center for Orthopaedics at University Medical Center and the group ZIK plasmatis at the Leibniz Institute for Plasma Science and Technology (INP) in Greifswald. You can appreciate the characteristic morphology and complex actin cytoskeleton that is crucial for the cellular function of hBM-MSCs. Can you spot the heart that is formed by the prominent actin protrusions of interconnected cells?
Image Metadata (using REMBI template):




Study Component




Imaging method


Spinning-disc confocal mode, epifluorescence




Biosample




Biological entity


Bone marrow-mesenchymal stem cells (BM-MSCs)




Organism


Homo sapiens




Specimen




Preparation method


Fixation (4% PFA)




Signal/contrast mechanism


Fluorescence




Channel 1 &ndash; content


4',6-Diamidin-2-phenylindol (DAPI; Thermo Fisher, USA), blue




Channel 1 &ndash; biological entity


Nuclei




Channel 2 &ndash; content


MitoSpy Green (Biolegend, USA), green




Channel 2 &ndash; biological entity


Mitochondria




Channel 3 &ndash; content


Flash Phalloidin Red (Biolegend, USA), orange




Channel 3 &ndash; biological entity


Actin




Image acquisition




Microscope model


Operetta CLS (PerkinElmer, USA)




Image data




Type


Raw and processed image in comparison




Magnification


20x air objective (NA = 0.8)




Excitation


Channel 1: 365 nm; Channel 2: 475 nm; Channel 3: 550 nm




Detection


Channel 1: 465 nm; Channel 2: 525 nm; Channel 3: 610 nm




Analysed data




Image processing method


Algorithm-based, unsupervised image segmentation with Harmony 4.9 analysis software (PerkinElmer, USA)




Submitted via NFDI4BIOIMAGE





[https://zenodo.org/records/16980217](https://zenodo.org/records/16980217)

[https://doi.org/10.5281/zenodo.16980217](https://doi.org/10.5281/zenodo.16980217)


---

## Reproducible Bio-Image Analysis using Python, Napari, Jupyter and AI

Robert Haase

Published 2025-09-09

Licensed CC-BY-4.0



In this slide deck we learn how to write reproducible bio-image analysis code in Jupyter notebooks. Goal is not just to have code running elsewhere reproducibly, but also enabling others to understand workflows to enable them reproducing the analysis also in their mind and potentially other tools. Additionally we cover how to generate Jupyter notebooks from Napari and using artificial intelligence, namely bia-bob.

Tags: Nfdi4Bioimage, Bioimage Analysis

[https://zenodo.org/records/17085991](https://zenodo.org/records/17085991)

[https://doi.org/10.5281/zenodo.17085991](https://doi.org/10.5281/zenodo.17085991)


---

## embo-bia-2025

Kevin Yamauchi

Published 2025-08-18T09:32:20+00:00

Licensed BSD-3-CLAUSE





Tags: Todo

Content type: Github Repository

[https://github.com/kevinyamauchi/embo-bia-2025](https://github.com/kevinyamauchi/embo-bia-2025)


---

