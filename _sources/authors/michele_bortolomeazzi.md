# Michele bortolomeazzi (8)
## I3D:bio's OMERO training material: Re-usable, adjustable, multi-purpose slides for local user training

Christian Schmidt, Michele Bortolomeazzi, Tom Boissonnet, Carsten Fortmann-Grote, Julia Dohle, Peter Zentis, Niraj Kandpal, Susanne Kunis, Thomas Zobel, Stefanie Weidtkamp-Peters, Elisa Ferrando-May

Published 2023-11-13

Licensed CC-BY-4.0



The open-source software OME Remote Objects (OMERO) is a data management software that allows storing, organizing, and annotating bioimaging/microscopy data. OMERO has become one of the best-known systems for bioimage data management in the bioimaging community. The Information Infrastructure for BioImage Data (I3D:bio) project facilitates the uptake of OMERO into research data management (RDM) practices at universities and research institutions in Germany. Since the adoption of OMERO into researchers' daily routines requires intensive training, a broad portfolio of training resources for OMERO is an asset. On top of using the OMERO guides curated by the Open Microscopy Environment Consortium (OME) team, imaging core facility staff at institutions where OMERO is used often prepare additional material tailored to be applicable for their own OMERO instances. Based on experience gathered in the Research Data Management for Microscopy group (RDM4mic) in Germany, and in the use cases in the I3D:bio project, we created a set of reusable, adjustable, openly available slide decks to serve as the basis for tailored training lectures, video tutorials, and self-guided instruction manuals directed at beginners in using OMERO. The material is published as an open educational resource complementing the existing resources for OMERO contributed by the community.

Tags: OMERO, Research Data Management, Nfdi4Bioimage, I3Dbio

Content type: Slide, Video

[https://zenodo.org/records/8323588](https://zenodo.org/records/8323588)

[https://www.youtube.com/playlist?list=PL2k-L-zWPoR7SHjG1HhDIwLZj0MB_stlU](https://www.youtube.com/playlist?list=PL2k-L-zWPoR7SHjG1HhDIwLZj0MB_stlU)

[https://doi.org/10.5281/zenodo.8323588](https://doi.org/10.5281/zenodo.8323588)


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

[https://zenodo.org/records/10805204](https://zenodo.org/records/10805204)

[https://doi.org/10.5281/zenodo.10805204](https://doi.org/10.5281/zenodo.10805204)


---

## The role of Helmholtz Centers in NFDI4BIOIMAGE - A national consortium enhancing FAIR data management for microscopy and bioimage analysis

Riccardo Massei, Christian Schmidt, Michele Bortolomeazzi, Julia Thoennissen, Jan Bumberger, Timo Dickscheid, Jan-Philipp Mallm, Elisa Ferrando-May

Published 2024-06-06

Licensed CC-BY-4.0



Germany&rsquo;s National Research Data Infrastructure (NFDI) aims to establish a sustained, cross-disciplinary research data management (RDM) infrastructure that enables researchers to handle FAIR (findable, accessible, interoperable, reusable) data. While&nbsp;FAIR principles have been&nbsp;adopted by funders, policymakers, and publishers, their practical implementation remains an ongoing effort. In the field of bio-imaging, harmonization of&nbsp;data formats, metadata ontologies, and open data repositories is necessary&nbsp;to achieve FAIR data.&nbsp;The NFDI4BIOIMAGE was established&nbsp;to address these issues and&nbsp;develop tools and best practices to facilitate FAIR microscopy and image analysis data in alignment with international community activities. The&nbsp;consortium operates through its Data Stewards team to provide expertise and direct support to help overcome RDM challenges. The three Helmholtz Centers in NFDI4BIOIMAGE aim to collaborate closely with other centers and initiatives, such as HMC, Helmholtz AI, and HIP. Here we present NFDI4BIOIMAGE&rsquo;s work and its significance for research in Helmholtz and beyond

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

[https://zenodo.org/records/11350689](https://zenodo.org/records/11350689)

[https://doi.org/10.5281/zenodo.11350689](https://doi.org/10.5281/zenodo.11350689)


---

