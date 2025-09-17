# Michele bortolomeazzi (18)
## BHG2023-OMERO-ARC

Andrea Schrader, Michele Bortolomeazzi, Niraj Kandpal, Torsten Stöter, Kevin Schneider, Peter Zentis, Josh Moore, Jeam-Marie Burel, Tom Boissonnet

Licensed CC-BY-4.0



Repository for documentation during the 2nd de.NBI BioHackathon Germany - 11.-15.12.2023 - OMERO-ARC project (in short: BHG2023-OMERO-ARC)

Tags: Nfdi4Bioimage, Bioinformatics, OMERO

Content type: Github Repository

[https://github.com/NFDI4BIOIMAGE/BHG2023-OMERO-ARC](https://github.com/NFDI4BIOIMAGE/BHG2023-OMERO-ARC)


---

## I3D:bio's OMERO training material: Re-usable, adjustable, multi-purpose slides for local user training

Christian Schmidt, Michele Bortolomeazzi, Tom Boissonnet, Carsten Fortmann-Grote, Julia Dohle, Peter Zentis, Niraj Kandpal, Susanne Kunis, Thomas Zobel, Stefanie Weidtkamp-Peters, Elisa Ferrando-May

Published 2023-11-13

Licensed CC-BY-4.0



The open-source software OME Remote Objects (OMERO) is a data management software that allows storing, organizing, and annotating bioimaging/microscopy data. OMERO has become one of the best-known systems for bioimage data management in the bioimaging community. The Information Infrastructure for BioImage Data (I3D:bio) project facilitates the uptake of OMERO into research data management (RDM) practices at universities and research institutions in Germany. Since the adoption of OMERO into researchers' daily routines requires intensive training, a broad portfolio of training resources for OMERO is an asset. On top of using the OMERO guides curated by the Open Microscopy Environment Consortium (OME) team, imaging core facility staff at institutions where OMERO is used often prepare additional material tailored to be applicable for their own OMERO instances. Based on experience gathered in the Research Data Management for Microscopy group (RDM4mic) in Germany, and in the use cases in the I3D:bio project, we created a set of reusable, adjustable, openly available slide decks to serve as the basis for tailored training lectures, video tutorials, and self-guided instruction manuals directed at beginners in using OMERO. The material is published as an open educational resource complementing the existing resources for OMERO contributed by the community.

Tags: OMERO, Research Data Management, Nfdi4Bioimage, I3Dbio

Content type: Slides, Video

[https://zenodo.org/records/8323588](https://zenodo.org/records/8323588)

[https://www.youtube.com/playlist?list=PL2k-L-zWPoR7SHjG1HhDIwLZj0MB_stlU](https://www.youtube.com/playlist?list=PL2k-L-zWPoR7SHjG1HhDIwLZj0MB_stlU)

[https://doi.org/10.5281/zenodo.8323588](https://doi.org/10.5281/zenodo.8323588)


---

## Introducing OMERO-vitessce: an OMERO.web plugin for multi-modal data

Michele Bortolomeazzi, Christian Schmidt, Jan-Philipp Mallm

Published 2025-02-07

Licensed CC-BY-4.0



omero-vitessce: an OMERO.web plugin for multi-modal data viewing.
OMERO is the most used research data management system (RDM) in the bioimaging domain, and has been adopted as a centralized RDM solution by several academic and research institutions. A main reason for this is the ability to directly view and annotate images from a web-based interface. However, this feature of OMERO is currently underpowered for the visualization of very large or multimodal datasets. These datasets, are becoming a more and more common foundation for biological and biomedical studies, due to the recent developments in imaging, and sequencing technologies which enabled their application to spatial-omics. In order to begin to provide this multimodal-data capability to OMERO, we developed omero-vitessce (https://github.com/NFDI4BIOIMAGE/omero-vitessce/tree/main), a new OMERO.web plugin for viewing data stored in OMERO with the Vitessce (http://vitessce.io/) multimodal data viewer. omero-vitessce can be installed as an OMERO.web plugin with PiPy (https://pypi.org/project/omero-vitessce/), and allows users to set up interactive visualizations of their images of cells and tissues through interactive plots which are directly linked to the image. This enables the visual exploration of bioimage-analysis results and of multimodal data such as those generated through spatial-omics experiments. The data visualization is highly customizable and can be configured not only through custom configuration files, but also with the graphical interface provided by the plugin, thus making omero-vitessce a highly user-friendly solution for multimodal data viewing. most biological datasets. We plan to extend the interoperability of omero-vitessce with the OME-NGFF and SpatialData file formats to leverage the efficiency of these cloud optimized formats.
The three files in this Zenodo Record are all the same poster saved in different format all with high resolution images.

Tags: Nfdi4Bioimage

[https://zenodo.org/records/14832855](https://zenodo.org/records/14832855)

[https://doi.org/10.5281/zenodo.14832855](https://doi.org/10.5281/zenodo.14832855)


---

## Introduction to OMERO - Frankfurt - online

Michele Bortolomeazzi, Tom Boissonnet

Published 2025-04-05

Licensed CC-BY-4.0



These slides were presented during an online introductory session to OMERO for the UB Frankfurt.
The two-hour session consisted of a first part highlighting the benefits that image data management brings to the lab. The second part showcased image analysis workflows with a Fiji macro and a Python notebook.
&nbsp;

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/15152576](https://zenodo.org/records/15152576)

[https://doi.org/10.5281/zenodo.15152576](https://doi.org/10.5281/zenodo.15152576)


---

## Key-Value pair template for annotation of datasets in OMERO (PERIKLES study)

Anett Jannasch, Silke Tulok, Vanessa Aphaia Fiona Fuchs, Tom Boissonnet, Christian Schmidt, Michele Bortolomeazzi, Gunar Fabig, Chukwuebuka Okafornta

Published 2024-06-26

Licensed CC-BY-4.0



This is a Key-Value pair template used for the annotation of datasets in OMERO. It is tailored for a research study (PERIKLES project) on the biocompatibility of newly designed biomaterials out of pericardial tissue for cardiovascular substitutes (https://doi.org/10.1063/5.0182672) conducted in the research department of Cardiac Surgery at the Faculty of Medicine Carl Gustav Carus at the Technische Universit&auml;t Dresden . A corresponding public example dataset is used in the publication "Setting up an institutional OMERO environment for bioimage data: perspectives from both facility staff and users" and is available here
(https://omero.med.tu-dresden.de/webclient/?show=dataset-1557).
The template is based on the REMBI recommendations (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8606015) and it was developed during the PoL-Bio-Image Analysis Symposium in Dresden Aug 28th- Sept 1th 2023.&nbsp;
With this template it is possible to create a csv-file, that can be used to annotate a dataset in OMERO using the annotation script (https://github.com/ome/omero-scripts/blob/develop/omero/annotation_scripts/).
How to use:
select and copy the data range containing Keys and Values
open a new excel sheet and paste transpose in column B1
type in A1 'dataset'
insert in A2 the exact name of the dataset, which should be annotated in OMERO
save the new excel sheet in csv- (comma seperated values) file format

Example can be seen in sheet 1 'csv import'. Important note; the code has to be 8-Bit UCS transformation format (UTF-8) otherwise several characters (for example &micro;, %,&deg;) might not be able to decode by the annotation script. We encountered this issue with old Microsoft Office versions (e.g. MS Office 2016).&nbsp;
Note: By filling the values in the excel sheet, avoid the usage of decimal delimiter.
&nbsp;
See cross reference:
10.5281/zenodo.12547566&nbsp;Key-Value pair template for annotation of datasets in OMERO (light- and electron microscopy data within the research group of Prof. Mueller-Reichert)
10.5281/zenodo.12578084 Key-Value pair template for annotation in OMERO for light microscopy data acquired with AxioScan7 - Core Facility Cellular Imaging (CFCI)

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/12546808](https://zenodo.org/records/12546808)

[https://doi.org/10.5281/zenodo.12546808](https://doi.org/10.5281/zenodo.12546808)


---

## Key-Value pair template for annotation of datasets in OMERO for light- and electron microscopy data within the research group of Prof. Müller-Reichert

Gunar Fabig, Anett Jannasch, Chukwuebuka Okafornta, Tom Boissonnet, Christian Schmidt, Michele Bortolomeazzi, Vanessa Aphaia Fiona Fuchs, Maria Koeckert, Aayush Poddar, Martin Vogel, Hanna-Margareta Schwarzbach, Andy Vogelsang, Michael Gerlach, Anja Nobst, Thomas Müller-Reichert, Silke Tulok

Published 2024-06-26

Licensed CC-BY-4.0



This are a two Key-Value pair templates used for the annotation of datasets in OMERO. They are tailored for light- and electron microcopy data for all research projects of the research group of Prof. T. Mueller-Reichert.&nbsp; All members of the Core Facility Cellular Imaging agreed for using these templates to annotate data in OMERO. Furthermore, there are a corresponding public example datasets used in the publication "Setting up an institutional OMERO environment for bioimage data: perspectives from both facility staff and users" and are available here:
https://omero.med.tu-dresden.de/webclient/?show=dataset-1552 --&gt; for lattice-light sheet microscopy
https://omero.med.tu-dresden.de/webclient/?show=dataset-1555--&gt; for electron microscopy data
That templates are based on the REMBI recommendations (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8606015) and were developed during the PoL-Bio-Image Analysis Symposium in Dresden Aug 28th- Sept 1st in 2023 and further adapeted during the usage of OMERO.&nbsp;
With every template it is possible to create a csv-file, that can be used to annotate a dataset in OMERO using the annotation script (https://github.com/ome/omero-scripts/blob/develop/omero/annotation_scripts/).
How to use:

fill the template with metadata
select and copy the data range containing the Keys and Values
open a new excel sheet and paste transpose in cell A1
Important: cell A1 contains always the name 'dataset' and cell A2 contains the exact name of the dataset, which should be annotated in OMERO
save the new excel sheet in csv-file (comma separated values) format

Examples can be seen in sheet 3 'csv_TOMO' and sheet 5 csv_TEM'.
Important note: The code has to be 8-Bit UCS transformation format (UTF-8) otherwise several characters (for example &micro;, %,&deg;) might be not able to decode by the annotation script. We encountered this issue with old Microsoft-Office versions (MS Office 2016).&nbsp;
Note: By filling the values in the excel sheet, avoid the usage of comma as decimal delimiter.
See cross reference:
10.5281/zenodo.12546808&nbsp;Key-Value pair template for annotation of datasets in OMERO (PERIKLES study)
10.5281/zenodo.12578084 Key-Value pair template for annotation in OMERO for light microscopy data acquired with AxioScan7 - Core Facility Cellular Imaging (CFCI)
&nbsp;

[https://zenodo.org/records/12547566](https://zenodo.org/records/12547566)

[https://doi.org/10.5281/zenodo.12547566](https://doi.org/10.5281/zenodo.12547566)


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

## NFDI4Bioimage - TA3-Hackathon - UoC-2023 (Cologne Hackathon)

Mohamed M. Abdrabbou, Mehrnaz Babaki, Tom Boissonnet, Michele Bortolomeazzi, Eik Dahms, Vanessa A. F. Fuchs, Moritz Hoevels, Niraj Kandpal, Christoph Möhl, Joshua A. Moore, Astrid Schauss, Andrea Schrader, Torsten Stöter, Julia Thönnißen, Monica Valencia-S., H. Lukas Weil, Jens Wendt and Peter Zentis

Licensed CC-BY-4.0



Tags: Arc, Dataplant, Hackathon, Nfdi4Bioimage, OMERO, Python, Research Data Management

Content type: Event, Publication, Documentation

[https://github.com/NFDI4BIOIMAGE/Cologne-Hackathon-2023](https://github.com/NFDI4BIOIMAGE/Cologne-Hackathon-2023)

[https://doi.org/10.5281/zenodo.10609770](https://doi.org/10.5281/zenodo.10609770)


---

## NFDI4Bioimage - TA3-Hackathon - UoC-2023 (Cologne-Hackathon-2023, GitHub repository)

Mohamed Abdrabbou, Mehrnaz Babaki, Tom Boissonnet, Michele Bortolomeazzi, Eik Dahms, Vanessa Fuchs, A. F. Moritz Hoevels, Niraj Kandpal, Christoph Möhl, Joshua A. Moore, Astrid Schauss, Andrea Schrader, Torsten Stöter, Julia Thönnißen, Monica Valencia-S., H. Lukas Weil, Jens Wendt, Peter Zentis

Licensed CC-BY-4.0



This repository documents the first NFDI4Bioimage - TA3-Hackathon - UoC-2023 (Cologne Hackathon), where topics like 'Interoperability', 'REMBI / Mapping', and 'Neuroglancer (OMERO / zarr)' were explored through collaborative discussions and workflow sessions, culminating in reports that bridge NFDI4Bioimage to DataPLANT. Funded by various DFG initiatives, this event emphasized documentation and use cases, contributing preparatory work for future interoperability projects at the 2nd de.NBI BioHackathon in Bielefeld.

Tags: Research Data Management, FAIR-Principles, Bioimage Analysis, Nfdi4Bioimage

Content type: Github Repository

[https://zenodo.org/doi/10.5281/zenodo.10609770](https://zenodo.org/doi/10.5281/zenodo.10609770)


---

## OMExcavator: a tool for exporting and connecting  Bioimaging-specific metadata in wider knowledge graphs

Stefan Dvoretskii, Klaus Maier-Hein, Marco Nolden, Christian Schmidt, Michele Bortolomeazzi, Josh Moore

Published 2025-05-15

Licensed CC-BY-4.0



[https://zenodo.org/records/15423904](https://zenodo.org/records/15423904)

[https://doi.org/10.5281/zenodo.15423904](https://doi.org/10.5281/zenodo.15423904)


---

## OMExcavator: a tool for exporting and connecting domain-specific metadata in a wider knowledge graph

Stefan Dvoretskii, Michele Bortolomeazzi, Marco Nolden, Christian Schmidt, Klaus Maier-Hein, Josh Moore

Published 2025-02-21

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage

[https://zenodo.org/records/15268798](https://zenodo.org/records/15268798)

[https://doi.org/10.5281/zenodo.15268798](https://doi.org/10.5281/zenodo.15268798)


---

## Setting up an institutional OMERO environment for bioimage data: Perspectives from both facility staff and users

Anett Jannasch, Silke Tulok, Chukwuebuka William Okafornta, Thomas Kugel, Michele Bortolomeazzi, Tom Boissonnet, Christian Schmidt, Andy Vogelsang

Published 2024-09-14

Licensed CC-BY-4.0



Modern bioimaging core facilities at research institutions are essential for managing and maintaining high-end instruments, providing training and support for researchers in experimental design, image acquisition and data analysis. 

Tags: Nfdi4Bioimage, OMERO, Bioimage Analysis

Content type: Publication

[https://onlinelibrary.wiley.com/doi/10.1111/jmi.13360](https://onlinelibrary.wiley.com/doi/10.1111/jmi.13360)


---

## The Information Infrastructure for BioImage Data (I3D:bio) project to advance FAIR microscopy data management for the community

Christian Schmidt, Michele Bortolomeazzi, Tom Boissonnet, Julia Dohle, Tobias Wernet, Janina Hanne, Roland Nitschke, Susanne Kunis, Karen Bernhardt, Stefanie Weidtkamp-Peters, Elisa Ferrando-May

Published 2024-03-04

Licensed CC-BY-4.0



Research data management (RDM) in microscopy and image analysis is a challenging task. Large files in proprietary formats, complex N-dimensional array structures, and various metadata models and formats can make image data handling inconvenient and difficult. For data organization, annotation, and sharing, researchers need solutions that fit everyday practice and comply with the FAIR (Findable, Accessible, Interoperable, Reusable) principles. International community-based efforts have begun creating open data models (OME), an open file format and translation library (OME-TIFF, Bio-Formats), data management software platforms, and microscopy metadata recommendations and annotation tools. Bringing these developments into practice requires support and training. Iterative feedback and tool&nbsp;improvement is needed to foster practical adoption by the scientific&nbsp;community. The Information Infrastructure for BioImage Data (I3D:bio) project&nbsp;works on guidelines, training resources, and practical assistance for FAIR&nbsp;microscopy RDM adoption with a focus on the management platform OMERO&nbsp;and metadata annotations.

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/10805204](https://zenodo.org/records/10805204)

[https://doi.org/10.5281/zenodo.10805204](https://doi.org/10.5281/zenodo.10805204)


---

## The role of Helmholtz Centers in NFDI4BIOIMAGE - A national consortium enhancing FAIR data management for microscopy and bioimage analysis

Riccardo Massei, Christian Schmidt, Michele Bortolomeazzi, Julia Thoennissen, Jan Bumberger, Timo Dickscheid, Jan-Philipp Mallm, Elisa Ferrando-May

Published 2024-06-06

Licensed CC-BY-4.0



Germany&rsquo;s National Research Data Infrastructure (NFDI) aims to establish a sustained, cross-disciplinary research data management (RDM) infrastructure that enables researchers to handle FAIR (findable, accessible, interoperable, reusable) data. While&nbsp;FAIR principles have been&nbsp;adopted by funders, policymakers, and publishers, their practical implementation remains an ongoing effort. In the field of bio-imaging, harmonization of&nbsp;data formats, metadata ontologies, and open data repositories is necessary&nbsp;to achieve FAIR data.&nbsp;The NFDI4BIOIMAGE was established&nbsp;to address these issues and&nbsp;develop tools and best practices to facilitate FAIR microscopy and image analysis data in alignment with international community activities. The&nbsp;consortium operates through its Data Stewards team to provide expertise and direct support to help overcome RDM challenges. The three Helmholtz Centers in NFDI4BIOIMAGE aim to collaborate closely with other centers and initiatives, such as HMC, Helmholtz AI, and HIP. Here we present NFDI4BIOIMAGE&rsquo;s work and its significance for research in Helmholtz and beyond

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/11501662](https://zenodo.org/records/11501662)

[https://doi.org/10.5281/zenodo.11501662](https://doi.org/10.5281/zenodo.11501662)


---

## [Workshop] Bioimage data management and analysis with OMERO

Riccardo Massei, Michele Bortolomeazzi, Christian Schmidt

Published 2024-05-13

Licensed CC-BY-4.0



Here we share the material used in a workshop held on May 13th, 2024, at the German Cancer Research Center in Heidelberg (on-premise)
Description:Microscopy experiments generate information-rich, multi-dimensional data, allowing us to investigate biological processes at high spatial and temporal resolution. Image processing and analysis is a standard procedure to retrieve quantitative information from biological imaging. Due to the complex nature of bioimaging files that often come in proprietary formats, it can be challenging to organize, structure, and annotate bioimaging data throughout a project. Data often needs to be moved between collaboration partners, transformed into open formats, processed with a variety of software tools, and exported to smaller-sized images for presentation. The path from image acquisition to final publication figures with quantitative results must be documented and reproducible.
In this workshop, participants learn how to use OMERO to organize their data and enrich the bioimage data with structured metadata annotations.We also focus on image analysis workflows in combination with OMERO based on the Fiji/ImageJ software and using Jupyter Notebooks. In the last part, we explore how OMERO can be used to create publication figures and prepare bioimage data for publication in a suitable repository such as the Bioimage Archive.
Module 1&nbsp;(9 am - 10.15 am):&nbsp;Basics of OMERO, data structuring and annotation
Module 2&nbsp;(10.45 am - 12.45 pm):&nbsp;OMERO and Fiji
Module 3&nbsp;(1.45 pm - 3.45 pm):&nbsp;OMERO and Jupyter Notebooks
Module 4&nbsp;(4.15 pm - 6. pm):&nbsp;Publication-ready figures and data with OMERO
The target group for this workshopThis workshop is directed at researchers at all career levels who plan to or have started to use OMERO for their microscopy research data management.&nbsp;We encourage the workshop participants to bring example data from their research to discuss suitable metadata annotation for their everyday practice.
Prerequisites:Users should bring their laptops and have access to the internet through one of the following options:- eduroam- institutional WiFi- VPN connection to their institutional networks to access OMERO
Who are the trainers?
Dr. Riccardo Massei (Helmholtz-Center for Environmental Research, UFZ, Leipzig) - Data Steward for Bioimaging Data in NFDI4BIOIMAGE
Dr. Michele Bortolomeazzi (DKFZ, Single cell Open Lab, bioimage data specialist, bioinformatician, staff scientist in the NFDI4BIOIMAGE project)
Dr. Christian Schmidt (Science Manager for Research Data Management in Bioimaging, German Cancer Research Center, Heidelberg, Project Coordinator of the NFDI4BIOIMAGE project)

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/11350689](https://zenodo.org/records/11350689)

[https://doi.org/10.5281/zenodo.11350689](https://doi.org/10.5281/zenodo.11350689)


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









Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/15026373](https://zenodo.org/records/15026373)

[https://doi.org/10.5281/zenodo.15026373](https://doi.org/10.5281/zenodo.15026373)


---

## [Workshop] Research Data Management for Microscopy and BioImage Analysis

Christian Schmidt, Tom Boissonnet, Michele Bortolomeazzi, Ksenia Krooß

Published 2024-09-30

Licensed CC-BY-4.0



Research Data Management for Microscopy and BioImage Analysis

Introduction to BioImaging Research Data Management, NFDI4BIOIMAGE and I3D:bioChristian Schmidt /DKFZ Heidelberg
OMERO as a tool for bioimaging data managementTom Boissonnet /Heinrich-Heine Universit&auml;t D&uuml;sseldorf
Reproducible image analysis workflows with OMERO software APIsMichele Bortolomeazzi /DKFZ Heidelberg
Publishing datasets in public archives for bioimage dataKsenia Kroo&szlig; /Heinrich-Heine Universit&auml;t D&uuml;sseldorf

Date &amp; Venue:Thursday, Sept. 26, 5.30 p.m.Haus 22 / Paul Ehrlich Lecture Hall (H22-1)University Hospital Frankfurt

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/13861026](https://zenodo.org/records/13861026)

[https://doi.org/10.5281/zenodo.13861026](https://doi.org/10.5281/zenodo.13861026)


---

## omero-vitessce

Michele Bortolomeazzi

Published 2024-11-25T10:51:01+00:00

Licensed AGPL-3.0



OMERO.web plugin for the Vitessce multimodal data viewer.

Tags: Nfdi4Bioimage

Content type: Github Repository

[https://github.com/NFDI4BIOIMAGE/omero-vitessce](https://github.com/NFDI4BIOIMAGE/omero-vitessce)


---

