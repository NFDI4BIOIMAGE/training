# Tom boissonnet (14)
## A practical guide to bioimaging research data management in core facilities

Christian Schmidt, Tom Boissonnet, Julia Dohle, Karen Bernhardt, Elisa Ferrando-May, Tobias Wernet, Roland Nitschke, Susanne Kunis, Stefanie Weidtkamp-Peters



Tags: Research Data Management

Content type: Publication

[https://onlinelibrary.wiley.com/doi/10.1111/jmi.13317](https://onlinelibrary.wiley.com/doi/10.1111/jmi.13317)


---

## From Paper to Pixels: Navigation through your Research Data - presentations of speakers

Marcelo Zoccoler, Simon Bekemeier, Tom Boissonnet, Simon Parker, Luca Bertinetti, Marc Gentzel, Riccardo Massei, Cornelia Wetzker

Published 2024-06-10

Licensed CC-BY-4.0



The workshop introduced key topics of research data management (RDM) and the implementation thereof on a life science campus. Internal and external experts of RDM including scientists that apply chosen software tools presented the basic concepts and their implementation to a broad audience.&nbsp;
Talks covered general aspects of data handling and sorting, naming conventions, data storage repositories and archives, licensing of material, data and code management using git, data protection particularly regarding patient data and in genome sequencing and more. Two data management concepts and exemplary tools were highlighted in particular, being electronic lab notebooks with eLabFTW and the bio-image management software OMERO. Those were chosen because of three aspects: the large benefit of these management tools for a life science campus, their free availability as open source tools with the option of contribution of required functionalities and first existing use cases on campus already supported by CMCB/PoL IT.
Two talks by Robert Haase (ScaDS.AI/ Uni Leipzig) and Robert M&uuml;ller (Kontaktstelle Forschungsdaten, TU Dresden with contributions from Denise D&ouml;rfel) that opened the symposium were shared independently:
https://zenodo.org/records/11382341
https://zenodo.org/records/11261115
The workshop organization was funded by the CMCB/PoL Networking Grant and supported by the consortium NFDI4BIOIMAGE (funded by DFG grant number NFDI 46/1, project number 501864659).

Tags: Research Data Management

Content type: Slides

[https://zenodo.org/records/11548617](https://zenodo.org/records/11548617)

[https://doi.org/10.5281/zenodo.11548617](https://doi.org/10.5281/zenodo.11548617)


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

## Key-Value pair template for annotation in OMERO for light microscopy data acquired with AxioScan7 - Core Facility Cellular Imaging (CFCI)

Silke Tulok, Anja Nobst, Anett Jannasch, Tom Boissonnet, Gunar Fabig

Published 2024-06-28

Licensed CC-BY-4.0



This Key-Value pair template is used for the data documentation during imaging experiments and the later data annotation in OMERO. It is tailored for the usage and image acquisition at the slide scanning system Zeiss AxioScan 7 in the Core Facility Cellular Imaging (CFCI). It contains important metadata of the imaging experiment, which are not saved in the corresponding imaging files. All users of the Core Facility Cellular Imaging are trained to use that file to document their imaging parameters directly during the data acquisition with the possibility for a later upload to OMERO. Furthermore, there is a corresponding public example image used in the publication "Setting up an institutional OMERO environment for bioimage data: perspectives from both facility staff and users" and is available here:
https://omero.med.tu-dresden.de/webclient/?show=image-33248
This template was developed by the CFCI staff during the setup and usage of the AxioScan 7 and is based on the REMBI recommendations (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8606015).
With this template it is possible to create a csv-file, that can be used to annotate an image or dataset in OMERO using the annotation script (https://github.com/ome/omero-scripts/blob/develop/omero/annotation_scripts/).
How to use:

fill the template sheet&nbsp; with your metadata
select and copy the data range containing the Keys and Values
open a new excel sheet and paste transpose in cell A1&nbsp;
Important: cell A1 contains always the name 'dataset' and cell A2 contains the exact name of the image/dataset, which should be annotated in OMERO
save the new excel sheet in csv-file (comma separated values) format

An example can be seen in sheet 3 'csv_AxioScan'.
Important note: The code has to be 8-Bit UCS transformation format (UTF-8) otherwise several characters (for example &micro;, %,&deg;) might be not able to decode by the annotation script. We encountered this issue with old Microsoft-Office versions (MS Office 2016).&nbsp;
Note: By filling the values in the excel sheet, avoid the usage of comma as decimal delimiter.
See cross reference:
10.5281/zenodo.12547566 Key-Value pair template for annotation of datasets in OMERO for light- and electron microscopy data within the research group of Prof. Mueller-Reichert
10.5281/zenodo.12546808&nbsp;Key-Value pair template for annotation of datasets in OMERO (PERIKLES study)

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/12578084](https://zenodo.org/records/12578084)

[https://doi.org/10.5281/zenodo.12578084](https://doi.org/10.5281/zenodo.12578084)


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

## The Information Infrastructure for BioImage Data (I3D:bio) project to advance FAIR microscopy data management for the community

Christian Schmidt, Michele Bortolomeazzi, Tom Boissonnet, Julia Dohle, Tobias Wernet, Janina Hanne, Roland Nitschke, Susanne Kunis, Karen Bernhardt, Stefanie Weidtkamp-Peters, Elisa Ferrando-May

Published 2024-03-04

Licensed CC-BY-4.0



Research data management (RDM) in microscopy and image analysis is a challenging task. Large files in proprietary formats, complex N-dimensional array structures, and various metadata models and formats can make image data handling inconvenient and difficult. For data organization, annotation, and sharing, researchers need solutions that fit everyday practice and comply with the FAIR (Findable, Accessible, Interoperable, Reusable) principles. International community-based efforts have begun creating open data models (OME), an open file format and translation library (OME-TIFF, Bio-Formats), data management software platforms, and microscopy metadata recommendations and annotation tools. Bringing these developments into practice requires support and training. Iterative feedback and tool&nbsp;improvement is needed to foster practical adoption by the scientific&nbsp;community. The Information Infrastructure for BioImage Data (I3D:bio) project&nbsp;works on guidelines, training resources, and practical assistance for FAIR&nbsp;microscopy RDM adoption with a focus on the management platform OMERO&nbsp;and metadata annotations.

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/10805204](https://zenodo.org/records/10805204)

[https://doi.org/10.5281/zenodo.10805204](https://doi.org/10.5281/zenodo.10805204)


---

## Workflow for user introduction into microscopy, OMERO and data management at Center for Advanced imaging

Ksenia Krooß, Fuchs, Vanessa Aphaia Fiona, Tom Boissonnet, Stefanie Weidtkamp-Peters

Published 2025-03-07

Licensed CC-BY-4.0



At the Center for Advanced Imaging (CAi) at the Heinrich Heine University D&uuml;sseldorf, Germany, we have established a workflow to guide users through all aspects of bioimaging. The process begins with an initial consultation with our imaging specialists regarding microscopy techniques for their specific project. Users then receive training in microscope operation, ensuring they can handle the equipment effectively. If needed, our specialists also provide support in image analysis. Next, we introduce users to OMERO, highlighting its features and the advantages of using a bioimage data management system. They are then trained to structure and annotate their data within OMERO according to the Recommended Metadata for Biological Images (REMBI), taking their specific research topics into account. As users prepare for data publication, we assist with data organization and repository uploads. Our goal is to educate researchers in managing bioimage data&nbsp;throughout its entire lifecycle, with a strong emphasis on the FAIR (findable, accessible, interoperable, reusable) principles.

[https://zenodo.org/records/14988921](https://zenodo.org/records/14988921)

[https://doi.org/10.5281/zenodo.14988921](https://doi.org/10.5281/zenodo.14988921)


---

## [Workshop Material] Fit for OMERO - How imaging facilities and IT departments work together to enable RDM for bioimaging, October 16-17, 2024, Heidelberg

Tom Boissonnet, Bettina Hagen, Susanne Kunis, Christian Schmidt, Stefanie Weidtkamp-Peters

Published 2024-11-18

Licensed CC-BY-4.0



Fit for OMERO: How imaging facilities and IT departments work together to enable RDM for bioimaging
Description:
Research data management (RDM) in bioimaging is challenging because of large file sizes, heterogeneous file formats and the variability of imaging methods. The image data management system OMERO (OME Remote Objects) allows for centralized and secure storage, organization, annotation, and interrogation of microscopy data by researchers. It is an internationally well-supported open-source software tool that has become one of the best-known image data management tools among bioimaging scientists. Nevertheless, the&nbsp;de novo&nbsp;setup of OMERO at an institute is a multi-stakeholder process that demands time, funds, organization and iterative implementation. In this workshop, participants learn how to begin setting up OMERO-based image data management at their institution. The topics include:

Stakeholder identification at the university / research institute
Process management, time line expectations, and resources planning
Learning about each other&lsquo;s perspectives on chances and challenges for RDM
Funding opportunities and strategies for IT and imaging core facilities
Hands-on: Setting up an OMERO server in a virtual machine environment

Target audience:
This workshop was directed at universities and research institutions who consider or plan to implement OMERO, or are in an early phase of implementation. This workshop was intended for teams from IT departments and imaging facilities to participate together with one person from the IT department, and one person from the imaging core facility at the same institution.
The trainers:

Prof. Dr. Stefanie Weidtkamp-Peters (Imaging Core Facility Head, Center for Advanced Imaging, Heinrich Heine University of D&uuml;sseldorf)
Dr. Susanne Kunis (Software architect, OMERO administrator, metadata specialist, University of Osnabr&uuml;ck)
Dr. Tom Boissonnet (OMERO admin and image metadata specialist, Center for Advanced Imaging, Heinrich Heine University of D&uuml;sseldorf)
Dr. Bettina Hagen&nbsp;(IT Administration and service specialist, Max Planck Institute for the Biology of Ageing, Cologne)&nbsp;
Dr. Christian Schmidt (Science Manager for Research Data Management in Bioimaging, German Cancer Research Center (DKFZ), Heidelberg)

Time and place
The format was a two-day, in-person workshop (October 16-17, 2024).&nbsp;Location: Heidelberg, Germany
Workshop learning goals

Learn the steps to establish a local RDM environment fit for bioimaging data
Create a network of IT experts and bioimaging specialists for bioimage RDM across institutions
Establish a stakeholder process management for installing OMERO-based RDM
Learn from each other, leverage different expertise
Learn how to train users, establish sustainability strategies, and foster FAIR RDM for bioimaging at your institution


Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/14178789](https://zenodo.org/records/14178789)

[https://doi.org/10.5281/zenodo.14178789](https://doi.org/10.5281/zenodo.14178789)


---

## [Workshop] FAIR data handling for microscopy: Structured metadata annotation in OMERO

Vanessa Fiona Aphaia Fuchs, Christian Schmidt, Tom Boissonnet

Published 2024-05-06

Licensed CC-BY-4.0



Description
Microscopy experiments generate information-rich, multi-dimensional data, allowing us to investigate biological processes at high spatial and temporal resolution. Image processing and analysis is a standard procedure to retrieve quantitative information from biological imaging. Due to the complex nature of bioimaging files that often come in proprietary formats, it can be challenging to organize, structure, and annotate bioimaging data throughout a project. Data often needs to be moved between collaboration partners, transformed into open formats, processed with a variety of software tools, and exported to smaller-sized images for presentation. The path from image acquisition to final publication figures with quantitative results must be documented and reproducible.
In this workshop, participants learn how to use structured metadata annotations in the image data management platform OMERO (OME Remote Objects) to optimize their data handling. This strategy helps both with organizing data for easier processing and analysis and for the preparation of data publication in journal manuscripts and in public repositories such as the BioImage Archive. Participants learn the principles of leveraging object-oriented data organization in OMERO to enhance findability and usability of their data, also in collaborative settings. The integration of OMERO with image analysis tools, in particular ImageJ/Fiji, will be trained. Moreover, users learn about community-accepted metadata checklists (REMBI) to enrich the value of their data toward reproducibility and reusability. In this workshop, we will provide hands-on training and recommendations on:

Structured metadata annotation features in OMERO and how to use them
Types of metadata in bioimaging: Technical metadata, sample metadata, analysis metadata
The use of ontologies and terminologies for metadata annotation
REMBI, the recommended metadata for biological images
Metadata-assisted image analysis streamlining
Tools for metadata annotation in OMERO

The target group for this workshop
This workshop is directed at researchers at all career levels who have started using OMERO for their microscopy research data management. We encourage the workshop participants to bring example data from their research to discuss suitable metadata annotation for their everyday practice.
Who are the trainers (see trainer description below for more details)

Dr. Vanessa Fuchs (NFDI4BIOIMAGE Data Steward, Center for Advanced Imaging, Heinrich-Heine University of D&uuml;sseldorf)
Dr. Tom Boissonnet (OMERO admin and image metadata specialist, Center for Advanced Imaging, Heinrich-Heine University of D&uuml;sseldorf)
Dr. Christian Schmidt (Science Manager for Research Data Management in Bioimaging, German Cancer Research Center, Heidelberg)

Material Description
Published here are the presentation slides that were used for input from the trainers during the different sessions of the programme. Additionally, a Fiji Macro is published that depends on the OMERO Extensions Plugin by Pouchin et al, 2022, F100Research, https://doi.org/10.12688/f1000research.110385.2&nbsp;
Programme Overview
Day 1 - April 29th, 2024&nbsp;09.00 a.m. to 10.00 a.m.: Session 1 - Welcome and Introduction
10.00 a.m. to 10.30 a.m.:&nbsp; Session 2 - Introduction to the FAIR principles &amp; data annotation
10:30 a.m. to 10:45 a.m.: Coffee break
10.45 a.m. to 12.00 a.m.: Session 3 - Data structure (datasets in OMERO) and organization with Tags&nbsp;
12.00 a.m. to 1.00 p.m.:&nbsp; Lunch Break
1.00 p.m. to 2.00 p.m.:&nbsp; Session 4 - REMBI, Key-Value pair annotations in bioimaging
2:00 p.m. to 2.30 p.m.:&nbsp; Session 5 - Ontologies for Key-Value Pairs in OMERO
2:30 p.m. to 2:45 p.m. Coffee break
2.45 p.m. to 3.45 p.m.:&nbsp; Wrap-up, discussion, outlook on day 2
Day 2 - April 30th, 2024
09.00 a.m. to 09.30 a.m.:&nbsp; Arrival and Start into day 2
09.30 a.m. to 11.30 a.m.:&nbsp; Session 6 - Hands-on : REMBI-based Key-Value Pair annotation in OMERO
11.30 a.m. to 12.30 a.m.:&nbsp; Lunch Break
12.30 a.m. to 1.15 p.m.: Session 7 - OMERO and OMERO.plugins
1.15 p.m. to 2.00 p.m.: Session 8 - Loading OMERO-hosted data into Fiji
2.00 p.m. to 2.15 p.m.:&nbsp;Coffee break&nbsp;
2.15 p.m. to 3.00 p.m.: Discussion, Outlook

[https://zenodo.org/records/11109616](https://zenodo.org/records/11109616)

[https://doi.org/10.5281/zenodo.11109616](https://doi.org/10.5281/zenodo.11109616)


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

## ome2024-ngff-challenge

Will Moore, Josh Moore, sherwoodf, jean-marie burel, Norman Rzepka, dependabot[bot], JensWendt, Joost de Folter, Torsten St\xF6ter, AybukeKY, Eric Perlman, Tom Boissonnet

Published 2024-08-30T12:00:53+00:00

Licensed BSD-3-CLAUSE



Project planning and material repository for the 2024 challenge to generate 1 PB of OME-Zarr data

Tags: Sharing, Nfdi4Bioimage, Research Data Management

Content type: Github Repository

[https://github.com/ome/ome2024-ngff-challenge](https://github.com/ome/ome2024-ngff-challenge)


---

