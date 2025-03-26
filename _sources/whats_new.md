# Recently added (10)
## Advancing FAIR Image Analysis in Galaxy: Tools, Workflows, and Training

Chiang Jurado, Diana, Riccardo Massei, Pavankumar Videm, Anup Kumar, Anne Fouilloux, Leonid Kostrykin, Beatriz Serrano-Solano, Björn Grüning

Published 2025-03-06

Licensed CC-BY-4.0



[https://zenodo.org/records/14979253](https://zenodo.org/records/14979253)

[https://doi.org/10.5281/zenodo.14979253](https://doi.org/10.5281/zenodo.14979253)


---

## Building FAIR image analysis pipelines for high-content-screening (HCS) data using Galaxy

Riccardo Massei, Matthias Berndt, Lucille Lopez-Delisle, Beatriz Serrano-Solano, Wibke Busch, Stefan Scholz, Hannes Bohring, Jo Nyffeler, Luise Reger, Jan Bumberger

Published 2025-02-25

Licensed CC-BY-4.0



Imaging is crucial across various scientific disciplines, particularly in life sciences, where it plays a key role in studies ranging from single molecules to whole organisms. However, the complexity and sheer volume of image data, especially from high-content screening (HCS) experiments involving cell lines or other organisms, present significant challenges. Managing and analysing this data efficiently requires well-defined image processing tools and analysis pipelines that align with the FAIR principles&mdash;ensuring they are findable, accessible, interoperable, and reusable across different domains.
In the frame of NFDI4BioImaging (the National Research Data Infrastructure focusing on bioimaging in Germany), we want to find viable solutions for storing, processing, analysing, and sharing HCS data. In particular, we want to develop solutions to make findable and machine-readable metadata using (semi)automatic analysis pipelines. In scientific research, such pipelines are crucial for maintaining data integrity, supporting reproducibility, and enabling interdisciplinary collaboration. These tools can be used by different users to retrieve images based on specific attributes as well as support quality control by identifying appropriate metadata.
Galaxy, an open-source, web-based platform for data-intensive research, offers a solution by enabling the construction of reproducible pipelines for image analysis. By integrating popular analysis software like CellProfiler and connecting with cloud services such as OMERO and IDR, Galaxy facilitates the seamless access and management of image data. This capability is particularly valuable in bioimaging, where automated pipelines can streamline the handling of complex metadata, ensuring data integrity and fostering interdisciplinary collaboration. This approach not only increases the efficiency of HCS bioimaging but also contributes to the broader scientific community's efforts to embrace FAIR principles, ultimately advancing scientific discovery and innovation.
In the present study, we proposed an automated analysis pipeline for storing, processing, analysing, and sharing HCS bioimaging data. The (semi)automatic workflow was developed by taking as a case study a dataset of zebrafish larvae and cell lines images previously obtained from an automated imaging system generating data in an HCS fashion. In our workflows, images are automatically enriched with metadata (i.e. key-value pairs, tags, raw data, regions of interest) and uploaded to the UFZ-OME Remote Objects (OMERO) server using a novel OMERO tool suite developed with GALAXY. Workflows give the possibility to the user to intuitively fetch images from the local server and perform image analysis (i.e. annotation) or even more complex toxicological analyses (dose response modelling). Furthermore, we want to improve the FAIRness of the protocol by adding a direct upload link to the Image Data Resource (IDR) repository to automatically prepare the data for publication and sharing.

[https://zenodo.org/records/14909526](https://zenodo.org/records/14909526)

[https://doi.org/10.5281/zenodo.14909526](https://doi.org/10.5281/zenodo.14909526)


---

## Galaxy meets OMERO! Overview on the Galaxy OMERO-suite and Vizarr Viewer

Riccardo Massei, Matthias Bernt, Beatriz Serrano-Solano, Lucille Lopez-Delisle, Jan Bumberger, Björn Grüning, Leonid Kostrykin

Published 2025-03-05

Licensed CC-BY-4.0



[https://zenodo.org/records/14975462](https://zenodo.org/records/14975462)

[https://doi.org/10.5281/zenodo.14975462](https://doi.org/10.5281/zenodo.14975462)


---

## Image Analysis using Galaxy

Beatriz Serrano-Solano, Leonid Kostrykin, Anne Fouilloux, Riccardo Massei

Published 2025-02-28

Licensed CC-BY-4.0



GloBIAS seminar series
&nbsp;
Part 3 in the topic:&nbsp;
Infrastructure for deploying image analysis workflows
Image analysis using Galaxy

Beatrix Serrano-Solano, Euro-BioImaging ERIC Bio-Hub, EMBL Heidelberg, Germany
&amp; Anne Fouilloux , Simula Research Laboratory, Oslo, Norway
&amp; Leonid Kostrykin, Biomedical Computer Vision Group, Heidelberg University, BioQuant, IPMB, Heidelberg, Germany
&amp; Ricardo Massei, Helmholtz Center for Environmental Research, UFZ, Leipzig, Germany
Abstract: This webinar will introduce the Galaxy Image Analysis Community and highlight our mission to advance the development of FAIR and reproducible image analysis workflows. As part of our commitment to making image data analysis more accessible and collaborative, we will showcase how Galaxy can serve the imaging community. The session will explore Galaxy&rsquo;s capabilities for integrating popular image analysis tools, interactive environments, and notebooks, making it a versatile platform for researchers across various scientific domains. We will also present how Galaxy facilitates the creation and sharing of reusable workflows, promoting open science and fostering collaboration. To give participants hands-on insight, we&rsquo;ll provide a live demonstration on designing and running image analysis workflows within Galaxy.&nbsp;

&nbsp;

[https://zenodo.org/records/14944040](https://zenodo.org/records/14944040)

[https://doi.org/10.5281/zenodo.14944040](https://doi.org/10.5281/zenodo.14944040)


---

## Leica (.lif) file with errors in channel order when imported with Bio-formats

Areli Rodriguez

Published 2025-02-26



The blue and red channels get swapped when imported with Bio-formats. Happens consistently with .lif imports in QuPath and ImageJ.

[https://zenodo.org/records/14933318](https://zenodo.org/records/14933318)

[https://doi.org/10.5281/zenodo.14933318](https://doi.org/10.5281/zenodo.14933318)


---

## Sample data for PR#4284 (https://github.com/ome/bioformats/pull/4284)

Jürgen Bohl

Published 2025-03-04

Licensed CC-BY-4.0



With this file the problem addressed in PR#4284 can be reproduced: when runningbfconvert -series 4 -channel 0 2025_01_27__0007_offline_Zen_3_9_5.czi output.png
the result is garbled.

[https://zenodo.org/records/14968770](https://zenodo.org/records/14968770)

[https://doi.org/10.5281/zenodo.14968770](https://doi.org/10.5281/zenodo.14968770)


---

## Workflow for user introduction into microscopy, OMERO and data management at Center for Advanced imaging

Ksenia Krooß, Fuchs, Vanessa Aphaia Fiona, Tom Boissonnet, Stefanie Weidtkamp-Peters

Published 2025-03-07

Licensed CC-BY-4.0



At the Center for Advanced Imaging (CAi) at the Heinrich Heine University D&uuml;sseldorf, Germany, we have established a workflow to guide users through all aspects of bioimaging. The process begins with an initial consultation with our imaging specialists regarding microscopy techniques for their specific project. Users then receive training in microscope operation, ensuring they can handle the equipment effectively. If needed, our specialists also provide support in image analysis. Next, we introduce users to OMERO, highlighting its features and the advantages of using a bioimage data management system. They are then trained to structure and annotate their data within OMERO according to the Recommended Metadata for Biological Images (REMBI), taking their specific research topics into account. As users prepare for data publication, we assist with data organization and repository uploads. Our goal is to educate researchers in managing bioimage data&nbsp;throughout its entire lifecycle, with a strong emphasis on the FAIR (findable, accessible, interoperable, reusable) principles.

[https://zenodo.org/records/14988921](https://zenodo.org/records/14988921)

[https://doi.org/10.5281/zenodo.14988921](https://doi.org/10.5281/zenodo.14988921)


---

## [N4BI AHM] Welcome to BioImage Town

Josh Moore

Published 2023-10-16

Licensed CC-BY-4.0



Keynote at the NFDI4BIOIMAGE All-Hands Meeting in Düsseldorf, Germany, October 16, 2023.

[https://zenodo.org/records/15031842](https://zenodo.org/records/15031842)

[https://doi.org/10.5281/zenodo.15031842](https://doi.org/10.5281/zenodo.15031842)


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









[https://zenodo.org/records/15026373](https://zenodo.org/records/15026373)

[https://doi.org/10.5281/zenodo.15026373](https://doi.org/10.5281/zenodo.15026373)


---

## imaris file not read by bfGetReader()

Julien Dubrulle

Published 2025-03-10

Licensed CC-BY-4.0



This file cannot be read by bfGetReader() v8.1.1 on a Windows operating workstation.

[https://zenodo.org/records/15001649](https://zenodo.org/records/15001649)

[https://doi.org/10.5281/zenodo.15001649](https://doi.org/10.5281/zenodo.15001649)


---

