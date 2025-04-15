# Cc-by-4.0 (271)
## "ZENODO und Co." Was bringt und wer braucht ein Repositorium?

Elfi Hesse, Jan-Christoph Deinert, Christian Löschen

Published 2021-01-25

Licensed CC-BY-4.0



Die Online-Veranstaltung fand am 21.01.2021 im Rahmen der SaxFDM-Veranstaltungsreihe &quot;Digital Kitchen - K&uuml;chengespr&auml;che mit SaxFDM&quot; statt. SaxFDM-Sprecherin Elfi Hesse (HTW Dresden) erl&auml;uterte zun&auml;chst Grunds&auml;tzliches zum Thema Repositorien. Anschlie&szlig;end teilten Nutzer (Jan Deinert &ndash; HZDR) und Anbieter (Christian L&ouml;schen &ndash; TU Dresden/ZIH) lokaler Repositorien ihre Erfahrungen mit uns.

Tags: Research Data Management

Content type: Slides

[https://zenodo.org/records/4461261](https://zenodo.org/records/4461261)

[https://doi.org/10.5281/zenodo.4461261](https://doi.org/10.5281/zenodo.4461261)


---

## 10 frames of fluorescent particles

Zach Marin, Maohan Su

Published 2024-12-05

Licensed CC-BY-4.0



10 frames of fluorescent particles. They don't do much, but they are a DCIMG version 0x7 file example.

[https://zenodo.org/records/14281237](https://zenodo.org/records/14281237)

[https://doi.org/10.5281/zenodo.14281237](https://doi.org/10.5281/zenodo.14281237)


---

## 3D Nuclei annotations and StarDist 3D model(s) (rat brain)

Romain Guiet

Published 2022-06-15

Licensed CC-BY-4.0



Name: 3D Nuclei annotations and StarDist3D model(s) (rat brain)

Images:&nbsp;&nbsp;From a large tiling acquisition ( https://doi.org/10.5281/zenodo.6646128 ) individual Tile (xyz : 1024x1024x62) were downsampled and cropped (128x128x62). Four crops, from different tiles (./annotations_BIOP/images/) were manually annotated with ITK-SNAP (./annotations_BIOP/masks/)

These four images, and their corresponding masks, were cropped into four quadrants (./crops_BIOP_v1/) in order to get 16 different images (64x64x62).

Conda environment:&nbsp;A conda environment was created using the yml file &nbsp;stardist0.8_TF1.15.yml

Training :&nbsp;Training was performed using the jupyter notebook 1-Training_notebook.ipynb.
Three different trainings (with the same random seed, same anisotropy, patch size and grid) were performed and produced three different models (./models/)

Validation images (from the random seed used) were exported to ease the visual inspection of the results(./val_rdm42/).

Validation:&nbsp;&nbsp;To save metrics in a csv file and compare predictions to the annotations the jupyter notebook 2-QC_notebook.ipynb can be used on the validation folder.

Large images: To test the model on larger images one can use Whole_ds441.tif (or Crop_ds441.tif )
These images were obtained using the plugin BigSticher on the raw data ( https://doi.org/10.5281/zenodo.6646128 ), resaved as h5 and exported the downsample&nbsp;by 4 version.

&nbsp;

&nbsp;

[https://zenodo.org/records/6645978](https://zenodo.org/records/6645978)

[https://doi.org/10.5281/zenodo.6645978](https://doi.org/10.5281/zenodo.6645978)


---

## 6 Steps Towards Reproducible Research

Heidi Seibold

Licensed CC-BY-4.0



A short book with 6 steps that get you closer to making your work reproducible.

Tags: Reproducibility, Research Data Management

Content type: Book

[https://zenodo.org/records/12744715](https://zenodo.org/records/12744715)


---

## A Cloud-Optimized Storage for Interactive Access of Large Arrays

Josh Moore, Susanne Kunis

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage, Research Data Management

Content type: Publication, Conference Abstract

[https://doi.org/10.52825/cordi.v1i.285](https://doi.org/10.52825/cordi.v1i.285)


---

## A Glimpse of the Open-Source FLIM Analysis Software Tools FLIMfit, FLUTE and napari-flim-phasor-plotter

Anca Margineanu, Chiara Stringari, Marcelo Zoccoler, Cornelia Wetzker

Published 2024-03-27

Licensed CC-BY-4.0



The presentations introduce open-source software to read in, visualize and analyse fluorescence lifetime imaging microscopy (FLIM) raw data developed for life scientists. The slides were presented at German Bioimaging (GerBI) FLIM Workshop held February 26 to 29 2024 at the Biomedical Center of LMU M&uuml;nchen by Anca Margineanu, Chiara Stringari and Conni Wetzker.&nbsp;

[https://zenodo.org/records/10886750](https://zenodo.org/records/10886750)

[https://doi.org/10.5281/zenodo.10886750](https://doi.org/10.5281/zenodo.10886750)


---

## A Hitchhiker's guide through the bio-image analysis software universe

Robert Haase, Elnaz Fazeli, David Legland, Michael Doube, Siân Culley, Ilya Belevich, Eija Jokitalo, Martin Schorb, Anna Klemm, Christian Tischer

Licensed CC-BY-4.0



This article gives an overview about commonly used bioimage analysis software and which aspects to consider when choosing a software for a specific project.

Tags: Bioimage Analysis

Content type: Publication

[https://febs.onlinelibrary.wiley.com/doi/full/10.1002/1873-3468.14451](https://febs.onlinelibrary.wiley.com/doi/full/10.1002/1873-3468.14451)


---

## A journey to FAIR microscopy data

Stefanie Weidtkamp-Peters, Janina Hanne, Christian Schmidt

Published 2023-05-03

Licensed CC-BY-4.0



Oral presentation, 32nd MoMAN &quot;From Molecules to Man&quot; Seminar, Ulm, online. Monday February 6th, 2023

Abstract:

Research data management is essential in nowadays research, and one of the big opportunities to accelerate collaborative and innovative scientific projects. To achieve this goal, all our data needs to be FAIR (findable, accessible, interoperable, reproducible). For data acquired on microscopes, however, a common ground for FAIR data sharing is still to be established. Plenty of work on file formats, data bases, and training needs to be performed to highlight the value of data sharing and exploit its potential for bioimaging data.

In this presentation, Stefanie Weidtkamp-Peters will introduce the challenges for bioimaging data management, and the necessary steps to achieve data FAIRification. German BioImaging - GMB e.V., together with other institutions, contributes to this endeavor. Janina Hanne will present how the network of imaging core facilities, research groups and industry partners is key to the German bioimaging community&rsquo;s aligned collaboration toward FAIR bioimaging data. These activities have paved the way for two data management initiatives in Germany: I3D:bio (Information Infrastructure for BioImage Data) and NFDI4BIOIMAGE, a consortium of the National Research Data Infrastructure. Christian Schmidt will introduce the goals and measures of these initiatives to the benefit of imaging scientist&rsquo;s work and everyday practice. &nbsp;

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/7890311](https://zenodo.org/records/7890311)

[https://doi.org/10.5281/zenodo.7890311](https://doi.org/10.5281/zenodo.7890311)


---

## Abdominal Imaging Window (AIW) for Intravital Imaging

Michael Gerlach

Published 2024-11-15

Licensed CC-BY-4.0



This upload features a simple model for the creation (Manufacturing/Prototyping) of an abdominal imaging window (AIW) for use in mice intravital microscopy.
Manufacture in titanium for chronic implantation. Measures in mm.

[https://zenodo.org/records/14168603](https://zenodo.org/records/14168603)

[https://doi.org/10.5281/zenodo.14168603](https://doi.org/10.5281/zenodo.14168603)


---

## Aberrated Bead Stack

Zach Marin

Published 2024-12-03

Licensed CC-BY-4.0



Bead stack taken on lower path of a 4Pi without deformable mirror corrections. DCIMG examples, not for other purposes.

[https://zenodo.org/records/14268554](https://zenodo.org/records/14268554)

[https://doi.org/10.5281/zenodo.14268554](https://doi.org/10.5281/zenodo.14268554)


---

## Abstract - NFDI Basic Service for Data Management Plans

Licensed CC-BY-4.0



The NFDI Basic Service DMP4NFDI supports consortia in developing and providing data management plans (DMP) services for their community.

Tags: Research Data Management

Content type: Document

[https://base4nfdi.de/images/AbstractDMP4NFDI.pdf](https://base4nfdi.de/images/AbstractDMP4NFDI.pdf)


---

## Advancing FAIR Image Analysis in Galaxy: Tools, Workflows, and Training

Chiang Jurado, Diana, Riccardo Massei, Pavankumar Videm, Anup Kumar, Anne Fouilloux, Leonid Kostrykin, Beatriz Serrano-Solano, Björn Grüning

Published 2025-03-06

Licensed CC-BY-4.0



[https://zenodo.org/records/14979253](https://zenodo.org/records/14979253)

[https://doi.org/10.5281/zenodo.14979253](https://doi.org/10.5281/zenodo.14979253)


---

## Alles meins – oder!? Urheberrechte klären für Forschungsdaten

Stephan Wünsche

Published 2024-06-04

Licensed CC-BY-4.0



Wem geh&ouml;ren Forschungsdaten? Diese Frage stellt sich bei Daten, an deren Entstehung mehrere Personen beteiligt waren, und besonders bei Textdaten, Bildern und Videos. Hier lernen Sie, f&uuml;r Ihr eigenes Forschungsvorhaben zu erkennen, wessen Urheber- und Leistungsschutzrechte zu ber&uuml;cksichtigen sind. Sie erfahren, wie Sie mit Hilfe von Vereinbarungen fr&uuml;hzeitig Rechtssicherheit herstellen, etwa um Daten weitergeben oder publizieren zu k&ouml;nnen.
&nbsp;
&nbsp;

Tags: Research Data Management, Licensing

Content type: Slides

[https://zenodo.org/records/11472148](https://zenodo.org/records/11472148)

[https://doi.org/10.5281/zenodo.11472148](https://doi.org/10.5281/zenodo.11472148)


---

## Angebote der NFDI für die Forschung im Bereich Zoologie

Birgitta König-Ries, Robert Haase, Daniel Nüst, Konrad Förstner, Judith Sophie Engel

Published 2024-12-04

Licensed CC-BY-4.0



In diesem Slidedeck geben wir einen Einblick in Angebote und Dienste der Nationalen Forschungsdaten Infrastruktur (NFDI), die Relevant f&uuml;r die Zoologie und angrenzende Disziplinen relevant sein k&ouml;nnten.

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/14278058](https://zenodo.org/records/14278058)

[https://doi.org/10.5281/zenodo.14278058](https://doi.org/10.5281/zenodo.14278058)


---

## Artificial Blobs and Labels image

Romain

Published 2023-05-10

Licensed CC-BY-4.0



A groovy script to use in Fiji to generate artificial images and labels, with example images.

[https://zenodo.org/records/7919117](https://zenodo.org/records/7919117)

[https://doi.org/10.5281/zenodo.7919117](https://doi.org/10.5281/zenodo.7919117)


---

## Astigmatic 4Pi bead stack

Zach Marin, Maohan Su

Published 2024-12-06

Licensed CC-BY-4.0



Bead stack taken on a 4Pi. DCIMG 0x1000000 file with a 4-pixel correction requirement.

[https://zenodo.org/records/14287640](https://zenodo.org/records/14287640)

[https://doi.org/10.5281/zenodo.14287640](https://doi.org/10.5281/zenodo.14287640)


---

## BIDS-lecture-2024

Robert Haase

Licensed CC-BY-4.0



Training resources for Students at Uni Leipzig who want to dive into bio-image data science with Python. The material developed here between April and July 2024.

Tags: Bioimage Analysis, Artificial Intelligence, Python

Content type: Github Repository

[https://github.com/ScaDS/BIDS-lecture-2024/](https://github.com/ScaDS/BIDS-lecture-2024/)


---

## BIOMERO - A scalable and extensible image analysis framework

Torec T. Luik, Rodrigo Rosas-Bertolini, Eric A.J. Reits, Ron A. Hoebe, Przemek M. Krawczyk

Published None

Licensed CC-BY-4.0



The authors introduce BIOMERO (bioimage analysis in OMERO), a bridge connecting OMERO, a renowned bioimaging data management platform, FAIR workflows, and high-performance computing (HPC) environments.

Tags: OMERO, Workflow, Bioimage Analysis

Content type: Publication

[https://doi.org/10.1016/j.patter.2024.101024](https://doi.org/10.1016/j.patter.2024.101024)


---

## Beads imaged over time

Zach Marin

Published 2025-04-04

Licensed CC-BY-4.0



DCIMG 0x1000000 images of beads over time (30 seconds, 0.03 s exposure).&nbsp;

[https://zenodo.org/records/15150937](https://zenodo.org/records/15150937)

[https://doi.org/10.5281/zenodo.15150937](https://doi.org/10.5281/zenodo.15150937)


---

## BigDataProcessor2: A free and open-source Fiji plugin for inspection and processing of TB sized image data

Christian Tischer, Ashis Ravindran, Sabine Reither, Nicolas Chiaruttini, Rainer Pepperkok, Nils Norlin

Licensed CC-BY-4.0



Tags: Research Data Management, Bioimage Analysis

Content type: Publication

[https://doi.org/10.1093/bioinformatics/btab106](https://doi.org/10.1093/bioinformatics/btab106)


---

## Bio-Image Data Strudel for Workshop on Research Data Management in TU Dresden Core Facilities

Cornelia Wetzker

Published 2023-11-08

Licensed CC-BY-4.0



This presentation gives a short outline of the complexity of data and metadata in the bioimaging universe. It introduces NFDI4BIOIMAGE as a newly formed consortium as part of the German 'Nationale Forschungsdateninfrastruktur' (NFDI) and its goals and tools for data management including its current members on TU Dresden campus. &nbsp;

Tags: Research Data Management, Nfdi4Bioimage

Content type: Slides

[https://zenodo.org/records/10083555](https://zenodo.org/records/10083555)

[https://doi.org/10.5281/zenodo.10083555](https://doi.org/10.5281/zenodo.10083555)


---

## Bio-image Analysis Code Generation

Robert Haase

Published 2024-10-28

Licensed CC-BY-4.0



Large Language Models are changing the way we interact with computers, especially how we write code. In this tutorial, we will generate bio-image analysis code using two LLM-based code generators, bia-bob and git-bob.
https://github.com/haesleinhuepf/bia-bob
https://github.com/haesleinhuepf/git-bob
&nbsp;

[https://zenodo.org/records/14001044](https://zenodo.org/records/14001044)

[https://doi.org/10.5281/zenodo.14001044](https://doi.org/10.5281/zenodo.14001044)


---

## Bio-image Analysis Code Generation using bia-bob

Robert Haase

Published 2024-10-09

Licensed CC-BY-4.0



In this presentation I introduce bia-bob, an AI-based code generator that integrates into Jupyter Lab and allows for easy generation of Bio-Image Analysis Python code. It highlights how to get started with using large language models and prompt engineering to get high-quality bio-image analysis code.

Tags: Artificial Intelligence, Bioimage Analysis

[https://zenodo.org/records/13908108](https://zenodo.org/records/13908108)

[https://doi.org/10.5281/zenodo.13908108](https://doi.org/10.5281/zenodo.13908108)


---

## Bio-image Analysis with the Help of Large Language Models

Robert Haase

Published 2024-03-13

Licensed CC-BY-4.0



Large Language Models (LLMs) change the way how we use computers. This also has impact on the bio-image analysis community. We can generate code that analyzes biomedical image data if we ask the right prompts. This talk outlines introduces basic principles, explains prompt engineering and how to apply it to bio-image analysis. We also compare how different LLM vendors perform on code generation tasks and which challenges are ahead for the bio-image analysis community.

Tags: Artificial Intelligence, Python

Content type: Slides

[https://zenodo.org/records/10815329](https://zenodo.org/records/10815329)

[https://doi.org/10.5281/zenodo.10815329](https://doi.org/10.5281/zenodo.10815329)


---

## Bio-image Data Science

Robert Haase

Licensed CC-BY-4.0



This repository contains training resources for Students at Uni Leipzig who want to dive into bio-image data science with Python.

Tags: Research Data Management, Artificial Intelligence, Bioimage Analysis, Python

Content type: Notebook

[https://github.com/ScaDS/BIDS-lecture-2024](https://github.com/ScaDS/BIDS-lecture-2024)


---

## Bio-image Data Science Lectures @ Uni Leipzig / ScaDS.AI

Robert Haase

Licensed CC-BY-4.0



These are the PPTx training resources for Students at Uni Leipzig who want to dive into bio-image data science with Python. The material developed here between April and July 2024.

Tags: Bioimage Analysis, Artificial Intelligence, Python

Content type: Slides

[https://zenodo.org/records/12623730](https://zenodo.org/records/12623730)


---

## Bio-image analysis, biostatistics, programming and machine learning for computational biology

Anna Poetsch, Biotec Dresden, Marcelo Leomil Zoccoler, Johannes Richard Müller, Robert Haase

Licensed CC-BY-4.0



Tags: Python, Bioimage Analysis, Napari

Content type: Notebook

[https://github.com/BiAPoL/Bio-image_Analysis_with_Python](https://github.com/BiAPoL/Bio-image_Analysis_with_Python)


---

## Bio.tools database

Licensed CC-BY-4.0



Tags: Bioinformatics

Content type: Collection

[https://bio.tools/](https://bio.tools/)


---

## BioFormats Command line (CLI) tools

Published 2024-10-24

Licensed CC-BY-4.0



Bio-Formats is a standalone Java library for reading and writing life sciences image file formats. There are several scripts for using Bio-Formats on the command line, which are listed here.

Content type: Documentation

[https://bio-formats.readthedocs.io/en/v8.0.0/users/comlinetools/index.html](https://bio-formats.readthedocs.io/en/v8.0.0/users/comlinetools/index.html)


---

## BioImage Analysis Notebooks

Robert Haase et al.

Licensed ['CC-BY-4.0', 'BSD-3-CLAUSE']



Tags: Python, Bioimage Analysis

Content type: Book, Notebook

[https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/intro.html](https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/intro.html)


---

## BioImage.IO Chatbot, GloBIAS Seminar

Caterina Fuster-Barcelo

Published 2024-10-02

Licensed CC-BY-4.0



The dynamic field of bioimage analysis continually seeks innovative tools to democratize access to analysis tools and its documentation. The BioImage.IO Chatbot, leveraging state-of-the-art AI technologies including Large Language Models (LLMs) and Retrieval Augmented Generation (RAG), provides an interactive platform that significantly integrates the exploration and application of bioimage analysis tools and models. This seminar will introduce the BioImage.IO Chatbot's capabilities, focusing on how it facilitates access to advanced analysis tools and documentation, allows for the execution of complex models, and enables users to create customized extensions adjusted to specific research needs. In a live demo, attendees will see how to interact with the chatbot and all its assistants and capabilities. Join us to explore how the BioImage.IO Chatbot ca transform your research by making sophisticated analysis more intuitive and accessible.

[https://zenodo.org/records/13880367](https://zenodo.org/records/13880367)

[https://doi.org/10.5281/zenodo.13880367](https://doi.org/10.5281/zenodo.13880367)


---

## Browsing the Open Microscopy Image Data Resource with Python

Robert Haase

Licensed CC-BY-4.0



Tags: OMERO, Python

Content type: Blog Post

[https://biapol.github.io/blog/robert_haase/browsing_idr/readme.html](https://biapol.github.io/blog/robert_haase/browsing_idr/readme.html)


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

## Building a FAIR image data ecosystem for microscopy communities

Isabel Kemmer, Antje Keppler, Beatriz Serrano-Solano, Arina Rybina, Bugra Özdemir, Johanna Bischof, Ayoub El Ghadraoui, John E. Eriksson, Aastha Mathur

Published 2023-03-31

Licensed CC-BY-4.0



Bioimaging has now entered the era of big data with faster than ever development of complex microscopy technologies leading to increasingly complex datasets. This enormous increase in data size and informational complexity within those datasets has brought with it several difficulties in terms of common and harmonized data handling, analysis and management practices, which are currently hampering the full potential of image data being realized. Here we outline a wide range of efforts and solutions currently being developed by the microscopy community to address these challenges on the path towards FAIR bioimage data. We also highlight how different actors in the microscopy ecosystem are working together, creating synergies that develop new approaches, and how research infrastructures, such as Euro-BioImaging, are fostering these interactions to shape the field.&nbsp;

[https://zenodo.org/records/7788899](https://zenodo.org/records/7788899)

[https://doi.org/10.5281/zenodo.7788899](https://doi.org/10.5281/zenodo.7788899)


---

## CZI (Carl Zeiss Image) dataset with artificial test camera images with various dimension for testing libraries reading

Sebastian Rhode

Published 2022-08-22

Licensed CC-BY-4.0



Set of CZI test images created by using a simulated microscope with a test grayscale camera (no LSM or AiryScan or RGB). The filename indicates the used dimension(s)&nbsp;for the acquisition experiment. The files can be used to test the basic functionality of libraries reading CZI files.

Examples:


	S=2_T=3_CH=1.czi = 2 Scenes, 3 TimePoints and 1 Channel
	
		Z-Stack was not activated inside acquisition experiment
	
	
	S=2_T=3_Z=5_CH=2.czi = 2 Scenes, 3 TimePoints, 5-Z-Planes and 1 Channels
	
		Z-Stack was activated inside acquisition experiment
	
	


The test files (so far) contain not any data with more &quot;advanced&quot; dimensions&nbsp;like AiryScan rawdata, illumination angles etc.&nbsp;Also no CZI files with&nbsp;pixel type RGB are included yet.

&nbsp;

&nbsp;

&nbsp;

[https://zenodo.org/records/7015307](https://zenodo.org/records/7015307)

[https://doi.org/10.5281/zenodo.7015307](https://doi.org/10.5281/zenodo.7015307)


---

## CZI file examples

Nicolas Chiaruttini

Published 2023-08-18

Licensed CC-BY-4.0



A set of public CZI files. These can be used for testing CZI readers.

- Demo LISH 4x8 15pct 647.czi: A cleared mouse brain acquired with a Zeiss LightSheet Z1 with 32 tiles. Courtesy of the Carl Petersen lab LSENS (https://www.epfl.ch/labs/lsens). Sampled prepared by Yanqi Liu an imaged by Olivier Burri.
- test_gray.czi: a synthetically generated CZI file without metadata, made by Sebastian Rhode

- Image_1_2023_08_18__14_32_31_964.czi: an example multi-part CZI file, containing only camera noise

- a xt scan, xz scan, xzt scan

- a set of multi angle, multi illumination, mutli tile acquisition, taken on the LightSheet Z1 microscope of the PTBIOP by Lorenzo Tal&agrave;

[https://zenodo.org/records/8305531](https://zenodo.org/records/8305531)

[https://doi.org/10.5281/zenodo.8305531](https://doi.org/10.5281/zenodo.8305531)


---

## Cellpose model for Digital Phase Contrast images

Laura Capolupo, Olivier Burri, Romain Guiet

Published 2022-02-09

Licensed CC-BY-4.0



Name: Cellpose model for Digital Phase Contrast images

Data type: Cellpose model, trained via transfer learning from &lsquo;cyto&rsquo; model.

Training Dataset: Light microscopy (Digital Phase Contrast) and Manual annotations (10.5281/zenodo.5996883)

Training Procedure: Model was trained using a&nbsp;Cellpose version 0.6.5 with GPU support (NVIDIA GeForce RTX 2080) using default settings as per the Cellpose documentation&nbsp;

python -m cellpose --train --dir TRAINING/DATASET/PATH/train --test_dir TRAINING/DATASET/PATH/test --pretrained_model cyto --chan 0 --chan2 0

The model file (MODEL NAME) in this repository is the result of this training.

Prediction Procedure: Using this model, a label image can be obtained from new unseen images in a given folder with

python -m cellpose --dir NEW/DATASET/PATH --pretrained_model FULL_MODEL_PATH --chan 0 --chan2 0 --save_tif --no_npy

[https://zenodo.org/records/6023317](https://zenodo.org/records/6023317)

[https://doi.org/10.5281/zenodo.6023317](https://doi.org/10.5281/zenodo.6023317)


---

## Cellpose models for Label Prediction from Brightfield and Digital Phase Contrast images

Romain Guiet, Olivier Burri

Published 2022-02-25

Licensed CC-BY-4.0



Name:&nbsp;Cellpose models for Brightfield and Digital Phase Contrast images

Data type:&nbsp;Cellpose models trained via transfer learning from the &lsquo;nuclei&rsquo; and &lsquo;cyto2&rsquo; pretrained model with additional Training Dataset . Includes&nbsp;corresponding&nbsp;csv files with &#39;Quality Control&#39; metrics(&sect;) (model.zip).

Training Dataset:&nbsp;Light microscopy (Digital Phase Contrast or Brightfield) and automatic annotations (nuclei or cyto) (https://doi.org/10.5281/zenodo.6140064)

Training Procedure: The cellpose models were trained using cellpose version 1.0.0 with GPU support (NVIDIA GeForce K40) using default settings as per the&nbsp;Cellpose documentation&nbsp;. Training was done using a Renku environment (renku template).

&nbsp;

Command Line Execution for the different trained models

nuclei_from_bf: 

cellpose --train --dir 'data/train/' --test_dir 'data/test/' --pretrained_model nuclei  --img_filter _bf --mask_filter _nuclei --chan 0 --chan2 0 --use_gpu --verbose

cyto_from_bf:

cellpose --train --dir 'data/train/' --test_dir 'data/test/' --pretrained_model cyto2 --img_filter _bf --mask_filter _cyto --chan 0 --chan2 0 --use_gpu --verbose

&nbsp;

nuclei_from_dpc:

cellpose --train --dir 'data/train/' --test_dir 'data/test/' --pretrained_model nuclei  --img_filter _dpc --mask_filter _nuclei --chan 0 --chan2 0 --use_gpu --verbose

cyto_from_dpc:

cellpose --train --dir 'data/train/' --test_dir 'data/test/' --pretrained_model cyto2 --img_filter _dpc --mask_filter _cyto --chan 0 --chan2 0 --use_gpu --verbose

&nbsp;

nuclei_from_sqrdpc:

cellpose --train --dir 'data/train/' --test_dir 'data/test/' --pretrained_model nuclei --img_filter _sqrdpc --mask_filter _nuclei --chan 0 --chan2 0 --use_gpu --verbose

cyto_from_sqrdpc:

cellpose --train --dir 'data/train/' --test_dir 'data/test/' --pretrained_model cyto2 --img_filter _sqrdpc --mask_filter _cyto --chan 0 --chan2 0 --use_gpu --verbose

&nbsp;

NOTE&nbsp;(&sect;):&nbsp;We provide&nbsp;a notebook for Quality Control, which is an adaptation of the&nbsp;&quot;Cellpose (2D and 3D)&quot; notebook from ZeroCostDL4Mic&nbsp;.

NOTE: This dataset used a training dataset from the Zenodo entry(https://doi.org/10.5281/zenodo.6140064) generated from the &ldquo;HeLa &ldquo;Kyoto&rdquo; cells&nbsp;under the scope&rdquo; &nbsp;dataset Zenodo entry(https://doi.org/10.5281/zenodo.6139958) in order to automatically generate the label images.

NOTE: Make sure that you delete the &ldquo;_flow&rdquo; images that are auto-computed when running the training. If you do not, then the flows from previous runs will be used for the new training, which might yield confusing results.

&nbsp;

[https://zenodo.org/records/6140111](https://zenodo.org/records/6140111)

[https://doi.org/10.5281/zenodo.6140111](https://doi.org/10.5281/zenodo.6140111)


---

## Challenges and opportunities for bio-image analysis core-facilities

Robert Haase

Licensed CC-BY-4.0



Tags: Research Data Management, Bioimage Analysis, Nfdi4Bioimage

Content type: Slides

[https://f1000research.com/slides/12-1054](https://f1000research.com/slides/12-1054)


---

## Challenges and opportunities for bioimage analysis core-facilities

Johannes Richard Soltwedel, Robert Haase

Licensed CC-BY-4.0



This article outlines common reasons for founding bioimage analysis core-facilities, services they can provide to fulfill certain need and conflicts of interest that arise from these services.

Tags: Bioimage Analysis, Research Data Management

Content type: Publication

[https://onlinelibrary.wiley.com/doi/full/10.1111/jmi.13192](https://onlinelibrary.wiley.com/doi/full/10.1111/jmi.13192)


---

## ChatGPT for Image Analysis

Robert Haase

Published 2024-08-25

Licensed CC-BY-4.0



Large Language Models (LLMs) such as ChatGPT are changing the way we interact with computers, including how we analye microscopy imaging data. In this talk I introduce basic concepts of asking LLMs to write code and how to modify the questions to get the best out of it. For trying out these prompt engineering basics there are additional online resources available: https://scads.github.io/prompt-engineering-basics-2024/intro.html

[https://zenodo.org/records/13371196](https://zenodo.org/records/13371196)

[https://doi.org/10.5281/zenodo.13371196](https://doi.org/10.5281/zenodo.13371196)


---

## Collaborative Working and Version Control with git[hub]

Robert Haase

Published 2024-01-10

Licensed CC-BY-4.0



This slide deck introduces the version control tool git, related terminology and the Github Desktop app for managing files in Git[hub] repositories. We furthermore dive into:* Working with repositories* Collaborative with others* Github-Zenodo integration* Github pages* Artificial Intelligence answering Github Issues

Tags: Nfdi4Bioimage, Globias, Research Data Management, Research Software Management

[https://zenodo.org/records/14626054](https://zenodo.org/records/14626054)

[https://doi.org/10.5281/zenodo.14626054](https://doi.org/10.5281/zenodo.14626054)


---

## Collaborative bio-image analysis script editing with git

Robert Haase

Licensed CC-BY-4.0



Introduction to version control using git for collaborative, reproducible script editing.

Tags: Sharing, Research Data Management

Content type: Blog Post

[https://focalplane.biologists.com/2021/09/04/collaborative-bio-image-analysis-script-editing-with-git/](https://focalplane.biologists.com/2021/09/04/collaborative-bio-image-analysis-script-editing-with-git/)


---

## Combining the BIDS and ARC Directory Structures for Multimodal Research Data Organization

Torsten Stöter, Tobias Gottschall, Andrea Schrader, Peter Zentis, Monica Valencia-Schneider, Niraj Kandpal, Werner Zuschratter, Astrid Schauss, Timo Dickscheid, Timo Mühlhaus, Dirk von Suchodoletz

Licensed CC-BY-4.0



Interdisciplinary collaboration and integrating large, diverse datasets are crucial for answering complex research questions, requiring multimodal data analysis and adherence to FAIR principles. To address challenges in capturing the full research cycle and contextualizing data, DataPLANT developed the Annotated Research Context (ARC), while the neuroimaging community extended the Brain Imaging Data Structure (BIDS) for microscopic image data, both providing standardized, file system-based storage structures for organizing and sharing data with metadata.

Tags: Research Data Management, FAIR-Principles

Content type: Poster

[https://zenodo.org/doi/10.5281/zenodo.8349562](https://zenodo.org/doi/10.5281/zenodo.8349562)


---

## Conference Slides - 4th Day of Intravital Microscopy

Dr. Hellen Ishikawa-Ankerhold

Published 2024-11-13

Licensed CC-BY-4.0



Conference Slides for the presentation of GerBI e.V. at the 4th Day of Intravital Microscopy in Leuven, Belgium.
Features Structure, activities and Links to join GerBI e.V.

[https://zenodo.org/records/14113714](https://zenodo.org/records/14113714)

[https://doi.org/10.5281/zenodo.14113714](https://doi.org/10.5281/zenodo.14113714)


---

## Crashkurs Forschungsdatenmanagement

Barbara Weiner, Stephan Wünsche, Stefan Kühne, Pia Voigt, Sebastian Frericks, Clemens Hoffmann, Romy Elze, Ronny Gey

Published 2020-04-30

Licensed CC-BY-4.0



Diese Pr&auml;sentation bietet einen Einstieg in alle relevanten Bereiche des Forschungsdatenmanagements an der Universit&auml;t Leipzig. Behandelt werden Grundlagen des Forschungsdatenmanagements, technische, ethische und rechtliche Aspekte sowie die Archivierung und Publikation von Forschungsdaten. Die Pr&auml;sentation enth&auml;lt zahlreiche weiterf&uuml;hrende Links (rot) und Literaturhinweise.

Erg&auml;nzend hierzu wird eine Pr&auml;sentation mit &Uuml;bungsaufgaben angeboten, die helfen soll, das Gelernte zu festigen und in der eigenen Forschungspraxis umzusetzen. Den Aufgaben folgen jeweils eine Antwortfolie sowie deren Aufl&ouml;sung.

Tags: Research Data Management

Content type: Slides

[https://zenodo.org/records/3778431](https://zenodo.org/records/3778431)

[https://doi.org/10.5281/zenodo.3778431](https://doi.org/10.5281/zenodo.3778431)


---

## Creating Workflows and Advanced Workflow Options

Licensed CC-BY-4.0



Tags: Workflow

Content type: Tutorial, Online Tutorial

[https://galaxyproject.org/learn/advanced-workflow/](https://galaxyproject.org/learn/advanced-workflow/)


---

## Creating a Research Data Management Plan using chatGPT

Robert Haase

Published 2023-11-06

Licensed CC-BY-4.0



In this blog post the author demonstrates how chatGPT can be used to combine a fictive project description with a DMP specification to produce a project-specific DMP.

Tags: Research Data Management, Artificial Intelligence

Content type: Blog Post

[https://focalplane.biologists.com/2023/11/06/creating-a-research-data-management-plan-using-chatgpt/](https://focalplane.biologists.com/2023/11/06/creating-a-research-data-management-plan-using-chatgpt/)


---

## Creating open computational curricula

Kari Jordan, Zhian Kamvar, Toby Hodges

Published 2020-12-11

Licensed CC-BY-4.0



In this interactive session, Carpentries team members will guide attendees through three stages of the backward design process to create a lesson development plan for the open source tool of their choosing. Attendees will leave having identified what practical skills they aim to teach (learning objectives), an approach for designing challenge questions (formative assessment), and mechanisms to give and receive feedback.

Content type: Slides

[https://zenodo.org/records/4317149](https://zenodo.org/records/4317149)

[https://doi.org/10.5281/zenodo.4317149](https://doi.org/10.5281/zenodo.4317149)


---

## Cultivating Open Training

Robert Haase

Published 2024-03-14

Licensed CC-BY-4.0



In this SaxFDM Digital Kitchen, I introduced current challenges and potential solutions for openly sharing training materials, softly focusing on bio-image analysis. In this field a lot of training materials circulate in private channels, but openly shared, reusable materials, according to the FAIR-principles, are still rare. Using the CC-BY license and uploading materials to publicly acessible repositories are proposed to fill this gap.

Tags: Open Science, Research Data Management, FAIR-Principles, Bioimage Analysis, Licensing

Content type: Slides

[https://zenodo.org/records/10816895](https://zenodo.org/records/10816895)

[https://doi.org/10.5281/zenodo.10816895](https://doi.org/10.5281/zenodo.10816895)


---

## Cultivating Open Training to advance Bio-image Analysis

Robert Haase

Published 2024-04-25

Licensed CC-BY-4.0




These slides introduce current challenges and potential solutions for openly sharing training materials, focusing on bio-image analysis. In this field a lot of training materials circulate in private channels, but openly shared, reusable materials, according to the FAIR-principles, are still rare. Using the CC-BY license and publicly acessible repositories are proposed to fill this gap.


Tags: Research Data Management, Licensing, FAIR-Principles

Content type: Slides

[https://zenodo.org/records/11066250](https://zenodo.org/records/11066250)

[https://doi.org/10.5281/zenodo.11066250](https://doi.org/10.5281/zenodo.11066250)


---

## DL4MicEverywhere

Iván Hidalgo, et al.

Licensed CC-BY-4.0



Tags: Bioimage Analysis

Content type: Notebook, Collection

[https://github.com/HenriquesLab/DL4MicEverywhere](https://github.com/HenriquesLab/DL4MicEverywhere)


---

## Data Carpentry for Biologists

Licensed ['CC-BY-4.0', 'MIT']



Content type: Tutorial, Code

[https://datacarpentry.org/semester-biology/](https://datacarpentry.org/semester-biology/)


---

## Data life cycle

ELIXIR (2021) Research Data Management Kit

Licensed CC-BY-4.0



In this section, information is organised according to the stages of the research data life cycle.

Tags: Data Life Cycle, Research Data Management

Content type: Collection, Website, Online Tutorial

[https://rdmkit.elixir-europe.org/data_life_cycle](https://rdmkit.elixir-europe.org/data_life_cycle)


---

## Data stewardship and research data management tools for multimodal linking of imaging data in plasma medicine

Mohsen Ahmadi, Robert Wagner, Philipp Mattern, Nick Plathe, Sander Bekeschus, Markus M. Becker, Torsten Stöter, Stefanie Weidtkamp-Peters

Published 2023-11-03

Licensed CC-BY-4.0



A more detailed understanding of the effect of plasmas on biological systems can be fostered by combining data from different imaging modalities, such as optical imaging, fluorescence imaging, and mass spectrometry imaging. This, however, requires the implementation and use of sophisticated research data management (RDM) solutions to incorporate the influence of plasma parameters and treatment procedures as well as the effects of plasma on the treated targets. In order to address this, RDM activities on different levels and from different perspectives are started and brought together within the framework of the NFDI consortium NFDI4BIOIMAGE.

[https://zenodo.org/records/10069368](https://zenodo.org/records/10069368)

[https://doi.org/10.5281/zenodo.10069368](https://doi.org/10.5281/zenodo.10069368)


---

## DataPLANT knowledge base

Published 2022-12-14

Licensed CC-BY-4.0



Explore fundamental topics on research data management (RDM), how DataPLANT implements these aspects to support plant researchers with RDM tools and services, read guides and manuals or search for some teaching materials.

Tags: Research Data Management, Dataplant

Content type: Collection

[https://nfdi4plants.org/nfdi4plants.knowledgebase/index.html](https://nfdi4plants.org/nfdi4plants.knowledgebase/index.html)


---

## Dataset from InCell 2200 microscope misread as a plate

Fabien Kuttler, Rémy Dornier

Published 2025-01-30

Licensed CC-BY-4.0



Two dummy datasets are provided in this repository :&nbsp;

Dataset_Ok : 96 wells, 9 fields of view per well, 4 different channels (DAPI, Cy3, FITC, Brightfield), no Z, no T. The .xcde file of this dataset is correctly read by BioFormats, as the dataset is recognized as a plate, and can be imported on OMERO
Dataset_fail: 20 wells, 4 fields of view per well, 5 channels, with one duplicate (DAPI, FITC, Cy3, Cy5 wix 4 , Cy5 wix 5), no Z, no T. The .xcde file of this dataset is not correctly read by BioFormats and no images are imported on OMERO.

BioFormats version: 8.0.1
A discussion thread has been open on this topic.

[https://zenodo.org/records/14769820](https://zenodo.org/records/14769820)

[https://doi.org/10.5281/zenodo.14769820](https://doi.org/10.5281/zenodo.14769820)


---

## Datenmanagement

Robert Haase

Published 2024-04-14

Licensed CC-BY-4.0



In dieser Data Management Session wird der Lebenszyklus von Daten n&auml;her beleuchtet. Wie entstehen Daten, was passiert mit ihnen, wenn sie verarbeitet werden? Wem geh&ouml;ren die Daten und wer ist daf&uuml;r verantwortlich, sie zu ver&ouml;ffentlichen, zu archivieren und gegebenenfalls wiederzuverwenden? Wir werden einen Datenmanagementplan in Gruppenarbeit entwerfen, ggf. mit Hilfe von ChatGPT.

Tags: Research Data Management

Content type: Slides

[https://zenodo.org/records/10970869](https://zenodo.org/records/10970869)

[https://doi.org/10.5281/zenodo.10970869](https://doi.org/10.5281/zenodo.10970869)


---

## Datenmanagement im Fokus: Organisation, Speicherstrategien und Datenschutz

Pia Voigt, Carolin Hundt

Published 2024-04-19

Licensed CC-BY-4.0



 Workshop zum Thema &bdquo;Datenmanagement im Fokus: Organisation, Speicherstrategien und Datenschutz&ldquo; auf der Data Week Leipzig
Der Umgang mit Daten ist im Alltag nicht immer leicht: Wie und wo speichert man Daten idealerweise? Welche Strategien helfen, den &Uuml;berblick zu behalten und wie geht man mit personenbezogenen Daten um? Diese Fragen m&ouml;chten wir gemeinsam mit Ihnen anhand individueller Datenprobleme besprechen und Ihnen L&ouml;sungen aufzeigen, wie Sie ihr Datenmanagement effizient gestalten k&ouml;nnen.

Tags: Research Data Management

Content type: Slides

[https://zenodo.org/records/11107798](https://zenodo.org/records/11107798)

[https://doi.org/10.5281/zenodo.11107798](https://doi.org/10.5281/zenodo.11107798)


---

## Datenmanagementpläne erstellen - Teil 1

Pia Voigt, Barbara Weiner

Published 2021-03-23

Licensed CC-BY-4.0



Was ist ein Datenmanagementplan? Welche Vorgaben sollte ich beachten? Wie erstelle ich einen solchen f&uuml;r mein Forschungsprojekt und welche n&uuml;tzlichen Tools kann ich hierf&uuml;r verwenden?

Die Anforderungen der Forschungsf&ouml;rderer zum Datenmanagement steigen stetig. Damit verbunden ist h&auml;ufig auch das Erstellen eines Datenmanagementplans. Dabei erwarten DFG, BMBF oder die EU jeweils unterschiedliche Angaben zur Erhebung, Speicherung und Ver&ouml;ffentlichung von projektbezogenen Forschungsdaten. Zudem bietet das Erstellen eines Datenmanagementplans viele Vorteile und hilft Ihnen nicht zuletzt, die Anforderungen der guten wissenschaftlichen Praxis strukturiert umzusetzen.

Was im ersten Moment un&uuml;bersichtlich und &uuml;berfordernd wirkt, soll in diesem Kurs anhand einer grundlegenden theoretischen Einf&uuml;hrung im ersten und praxisorientierter Beispiele im zweiten Teil der Veranstaltung handhabbar gemacht werden. Sie lernen, was hinter den Anforderungen der Forschungsf&ouml;rderer steckt, welche Elemente ein Datenmanagementplan enthalten sollte und wie sie einen solchen mithilfe interaktiver Tools selbst erstellen k&ouml;nnen.

Tags: Research Data Management

Content type: Slides

[https://zenodo.org/records/4630788](https://zenodo.org/records/4630788)

[https://doi.org/10.5281/zenodo.4630788](https://doi.org/10.5281/zenodo.4630788)


---

## Datenmanagementpläne erstellen - Teil 2

Pia Voigt, Barbara Weiner

Published 2021-03-30

Licensed CC-BY-4.0



Was ist ein Datenmanagementplan? Welche Vorgaben sollte ich beachten? Wie erstelle ich einen solchen f&uuml;r mein Forschungsprojekt und welche n&uuml;tzlichen Tools kann ich hierf&uuml;r verwenden?

Die Anforderungen der Forschungsf&ouml;rderer zum Datenmanagement steigen stetig. Damit verbunden ist h&auml;ufig auch das Erstellen eines Datenmanagementplans. Dabei erwarten DFG, BMBF oder die EU jeweils unterschiedliche Angaben zur Erhebung, Speicherung und Ver&ouml;ffentlichung von projektbezogenen Forschungsdaten. Zudem bietet das Erstellen eines Datenmanagementplans viele Vorteile und hilft Ihnen nicht zuletzt, die Anforderungen der guten wissenschaftlichen Praxis strukturiert umzusetzen.

Was im ersten Moment un&uuml;bersichtlich und &uuml;berfordernd wirkt, soll in diesem Kurs anhand einer grundlegenden theoretischen Einf&uuml;hrung im ersten und praxisorientierter Beispiele im zweiten Teil der Veranstaltung handhabbar gemacht werden. Sie lernen, was hinter den Anforderungen der Forschungsf&ouml;rderer steckt, welche Elemente ein Datenmanagementplan enthalten sollte und wie sie einen solchen mithilfe interaktiver Tools selbst erstellen k&ouml;nnen.

Version 2 enth&auml;lt aktuelle Links und weiterf&uuml;hrende Hinweise zu einzelnen Aspekten eines Datenmanagementplans.

Version 3 ist die &uuml;berarbeitete und aktualisierte Version der ersten beiden und enth&auml;lt u.a. Hinweise zur Lizenzierung und zu Nutzungsrechten an Forschungsdaten.

Tags: Research Data Management

Content type: Slides

[https://zenodo.org/records/4748534](https://zenodo.org/records/4748534)

[https://doi.org/10.5281/zenodo.4748534](https://doi.org/10.5281/zenodo.4748534)


---

## Deconvolution Test Dataset

Romain Guiet

Published 2021-07-14

Licensed CC-BY-4.0



This a test dataset, HeLa cells stained for action using Phalloidin-488&nbsp;acquired on confocal Zeiss LSM710, which contains

- Ph488.czi (contains all raw metadata)

- Raw_large.tif ( is the tif version of Ph488.czi, provided for conveninence as&nbsp;tif doesn&#39;t need Bio-Formats&nbsp;to be open in Fiji&nbsp;)

- Raw.tif , is a crop of the large image

-&nbsp;PSFHuygens_confocal_Theopsf.tif , is a theoretical PSF generated with HuygensPro

-&nbsp;PSFgen_WF_WBpsf.tif&nbsp; , is a theoretical PSF generated with PSF generator

- PSFgen_WFsquare_WBpsf.tif, is the result of&nbsp;the&nbsp;square operation on PSFgen_WF_WBpsf.tif , to approximate a confocal PSF

[https://zenodo.org/records/5101351](https://zenodo.org/records/5101351)

[https://doi.org/10.5281/zenodo.5101351](https://doi.org/10.5281/zenodo.5101351)


---

## Developing (semi)automatic analysis pipelines and technological solutions for metadata annotation and management in high-content screening (HCS) bioimaging

Riccardo Massei, Stefan Scholz, Wibke Busch, Thomas Schnike, Hannes Bohring, Jan Bumberger

Licensed CC-BY-4.0



High-content screening (HCS) bioimaging automates the imaging and analysis of numerous biological samples, generating extensive metadata that is crucial for effective image management and interpretation. Efficiently handling this complex data is essential to implementing FAIR principles and realizing HCS's full potential for scientific discoveries.

Tags: Bioimage Analysis

Content type: Poster

[https://doi.org/10.5281/zenodo.8434325](https://doi.org/10.5281/zenodo.8434325)


---

## Developing a Training Strategy

Robert Haase

Published 2024-11-08

Licensed CC-BY-4.0



When training people in topics such as programming, bio-image analysis or data science, it makes sense to define a training strategy with a wider perspective than just trainees needs. This slide deck gives insights into aspects to consider when defining a training strategy. It considers funder's interests, financial aspects, metrics / goals, steps towards sustainability and opportunities for outreach and for founding future collaborations.

[https://zenodo.org/records/14053758](https://zenodo.org/records/14053758)

[https://doi.org/10.5281/zenodo.14053758](https://doi.org/10.5281/zenodo.14053758)


---

## Developing open-source software for bioimage analysis: opportunities and challenges

Florian Levet, Anne E. Carpenter, Kevin W. Eliceiri, Anna Kreshuk, Peter Bankhead, Robert Haase

Licensed CC-BY-4.0



This article outlines common challenges and practices when developing open-source software for bio-image analysis.

Tags: Neubias

Content type: Publication

[https://f1000research.com/articles/10-302](https://f1000research.com/articles/10-302)


---

## Development of a platform for advanced optics education, training and prototyping

Nadine Utz, Sabine Reither, Ruth Hans, Christian Feldhaus

Published 2023-10-05

Licensed CC-BY-4.0



In bio-medical research we often need to combine a broad range of expertise to run complex experiments and analyse and interpret their results. Also, it is desirable that all stakeholders of a project understand all parts of the experiment and analysis to draw and support the right conclusions. For imaging experiments this usually requires a basic understanding of the underlying physics. This has not necessarily been part of the professional training of all stakeholders, e.g. biologists or data scientists. Therefore an affordable platform for easily demonstrating and explaining imaging principles would be desirable.
Building up on a commercially available STEM Optics kit we developed extensions with widely available and affordable components to demonstrate advanced imaging techniques like e.g. confocal, lightsheet, OPT, spectral imaging. All models are quick and easy to build, yet demonstrate the important physical principles each imaging technique is based on.
Further use cases for this kit are training courses, demonstrations for imaging newbies when designing an experiment and outreach activities but also basic level prototyping.

[https://zenodo.org/records/10925217](https://zenodo.org/records/10925217)

[https://doi.org/10.5281/zenodo.10925217](https://doi.org/10.5281/zenodo.10925217)


---

## Digital Phase Contrast on Primary Dermal Human Fibroblasts cells

Laura Capolupo

Published 2022-02-09

Licensed CC-BY-4.0



Name: Digital Phase Contrast on Primary Dermal Human Fibroblasts cells&nbsp;

Data type: Paired microscopy images (Digital Phase Contrast, square rooted) and corresponding labels/masks used for cellpose training (the corresponding Brightfield images are also present), organized as recommended by cellpose documentation.

Microscopy data type: Light microscopy (Digital Phase Contrast and Brighfield )

Manual annotations: Labels/masks obtained via manual segmentation.&nbsp;For each region, all cells were annotated manually. Uncertain objects (Dust, fused cells) were left unannotated, so that the cellpose model (10.5281/zenodo.6023317) may mimic the same user bias during prediction. This was particularly necessary due to the accumulation of floating debris in the center of the well.

Microscope: Perkin Elmer Operetta microscope with a 10x 0.35 NA objective

Cell type: Primary Dermal Human Fibroblasts cells

File format: .tif (16-bit for DPC and 16-bit for the masks)

Image size: 1024x1024 (Pixel size: 634 nm)

NOTE : This dataset was used to train cellpose model ( 10.5281/zenodo.6023317 )

&nbsp;

[https://zenodo.org/records/5996883](https://zenodo.org/records/5996883)

[https://doi.org/10.5281/zenodo.5996883](https://doi.org/10.5281/zenodo.5996883)


---

## EDAM-bioimaging - The ontology of bioimage informatics operations, topics, data, and formats

Matúš Kalaš et al.

Licensed CC-BY-4.0



EDAM-bioimaging is an extension of the EDAM ontology, dedicated to bioimage analysis, bioimage informatics, and bioimaging.

Tags: Ontology, Bioimage Analysis

Content type: Poster

[https://hal.science/hal-02267597/document](https://hal.science/hal-02267597/document)


---

## EDAM-bioimaging: The ontology of bioimage informatics operations, topics, data, and formats (update 2020)

Matúš Kalaš, Laure Plantard, Joakim Lindblad, Martin Jones, Nataša Sladoje, Moritz A Kirschmann, Anatole Chessel, Leandro Scholz, Fabianne Rössler, Laura Nicolás Sáenz, Estibaliz Gómez de Mariscal, John Bogovic, Alexandre Dufour, Xavier Heiligenstein, Dominic Waithe, Marie-Charlotte Domart, Matthia Karreman, Raf Van de Plas, Robert Haase, David Hörl, Lassi Paavolainen, Ivana Vrhovac Madunić, Dean Karaica, Arrate Muñoz-Barrutia, Paula Sampaio, Daniel Sage, Sebastian Munck, Ofra Golani, Josh Moore, Florian Levet, Jon Ison, Alban Gaignard, Hervé Ménager, Chong Zhang, Kota Miura, Julien Colombelli, Perrine Paul-Gilloteaux

Licensed CC-BY-4.0



Tags: Metadata

Content type: Publication, Poster

[https://f1000research.com/posters/9-162](https://f1000research.com/posters/9-162)


---

## Efficiently starting institutional research data management

Katarzyna Biernacka, Katrin Cortez, Kerstin Helbig

Published 2019-10-15

Licensed CC-BY-4.0



Researchers are increasingly often confronted with research data management (RDM) topics during their work. Higher education institutions therefore begin to offer services for RDM at some point to give support and advice. However, many groundbreaking decisions have to be made at the very beginning of RDM services. Priorities must be set and policies formulated. Likewise, the staff must first be qualified in order to provide advice and adequately deal with the manifold problems awaiting.
The FDMentor project has therefore bundled the expertise of five German universities with different experiences and levels of RDM knowledge to jointly develop strategies, roadmaps, guidelines, and open access training material. Humboldt-Universit&auml;t zu Berlin, Freie Universit&auml;t Berlin, Technische Universit&auml;t Berlin, University of Potsdam, and European University Viadrina Frankfurt (Oder) have worked together on common solutions that are easy to adapt. With funding of the German Federal Ministry of Education and Research, the collaborative project addressed four problem areas: strategy development, legal issues, policy development, and competence enhancement. The aim of the project outcomes is to provide other higher education institutions with the best possible support for the efficient introduction of research data management. Therefore, all project results are freely accessible under the CC-BY 4.0 international license. The early involvement of the community in the form of workshops and the collection of feedback has proven its worth: the FDMentor strategies, roadmaps, guidelines, and training materials are applied and adapted beyond the partner universities.

Tags: Research Data Management

Content type: Document

[https://zenodo.org/record/3490058](https://zenodo.org/record/3490058)

[https://doi.org/10.5281/zenodo.3490058](https://doi.org/10.5281/zenodo.3490058)


---

## Einblicke ins Forschungsdatenmanagement - Darf ich das veröffentlichen? Rechtsfragen im Umgang mit Forschungsdaten

Stephan Wünsche, Pia Voigt

Published 2021-05-11

Licensed CC-BY-4.0



Diese Pr&auml;sentation wurde im Zuge der digitalen Veranstaltungsreihe &quot;Einblicke ins Forschungsdatenmanagement&quot; erstellt. Diese findet seit dem SS 2020 an der Universit&auml;t Leipzig f&uuml;r alle Interessierten zu verschiedenen Themen des Forschungsdatenmanagements statt.

Dieser Teil der Reihe dreht sich um Rechtsfragen im Umgang mit Forschungsdaten und deren Bedeutung f&uuml;r die wissenschaftliche Praxis. Sie finden in der vorliegenden Pr&auml;sentation einen &Uuml;berblick &uuml;ber relevante Rechtsbereiche sowie Erl&auml;uterungen zum Datenschutz, Urheberrecht und den Grunds&auml;tzen der guten wissenschaftlichen Praxis mit Fokus auf deren Bedeutung im Forschungsdatenmanagement.

Tags: Research Data Management, Data Protection

Content type: Slides

[https://zenodo.org/records/4748510](https://zenodo.org/records/4748510)

[https://doi.org/10.5281/zenodo.4748510](https://doi.org/10.5281/zenodo.4748510)


---

## Erstellung und Realisierung einer institutionellen Forschungsdaten-Policy

Uli Hahn, Kerstin Helbig, Gerald Jagusch, Jessica Rex

Published  2018-10-22

Licensed CC-BY-4.0



Die vorliegende Empfehlung sowie die zugehörigen Erfahrungsberichte geben einen Überblick über die verschiedenen Möglichkeiten der Gestaltung einer Forschungsdatenmanagement Policy sowie Wege zu deren Erstellung.

Tags: Research Data Management

Content type: Publication

[https://bausteine-fdm.de/article/view/7945](https://bausteine-fdm.de/article/view/7945)

[https://doi.org/10.17192/bfdm.2018.1.7945](https://doi.org/10.17192/bfdm.2018.1.7945)


---

## Euro-BioImaging  Scientific Ambassadors Program

Beatriz Serrano-Solano

Published 2023-07-25

Licensed CC-BY-4.0



Graduation presentation for the 7th cohort of the Open Seeds mentoring &amp; training program for Open Science ambassadors. The project presented is called &quot;Euro-BioImaging &nbsp;Scientific Ambassadors Program&quot;.

[https://zenodo.org/records/8182154](https://zenodo.org/records/8182154)

[https://doi.org/10.5281/zenodo.8182154](https://doi.org/10.5281/zenodo.8182154)


---

## Euro-BioImaging ERIC Annual Report 2022

Euro-BioImaging ERIC

Published 2023-07-14

Licensed CC-BY-4.0



Euro-BioImaging ERIC is the European landmark research infrastructure for biological and biomedical imaging as recognized by the European Strategy Forum on Research Infrastructures (ESFRI). Euro-BioImaging is the gateway to world-class imaging facilities across Europe. This document is the Euro-BioImaging Annual Report for the year 2022.

[https://zenodo.org/records/8146412](https://zenodo.org/records/8146412)

[https://doi.org/10.5281/zenodo.8146412](https://doi.org/10.5281/zenodo.8146412)


---

## Euro-BioImaging's Guide to FAIR BioImage Data - Practical Tasks

Isabel Kemmer, Euro-BioImaging ERIC

Published 2024-06-04

Licensed CC-BY-4.0



Hands-on exercises on FAIR Bioimage Data from the interactive online workshop "Euro-BioImaging's Guide to FAIR BioImage Data 2024" (https://www.eurobioimaging.eu/news/a-guide-to-fair-bioimage-data-2024/).&nbsp; Types of tasks included: FAIR characteristics of a real world dataset Data Management Plan (DMP) Journal Policies on FAIR data sharing Ontology search Metadata according to REMBI scheme (Image from: Sarkans, U., Chiu, W., Collinson, L. et al. REMBI: Recommended Metadata for Biological Images&mdash;enabling reuse of microscopy data in biology. Nat Methods 18, 1418&ndash;1422 (2021). https://doi.org/10.1038/s41592-021-01166-8) Matching datasets to bioimage repositories Browsing bioimage repositories

Tags: Bioimage Analysis, FAIR-Principles, Research Data Management

Content type: Slides, Tutorial

[https://zenodo.org/records/11474407](https://zenodo.org/records/11474407)

[https://doi.org/10.5281/zenodo.11474407](https://doi.org/10.5281/zenodo.11474407)


---

## Euro-BioImaging's Template for Research Data Management Plans

Isabel Kemmer, Euro-BioImaging ERIC

Published 2024-06-04

Licensed CC-BY-4.0



Euro-BioImaging has developed a Data Management Plan (DMP) template with questions tailored to bioimaging research projects. Outlining data management practices in this way ensures traceability of project data, allowing for a continuous and unambiguous flow of information throughout the research project. This template can be used to satisfy the requirement to submit a DMP to certain funders. Regardless of the funder, Euro-BioImaging users are encouraged to provide a DMP and can use this template accordingly.&nbsp;
This DMP template is available as a fillable PDF with further instructions and sample responses available by hovering over the fillable fields.&nbsp;

Tags: Bioimage Analysis, FAIR-Principles, Research Data Management

Content type: Collection, Tutorial

[https://zenodo.org/records/11473803](https://zenodo.org/records/11473803)

[https://doi.org/10.5281/zenodo.11473803](https://doi.org/10.5281/zenodo.11473803)


---

## Euro-BioImaging/BatchConvert: v0.0.4

bugraoezdemir

Published 2024-02-19

Licensed CC-BY-4.0



Changes implemented since v0.0.3

Support provided for file paths with spaces.
Support provided for globbing filenames from s3 for one-to-one conversion (parse_s3_filenames.py modified).
Support provided for single file import from s3 (parse_s3_filenames.py modified).
run_conversion.py replaces batchconvert_cli.sh and construct_cli.py, uniting them.
Error handling updated for each process


[https://zenodo.org/records/10679318](https://zenodo.org/records/10679318)

[https://doi.org/10.5281/zenodo.10679318](https://doi.org/10.5281/zenodo.10679318)


---

## Evident OIR sample files tiles + stitched image - FV 4000

Nicolas Chiaruttini

Published 2024-09-04

Licensed CC-BY-4.0



The files contained in this repository are confocal images taken with the Evident FV 4000 of a sample containing DAPI and mCherry stains, excited with a 405 nm laser and a 561 nm laser

individual tiles are named `tiling-sample-brain-section_A01_G001_{i}.oir`
The stiched image is named `Stitch_A01_G001` and contains an extra file `Stitch_A01_G001_00001`
Some metadata like the tiles positions are stored in the extra files (omp2info)

&nbsp;

[https://zenodo.org/records/13680725](https://zenodo.org/records/13680725)

[https://doi.org/10.5281/zenodo.13680725](https://doi.org/10.5281/zenodo.13680725)


---

## Evident OIR sample files with lambda scan - FV 4000

Nicolas Chiaruttini

Published 2024-07-18

Licensed CC-BY-4.0



The files contained in this repository are confocal images taken with the Evident FV 4000 of a sample containing DAPI and mCherry stains, excited with the 405 nm laser and images for different emission windows (lambda scan).
They are public sample files which goal is to help test edge cases of the bio-formats library (https://www.openmicroscopy.org/bio-formats/), in particular for the proper handling of lambda scans.

DAPI_mCherry_22Lambda-420-630-w10nm-s10nm.oir : 22 planes, each plane is an emission window, starting from 420 nm up to 630 nm by steps of 10 nm
DAPI_mCherry_4T_5Lambda-420-630-w10nm-s50nm.oir : 20 planes, 5 lambdas from 420 to 630 nm by steps of 50 nm, 4 timepoints
DAPI_mCherry_4Z_5Lambda-420-630-w10nm-s50nm.oir : 20 planes, 5 lambdas from 420 to 630 nm by steps of 50 nm, 4 slices
DAPI-mCherry_3T_4Z_5Lambda-420-630-w10nm-s50nm.oir : 60 planes, 5 lambdas from 420 to 630 nm by steps of 50 nm, 4 slices, 3 timepoints


[https://zenodo.org/records/12773657](https://zenodo.org/records/12773657)

[https://doi.org/10.5281/zenodo.12773657](https://doi.org/10.5281/zenodo.12773657)


---

## Example Imaris ims datasets.

Marco Stucchi

Published 2024-11-28

Licensed CC-BY-4.0



The files contained in this repository are example Imaris ims images.
&nbsp;
Initially related to https://github.com/ome/bioformats/pull/4249

[https://zenodo.org/records/14235726](https://zenodo.org/records/14235726)

[https://doi.org/10.5281/zenodo.14235726](https://doi.org/10.5281/zenodo.14235726)


---

## Example Microscopy Metadata JSON files produced using Micro-Meta App to document example microscopy experiments performed at individual core facilities

Alessandro Rigano, Ulrike Boehm, Claire M. Brown, Joel Ryan, James J. Chambers, Robert A. Coleman, Orestis Faklaris, Thomas Guilbert, Michelle S. Itano, Judith Lacoste, Alex Laude, Marco Marcello, Paula Montero-Llopis, Glyn Nelson, Roland Nitschke, Jaime A. Pimentel, Stefanie Weidtkamp-Peters, Caterina Strambio-De-Castillia

Published 2022-01-15

Licensed CC-BY-4.0



Example Microscopy Metadata (Microscope.JSON and Settings.JSON) files produced using Micro-Meta App to document the Hardware Specifications of example Microscopes and the Image Acquisition Settings utilized to acquire example images as listed in the table below.


For each facility, the dataset contains two JSON files:


	Microscope.JSON file (e.g., 01_marcello_uliverpool_cci_zeiss_axioobserz1_lsm710.json)
	Settings.JSON file (indicated with the name of the image and with the _AS suffix)



Micro-Meta App was developed as part of a global community initiative including the 4D Nucleome (4DN) Imaging Working Group, BioImaging North America (BINA) Quality Control and Data Management Working Group, and QUAlity and REProducibility for Instrument and Images in Light Microscopy (QUAREP-LiMi), to extend the Open Microscopy Environment (OME) data model.


The works of this global community effort resulted in multiple publications featured on a recent Nature Methods FOCUS ISSUE dedicated to Reporting and reproducibility in microscopy.



Learn More! For a thorough description of Micro-Meta App consult our recent Nature Methods and BioRxiv.org publications!


&nbsp;


	
		
			Nr.
			Manufacturer
			Model
			Tier
			&Epsilon;xperiment Type
			Facility Name
			Department and Institution
			URL
			References
		
		
			1
			Carl Zeiss Microscopy
			Axio Observer Z1 (with LSM 710 scan head)
			1
			3D visualization of superhydrophobic polymer-nanoparticles
			Centre for Cell Imaging (CCI)
			University of Liverpool
			https://cci.liv.ac.uk/equipment_710.html
			Upton et al., 2020
		
		
			2
			Carl Zeiss Microscopy
			Axio Observer (Axiovert 200M)
			2
			&Mu;easurement of illumination stability on Chinese Hamster Ovary cells expressing Paxillin-EGFP
			Advanced BioImaging Facility (ABIF).
			McGill University
			https://www.mcgill.ca/abif/equipment/axiovert-1
			Kiepas et al., 2020
		
		
			3
			Carl Zeiss Microscopy
			Axio Observer Z1 (with Spinning Disk)
			2
			Immunofluorescence imaging of cryosection of Mouse kidney
			Imagerie Cellulaire; Quality Control managed by Miacellavie (https://miacellavie.com/)
			Centre de recherche du Centre Hospitalier Universit&eacute; de Montr&eacute;al (CR CHUM), University of Montreal
			https://www.chumontreal.qc.ca/crchum/plateformes-et-services&nbsp; (the web site is for all core facilities, not specifically for the core facility hosting this microscope)
			Pilliod et al., 2020
		
		
			4
			Carl Zeiss Microscopy
			Axio Imager Z2 (with Apotome)
			2
			Immunofluorescence imaging of mitotic division in Hela cells using&nbsp;&nbsp;
			Bioimaging Unit
			Newcastle University
			https://www.ncl.ac.uk/bioimaging/
			Watson et al., 2020
		
		
			5
			Carl Zeiss Microscopy
			Axio Observer Z1
			2
			Fluorescence microscopy of human skin fibroblasts from Glycogen Storage Disease patients.
			Life Imaging Center (LIC)
			Centre for Integrative Signalling Analysis (CISA), University of Freiburg
			https://miap.eu/equipments/sd-i-abl/
			Hannibal et al., 2020
		
		
			6
			Leica Microsystems
			DMI6000B
			2
			3D immunofluorescence imaging&nbsp; rhinovirus infected macrophages&nbsp;
			IMAG&#39;IC Confocal Microscopy Facility
			Institut Cochin, CNRS, INSERM, Universit&eacute; de Paris
			https://www.institutcochin.fr/core_facilities/confocal-microscopy/cochin-imaging-photonic-microscopy/organigram_team/10054/view
			Jubrail et al., 2020
		
		
			7
			Leica Microsystems
			DM5500B
			2
			Immunofluorescence analysis of the colocalization of PML bodies with DNA double-strand breaks
			Bioimaging Unit
			Edwardson Building on the Campus for Ageing and Vitality, Newcastle University
			https://www.ncl.ac.uk/bioimaging/equipment/leica-dm5500/#overview
			da Silva et al., 2019; Nelson et al., 2012
			&nbsp;&nbsp;
		
		
			8
			Leica Microsystems
			DMI8-CS (with TCS SP8 STED 3X)
			2
			Live-cell imaging of N. benthamiana leaves cells-derived protoplasts
			Center for Advanced Imaging (CAi)
			School of Mathematics/Natural Sciences, Heinrich-Heine-Universit&auml;t D&uuml;sseldorf
			https://www.cai.hhu.de/en/equipment/super-resolution-microscopy/leica-tcs-sp8-sted-3x
			Singer et al., 2017; H&auml;nsch et al., 2020
		
		
			9
			Nikon Instruments
			Eclipse Ti
			2
			Immunofluorescence analysis of the cytoskeleton structure in COS cells
			Advanced Imaging Center (AIC)
			Janelia Research Campus, Howard Hughes Medical Institute
			https://www.janelia.org/support-team/light-microscopy/equipment
			Abdelfattah et al., 2019; Qian et al., 2019; Grimm et al., 2020
		
		
			10
			Nikon Instruments
			Eclipse Ti-E (HCA)
			2
			&Tau;ime-lapse analysis of the bursting behavior of amine-functionalized vesicular assemblies
			Light Microscopy Facility (IALS-LIF)
			Institute for Applied Life Sciences, University of Massachusetts at Amherst
			https://www.umass.edu/ials/light-microscopy
			Fernandez et al., 2020
		
		
			11
			Nikon Instruments/Coleman laboratory (customized)
			TIRF HILO Epifluorescence light Microscope (THEM)/ Eclipse Ti
			2
			Single-particle tracking of Halo-tagged PCNA in Lox cells
			Coleman laboratory
			Anatomy and Structural Biology Department, The Albert Einstein College of Medicine
			https://einsteinmed.org/faculty/12252/robert-coleman/
			Drosopoulos et al., 2020
		
		
			12
			Nikon Instruments
			Eclipse Ti (with Andor Dragon Fly Spinning Disk)
			2
			Investigation of the 3D structure of cerebral organoids
			Montpellier Resources Imagerie
			Centre de Recherche de Biologie cellulaire de Montpellier (MRI-CRBM), CNRS, Univerity of Montpellier
			https://www.mri.cnrs.fr/en/optical-imaging/our-facilities/mri-crbm.html
			Ayala-Nunez et al., 2019
		
		
			13
			Nikon Instruments
			Eclipse Ti2
			2
			&Iota;mmunofluorescence imaging of cryosections of mouse hearth myocardium&nbsp;
			Neuroscience Center Microscopy Core
			Neuroscience Center, University of North Carolina
			https://www.med.unc.edu/neuroscience/core-facilities/neuro-microscopy/
			Aghajanian et al., 2021
		
		
			14
			Nikon Instruments
			Eclipse Ti2
			2
			Live-cell imaging of bacterial cells expressing GFP-PopZ
			Microscopy Resources on the North Quad (MicRoN)
			Harvard Medical School&nbsp;
			https://micron.hms.harvard.edu/
			Lim and Bernhardt 2019; Lim et al., 2019
		
		
			15
			Olympus/Biomedical Imaging Group (customized)
			TIRF Epifluorescence Structured light Microscope (TESM)/IX71
			3
			3D distribution of HIV-1 in the nucleus of human cells
			Biomedical Imaging Group
			Program in Molecular Medicine, University of Massachusetts Medical School
			https://trello.com/b/BQ8zCcQC/tirf-epi-fluorescence-structured-light-microscope
			Navaroli et al., 2012
		
		
			16
			Olympus/Computer Vision Laboratory (customized)
			3D BrightField Scanner/IX71
			3
			Transmitted light brightfield visualization of swimming spermatocytes
			Laboratorio Nacional de Microscopia Avanzada (LNMA) and Computer Vision Laboratory of the Institute of Biotechnology
			Universidad Nacional Autonoma de Mexico (UNAM)
			https://lnma.unam.mx/wp/
			Pimentel et al., 2012; Silva-Villalobos et al., 2014
		
	


Getting started

Use these videos to get started with using Micro-Meta App after installation into OMERO and downloading the example data files:


	Video 1
	Video 2


More information


For full information on how to use Micro-Meta App please utilize the following resources:


	Micro-Meta App website
	Full documentation
	Installation instructions
	Step-by-Step Instructions
	Tutorial Videos



Background

If you want to learn more about the importance of metadata and quality control to ensure full reproducibility, quality and scientific value in light microscopy, please take a look at our recent publications describing the development of community-driven light 4DN-BINA-OME Microscopy Metadata specifications Nature Methods and BioRxiv.org and our overview manuscript entitled A perspective on Microscopy Metadata: data provenance and quality control.

&nbsp;

&nbsp;

[https://zenodo.org/records/5847477](https://zenodo.org/records/5847477)

[https://doi.org/10.5281/zenodo.5847477](https://doi.org/10.5281/zenodo.5847477)


---

## Example Operetta Dataset

Nicolas Chiaruttini

Published 2023-07-17

Licensed CC-BY-4.0



This is a microscopy image dataset generated by the Perkin Elmer Operetta HCS microscope by of the user of the PTBIOP EPFL facility.
As of the 17th of July 2023, opening this file in ImageJ/Fiji using the BioFormats 6.14 library, this dataset generates a Null Pointer Exception.

A post on forum.image.sc is linked to this issue:

https://forum.image.sc/t/null-pointer-exception-in-perkin-elmer-operetta-dataset-with-bio-formats-6-14/83784

&nbsp;

&nbsp;

[https://zenodo.org/records/8153907](https://zenodo.org/records/8153907)

[https://doi.org/10.5281/zenodo.8153907](https://doi.org/10.5281/zenodo.8153907)


---

## Excel template for adding Key-Value Pairs to images

Thomas Zobel, Jens Wendt

Published 2024-10-30

Licensed CC-BY-4.0



This Excel Workbook contains some simple Macros to help with the generation of a .csv in the necessary format for Key-Value pair annotations of images in OMERO.
The format is tailored for the OMERO.web script&nbsp;"KeyVal_from_csv.py"&nbsp; (from the version &lt;=5.8.3 of the core omero-scripts).
Attached is also a video of Thomas Zobel, the head of the imaging core facility Uni M&uuml;nster, showcasing the use of the Excel workbook.The video uses a slightly older version of the workbook and OMERO, but the core functionality remains unchanged.
Please keep in mind, that the OMERO.web script(s) to handle Key-Value Pairs from/to .csv files will undergo a major change very soon.This might break the compatibility with the format used now for the generated .csv from the workbook.

[https://zenodo.org/records/14014252](https://zenodo.org/records/14014252)

[https://doi.org/10.5281/zenodo.14014252](https://doi.org/10.5281/zenodo.14014252)


---

## FAIR BioImage Data

Licensed CC-BY-4.0



Tags: Research Data Management, Fair, Bioimage Analysis

Content type: Collection, Video

[https://www.youtube.com/watch?v=8zd4KTy-oYI&list=PLW-oxncaXRqU4XqduJzwFHvWLF06PvdVm](https://www.youtube.com/watch?v=8zd4KTy-oYI&list=PLW-oxncaXRqU4XqduJzwFHvWLF06PvdVm)


---

## FAIR High Content Screening in Bioimaging

Rohola Hosseini, Matthijs Vlasveld, Joost Willemse, Bob van de Water, Sylvia E. Le Dévédec, Katherine J. Wolstencroft

Published 2023-07-17

Licensed CC-BY-4.0



The authors show the utility of Minimum Information for High Content Screening Microscopy Experiments (MIHCSME) for High Content Screening (HCS) data using multiple examples from the Leiden FAIR Cell Observatory, a Euro-Bioimaging flagship node for high content screening and the pilot node for implementing FAIR bioimaging data throughout the Netherlands Bioimaging network.

Tags: FAIR-Principles, Metadata, Research Data Management

Content type: Publication

[https://www.nature.com/articles/s41597-023-02367-w](https://www.nature.com/articles/s41597-023-02367-w)


---

## FAIR Priciples

Licensed CC-BY-4.0



In 2016, the ‘FAIR Guiding Principles for scientific data management and stewardship’ were published in Scientific Data. The authors intended to provide guidelines to improve the Findability, Accessibility, Interoperability, and Reuse of digital assets.

Tags: FAIR-Principles, Data Stewardship, Research Data Management

Content type: Collection

[https://www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)


---

## FAIRy deep-learning for bioImage analysis

Estibaliz Gómez de Mariscal

Licensed CC-BY-4.0



Introduction to FAIR deep learning. Furthermore, tools to deploy trained DL models (deepImageJ), easily train and evaluate them (ZeroCostDL4Mic and DeepBacs) ensure reproducibility (DL4MicEverywhere), and share this technology in an open-source and reproducible manner (BioImage Model Zoo) are introduced.

Tags: Artificial Intelligence, FAIR-Principles, Bioimage Analysis

Content type: Slides

[https://f1000research.com/slides/13-147](https://f1000research.com/slides/13-147)


---

## Finding and using publicly available data

Anna Swan

Published 2024-01-01

Licensed CC-BY-4.0



Sharing knowledge and data in the life sciences allows us to learn from each other and built on what others have discovered. This collection of online courses brings together a variety of training, covering topics such as biocuration, open data, restricted access data and finding publicly available data, to help you discover and make the most of publicly available data in the life sciences.

Tags: Open Science, Teaching, Sharing

Content type: Collection, Tutorial, Video

[https://www.ebi.ac.uk/training/online/courses/finding-using-public-data/](https://www.ebi.ac.uk/training/online/courses/finding-using-public-data/)


---

## Forschungsdaten.org

Licensed CC-BY-4.0



Research Data Management Wiki in German

Tags: Research Data Management

Content type: Collection

[https://www.forschungsdaten.org/](https://www.forschungsdaten.org/)


---

## Forschungsdatenmanagement zukunftsfest gestalten – Impulse für die   Strukturevaluation der Nationalen Forschungsdateninfrastruktur (NFDI)

Steuerungsgremium Allianz-Schwerpunkt, Alexander von Humboldt Foundation, Deutsche Forschungsgemeinschaft, Fraunhofer Society, German Rectors' Conference, Leibniz Association, German National Academy of Sciences Leopoldina, German Academic Exchange Service, Helmholtz Association of German Research Centres, Max Planck Society

Published 2024-11-04

Licensed CC-BY-4.0



Arbeitspapier des Steuerungsgremiums des Allianz-Schwerpunkts "Digitalit&auml;t in der Wissenschaft"

[https://zenodo.org/records/14032908](https://zenodo.org/records/14032908)

[https://doi.org/10.5281/zenodo.14032908](https://doi.org/10.5281/zenodo.14032908)


---

## From Cells to Pixels: Bridging Biologists and  Image Analysts Through a Common Language

Elnaz Fazeli, Haase Robert, Doube Michael, Miura Kota, Legland David

Published 2024-08-16

Licensed CC-BY-4.0



Bioimaging has transformed our understanding of biological processes, yet extracting&nbsp;meaningful information from complex datasets remains a challenge, particularly for&nbsp;early career scientists. This paper proposes a simplified, systematic approach to&nbsp;bioimage analysis, focusing on categorizing commonly observed structures and&nbsp;shapes, and providing relevant analysis methods. Our approach includes illustrative&nbsp;examples and a visual flowchart, enabling researchers to define analysis objectives&nbsp;clearly. By understanding the diversity of bioimage structures and aligning them with&nbsp;appropriate analysis approaches, the framework empowers researchers to navigate&nbsp;bioimage datasets more efficiently. It also aims to foster a common language between&nbsp;researchers and analysts, thereby enhancing mutual understanding and facilitating&nbsp;effective communication.

[https://zenodo.org/records/13331351](https://zenodo.org/records/13331351)

[https://doi.org/10.5281/zenodo.13331351](https://doi.org/10.5281/zenodo.13331351)


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

## Galaxy Training

Published None

Licensed CC-BY-4.0



Collection of tutorials developed and maintained by the worldwide Galaxy community.

Tags: Bioimage Analysis, Data Analysis

Content type: Collection, Tutorial

[https://training.galaxyproject.org/](https://training.galaxyproject.org/)


---

## Galaxy meets OMERO! Overview on the Galaxy OMERO-suite and Vizarr Viewer

Riccardo Massei, Matthias Bernt, Beatriz Serrano-Solano, Lucille Lopez-Delisle, Jan Bumberger, Björn Grüning, Leonid Kostrykin

Published 2025-03-05

Licensed CC-BY-4.0



[https://zenodo.org/records/14975462](https://zenodo.org/records/14975462)

[https://doi.org/10.5281/zenodo.14975462](https://doi.org/10.5281/zenodo.14975462)


---

## Generative artificial intelligence for bio-image analysis

Robert Haase

Licensed CC-BY-4.0



Tags: Python, Bioimage Analysis, Artificial Intelligence

Content type: Slides

[https://f1000research.com/slides/12-971](https://f1000research.com/slides/12-971)


---

## GerBI-Chat: Teil 1 - Vom Bedarf bis zum Großgeräteantrag-Schreiben

Financial & Legal Framework of Core Facilities, Elmar Endl, Jana Hedrich, Juliane Hoth, Julia Nagy, Astrid Schauss, Nina Schulze, Silke Tulok

Published 2024-09-11

Licensed CC-BY-4.0



Die GermanBioImaging (GerBI-GMB) - Deutsche Gesellschaft f&uuml;r Mikroskopie und Bildanalyse e.V. bietet &uuml;ber regelm&auml;&szlig;ig stattfindende Treffen (GerBI-Chats) die M&ouml;glichkeit zum aktiven Austausch der Mitglieder untereinander. Das GerBI-GMB Team "Legal und Finacial Framwork", welches sich mit administrativen Aufgaben rund um das Core Facility Management besch&auml;ftigt, nutzt diese M&ouml;glichkeit zum aktiven Austausch innerhalb des Netzwerkes und dar&uuml;ber hinaus.&nbsp;
Der Beschaffungsprozess von Forschungsgro&szlig;ger&auml;ten ist komplex und je nach Institution unterschiedlich geregelt. Aus unserer Sicht l&auml;sst sich dieser Prozess grob in drei Stufen aufteilen:

Bedarfsanmeldung
Antragsvorbereitung und -fertigstellung
Antragsbewilligung und Nutzung&nbsp;

Dieser hier enthaltene Beitrag ist der Initialvortrag des GerBi-Chats zum Teil 1 - Von der Bedarfsanmeldung bis zum Beginn der Antragststellung. Die weiteren Stufen der Gro&szlig;ger&auml;tebeschaffung werden in nachfolgenden Beitr&auml;gen behandelt.

[https://zenodo.org/records/13810879](https://zenodo.org/records/13810879)

[https://doi.org/10.5281/zenodo.13810879](https://doi.org/10.5281/zenodo.13810879)


---

## GerBI-Chat: Teil 2 - Wie schreibe ich am besten einen Großegräteantrag

Financial & Legal Framework of Core Facilities, Elmar Endl, Jana Hedrich, Juliane Hoth, Julia Nagy, Astrid Schauss, Nina Schulze, Silke Tulok

Published 2024-10-02

Licensed CC-BY-4.0



Die&nbsp;GermanBioImaging (GerBI-GMB)&nbsp;- Deutsche Gesellschaft f&uuml;r Mikroskopie und Bildanalyse e.V. bietet &uuml;ber regelm&auml;&szlig;ig stattfindende Treffen (GerBI-Chats) die M&ouml;glichkeit zum aktiven Austausch der Mitglieder untereinander. Das GerBI-GMB Team "Legal und Finacial Framwork", welches sich mit administrativen Aufgaben rund um das Core Facility Management besch&auml;ftigt, nutzt diese M&ouml;glichkeit zum aktiven Austausch innerhalb des Netzwerkes und dar&uuml;ber hinaus.&nbsp;
Der Beschaffungsprozess von Forschungsgro&szlig;ger&auml;ten ist komplex und je nach Institution unterschiedlich geregelt. Aus unserer Sicht l&auml;sst sich dieser Prozess grob in drei Stufen aufteilen:

Bedarfsanmeldung
Antragsvorbereitung und -fertigstellung
Antragsbewilligung und Nutzung&nbsp;

Nach dem Initialvortrag der GerBI-Chat Reihe, in dem das Thema Bedarfsanmeldung im Fokus stand, geht es im hier enthaltenen zweiten Teil &bdquo;Antragsvorbereitung und -fertigstellung: Wie schreibe ich am besten einen Gro&szlig;ger&auml;teantrag?&ldquo; um die Beantragung von Forschungsgro&szlig;ger&auml;ten nach Art. 91b GG.

[https://zenodo.org/records/13807114](https://zenodo.org/records/13807114)

[https://doi.org/10.5281/zenodo.13807114](https://doi.org/10.5281/zenodo.13807114)


---

## Getting started with Mambaforge and Python

Mara Lampert

Licensed CC-BY-4.0



Tags: Python, Conda, Mamba

Content type: Blog Post

[https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html)


---

## Getting started with Python: intro and set-up a conda environment

Riccardo Massei

Published 2024-10-09

Licensed CC-BY-4.0



YMIA python event 2024
Presentation :&nbsp; "Getting started with Python: intro and set-up a conda environment with Dr. Riccardo Massei"

[https://zenodo.org/records/13908480](https://zenodo.org/records/13908480)

[https://doi.org/10.5281/zenodo.13908480](https://doi.org/10.5281/zenodo.13908480)


---

## GloBIAS in-person workshop 2024

Christa Walther

Published 2025-04-07

Licensed CC-BY-4.0



This document reports on the first in-person workshop supported by GloBIAS. Each session has its own chapter provided by the people chairing the sessions, summarising the outputs achieved.&nbsp;

[https://zenodo.org/records/15168241](https://zenodo.org/records/15168241)

[https://doi.org/10.5281/zenodo.15168241](https://doi.org/10.5281/zenodo.15168241)


---

## Guidance for Developing a Research Data Management (RDM) Policy

Published 2017

Licensed CC-BY-4.0



This document provides the essential elements of a Research Data Management (RDM) Policy and is part of the LEARN Toolkit containing the Model Policy for Research Data Management (RDM) at Research Institutions/Institutes.

Tags: Research Data Management

Content type: Book

[https://discovery.ucl.ac.uk/id/eprint/1546596/1/26_Learn_Guidance_137-140.pdf](https://discovery.ucl.ac.uk/id/eprint/1546596/1/26_Learn_Guidance_137-140.pdf)

[https://doi.org/10.14324/000.learn.27](https://doi.org/10.14324/000.learn.27)


---

## Gut Analysis Toolbox

Luke Sorensen, Ayame Saito, Sabrina Poon, Myat Noe Han, Ryan Hamnett, Peter Neckel, Adam Humenick, Keith Mutunduwe, Christie Glennan, Narges Mahdavian, Simon JH Brookes, Rachel M McQuade, Jaime PP Foong, Estibaliz Gómez-de-Mariscal, Arrate Muñoz Barrutia, Julia A. Kaltschmidt, Sebastian K. King, Robert Haase, Simona Carbone, Nicholas A. Veldhuis, Daniel P. Poole, Pradeep Rajasekhar

Published 2024-09-10

Licensed CC-BY-4.0



What's Changed

Updating User Dialogs by @mattyrowey in https://github.com/pr4deepr/GutAnalysisToolbox/pull/18
Added Dialog Boxes and Grammar Corrections by @mattyrowey in https://github.com/pr4deepr/GutAnalysisToolbox/pull/19
Updated Dialog Prompts for Clarity by @mattyrowey in https://github.com/pr4deepr/GutAnalysisToolbox/pull/20
Batch analysis option added.
fixed a bunch of bugs related to ganglia segmentation and user workflow

New Contributors

@mattyrowey made their first contribution in https://github.com/pr4deepr/GutAnalysisToolbox/pull/18

Full Changelog: https://github.com/pr4deepr/GutAnalysisToolbox/compare/v0.6...v0.7

[https://zenodo.org/records/13739137](https://zenodo.org/records/13739137)

[https://doi.org/10.5281/zenodo.13739137](https://doi.org/10.5281/zenodo.13739137)


---

## Gut Analysis Toolbox: Training data and 2D models for segmenting enteric neurons, neuronal subtypes and ganglia

Luke Sorensen, Ayame Saito, Sabrina Poon, Myat Noe Han, Adam Humenick, Peter Neckel, Keith Mutunduwe, Christie Glennan, Narges Mahdavian, Simon JH Brookes, Rachel M McQuade, Jaime PP Foong, Sebastian K. King, Estibaliz  Gómez-de-Mariscal, Arrate Muñoz-Barrutia, Robert Haase, Simona Carbone, Nicholas A. Veldhuis, Daniel P. Poole, Pradeep Rajasekhar

Published 2022-02-15

Licensed CC-BY-4.0



This upload is associated with the software, Gut Analysis Toolbox&nbsp;(GAT).
If you use it please cite:
Sorensen et al.&nbsp;Gut Analysis Toolbox: Automating quantitative analysis of enteric neurons.&nbsp;J Cell Sci&nbsp;2024; jcs.261950. doi:&nbsp;https://doi.org/10.1242/jcs.261950
The upload contains&nbsp;StarDist models for segmenting enteric neurons in 2D, enteric neuronal subtypes in 2D and UNet model for enteric ganglia in 2D in gut wholemount tissue. GAT is implemented in Fiji, but the models can be used in any software that supports StarDist and the use of 2D UNet models.&nbsp;The files here also consist of&nbsp;Python notebooks (Google Colab), training and test data as well as reports on model performance.
The model files are located in the respective folders as zip files. The folders have also been zipped:

Neuron (Hu; StarDist&nbsp;model):

Main folder: 2D_enteric_neuron_model_QA.zip
Model File:2D_enteric_neuron_v4_1.zip&nbsp;


Neuronal subtype (StarDist&nbsp;model):&nbsp;

Main folder: 2D_enteric_neuron_subtype_model_QA.zip
Model File: 2D_enteric_neuron_subtype_v4.zip


Enteric ganglia (2D UNet model; Use in FIJI with deepImageJ)

Main folder: 2D_enteric_ganglia_model_QA.zip
Model File: 2D_Ganglia_RGB_v2.bioimage.io.model.zip (Compatible with deepimageJ v3)



For the all models, files included are:

Model for segmenting cells or ganglia in 2D FIJI. StarDist or 2D UNet.
Training and Test datasets used for training.
Google Colab notebooks used for training and quality assurance (ZeroCost DL4Mic notebooks).
Quality assurance reports generated from above notebooks.
StarDist model exported for use in QuPath.

The model files can be used within can be used within the software,&nbsp;StarDist. They&nbsp;are intended to be used within FIJI or QuPath, but can be used in any software that supports the implementation of StarDist in 2D.
Data:
All the images were collected from 4 different research labs and a public database (SPARC database) to account for variations in image acquisition, sample preparation and immunolabelling.
For enteric neurons&nbsp;the pan-neuronal marker, Hu&nbsp;has been used and the&nbsp; 2D wholemounts images from mouse, rat and human tissue.
For enteric neuronal subtypes, 2D images for nNOS, MOR, DOR, ChAT, Calretinin, Calbindin, Neurofilament, CGRP and SST from mouse tissue have been used..
25 images were used&nbsp;from the following entries in the&nbsp;SPARC database:

Howard, M. (2021). 3D imaging of enteric neurons in mouse (Version 1) [Data set]. SPARC Consortium. 
Graham, K. D., Huerta-Lopez, S., Sengupta, R., Shenoy, A., Schneider, S., Wright, C. M., Feldman, M., Furth, E., Lemke, A., Wilkins, B. J., Naji, A., Doolin, E., Howard, M., &amp; Heuckeroth, R. (2020). Robust 3-Dimensional visualization of human colon enteric nervous system without tissue sectioning (Version 1) [Data set]. SPARC Consortium.
Wang, L., Yuan, P.-Q., Gould, T. and Tache, Y. (2021). Antibodies Tested in theColon &ndash; Mouse (Version 1) [Data set]. SPARC Consortium. doi:10.26275/i7dl-58h

The images have been acquired using a combination different microscopes. The images for the mouse tissue were acquired using:&nbsp;


Leica TCS-SP8 confocal system (20x HC PL APO NA 1.33, 40 x HC PL APO NA 1.3)&nbsp;


Leica TCS-SP8 lightning confocal system (20x HC PL APO NA 0.88)&nbsp;


Zeiss Axio Imager M2 (20X HC PL APO NA 0.3)&nbsp;


Zeiss Axio Imager Z1 (10X HC PL APO NA 0.45)&nbsp;


Human tissue images were acquired using:&nbsp;


IX71 Olympus microscope (10X HC PL APO NA 0.3)&nbsp;


For more information, visit the&nbsp;Documentation website.
NOTE: The images for enteric neurons and neuronal subtypes have been rescaled to 0.568 &micro;m/pixel for mouse and rat. For human neurons, it has been rescaled to 0.9 &micro;m/pixel . This is to ensure the neuronal cell bodies have similar pixel area across images. The area of cells in pixels can vary based on resolution of image, magnification of objective used, animal species (larger animals -&gt; larger neurons) and potentially how the tissue is stretched during wholemount preparation&nbsp;
Average neuron area for neuronal model:&nbsp;701.2 &plusmn; 195.9 pixel2 (Mean &plusmn; SD, 6267 cells)
Average neuron area for neuronal subtype model:&nbsp;880.9 &plusmn; 316 pixel2 (Mean &plusmn; SD, 924 cells)
Software References:
Stardist
Schmidt, U., Weigert, M., Broaddus, C., &amp; Myers, G. (2018, September). Cell detection with star-convex polygons. In&nbsp;International Conference on Medical Image Computing and Computer-Assisted Intervention&nbsp;(pp. 265-273). Springer, Cham.
deepImageJ
G&oacute;mez-de-Mariscal, E., Garc&iacute;a-L&oacute;pez-de-Haro, C., Ouyang, W., Donati, L., Lundberg, E., Unser, M., Mu&ntilde;oz-Barrutia, A. and Sage, D., 2021. DeepImageJ: A user-friendly environment to run deep learning models in ImageJ.&nbsp;Nature Methods,&nbsp;18(10), pp.1192-1195.
ZeroCost DL4Mic
von Chamier, L., Laine, R.F., Jukkala, J., Spahn, C., Krentzel, D., Nehme, E., Lerche, M., Hern&aacute;ndez-P&eacute;rez, S., Mattila, P.K., Karinou, E. and Holden, S., 2021. Democratising deep learning for microscopy with ZeroCostDL4Mic.&nbsp;Nature communications,&nbsp;12(1), pp.1-18.

[https://zenodo.org/records/10460434](https://zenodo.org/records/10460434)

[https://doi.org/10.5281/zenodo.10460434](https://doi.org/10.5281/zenodo.10460434)


---

## Hackaton Results - Conversion of KNIME image analysis workflows to Galaxy

Riccardo Massei

Published 2024-03-07

Licensed CC-BY-4.0



Results of the project "Conversion of KNIME image analysis workflows to Galaxy" during the Hackathon "Image Analysis in Galaxy" (Freiburg 26 Feb - 01 Mar 2024)
&nbsp;

[https://zenodo.org/records/10793700](https://zenodo.org/records/10793700)

[https://doi.org/10.5281/zenodo.10793700](https://doi.org/10.5281/zenodo.10793700)


---

## HeLa "Kyoto" cells under the scope

Romain Guiet

Published 2022-02-25

Licensed CC-BY-4.0



Name: HeLa &ldquo;Kyoto&rdquo; cells&nbsp;under the scope

Microscope: Perkin Elmer Operetta microscope with a 20x N.A. 0.8 objective and an&nbsp;Andor Zyla 5.5 camera.

Microscopy data type: The time-lapse datasets were acquired every 15 minutes, for 60 hours. From the individual plan images (channels, time-points, field of view exported by the PerkinElmer software Harmony) multi-dimension images were generated using the Operetta_Importer-0.1.21 &nbsp;with a downscaling of 4.&nbsp;

Channel 1 : Low Contrast DPC (Digital Phase Contrast)

Channel 2 : High Contrast DPC

Channel 3 : Brightfield

Channel 4 : EGFP-&alpha;-tubulin

Channel 5 : mCherry-H2B

File format: .tif (16-bit)

Image size: 540x540 (Pixel size: 0.299 nm), 5c, 1z , 240t

&nbsp;

Cell type: HeLa &ldquo;Kyoto&rdquo; cells, expressing EGFP-&alpha;-tubulin and mCherry-H2B ( Schmitz&nbsp;et&nbsp;al,&nbsp;2010 )

Protocol: Cells were resuspended in Imaging media and were seeded in a microscopy grade 96 wells plate ( CellCarrier Ultra 96, Perkin Elmer). The day after seeding, and for 60 hours, images were acquired in 3 wells, in 25 different fields of view, every 15 minutes.

Imaging media: DMEM red-phenol-free media (FluoroBrite&trade; DMEM, Gibco) complemented with Fetal Calf Serum and Glutamax.

&nbsp;

NOTE: This dataset was used to automatically generate label images in the following Zenodo entry:&nbsp; https://doi.org/10.5281/zenodo.6140064

NOTE: This dataset was used to train the cellpose models in the following Zenodo entry: https://doi.org/10.5281/zenodo.6140111

[https://zenodo.org/records/6139958](https://zenodo.org/records/6139958)

[https://doi.org/10.5281/zenodo.6139958](https://doi.org/10.5281/zenodo.6139958)


---

## High throughput & automated data analysis and data management workflow with Cellprofiler and OMERO

Sarah Weischer, Jens Wendt, Thomas Zobel

Licensed CC-BY-4.0



In this workshop a fully integrated data analysis solutions employing OMERO and commonly applied image analysis tools (e.g., CellProfiler, Fiji) using existing python interfaces (OMERO Python language bindings, ezOmero, Cellprofiler Python API) is presented.

Tags: OMERO, Data Analysis, Bioimage Analysis

Content type: Collection

[https://zenodo.org/doi/10.5281/zenodo.8139353](https://zenodo.org/doi/10.5281/zenodo.8139353)


---

## Highlights from the 2016-2020 NEUBIAS training schools for Bioimage Analysts: a success story and key asset for analysts and life scientists

Gabriel G. Martins, Fabrice P. Cordelières, Julien Colombelli, Rocco D’Antuono, Ofra Golani, Romain Guiet, Robert Haase, Anna H. Klemm, Marion Louveaux, Perrine Paul-Gilloteaux, Jean-Yves Tinevez, Kota Miura

Published 2021

Licensed CC-BY-4.0



Tags: Bioimage Analysis, Neubias

Content type: Publication

[https://f1000research.com/articles/10-334/v1](https://f1000research.com/articles/10-334/v1)


---

## Hitchhiking through a diverse Bio-image Analysis Software Universe

Robert Haase

Published 2022-07-22

Licensed CC-BY-4.0



Overview about decision making and how to influence decisions in the bio-image analysis software context.

Tags: Bioimage Analysis

Content type: Slides, Presentation

[https://f1000research.com/slides/11-746](https://f1000research.com/slides/11-746)

[https://doi.org/10.7490/f1000research.1119026.1](https://doi.org/10.7490/f1000research.1119026.1)


---

## Human DAB staining Axioscan BF 20x

Mario Garcia

Published 2024-05-21

Licensed CC-BY-4.0



Human brain tissue with DAB immunostaining. Image acquired by BF microscopy in&nbsp; Zeiss Axioscan at 20x.&nbsp;

[https://zenodo.org/records/11234863](https://zenodo.org/records/11234863)

[https://doi.org/10.5281/zenodo.11234863](https://doi.org/10.5281/zenodo.11234863)


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

## ICS/IDS stitched file

IMCF

Published 2024-06-13

Licensed CC-BY-4.0



Hi&nbsp;@ome&nbsp;team !
We usually use ICS/IDS file formats as an output to our stitching pipeline as the reading and writing is pretty fast. However, it seems that since Bio-Formats 7.x opening the files is not working anymore.
I tried with a Fiji with Bio-Formats 6.10.1 and the files open, but more recent versions give an issue.
&nbsp;
java.lang.NullPointerException
	at loci.formats.in.ICSReader.initFile(ICSReader.java:1481)
	at loci.formats.FormatReader.setId(FormatReader.java:1480)
	at loci.plugins.in.ImportProcess.initializeFile(ImportProcess.java:498)
	at loci.plugins.in.ImportProcess.execute(ImportProcess.java:141)
	at loci.plugins.in.Importer.showDialogs(Importer.java:156)
	at loci.plugins.in.Importer.run(Importer.java:77)
	at loci.plugins.LociImporter.run(LociImporter.java:78)
	at ij.IJ.runUserPlugIn(IJ.java:244)
	at ij.IJ.runPlugIn(IJ.java:210)
	at ij.Executer.runCommand(Executer.java:152)
	at ij.Executer.run(Executer.java:70)
	at ij.IJ.run(IJ.java:326)
	at ij.IJ.run(IJ.java:337)
	at ij.macro.Functions.doRun(Functions.java:703)
	at ij.macro.Functions.doFunction(Functions.java:99)
	at ij.macro.Interpreter.doStatement(Interpreter.java:281)
	at ij.macro.Interpreter.doStatements(Interpreter.java:267)
	at ij.macro.Interpreter.run(Interpreter.java:163)
	at ij.macro.Interpreter.run(Interpreter.java:93)
	at ij.macro.MacroRunner.run(MacroRunner.java:146)
	at java.lang.Thread.run(Thread.java:750)

You can find one example file at&nbsp;this link&nbsp;1.
Thanks for your help !Best,Laurent

[https://zenodo.org/records/11637422](https://zenodo.org/records/11637422)

[https://doi.org/10.5281/zenodo.11637422](https://doi.org/10.5281/zenodo.11637422)


---

## If you license it, it’ll be harder to steal it. Why we should license our work

Robert Haase

Licensed CC-BY-4.0



Blog post about why we should license our work and what is important when choosing a license.

Tags: Licensing, Research Data Management

Content type: Blog Post

[https://focalplane.biologists.com/2023/05/06/if-you-license-it-itll-be-harder-to-steal-it-why-we-should-license-our-work/](https://focalplane.biologists.com/2023/05/06/if-you-license-it-itll-be-harder-to-steal-it-why-we-should-license-our-work/)


---

## Image Analysis Training Resources

Licensed CC-BY-4.0



Tags: Neubias, Bioimage Analysis

Content type: Book

[https://neubias.github.io/training-resources/](https://neubias.github.io/training-resources/)


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

## Image Processing with Python

Mark Meysenburg, Toby Hodges, Dominik Kutra, Erin Becker, David Palmquist, et al.

Licensed CC-BY-4.0



This lesson shows how to use Python and scikit-image to do basic image processing.

Tags: Bioimage Analysis, Python

Content type: Tutorial, Workflow

[https://datacarpentry.org/image-processing/key-points.html](https://datacarpentry.org/image-processing/key-points.html)


---

## Image Repository Decision Tree - Where do I deposit my imaging data

Isabel Kemmer, Feriel Romdhane, Euro-BioImaging ERIC

Published 2024-10-22

Licensed CC-BY-4.0



Depositing data in quality data repositories is one crucial step towards FAIR (Findable, Accessible, Interoperable, and Reusable) data. Accordingly, Euro-BioImaging strongly encourages sharing scientific imaging data in established, thematic repositories.&nbsp;
To guide you in the selection of appropriate repositories, we have created an overview of available repositories for different types of image data, including their scope and requirements. This decision tree guides you through questions about your data and directs you to the correct repository, and/or provides instructions for further processing to meet the critera of the repositories.&nbsp;
Three seperate trees are provided for different classes of imaging data: open bioimage data, preclinical data, and human imaging data.&nbsp;

[https://zenodo.org/records/13945179](https://zenodo.org/records/13945179)

[https://doi.org/10.5281/zenodo.13945179](https://doi.org/10.5281/zenodo.13945179)


---

## ImageJ tool for percentage estimation of pneumonia in lungs

Martin Schätz, Olga Rubešová, Jan Mareš, Alan Spark

Published 2023-05-02

Licensed CC-BY-4.0



The software tool is developed on demand of Radiological Department of Faculty Hospital of Kr&aacute;lovsk&eacute; Vinohrady, with the aim to provide a tool to estimate the percentage of pneumonia (or COVID-19 presence) in lungs. Paper&nbsp;Estimation of Covid-19 lungs damage based on computer tomography images analysis presenting the tool is available on F1000reserach&nbsp;DOI: 10.12688/f1000research.109020.1. The underlying dataset is published in Zenodo (DOI:10.5281/zenodo.5805939).&nbsp;One of the challenges was to design a tool that would be available without complicated install procedures and would process data in a reasonable time even on office computers. For this reason, 8-bit and 16-bit version of the tool exists. The FIJI software (or ImageJ with Bio-Formats plugin installed) was selected as the best candidate. Examples of use and tutorials are available at GitHub.&nbsp;

Underlying data:
DOI:10.5281/zenodo.5805939
The first five datasets are analyzed using this tool, with results and parameters to repeat the analysis in results_csv.csv or results.xlsx.

Contributions:
Martin SCH&Auml;TZ:&nbsp; &nbsp; &nbsp; &nbsp;Coding, tool testing, data curation, data set analysis
Olga RUBE&Scaron;OV&Aacute;:&nbsp; &nbsp; Code review, tutorial preparation, tool testing, data set analysis
Jan MARE&Scaron;:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Tool testing, data set analysis
Alan SPARK:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Tool testing

The work was funded by the Ministry of Education, Youth and Sports by grant &lsquo;Development of Advanced Computational Algorithms for evaluating post-surgery rehabilitation&rsquo; number LTAIN19007. The work was also supported from the grant of Specific university research &ndash; grant No FCHI 2022-001.

&nbsp;

[https://zenodo.org/records/7885379](https://zenodo.org/records/7885379)

[https://doi.org/10.5281/zenodo.7885379](https://doi.org/10.5281/zenodo.7885379)


---

## InCell datasets with mix of 2D and 3D failed to be read

Fabien Kuttler, Rémy Dornier

Published 2025-01-31

Licensed CC-BY-4.0



The provided dataset contains 2 wells, 4 fields of view, 4 channels, no T but different number of Z according to the channel

Cy3 : 1 Z
DAPI : 16 Z
FITC : 1 Z
Brightfield : 1 Z

The mix 2D/3D is not correctly supported and the .xcde file cannot be read.
A discussion thread is already open on that topic.
Bio-Formats version : 8.0.1
&nbsp;

[https://zenodo.org/records/14777242](https://zenodo.org/records/14777242)

[https://doi.org/10.5281/zenodo.14777242](https://doi.org/10.5281/zenodo.14777242)


---

## Insights and Impact From Five Cycles of Essential Open Source Software for Science

Kate Hertweck, Carly Strasser, Dario Taraborelli

Licensed CC-BY-4.0



Open source software (OSS) is essential for advancing scientific discovery, particularly in biomedical research, yet funding to support these vital tools has been limited. The Chan Zuckerberg Initiative's Essential Open Source Software for Science (EOSS) program has significantly contributed to this field by providing $51.8 million in funding over five years to support the maintenance, growth, and community engagement of critical OSS tools. The program has impacted scientific OSS projects by improving their technical outputs, community building, and sustainability practices, and fostering collaborations within the OSS community. Additionally, EOSS funding has enhanced diversity, equity, and inclusion within the OSS community, although changes in principal investigator demographics were not observed. The funded projects have had a substantial impact on biomedical research by improving the usability and accessibility of scientific software, which has led to increased adoption and advancements in various biomedical fields.

Tags: Open Source Software, Funding, Sustainability

Content type: Publication

[https://zenodo.org/records/11201216](https://zenodo.org/records/11201216)


---

## Insights from Acquiring Open Medical Imaging  Datasets for Foundation Model Development

Stefan Dvoretskii

Published 2024-04-10

Licensed CC-BY-4.0



[https://zenodo.org/records/11503289](https://zenodo.org/records/11503289)

[https://doi.org/10.5281/zenodo.11503289](https://doi.org/10.5281/zenodo.11503289)


---

## Insights from Acquiring Open Medical Imaging Datasets for Foundation Model Development

Stefan Dvoretskii

Published 2024-04-10

Licensed CC-BY-4.0



[https://zenodo.org/records/13380289](https://zenodo.org/records/13380289)

[https://doi.org/10.5281/zenodo.13380289](https://doi.org/10.5281/zenodo.13380289)


---

## Institutionalization and Collaboration as a Way of Addressing the Challenges Open Science Presents to Libraries: The University of Konstanz as a National Pioneer

Sophie Habinger, Maximilian Heber, Sonja Kralj, Emilia Mikautsch

Published 2024-07-09

Licensed CC-BY-4.0



The rise of Open Science (OS) and the academic community&rsquo;s needs that come with it bring about a range of challenges for academic libraries. To face these challenges, the University of Konstanz has created a competence unit called&nbsp;Team Open Science&nbsp;in the Communication, Information, Media Center (KIM) - a joint unit of library and IT infrastructure. The Team creates synergies within itself and across the library. In December 2023, it involved 12 staff members specialising in open access (OA), research data management (RDM), open educational resources (OER) and virtual research environments (VRE). It collaborates closely with other KIM departments. This submission shall serve as a best practice example for the impact of OS on research libraries and, beyond that, the impact of research libraries on universities.
To enhance and foster OS, the Team provides individual consultations, services and office hours for researchers. Here, it collaborates closely with other librarians like subject specialists and the Team University Publications. Along similar lines, the KIM offers institutional repositories for publications (KOPS) and research data (KonDATA). Beyond that, the Team provides solutions to host OA journals and analyses researchers&rsquo; VRE needs to decide on implementation options. In sum, the Team is the central OS contact point for the entire university, underlining the major role the library holds in making institutional impact.
Furthermore, the Team had the leading role in creating the University of Konstanz&rsquo; OS Policy, one of the first ones passed by a German university. This policy stands out because it encompasses various OS domains. It demands, among other things, that text publications be made OA and that research data be managed according to relevant subject-specific standards. If permissible and reasonable, it demands that research data should be made publicly available at the earliest possible time. Along these lines, the policy has a large impact on how the library handles closed access books and subscription-based journals. As a consequence, OA is pursued wherever possible, leading to the highest OA quota of all German universities. In that sense, the Team is a crucial driving force of OS in the University of Konstanz, which ties in with the library&rsquo;s major role of open research transformation.
Beyond the University of Konstanz, the Team is involved in a range of national and international projects collaborating with other libraries. On a national level, they lead the project open.access-network which provides an information platform for researchers and librarians and connects the German-speaking OA community through events like bar camps. The project KOALA-AV supports libraries in establishing consortial solutions for financing Diamond OA publications. Moreover, the Team is involved in the federal state initiative for RDM in Baden-W&uuml;rttemberg (bwFDM). Here, the Team is in charge of forschungsdaten.info, the German-speaking countries&rsquo; leading RDM information platform, which will be offered in English within the next years. Internationally, the Team cooperates with librarians and other OS professionals from the European Reform University Alliance (ERUA) and the European University for Well-Being (EUniWell), establishing formats for best practice exchange, such as monthly OS Meet-Ups.

[https://zenodo.org/records/12699637](https://zenodo.org/records/12699637)

[https://doi.org/10.5281/zenodo.12699637](https://doi.org/10.5281/zenodo.12699637)


---

## Interactive Image Data Flow Graphs

Martin Schätz

Published 2022-10-17

Licensed CC-BY-4.0



The slides were presented during the Macro programming with ImageJ workshop (https://www.16mcm.cz/programme/#workshops) which was part of the&nbsp;16th Multinational Congress on Microscopy. It is a collection and &quot;reshuffle&quot; of slides originally made by Robert Haase on topics from Image Analysis in general up to&nbsp;User-friendly GPU-accelerated bio-image analysis and CLIJ2.

[https://zenodo.org/records/7215114](https://zenodo.org/records/7215114)

[https://doi.org/10.5281/zenodo.7215114](https://doi.org/10.5281/zenodo.7215114)


---

## Intravital microscopy contrasting agents for application - Database

Michael Gerlach

Published 2024-06-19

Licensed CC-BY-4.0



This is a set of databases containing published use of substances which can be applied to rodents in order to contrast specific structures for optical intravital microscopy.
The first dataset contains applied final dosages, calculated for 25g-mice, as well as the orignally published amounts, concentrations and application routes of agents directly applied into the target organism.
The second dataset contains dosages and cell numbers for the external contrastation and subsequent application of cells into the target organism.
Filtering possible for organ system and contrasted structure/cell type in both datasets, substance class and fluorescent detection windows can be filtered in the dataset for direct agent application.
Source publications are listed by DOI.
&nbsp;

[https://zenodo.org/records/12166710](https://zenodo.org/records/12166710)

[https://doi.org/10.5281/zenodo.12166710](https://doi.org/10.5281/zenodo.12166710)


---

## Introducing OMERO-vitessce: an OMERO.web plugin for multi-modal data

Michele Bortolomeazzi, Christian Schmidt, Jan-Philipp Mallm

Published 2025-02-07

Licensed CC-BY-4.0



omero-vitessce: an OMERO.web plugin for multi-modal data viewing.
OMERO is the most used research data management system (RDM) in the bioimaging domain, and has been adopted as a centralized RDM solution by several academic and research institutions. A main reason for this is the ability to directly view and annotate images from a web-based interface. However, this feature of OMERO is currently underpowered for the visualization of very large or multimodal datasets. These datasets, are becoming a more and more common foundation for biological and biomedical studies, due to the recent developments in imaging, and sequencing technologies which enabled their application to spatial-omics. In order to begin to provide this multimodal-data capability to OMERO, we developed omero-vitessce (https://github.com/NFDI4BIOIMAGE/omero-vitessce/tree/main), a new OMERO.web plugin for viewing data stored in OMERO with the Vitessce (http://vitessce.io/) multimodal data viewer. omero-vitessce can be installed as an OMERO.web plugin with PiPy (https://pypi.org/project/omero-vitessce/), and allows users to set up interactive visualizations of their images of cells and tissues through interactive plots which are directly linked to the image. This enables the visual exploration of bioimage-analysis results and of multimodal data such as those generated through spatial-omics experiments. The data visualization is highly customizable and can be configured not only through custom configuration files, but also with the graphical interface provided by the plugin, thus making omero-vitessce a highly user-friendly solution for multimodal data viewing. most biological datasets. We plan to extend the interoperability of omero-vitessce with the OME-NGFF and SpatialData file formats to leverage the efficiency of these cloud optimized formats.
The three files in this Zenodo Record are all the same poster saved in different format all with high resolution images.

[https://zenodo.org/records/14832855](https://zenodo.org/records/14832855)

[https://doi.org/10.5281/zenodo.14832855](https://doi.org/10.5281/zenodo.14832855)


---

## Introduction to Bioimage Analysis

Pete Bankhead

Licensed CC-BY-4.0



Tags: Python, Imagej, Bioimage Analysis

Content type: Book, Notebook

[https://bioimagebook.github.io/index.html](https://bioimagebook.github.io/index.html)


---

## Introduction to Research Data Management and Open Research

Shanmugasundaram

Published 2024-05-17

Licensed CC-BY-4.0



Introduction to RDM primarily for researchers. Can be seen as primer to all other materials in this catalogue.

Tags: Research Data Management, Open Science

Content type: Slides

[https://zenodo.org/records/4778265](https://zenodo.org/records/4778265)


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

## Kollaboratives Arbeiten und Versionskontrolle mit Git

Robert Haase

Published 2024-04-15

Licensed CC-BY-4.0



Gemeinsames Arbeiten im Internet stellt uns vor neue Herausforderungen: Wer hat eine Datei wann hochgeladen? Wer hat zum Inhalt beigetragen? Wie kann man Inhalte zusammenfuehren, wenn mehrere Mitarbeiter gleichzeitig Aenderungen gemacht haben? Das Versionskontrollwerkzeug git stellt eine umfassende Loesung fuer solche Fragen bereit. Die Onlineplatform github.com stellt nicht nur Softwareentwicklern weltweit eine git-getriebene Platform zur Verfuegung und erlaubt ihnen effektiv zusammen zu arbeiten. In diesem Workshop lernen wir:

Infuerung in FAIR-Prinzipien im Softwarecontext
Arbeiten mit git: Pull-requests
Aufloesen von Merge-Konflikten
Automatisiertes Archivieren von Inhalten nach Zenodo.org
Eigene Webseiten auf github.io publizieren


Tags: Research Data Management, FAIR-Principles, Git, Zenodo

Content type: Slides

[https://zenodo.org/records/10972692](https://zenodo.org/records/10972692)

[https://doi.org/10.5281/zenodo.10972692](https://doi.org/10.5281/zenodo.10972692)


---

## Kriterienkatalog für Materialien aus dem Themenbereich Forschungsdatenmanagement

Linda Zollitsch, Swantje Piotrowski

Published 2025-01-24

Licensed CC-BY-4.0



Im Rahmen von FDM-SH Kontor &ndash; einem Projekt, das im Kontext der AG Kompetenzentwicklung von der Landesinitiative FDM-SH durchgef&uuml;hrt wurde - haben wir zum Ziel, eine kuratierte Materialbasis f&uuml;r Fortbildungen und Schulungen zu schaffen. Dies stellte uns vor die Herausforderung, festzulegen, wie die Materialien ausgew&auml;hlt werden sollen.
Dieser Kriterienkatalog ist ein Versuch, erste Qualit&auml;tskriterien (insbesondere hinsichtlich der Nachnutzbarkeit und den FAIR-Prinzipien) f&uuml;r Materialien auf Basis von Metadaten zu erstellen. Dabei wurde das Vorgehen des Open Science Learning Gates (https://zenodo.org/records/12772135), als Vorbild genommen. Neben dem Metadatenschema der RDA (https://zenodo.org/records/6769695#.YrrP9-xBybQ) haben wir auf das Metadatenschema der DINI/nestor UAG Schulungen/Fortbildungen (https://zenodo.org/records/3760398) sowie das DALIA Interchange Format (https://zenodo.org/records/11521029) zur&uuml;ckgegriffen.

[https://zenodo.org/records/14729452](https://zenodo.org/records/14729452)

[https://doi.org/10.5281/zenodo.14729452](https://doi.org/10.5281/zenodo.14729452)


---

## LEO: Linking ELN with OMERO

Escobar Diaz Guerrero, Rodrigo

Published 2024-05-08

Licensed CC-BY-4.0



First updates of LEO (Linking ELN with OMERO)

[https://zenodo.org/records/11146807](https://zenodo.org/records/11146807)

[https://doi.org/10.5281/zenodo.11146807](https://doi.org/10.5281/zenodo.11146807)


---

## LSM example J. Dubrulle

Salama Lab Fred Hutchinson Cancer Center

Published 2024-12-17

Licensed CC-BY-4.0



[https://zenodo.org/records/14510432](https://zenodo.org/records/14510432)

[https://doi.org/10.5281/zenodo.14510432](https://doi.org/10.5281/zenodo.14510432)


---

## LZ4-compressed Imaris ims example datasets.

Marco Stucchi

Published 2024-11-21

Licensed CC-BY-4.0



The files contained in this repository are cropped versions of Imaris demo images compressed with LZ4.

[https://zenodo.org/records/14197622](https://zenodo.org/records/14197622)

[https://doi.org/10.5281/zenodo.14197622](https://doi.org/10.5281/zenodo.14197622)


---

## Large Language Models: An Introduction for Life Scientists

Robert Haase

Published 2024-12-12

Licensed CC-BY-4.0



This slide deck introduces Large Language Models to an audience of life-scientists. We first dive into terminology: Different kinds of Language Models and what they can be used for. The remaining slides are optional slides to allow us to dive deeper into topics such as tools for using LLMs in Science, Quality Assurance, Techniques such as Retrieval Augmented Generation and Prompt Engineering.

Tags: Globias, Artificial Intelligence

[https://zenodo.org/records/14418209](https://zenodo.org/records/14418209)

[https://doi.org/10.5281/zenodo.14418209](https://doi.org/10.5281/zenodo.14418209)


---

## Large tiling confocal acquisition (rat brain)

Julie Meystre

Published 2022-06-15

Licensed CC-BY-4.0



Name: Large tiling confocal acquisition (rat brain)

Microscope: Zeiss LSM700

Microscopy data type:&nbsp;108 tiles, each with 62 z-slices and 2 channels :
Channel 1: DAPI
Channel 2: cck staining

File format: .lsm (16-bit)

Image size: 1024x1024x62 (Pixel size: 0.152 x 0.152 x 1 micron), 2 channels.

&nbsp;

NOTE : Some tiles were annotated and used to train a StarDist3D model (https://doi.org/10.5281/zenodo.6645978 &nbsp;&nbsp;)

[https://zenodo.org/records/6646128](https://zenodo.org/records/6646128)

[https://doi.org/10.5281/zenodo.6646128](https://doi.org/10.5281/zenodo.6646128)


---

## Leitfaden zur digitalen Datensparsamkeit (mit Praxisbeispielen)

Maximilian Heber, Moritz Jakob, Matthias Landwehr, Jan Leendertse, Maximilian Müller, Gabriel Schneider, Dirk von Suchodoletz, Robert Ulrich

Published 2024-06-03

Licensed CC-BY-4.0



Im Zuge der stetig wachsenden Brisanz des Forschungsdatenmanagements fallen immer gr&ouml;&szlig;ere Mengen an Forschungsdaten an. Diese an sich begr&uuml;&szlig;enswerte Entwicklung f&uuml;hrt zu technischen und organisatorischen Herausforderungen nicht nur im Bereich der Speicherung von Forschungsdaten, sondern in allen Phasen des Forschungsdatenlebenszyklus. Der vorliegende Beitrag erl&auml;utert vor diesem Hintergrund m&ouml;gliche Motivationen hinter digitaler Datensparsamkeit mit Blick auf organisatorische, technische und ethische Kriterien, Datenschutz und Nachhaltigkeit. Anschlie&szlig;end werden vor dem Hintergrund zentraler Herausforderungen Umsetzungsvorschl&auml;ge f&uuml;r das Vorfeld sowie den Verlauf eines Forschungsvorhabens gemacht. Zudem werden grundlegende Empfehlungen zur digitalen Datensparsamkeit ausgesprochen.
Eine k&uuml;rzere Ausgabe des Leitfadens ist im Mai 2024 in der Zeitschrift o | bib erschienen: https://doi.org/10.5282/o-bib/6036 
Diese Ausgabe enth&auml;lt ein zus&auml;tzliches Kapitel (4.2) mit konkreten Praxisbeispielen.
Dieser Artikel wurde ins Englische &uuml;bersetzt:
Heber, M., Jakob, M., Landwehr, M., Leendertse, J., M&uuml;ller, M., Schneider, G., von Suchodoletz, D., &amp; Ulrich, R. (2024). A Users' Guide to Economical Digital Data Usage. Zenodo. https://doi.org/10.5281/zenodo.13752220

[https://zenodo.org/records/11445843](https://zenodo.org/records/11445843)

[https://doi.org/10.5281/zenodo.11445843](https://doi.org/10.5281/zenodo.11445843)


---

## Leitlinie? Grundsätze? Policy? Richtlinie? – Forschungsdaten-Policies an deutschen Universitäten

Bea Hiemenz, Monika Kuberek

Published 2018-07-13

Licensed CC-BY-4.0



As a methodological approach, research data policies of German universities are collected and evaluated, and compared to international recommendations on research data policies.

Tags: Research Data Management, FAIR-Principles

Content type: Publication

[https://www.o-bib.de/bib/article/view/2018H2S1-13](https://www.o-bib.de/bib/article/view/2018H2S1-13)


---

## LimeSeg Test Datasets

Sarah Machado, Vincent Mercier, Nicolas Chiaruttini

Published 2018-10-27

Licensed CC-BY-4.0



Image datasets from the&nbsp;publication :&nbsp;LimeSeg: A coarse-grained lipid membrane simulation for 3D image segmentation


	Vesicles.tif: spinning-disc confocal images of giant unilamellar vesicles
	HelaCell-FIBSEM.tif:&nbsp;a 3D Electron&nbsp;Microscopy (EM)&nbsp;dataset of nearly isotropic sections of a Hela cell, acquired with a focused ion beam scanning electron microscope (FIB-SEM). Sections are aligned with TrackEm2 (doi: ), without additional preprocessing.
	DrosophilaEggChamber.tif: point scanning confocal images of a Drosophila egg chamber. Channel&nbsp;1: cell nuclei &nbsp;stained with DAPI. Channel 2:&nbsp;cell membranes visualized with fused membrane proteins Nrg::GFP and Bsg::GFP.&nbsp;


Image metadata contains extra information including voxel sizes.

&nbsp;

[https://zenodo.org/records/1472859](https://zenodo.org/records/1472859)

[https://doi.org/10.5281/zenodo.1472859](https://doi.org/10.5281/zenodo.1472859)


---

## Linked (Open) Data for Microbial Population Biology

Carsten Fortmann-Grote

Published 2024-03-12

Licensed CC-BY-4.0



[https://zenodo.org/records/10808486](https://zenodo.org/records/10808486)

[https://doi.org/10.5281/zenodo.10808486](https://doi.org/10.5281/zenodo.10808486)


---

## Liver Micrometastases area quantification using QuPath and pixel classifier

Laia Simó-Riudalbas, Romain Guiet, Olivier Burri, Julien Duc, Didier Trono

Published 2022-05-06

Licensed CC-BY-4.0



Sample: Mouse (NSG) liver slices with human colorectal cancer cells metastases, stained with Hematoxylin &amp; Eosin.&nbsp;

Image Acquisition: Images were acquired on an Olympus VS120 Whole Slide Scanner, using a 20x objective (UPLSAPO, N.A. 0.75) and a color camera (Pike F505 Color) with an image pixel size of 0.345 microns.

Image Processing and Analysis: Obtained images were analyzed using the software QuPath [1] (version 0.3.2) using groovy scripts, making use of a pixel classifier to segment and measure cancer cell clusters.

Files :

Detailed_worflow.pdf : contains a detailed description of how pixel classifier was created

images_for_classifier_training.zip : contains all the vsi file obtained from the microscope and used for the training

project_for_classifier_training.zip : contains the QuPath project, with Training Image, annotations, classifiers and scripts for analysis

PythonCode.txt : code ran to transform output results from QuPath to final results

&nbsp;

[1] Bankhead, P. et al.&nbsp;QuPath: Open source software for digital pathology image analysis.&nbsp;Scientific Reports&nbsp;(2017). https://doi.org/10.1038/s41598-017-17204-5

[https://zenodo.org/records/6523649](https://zenodo.org/records/6523649)

[https://doi.org/10.5281/zenodo.6523649](https://doi.org/10.5281/zenodo.6523649)


---

## Making the most of bioimaging data through interdisciplinary interactions

Virginie Uhlmann, Matthew Hartley, Josh Moore, Erin Weisbart, Assaf Zaritsky

Published 2024-10-23

Licensed CC-BY-4.0



Tags: Bioimage Analysis, Open Science, Microscopy

Content type: Publication

[https://journals.biologists.com/jcs/article/137/20/jcs262139/362478/Making-the-most-of-bioimaging-data-through](https://journals.biologists.com/jcs/article/137/20/jcs262139/362478/Making-the-most-of-bioimaging-data-through)


---

## Making your package available on conda-forge

Kevin Yamauchi

Licensed CC-BY-4.0



Tags: Deployment, Python

Content type: Documentation

[https://kevinyamauchi.github.io/open-image-data/how_tos/conda_forge_packaging.html](https://kevinyamauchi.github.io/open-image-data/how_tos/conda_forge_packaging.html)


---

## Managing Scientific Python environments using Conda, Mamba and friends

Robert Haase

Licensed CC-BY-4.0



Tags: Python, Conda, Mamba

Content type: Blog Post

[https://focalplane.biologists.com/2022/12/08/managing-scientific-python-environments-using-conda-mamba-and-friends/](https://focalplane.biologists.com/2022/12/08/managing-scientific-python-environments-using-conda-mamba-and-friends/)


---

## Measuring reporter activity domain in EPI aggregates and Gastruloids.ijm

Romain Guiet, Olivier Burri, Mehmet Girgin, Matthias Lutolf

Published 2022-12-07

Licensed CC-BY-4.0



This imagej macro analyses the reporter intensity activity and expression domain in EPI aggregates and Gastruloids.

[https://zenodo.org/records/7409423](https://zenodo.org/records/7409423)

[https://doi.org/10.5281/zenodo.7409423](https://doi.org/10.5281/zenodo.7409423)


---

## Meeting in the Middle: Towards Successful Multidisciplinary Bioimage Analysis Collaboration

Anjalie Schlaeppi, Wilson Adams, Robert Haase, Jan Huisken, Ryan B. MacDonald, Kevin W. Eliceiri, Elisabeth C. Kugler

Licensed CC-BY-4.0



Tags: Bioimage Analysis

Content type: Publication

[https://www.frontiersin.org/articles/10.3389/fbinf.2022.889755/full](https://www.frontiersin.org/articles/10.3389/fbinf.2022.889755/full)


---

## Memorandum of Understanding of NFDI consortia from Earth-, Chemical and Life Sciences to support a network called the Geo-Chem-Life Science Helpdesk Cluster

Lars Bernard, Maike Brück, Christian Busse, Judith Engel, Jan Eufinger, Frank Ewert, Juliane Fluck, Konrad Förstner, Julia Fürst, Holger Gauza, Klaus Getzlaff, Glöckner, Frank Oliver, Johannes Hunold, Oliver Koepler, Ksenia Krooß, Birte Lindstädt, McHardy, Alice C., Hela Mehrtens, Elena Rey-Mazon, Marcus Schmidt, Isabel Schober, Annett Schröter, Oliver Stegle, Christoph Steinbeck, Feray Steinhart, von Suchodoletz, Dirk, Stefanie Weidtkamp-Peters, Jens Wendt, Conni Wetzker

Published 2025-04-02

Licensed CC-BY-4.0



In a Memorandum of Understanding, the undersigned consortia agree to work together to enhance their support capabilities (helpdesks) to meet the needs of interdisciplinary research in&nbsp;Earth-, Chemical and Life Sciences.

[https://zenodo.org/records/15065070](https://zenodo.org/records/15065070)

[https://doi.org/10.5281/zenodo.15065070](https://doi.org/10.5281/zenodo.15065070)


---

## Metadata Annotation Workflow for OMERO with Tabbles

Wendt Jens

Published 2023-09-04

Licensed CC-BY-4.0



Short presentation given at at PoL BioImage Analysis Symposium Dresden 2023

[https://zenodo.org/records/8314968](https://zenodo.org/records/8314968)

[https://doi.org/10.5281/zenodo.8314968](https://doi.org/10.5281/zenodo.8314968)


---

## Metadata in Bioimaging

Josh Moore, Susanne Kunis

Published 2025-03-25

Licensed CC-BY-4.0



Presentation given to the Search &amp; Harvesting workgroup of the Metadata section of NFDI on March 25th, 2025

[https://zenodo.org/records/15083018](https://zenodo.org/records/15083018)

[https://doi.org/10.5281/zenodo.15083018](https://doi.org/10.5281/zenodo.15083018)


---

## Methods in bioimage analysis

Christian Tischer

Licensed CC-BY-4.0



Tags: Bioimage Analysis

Content type: Online Tutorial, Video, Slides

[https://www.ebi.ac.uk/training/events/methods-bioimage-analysis/](https://www.ebi.ac.uk/training/events/methods-bioimage-analysis/)

[https://doi.org/10.6019/TOL.BioImageAnalysis22-w.2022.00001.1](https://doi.org/10.6019/TOL.BioImageAnalysis22-w.2022.00001.1)

[https://drive.google.com/file/d/1MhuqfKhZcYu3bchWMqogIybKjamU5Msg/view](https://drive.google.com/file/d/1MhuqfKhZcYu3bchWMqogIybKjamU5Msg/view)


---

## MicroSam-Talks

Constantin Pape

Published 2024-05-23

Licensed CC-BY-4.0



Talks about Segment Anything for Microscopy: https://github.com/computational-cell-analytics/micro-sam.
Currently contains slides for two talks:

Overview of Segment Anythign for Microscopy given at the SWISSBIAS online meeting in April 2024
Talk about vision foundation models and Segment Anything for Microscopy given at Human Technopole as part of the EMBO Deep Learning Course in May 2024


Tags: Bioimage Analysis, Artificial Intelligence

Content type: Slides

[https://zenodo.org/records/11265038](https://zenodo.org/records/11265038)

[https://doi.org/10.5281/zenodo.11265038](https://doi.org/10.5281/zenodo.11265038)


---

## Microscopy data analysis: machine learning and the BioImage Archive

Andrii Iudin, Anna Foix-Romero, Anna Kreshuk, Awais Athar, Beth Cimini, Dominik Kutra, Estibalis Gomez de Mariscal, Frances Wong, Guillaume Jacquemet, Kedar Narayan, Martin Weigert, Nodar Gogoberidze, Osman Salih, Petr Walczysko, Ryan Conrad, Simone Weyend, Sriram Sundar Somasundharam, Suganya Sivagurunathan, Ugis Sarkans

Licensed CC-BY-4.0



The Microscopy data analysis: machine learning and the BioImage Archive course, which focused on introducing programmatic approaches used in the analysis of bioimage data via the BioImage Archive, ran in May 2023.

Tags: Bioimage Analysis, Python, Artificial Intelligence

Content type: Video, Slides

[https://www.ebi.ac.uk/training/materials/microscopy-data-analysis-machine-learning-and-the-bioimage-archive-materials/](https://www.ebi.ac.uk/training/materials/microscopy-data-analysis-machine-learning-and-the-bioimage-archive-materials/)


---

## Microscopy-BIDS - An Extension to the Brain Imaging Data Structure for Microscopy Data

Marie-Hélène Bourget, Lee Kamentsky, Satrajit S. Ghosh, Giacomo Mazzamuto, Alberto Lazari, et al.

Published 2022-04-19

Licensed CC-BY-4.0



The Brain Imaging Data Structure (BIDS) is a specification for organizing, sharing, and archiving neuroimaging data and metadata in a reusable way.

Tags: Research Data Management

Content type: Publication

[https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.871228/full](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.871228/full)


---

## Modeling community standards for metadata as templates makes data FAIR

Mark A Musen, Martin J O'Connor, Erik Schultes, Marcos Martínez-Romero, Josef Hardi, John Graybeal

Published 2022-11-12

Licensed CC-BY-4.0



The authors have developed a model for scientific metadata, and they have made that model usable by both CEDAR and FAIRware. The approach shows that a formal metadata model can standardize reporting guidelines and that it can enable separate software systems to assist (1) in the authoring of standards-adherent metadata and (2) in the evaluation of existing metadata.

Tags: Data Stewardship, FAIR-Principles, Metadata

Content type: Publication

[https://pubmed.ncbi.nlm.nih.gov/36371407/](https://pubmed.ncbi.nlm.nih.gov/36371407/)

[https://www.nature.com/articles/s41597-022-01815-3](https://www.nature.com/articles/s41597-022-01815-3)


---

## Modular training resources for bioimage analysis

Christian Tischer, Antonio Politi, Tim-Oliver Buchholz, Elnaz Fazeli, Nicola Gritti, Aliaksandr Halavatyi, Sebastian Gonzalez Tirado, Julian Hennies, Toby Hodges, Arif Khan, Dominik Kutra, Stefania Marcotti, Bugra Oezdemir, Felix Schneider, Martin Schorb, Anniek Stokkermans, Yi Sun, Nima Vakili

Published 2024-12-03

Licensed CC-BY-4.0



Resources for teaching/preparing to teach bioimage analysis

Tags: Neubias, Bioimage Analysis

[https://zenodo.org/records/14264885](https://zenodo.org/records/14264885)

[https://doi.org/10.5281/zenodo.14264885](https://doi.org/10.5281/zenodo.14264885)


---

## Morphological analysis of neural cells with WEKA and SNT Fiji plugins

Daniel Waiger

Published 2022-07-14

Licensed CC-BY-4.0



A simple workflow to detect Soma and neurite paths, from light microscopy&nbsp;datasets.

Using open-source tools for beginners.

[https://zenodo.org/records/6834214](https://zenodo.org/records/6834214)

[https://doi.org/10.5281/zenodo.6834214](https://doi.org/10.5281/zenodo.6834214)


---

## Multi-Template-Matching for object-detection (slides)

Laurent Thomas

Published 2022-05-16

Licensed CC-BY-4.0



This presentations describes Multi-Template-Matching, a novel method extending on template-matching for object-detection in images.

The project was part of the PhD project of Laurent Thomas between 2017 and 2020, under supervision of Jochen Gehrig. The project was hosted at ACQUIFER Imaging with collaboration of the medical university of Heidelberg, and part of the ImageInLife Horizon2020 ITN (PhD program).&nbsp;

[https://zenodo.org/records/6554166](https://zenodo.org/records/6554166)

[https://doi.org/10.5281/zenodo.6554166](https://doi.org/10.5281/zenodo.6554166)


---

## Multiplexed histology of COVID-19 post-mortem lung samples - CONTROL CASE 1 FOV1

Anna Pascual Reguant, Ronja Mothes, Helena Radbruch, Anja E. Hauser

Published 2022-12-16

Licensed CC-BY-4.0



Image-based data set of a post-mortem lung sample from a non-COVID-related pneumonia donor (CONTROL CASE 1, FOV1)

Each image shows the same field of view (FOV), sequentially stained with the depicted fluorescence-labelled antibodies, including surface proteins, intracellular proteins and transcription factors. Images contain 2024 x 2024 pixels and are generated using an inverted wide-field fluorescence microscope with a 20x objective, a lateral resolution of 325 nm and an axial resolution above 5 &micro;m. Images have&nbsp;been normalized and intensities adjusted.

[https://zenodo.org/records/7447491](https://zenodo.org/records/7447491)

[https://doi.org/10.5281/zenodo.7447491](https://doi.org/10.5281/zenodo.7447491)


---

## Multiplexed tissue imaging - tools and approaches

Agustín Andrés Corbat, OmFrederic, Jonas Windhager, Kristína Lidayová

Licensed CC-BY-4.0



Material for the I2K 2024 "Multiplexed tissue imaging - tools and approaches" workshop

Tags: Bioimage Analysis

Content type: Github Repository, Slides, Workshop

[https://github.com/BIIFSweden/I2K2024-MTIWorkshop](https://github.com/BIIFSweden/I2K2024-MTIWorkshop)

[https://docs.google.com/presentation/d/1R9-4lXAmTYuyFZpTMDR85SjnLsPZhVZ8/edit#slide=id.p1](https://docs.google.com/presentation/d/1R9-4lXAmTYuyFZpTMDR85SjnLsPZhVZ8/edit#slide=id.p1)


---

## My Journey Through Bioimage Analysis Teaching Methods From Classroom to Cloud

Elnaz Fazeli

Published 2024-02-19

Licensed CC-BY-4.0



In these slides I introducemy journey through teaching bioimage analysis courses in different formats, from in person courses to online material. I have an overview of different training formats and comparing these for different audiences.&nbsp;

Tags: Teaching

Content type: Slides

[https://zenodo.org/records/10679054](https://zenodo.org/records/10679054)

[https://doi.org/10.5281/zenodo.10679054](https://doi.org/10.5281/zenodo.10679054)


---

## NFDI4BIOIMAGE

Carsten Fortmann-Grote

Published 2024-04-22

Licensed CC-BY-4.0



This presentation was given at the 2nd MPG-NFDI Workshop on April 18th.

[https://zenodo.org/records/11031747](https://zenodo.org/records/11031747)

[https://doi.org/10.5281/zenodo.11031747](https://doi.org/10.5281/zenodo.11031747)


---

## NFDI4BIOIMAGE - National Research Data Infrastructure for Microscopy and BioImage Analysis - Online Kick-Off 2023

Stefanie Weidtkamp-Peters

Licensed CC-BY-4.0



NFDI4BIOIMAGE core mission, bioimage data challenge, task areas, FAIR bioimage workflows.

Tags: Research Data Management, FAIR-Principles, Bioimage Analysis, Nfdi4Bioimage

Content type: Slides

[https://doi.org/10.5281/zenodo.8070038](https://doi.org/10.5281/zenodo.8070038)


---

## NFDI4BIOIMAGE - National Research Data Infrastructure for Microscopy and BioImage Analysis [conference talk: The Pelagic Imaging Consortium meets Helmholtz Imaging, 5.10.2023, Hamburg]

Riccardo Massei

Licensed CC-BY-4.0



NFDI4BIOIMAGE is a consortium within the framework of the National Research Data Infrastructure (NFDI) in Germany. In this talk, the consortium and the contribution to the work programme by the Helmholtz Centre for Environmental Research (UFZ) in Leipzig are outlined.

Tags: Research Data Management, Bioimage Analysis, Nfdi4Bioimage

Content type: Slides

[https://zenodo.org/doi/10.5281/zenodo.8414318](https://zenodo.org/doi/10.5281/zenodo.8414318)


---

## NFDI4BIOIMAGE - National Research Data Infrastructure for Microscopy and Bioimage Analysis

NFDI4BIOIMAGE Consortium

Published 2024-08-07

Licensed CC-BY-4.0



Bioimaging refers to a collection of methods to visualize the internal structures and mechanisms of living organisms. The fundamental tool, the microscope, has enabled seminal discoveries like that of the cell as the smallest unit of life, and continues to expand our understanding of biological processes. Today, we can follow the interaction of single molecules within nanoseconds in a living cell, and the development of complete small organisms like fish and flies over several days starting from the fertilized egg. Each image pixel encodes multiple spatiotemporal and spectral dimensions, compounding the massive volume and complexity of bioimage data. Proper handling of this data is indispensable for analysis and its lack has become a growing hindrance for the many disciplines of the life and biomedical sciences relying on bioimaging. No single domain has the expertise to tackle this bottleneck alone.
As a method-specific consortium, NFDI4BIOMAGE seeks to address these issues, enabling bioimaging data to be shared and re-used like they are acquired, i.e., independently of disciplinary boundaries. We will provide solutions for exploiting the full information content of bioimage data and enable new discoveries through sharing and re-analysis. Our RDM strategy is based on a robust needs analysis that derives not only from a community survey but also from over a decade of experience in German BioImaging, the German Society for Microscopy and Image Analysis. It considers the entire lifecycle of bioimaging data, from acquisition to archiving, including analysis and enabling re-use. A foundational element of this strategy is the definition of a common, cloud-compatible, and interoperable digital object that bundles binary images with their descriptive and provenance metadata. With members from plant biology to neuroscience, NFDI4BIOIMAGE will champion the standardization of bioimage data to create a framework that answers discipline-specific needs while ensuring communication and interoperability with data types and RDM systems across domains. Integration of bioimage data with, e.g., omics data as the basis for spatial omics, holds great promise for fields such as cancer medicine. Unlocking the full potential of bioimage data will rely on the development and broad availability of exceptional analysis tools and training sets. NFDI4BIOIMAGE will make these accessible and usable including cutting-edge AI-based methods in scalable cloud environments. NFDI4BIOIMAGE intersects with multiple NFDI consortia, most prominently with GHGA for linking image and genomics data and with DataPLANT on the definition of FAIR data objects. Last but not least, NFDI4BIOIMAGE is internationally well connected and represents the opportunity for German scientists to keep path with and have a voice in several international initiatives focusing on the FAIRification of bioimage data as one of the main challenges for the advancement of knowledge in the life and biomedical sciences.

[https://zenodo.org/records/13168693](https://zenodo.org/records/13168693)

[https://doi.org/10.5281/zenodo.13168693](https://doi.org/10.5281/zenodo.13168693)


---

## NFDI4BIOIMAGE data management illustrations by Henning Falk

NFDI4BIOIMAGE Consortium

Published 2024-11-29

Licensed CC-BY-4.0



These illustrations were contracted by the Heinrich Heine University D&uuml;sseldorf in the frame of the consortium NFDI4BIOIMAGE from Henning Falk for the purpose of education and public outreach. The illustrations are free to use under a CC-BY 4.0 license.AttributionPlease include an attribution similar to: "Data annoation matters", NFDI4BIOIMAGE Consortium (2024): NFDI4BIOIMAGE data management illustrations by Henning Falk, Zenodo,&nbsp;https://doi.org/10.5281/zenodo.14186100, is used under a CC-BY 4.0 license. Modifications to this illustration include cropping.
&nbsp;

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/14186101](https://zenodo.org/records/14186101)

[https://doi.org/10.5281/zenodo.14186101](https://doi.org/10.5281/zenodo.14186101)


---

## NFDI4BIOIMAGE: Perspective for a national bioimaging standard

Josh Moore, Susanne Kunis

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage

Content type: Publication

[https://ceur-ws.org/Vol-3415/paper-27.pdf](https://ceur-ws.org/Vol-3415/paper-27.pdf)


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

## NFDI4Bioimage Calendar 2024 October; original image

Christian Jüngst, Peter Zentis

Published 2024-09-25

Licensed CC-BY-4.0



Raw microscopy image from the NFDI4Bioimage calendar October 2024

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/13837146](https://zenodo.org/records/13837146)

[https://doi.org/10.5281/zenodo.13837146](https://doi.org/10.5281/zenodo.13837146)


---

## NFDI4Bioimage Calendar 2025 March; original image

Sonja Schimmler, Reinhard Altenhöner, Lars Bernard, Juliane Fluck, Axel Klinger, Sören Lorenz, Brigitte Mathiak, Bernhard Miller, Raphael Ritz, Thomas Schörner-Sadenius, Alexander Sczyrba, Regine Stein

Published 2025-02-27

Licensed CC-BY-4.0



Raw microscopy image from the NFDI4Bioimage calendar March 2025.
The image shows 125x magnified microscopic details of a biofilm formed by Pseudomonas fluorescence on the surface of a liquid culture medium. The culture was inoculated with a cellulose-overexpressing and surface-colonizing mScarlet-tagged wild type and a GFP-tagged mutant that is unable to colonize the surface. The biofilm can collapse over time due to its own mass, so that new strategies have to be developed and thus a life cycle emerges.
Image Metadata (using REMBI template):



Study
&nbsp;


Study description
Biofilm formation


Study Component
&nbsp;


Imaging method
Stereo microscopy


Biosample
&nbsp;


Biological entity
Bacteria


Organism
Pseudomonas fluorescence


Specimen
&nbsp;


Signal/contrast mechanism
Relief, fluorescence


Channel 1 - content
Relief, grey


Channel 1 - biological entity
Details of the biofilm in transmitted light


Channel 2 - content
mScarlet, red


Channel 2 - biological entity
WT over-expressing cellulose and colonizing the surface


Channel 3 - content
GFP, green


Channel 3 - biological entity
∆wss mutant unable to colonize the surface


Image Acquisition
&nbsp;


Microscope model
Zeiss Axio Zoom V16


Image Data
&nbsp;


Magnification
125x


Objective
PlanNeoFluar Z 1.0x


Dimension extents
x: 2752, y: 2208


Pixel size description
0.91 &micro;m x 0.91 &micro;m


Image area
2500&micro;m x 2500&micro;m



&nbsp;

[https://zenodo.org/records/14937632](https://zenodo.org/records/14937632)

[https://doi.org/10.5281/zenodo.14937632](https://doi.org/10.5281/zenodo.14937632)


---

## New Kid on the (NFDI) Block: NFDI4BIOIMAGE  - A National Initiative for FAIR Data Management in Bioimaging and Bioimage Analysis

Cornelia Wetzker

Published 2024-10-29

Licensed CC-BY-4.0



The poster introduces the consortium NFDI4BIOIMAGE with its central objectives, provides an overview of challenges in bioimage data handling, sharing and analysis and lists support options by the consortium through its data stewardship team.
It is part of the work of the German consortium NFDI4BIOIMAGE funded by the Deutsche Forschungsgemeinschaft (DFG grant number NFDI 46/1, project number 501864659) and has been presented at the conference FDM@Campus held in G&ouml;ttingen September 23-25, 2024.

[https://zenodo.org/records/14006558](https://zenodo.org/records/14006558)

[https://doi.org/10.5281/zenodo.14006558](https://doi.org/10.5281/zenodo.14006558)


---

## Nextflow: Scalable and reproducible scientific workflows

Floden Evan, Di Tommaso Paolo

Published 2020-12-17

Licensed CC-BY-4.0



Nextflow is an open-source workflow management system that prioritizes portability and reproducibility. It enables users to develop and seamlessly scale genomics workflows locally, on HPC clusters, or in major cloud providers&rsquo; infrastructures. Developed since 2014 and backed by a fast-growing community, the Nextflow ecosystem is made up of users and developers across academia, government and industry. It counts over 1M downloads and over 10K users worldwide.

Tags: Workflow Engine

Content type: Slides

[https://zenodo.org/records/4334697](https://zenodo.org/records/4334697)

[https://doi.org/10.5281/zenodo.4334697](https://doi.org/10.5281/zenodo.4334697)


---

## OME Documentation

Licensed CC-BY-4.0



Tags: OMERO

Content type: Documentation

[https://www.openmicroscopy.org/docs/](https://www.openmicroscopy.org/docs/)


---

## OME-NGFF: a next-generation file format for expanding bioimaging data-access strategies

Josh Moore, Chris Allan, Sébastien Besson, jean-marie burel, Erin Diel, David Gault, Kevin Kozlowski, Dominik Lindner, Melissa Linkert, Trevor Manz, Will Moore, Constantin Pape, Christian Tischer, Jason R. Swedlow

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage, Research Data Management

Content type: Publication

[https://www.nature.com/articles/s41592-021-01326-w](https://www.nature.com/articles/s41592-021-01326-w)


---

## OME2024 NGFF Challenge Results

Josh Moore

Published 2024-11-01

Licensed CC-BY-4.0



Presented at the 2024 FoundingGIDE event in Okazaki, Japan: https://founding-gide.eurobioimaging.eu/event/foundinggide-community-event-2024/
Note: much of the presentation was a demonstration of the OME2024-NGFF-Challenge -- https://ome.github.io/ome2024-ngff-challenge/ especially of querying an extraction of the metadata (https://github.com/ome/ome2024-ngff-challenge-metadata)
&nbsp;

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/14234608](https://zenodo.org/records/14234608)

[https://doi.org/10.5281/zenodo.14234608](https://doi.org/10.5281/zenodo.14234608)


---

## Omero-tools

Johannes Soltwedel

Licensed CC-BY-4.0



This repository contains a collection of tools for working with OMERO. Such tools can be working with the OMERO command line interface to transfer datasets between repositories, etc.

Tags: OMERO, Bioimage Analysis

Content type: Github Repository

[https://biapol.github.io/omero-tools/](https://biapol.github.io/omero-tools/)


---

## Open Image Data Handbook

Kevin Yamauchi

Licensed CC-BY-4.0



Tags: Neubias, Research Data Management, Napari, Python, Bioimage Analysis

Content type: Book, Notebook

[https://kevinyamauchi.github.io/open-image-data/intro.html](https://kevinyamauchi.github.io/open-image-data/intro.html)


---

## Open Micoscropy Environment (OME) Youtube Channel

Published None

Licensed CC-BY-4.0



OME develops open-source software and data format standards for the storage and manipulation of biological microscopy data

Tags: Open Source Software

Content type: Video, Collection

[https://www.youtube.com/@OpenMicroscopyEnvironment](https://www.youtube.com/@OpenMicroscopyEnvironment)


---

## Open Science, Sharing & Licensing

Robert Haase

Published 2024-04-18

Licensed CC-BY-4.0



Wir tauchen ein in die Welt der Open Science und definieren Begriffe wie Open Source, Open Access und die FAIR-Prinzipien (Findable, Accessible, Interoperable and Reuasable). Wir diskutieren, wie diese Methoden der [wissenschaftlichen] Kommunikation und des Datenmanagements die Welt ver&auml;ndern und wie wir sie praktisch in unsere Arbeit integrieren k&ouml;nnen. Dabei spielen Aspekte wie Copyright und Lizenzierung eine wichtige Rolle.

Tags: Research Data Management, Open Access, FAIR-Principles, Licensing

Content type: Slides

[https://zenodo.org/records/10990107](https://zenodo.org/records/10990107)

[https://doi.org/10.5281/zenodo.10990107](https://doi.org/10.5281/zenodo.10990107)


---

## Optimisation and Validation of a Swarm Intelligence based Segmentation Algorithm for low Contrast Positron Emission Tomography

Robert Haase

Published 2014-04-01

Licensed CC-BY-4.0



In the field of radiooncological research, individualised therapy is one of the hot topics at the moment. As a key aspect biologically-adapted therapy is discussed. Therapy adaption based on biological parameters&nbsp;may include tomographic imaging to determine biological properties of the tumour. One often invoked&nbsp;imaging modality is positron emission tomography (PET) using the tracer [18F]-fluoromisonidazole&nbsp;(FMISO) for hypoxia imaging. Hypoxia imaging is of interest, because hypoxic tumours are known to be radiorestistant. Even further, patients with hypoxic tumours have worse prognosis compared to patients&nbsp;with normoxic tumours. Thus, hypoxia imaging appears promising for radiotherapy treatment adaption.&nbsp;For example, volumetric analysis of FMISO PET could deliver additional hypoxia target volumes, which&nbsp;may be irradiated with higher radiation doses to improve the therapeutic effect. However, limited contrast&nbsp;between target volume and background in FMISO PET images interferes image analysis.Established&nbsp;methods for target volume delineation in PET do not allow determination of reliable contours in FMISO PET. To tackle this aspect, this thesis focusses on an earlier developed swarm intelligence based&nbsp;segmentation algorithm for FMISO PET and rather, its optimisation and validation in a clinically relevant&nbsp;setting. In this setting, clinical FMISO PET images were used which were acquired as part of a clinical&nbsp;trial performed at the Clinic and Policlinic for Radiation Therapy and Radiooncology of the University&nbsp;Hospital Carl Gustav Carus Dresden. The segmentation algorithm was applied to these imaging data&nbsp;sets and optimised using a cross-validation approach incorporating reference contours from experienced&nbsp;observers who outlined FMISO PET positive volumes manually. Afterwards, the performance of the algorithm&nbsp;and the properties of the resulting contours were studied in more detail. The algorithm was shown&nbsp;to deliver contours which were similar to manually-created contours to a degree like manually-created&nbsp;contours were similar to each other. Thus, the application of the algorithm in clinical research is recommended&nbsp;to eliminate inter-observer-variabilities. Finally, it was shown that repeated FMISO PET imaging&nbsp;before and shortly after the beginning of combined radiochemotherapy lead to manually-created contours&nbsp;with significantly higher variations than the variations of automatically-created contours using the&nbsp;proposed algorithm. Increased contour similarity in subsequently acquired imaging data highlights the&nbsp;observer-independence of the algorithm. While several observers outline different volumes, in identical&nbsp;data sets as well as in subsequent imaging data sets, the algorithm outlines more stable volumes in both&nbsp;cases. Thus, increased contour reproducibility is reached by automation of the delineation process by&nbsp;the proposed algorithm.&nbsp;

[https://zenodo.org/records/7209862](https://zenodo.org/records/7209862)

[https://doi.org/10.5281/zenodo.7209862](https://doi.org/10.5281/zenodo.7209862)


---

## Optimized cranial window implantation for subcellular and functional imaging in vivo

Ben Vermaercke

Published 2025-01-13

Licensed CC-BY-4.0



Intravital workshop 15/11/2024

[https://zenodo.org/records/14641777](https://zenodo.org/records/14641777)

[https://doi.org/10.5281/zenodo.14641777](https://doi.org/10.5281/zenodo.14641777)


---

## Overview of the Galaxy OMERO-suite - Upload images and metadata in OMERO using Galaxy

Riccardo Massei, Björn Grüning

Published 2024-12-02

Licensed CC-BY-4.0



Tags: OMERO, Galaxy, Metadata, Nfdi4Bioimage

Content type: Tutorial, Framework, Workflow

[https://training.galaxyproject.org/training-material/topics/imaging/tutorials/omero-suite/tutorial.html](https://training.galaxyproject.org/training-material/topics/imaging/tutorials/omero-suite/tutorial.html)


---

## Parallelization and heterogeneous computing: from pure CPU to GPU-accelerated image processing

Robert Haase

Licensed CC-BY-4.0



Content type: Slides

[https://f1000research.com/slides/11-1171](https://f1000research.com/slides/11-1171)

[https://doi.org/10.7490/f1000research.1119154.1](https://doi.org/10.7490/f1000research.1119154.1)


---

## Photonic data analysis in 2050

Oleg Ryabchykov, Shuxia Guo, Thomas Bocklitz

Licensed CC-BY-4.0



Photonic data analysis, combining imaging, spectroscopy, machine learning, and computer science, requires flexible methods and interdisciplinary collaborations to advance. Essential developments include standardizing data infrastructure for comparability, optimizing data-driven models for complex investigations, and creating techniques to handle limited or unbalanced data and device variations.

Tags: FAIR-Principles, Machine Learning, Research Data Management

Content type: Publication

[https://doi.org/10.1016/j.vibspec.2024.103685](https://doi.org/10.1016/j.vibspec.2024.103685)


---

## PoL Bio-Image Analysis Training School on GPU-Accelerated Image Analysis

Stephane Rigaud, Brian Northan, Till Korten, Neringa Jurenaite, Apurv Deepak Kulkarni, Peter Steinbach, Sebastian Starke, Johannes Soltwedel, Marvin Albert, Robert Haase

Licensed CC-BY-4.0



This repository hosts notebooks, information and data for the GPU-Accelerated Image Analysis Track of the PoL Bio-Image Analysis Symposium.

Tags: Gpu, Clesperanto, Dask, Python

Content type: Notebook

[https://github.com/BiAPoL/PoL-BioImage-Analysis-TS-GPU-Accelerated-Image-Analysis/](https://github.com/BiAPoL/PoL-BioImage-Analysis-TS-GPU-Accelerated-Image-Analysis/)


---

## Practical Guide to the International Alignment of Research Data Management - Extended Edition

Licensed CC-BY-4.0



Content type: Book

[https://www.scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/](https://www.scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/)

[https://doi.org/10.5281/zenodo.4915861](https://doi.org/10.5281/zenodo.4915861)


---

## Preprint: "Be Sustainable", Recommendations for FAIR Resources in Life Sciences research: EOSC-Life's Lessons

Romain David, Arina Rybina, jean-marie burel, Jean-Karim Heriche, Pauline Audergon, Jan-Willem Boiten, Frederik Coppens, Sara Crockett, Exter Katrina, Sven Fahrener, Maddalena Fratelli, Carole Goble, Philipp Gormanns, Tobias Grantner, Bjorn Gruning, Kim Tamara Gurwitz, John Hancock, Henriette Harmse, Petr Holub, Nick Juty, Geoffrey Karnbach, Emma Karoune, Antje Keppler, Jessica Klemeier, Carla Lancelotti, Jean-Luc Legras, L. Allyson Lister, Dario Livio Longo, Rebecca Ludwig, Benedicte Madon, Marzia Massimi, Vera Matser, Rafaele Matteoni, Mayrhofer Michaela Th., Christian Ohmann, Maria Panagiotopoulou, Helen Parkinson, Isabelle Perseil, Claudia Pfander, Roland Pieruschka, Michael Raess, Andreas Rauber, Audrey S. Richard, Paolo Romano, Antonio Rosato, Alex Sanchez-Pla, Susanna-Assunta Sansone, Ugis Sarkans, Beatriz Serrano-Solano, Jing Tang, Ziaurrehman Tanoli, Jonathan Tedds, Harald Wagener, Martin Weise, Hans V. Westerhoff, Rudolf Wittner, Jonathan Ewbank, Niklas Blomberg, Philip Gribbon

Published 2023-09-12

Licensed CC-BY-4.0



"Be SURE - Be SUstainable REcommendations"The main goals and challenges for the Life Science (LS) communities in the Open Science framework are to increase reuse and sustainability of data resources, software tools, and workflows, especially in large-scale data-driven research and computational analyses. Here, we present key findings, procedures, effective measures and recommendations for generating and establishing sustainable LS resources based on the collaborative, cross-disciplinary work done within the EOSC-Life (European Open Science Cloud for Life Sciences) consortium. Bringing together 13 European LS Research Infrastructures (RIs), it has laid the foundation for an open, digital space to support biological and medical research. Using lessons learned from 27 selected projects, we describe the organisational, technical, financial and legal/ethical challenges that represent the main barriers to sustainability in the life sciences. We show how EOSC-Life provides a model for sustainable FAIR data management, including solutions for sensitive- and industry-related resources, by means of cross-disciplinary training and best practices sharing. Finally, we illustrate how data harmonisation and collaborative work facilitate interoperability of tools, data, solutions and lead to a better understanding of concepts, semantics and functionalities in the life sciences.IN PRESS EMBO Journal:&nbsp;https://www.embopress.org/journal/14602075&nbsp;AVAILABLE SOON at : https://doi.org/10.15252/embj.2023115008&nbsp;

[https://zenodo.org/records/8338931](https://zenodo.org/records/8338931)

[https://doi.org/10.5281/zenodo.8338931](https://doi.org/10.5281/zenodo.8338931)


---

## Prompt Engineering, Agentic Workflows and Multi-modal Large Language Models

Robert Haase

Published 2025-01-19

Licensed CC-BY-4.0



In these two slide-decks we explore applications of large language models. In the first slide deck we dive into prompt engineering, function calling and how to build agentic workflows. In the second slide-deck we explore multi-modal large language models focusing on vision language models and image generation models.&nbsp;

[https://zenodo.org/records/14692037](https://zenodo.org/records/14692037)

[https://doi.org/10.5281/zenodo.14692037](https://doi.org/10.5281/zenodo.14692037)


---

## QI 2024 Analysis Lab Manual

Beth Cimini, Florian Jug, QI 2024

Licensed CC-BY-4.0



This book contains the quantitative analysis labs for the QI CSHL course, 2024

Tags: Python

Content type: Notebook

[https://bethac07.github.io/qi_2024_analysis_lab_manual/intro.html](https://bethac07.github.io/qi_2024_analysis_lab_manual/intro.html)


---

## QM Course Lectures on Bio-Image Analysis with napari 2024

Marcelo Leomil Zoccoler

Licensed CC-BY-4.0



In these lectures, we will explore ways to analyze microscopy images with Python and visualize them with napari, an nD viewer open-source software. The analysis will be done in Python mostly using the scikit-image, pyclesperanto and apoc libraries, via Jupyter notebooks. We will also explore some napari plugins as an interactive and convenient alternative way of performing these analysis, especially the napari-assistant, napari-apoc and napari-flim-phasor-plotter plugins.

Tags: Napari, Python

Content type: Notebook

[https://zoccoler.github.io/QM_Course_Bio_Image_Analysis_with_napari_2024](https://zoccoler.github.io/QM_Course_Bio_Image_Analysis_with_napari_2024)


---

## QUAREP-LiMi: A community-driven initiative to establish guidelines for quality assessment and reproducibility for instruments and images in light microscopy

Glyn Nelson, Ulrike Boehme, et al.

Licensed CC-BY-4.0



Tags: Quareo-Limi

Content type: Publication

[https://onlinelibrary.wiley.com/doi/10.1111/jmi.13041](https://onlinelibrary.wiley.com/doi/10.1111/jmi.13041)


---

## QuPath: Open source software for analysing (awkward) images

Peter Bankhead

Published 2020-12-16

Licensed CC-BY-4.0



Slides from the CZI/EOSS online meeting in December 2020.

Tags: Bioimage Analysis

Content type: Slides

[https://zenodo.org/records/4328911](https://zenodo.org/records/4328911)

[https://doi.org/10.5281/zenodo.4328911](https://doi.org/10.5281/zenodo.4328911)


---

## RDF as a bridge to domain-platforms like OMERO, or There and back again.

Josh Moore, Andra Waagmeester, Kristina Hettne, Katherine Wolstencroft, Susanne Kunis

Licensed CC-BY-4.0



In 2005, the first version of OMERO stored RDF natively. However, just a year after the 1.0 release of RDF, performance considerations led to the development of a more traditional SQL approach for OMERO. A binary protocol makes it possible to query and retrieve metadata but the resulting information cannot immediately be combined with other sources. This is the adventure of rediscovering the benefit of RDF triples as a -- if not the -- common exchange mechanism.

Tags: Research Data Management, FAIR-Principles, Bioimage Analysis

Content type: Slides

[https://zenodo.org/doi/10.5281/zenodo.10687658](https://zenodo.org/doi/10.5281/zenodo.10687658)


---

## RDM Starter Kit

GO FAIR

Licensed CC-BY-4.0



This page is supposed to serve as a Starter Kit for research data management (RDM). It lists resources designed to help researchers get started to organize their data.

Tags: Research Data Management

Content type: Website

[https://www.go-fair.org/resources/rdm-starter-kit/](https://www.go-fair.org/resources/rdm-starter-kit/)


---

## RDM4Mic Presentations

Licensed CC-BY-4.0



Tags: Research Data Management

Content type: Collection

[https://github.com/German-BioImaging/RDM4mic/tree/master/presentations](https://github.com/German-BioImaging/RDM4mic/tree/master/presentations)


---

## RDMKit Training Resources

Licensed CC-BY-4.0



Tags: Research Data Management

Content type: Collection

[https://rdmkit.elixir-europe.org/all_training_resources](https://rdmkit.elixir-europe.org/all_training_resources)


---

## RESEARCH DATA MANAGEMENT on Campus and in NFDI4BIOIMAGE

Cornelia Wetzker, Michael Schlierf

Published 2024-08-29

Licensed CC-BY-4.0



The poster is part of the work of the German consortium NFDI4BIOIMAGE funded by the Deutsche Forschungsgemeinschaft (DFG grant number NFDI 46/1, project number 501864659).

[https://zenodo.org/records/13684187](https://zenodo.org/records/13684187)

[https://doi.org/10.5281/zenodo.13684187](https://doi.org/10.5281/zenodo.13684187)


---

## Rechtsfragen bei Open Science - Ein Leitfaden

Till Kreutzer, Henning Lahmann

Published 2021-05-25

Licensed CC-BY-4.0



Die Digitalisierung ermöglicht eine offene Wissenschaft (Open Science). Diese hat viele Aspekte, insbesondere den freien Zugang zu wissenschaftlichen Veröffentlichungen und Materialien (Open Access), transparente Begutachtungsverfahren (Open Peer Review) oder quelloffene Technologien (Open Source). Das Programm Hamburg Open Science (Laufzeit 2018–2020) unterstützt unter anderem den Kulturwandel in der Wissenschaft. In diesem Kontext entstand der nun vorliegende Leitfaden, der das rechtliche Umfeld greifbar machen soll. Der Leitfaden erarbeitet die betroffenen Rechtsgebiete zunächst systematisch. Im zweiten Teil werden rechtliche Fragen zu Open Science beantwortet, die direkt aus den Universitäten und Bibliotheken kommen.

Tags: Open Science, Open Access, Copyright

Content type: Book

[https://hup.sub.uni-hamburg.de/oa-pub/catalog/book/205](https://hup.sub.uni-hamburg.de/oa-pub/catalog/book/205)


---

## Reconstructed images of a 2DSIM multiposition acquisition.

Louis Romette

Published 2025-02-19

Licensed CC-BY-4.0



Acquired with an Nikon SIM, in 2D-SIM mode at 488nm of excitation with 30% laser power and 200ms of exposition.&nbsp; Fluorescence is a knocked-in mStayGold-&beta;2Spectrin. Cells are rat hippocampal neurons &agrave; DIV 3. The file is a reconstructed multiposition acquisition (10 positions). Uploaded to show a probable issue with Bio-Formats in Fiji, where SIM reconstrcuted multipositions files open like static noise.&nbsp;

[https://zenodo.org/records/14893791](https://zenodo.org/records/14893791)

[https://doi.org/10.5281/zenodo.14893791](https://doi.org/10.5281/zenodo.14893791)


---

## Report on a pilot study:  Implementation of OMERO for  microscopy data management

Silke Tulok, Gunar Fabig, Andy Vogelsang, Thomas Kugel, Thomas Müller-Reichert

Published 2023-11-10

Licensed CC-BY-4.0



The Core Facility Cellular Imaging (CFCI) at the Faculty of Medicine Carl Gustav Carus (TU Dresden) is currently running a pilot project for testing the use and handling of the OMERO software. This is done together with interested users of the imaging facility and a research group. Currently, we are pushing forward this pilot study on a small scale without any data steward. Our experiences argue so far for giving data management issues into the hands of dedicated personnel not fully involved in research projects. As funding agencies will ask for higher and higher standards for implementing FAIRdata principles in the future, this will be a releva

[https://zenodo.org/records/10103316](https://zenodo.org/records/10103316)

[https://doi.org/10.5281/zenodo.10103316](https://doi.org/10.5281/zenodo.10103316)


---

## Research Data Management Seminar - Slides

Stefano Della Chiesa

Published 2022-05-18

Licensed CC-BY-4.0



This Research Data Management (RDM) Slides introduce to the multidisciplinary knowledge and competencies required to address policy compliance and research data management best practices throughout a project lifecycle, and beyond it.


	Module 1 - Introduces the RDM giving its context in the Research Data Governance
	Module 2 - Illustrates the most important RDM policies and principles
	Module 3 - Provides the most relevant RDM knowledge bricks
	Module 4 - Discuss the Data Management Plans (DMPs), examples, templates and guidance


&nbsp;

Tags: Research Data Management

Content type: Slides

[https://zenodo.org/record/6602101](https://zenodo.org/record/6602101)

[https://doi.org/10.5281/zenodo.6602101](https://doi.org/10.5281/zenodo.6602101)


---

## Research Data Managemet and how not to get overwhelmed with data

Martin Schätz

Published 2023-09-23

Licensed CC-BY-4.0



Research data management and how not to get overwhelmed with data presentation is an overview of bioimage analysis with a focus on the basics for data management planning, FAIR principles, and how to practically organize folders and prepares naming convention. The presentation includes an overview of metadata, Creative Common licenses, and a sum up of electronic laboratory notebooks. The last two slides go through how all of that works in practice in open access core microscopy facility.

[https://zenodo.org/records/8372703](https://zenodo.org/records/8372703)

[https://doi.org/10.5281/zenodo.8372703](https://doi.org/10.5281/zenodo.8372703)


---

## Research Data Reusability - Conceptual Foundations, Barriers and Enabling Technologies

Costantino Thanos

Published 2017-01-09

Licensed CC-BY-4.0



This article discusses various aspects of data reusability in the context of scientific research, including technological, legal, and policy frameworks.

Tags: Research Data Management, Open Science, Data Protection

Content type: Publication

[https://www.mdpi.com/2304-6775/5/1/2](https://www.mdpi.com/2304-6775/5/1/2)


---

## Research data management for bioimaging - the 2021 NFDI4BIOIMAGE community survey

Christian Schmidt, Janina Hanne, Josh Moore, Christian Meesters, Elisa Ferrando-May, et al.

Published 2022-09-20

Licensed CC-BY-4.0



As an initiative within Germany's National Research Data Infrastructure, the authors conducted this community survey in summer 2021 to assess the state of the art of bioimaging RDM and the community needs.

Tags: Research Data Management

Content type: Publication

[https://f1000research.com/articles/11-638/v2](https://f1000research.com/articles/11-638/v2)


---

## Research data management for bioimaging: the 2021 NFDI4BIOIMAGE community survey

Christian Schmidt, Janina Hanne, Josh Moore, Christian Meesters, Elisa Ferrando-May, Stefanie Weidtkamp-Peters, members of the NFDI4BIOIMAGE initiative

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage, Research Data Management

Content type: Publication

[https://f1000research.com/articles/11-638](https://f1000research.com/articles/11-638)


---

## Round Table Workshop 1 - Sample Stabilization in intravital Imaging

Michael Gerlach, Hans-Ulrich Fried, Christiane Peuckert

Published 2024-11-14

Licensed CC-BY-4.0



Notes from a round table workshop on the 4th Day of Intravital Microscopy in Leuven, Belgium.
Contains hands-on tips, tricks and schemes to improve sample stability during various models of Intravital Miroscopy.

[https://zenodo.org/records/14161289](https://zenodo.org/records/14161289)

[https://doi.org/10.5281/zenodo.14161289](https://doi.org/10.5281/zenodo.14161289)


---

## Round Table Workshop 2 - Correction of Drift and Movement

Dr. Hellen Ishikawa-Ankerhold, Max Nobis

Published 2024-11-14

Licensed CC-BY-4.0



Session 2 of a round table workshop. Features description of image processing methods useful in intravital imaging to compensate for the motion of living tissue.

[https://zenodo.org/records/14161633](https://zenodo.org/records/14161633)

[https://doi.org/10.5281/zenodo.14161633](https://doi.org/10.5281/zenodo.14161633)


---

## Running Deep-Learning Scripts in the BiA-PoL Omero Server

Marcelo Zoccoler

Licensed CC-BY-4.0



Tags: Python, Artificial Intelligence, Bioimage Analysis

Content type: Blog Post

[https://biapol.github.io/blog/marcelo_zoccoler/omero_scripts/readme.html](https://biapol.github.io/blog/marcelo_zoccoler/omero_scripts/readme.html)


---

## SWC/GCNU Software Skills

Licensed CC-BY-4.0



Computational skills training at the UCL Sainsbury Wellcome Centre and Gatsby Computational Neuroscience Unit, delivered by members of the Neuroinformatics Unit.

Content type: Collection, Online Course, Video, Tutorial

[https://software-skills.neuroinformatics.dev/index.html](https://software-skills.neuroinformatics.dev/index.html)


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

## Sharing and licensing material

Robert Haase

Licensed CC-BY-4.0



Introduction to sharing resources online and licensing

Tags: Sharing, Research Data Management

Content type: Slides

[https://f1000research.com/slides/10-519](https://f1000research.com/slides/10-519)


---

## Sharing research data with Zenodo

Robert Haase

Licensed CC-BY-4.0



Blog post about how to share data using zenodo.org

Tags: Sharing, Research Data Management

Content type: Blog Post

[https://focalplane.biologists.com/2023/02/15/sharing-research-data-with-zenodo/](https://focalplane.biologists.com/2023/02/15/sharing-research-data-with-zenodo/)


---

## Slides about FLUTE: a Python GUI for interactive phasor analysis of FLIM data

Chiara Stringari

Published 2024-03-19

Licensed CC-BY-4.0



This presentation introduces the open source software to analyze FLIM data:
FLUTE &ndash; (F)luorescence (L)ifetime (U)ltima(T)e (E)xplorer:
a Python GUI for interactive phasor analysis of FLIM data
&nbsp;
The software is available on GitHub: https://github.com/LaboratoryOpticsBiosciences/FLUTE
and it is published on Biological imaging Journal: Gottlieb, D., Asadipour, B., Kostina, P., Ung, T., &amp; Stringari, C. (2023). FLUTE: A Python GUI for interactive phasor analysis of FLIM data. Biological Imaging, 1-22. doi:10.1017/S2633903X23000211
The lecture was part of the short talks on community developed FLIM-software at the German BioImaging workshop on FLIM in Munich.

[https://zenodo.org/records/10839310](https://zenodo.org/records/10839310)

[https://doi.org/10.5281/zenodo.10839310](https://doi.org/10.5281/zenodo.10839310)


---

## So geschlossen wie nötig, so offen wie möglich - Datenschutz beim Umgang mit Forschungsdaten

Pia Voigt

Published 2024-05-30

Licensed CC-BY-4.0



Der Umgang mit personenbezogenen Daten stellt Forschende oft vor rechtliche Herausforderungen: Unter welchen Bedingungen d&uuml;rfen personenbezogene Daten verarbeitet werden? Welche Voraussetzungen m&uuml;ssen erf&uuml;llt sein und welche Strategien k&ouml;nnen angewendet werden, um Daten sicher speichern, verarbeiten, teilen und aufbewahren zu k&ouml;nnen? Mit Hilfe dieses Foliensatzes erhalten Sie Einblicke in datenschutzrechtliche Aspekte beim Umgang mit Ihren Forschungsdaten.&nbsp;

Tags: Research Data Management, Data Protection, FAIR-Principles

Content type: Slides

[https://zenodo.org/records/11396199](https://zenodo.org/records/11396199)

[https://doi.org/10.5281/zenodo.11396199](https://doi.org/10.5281/zenodo.11396199)


---

## SpatialData: an open and universal data framework for spatial omics

Luca Marconato, Giovanni Palla, Kevin A Yamauchi, Isaac Virshup, Elyas Heidari, Tim Treis, Marcella Toth, Rahul Shrestha, Harald Vöhringer, Wolfgang Huber, Moritz Gerstung, Josh Moore, Fabian J Theis, Oliver Stegle

Licensed CC-BY-4.0



Tags: Python

Content type: Publication, Preprint

[https://www.biorxiv.org/content/10.1101/2023.05.05.539647v1.abstract](https://www.biorxiv.org/content/10.1101/2023.05.05.539647v1.abstract)


---

## Stackview sliceplot example data

Robert Haase

Published 2024-11-03

Licensed CC-BY-4.0



This is a dataset of PNG images of [Bio-Image Data Science teaching slides](https://zenodo.org/records/12623730). The png_umap.yml file contains a list of all images and a dimensionality reduced embedding (Uniform Manifold Approximation Projection, UMAP) made using OpenAI's text-embedding-ada-002 model.
A notebook for visualizing this data is published here: https://github.com/haesleinhuepf/stackview/blob/main/docs/sliceplot.ipynb

[https://zenodo.org/records/14030307](https://zenodo.org/records/14030307)

[https://doi.org/10.5281/zenodo.14030307](https://doi.org/10.5281/zenodo.14030307)


---

## Structuring of Data and Metadata in Bioimaging: Concepts and technical Solutions in the Context of Linked Data

Sarah Weischer, Jens Wendt, Thomas Zobel

Published 2022-07-12

Licensed CC-BY-4.0



Provides an overview of contexts, frameworks, and models from the world of bioimage data as well as metadata. Visualizes the techniques for structuring this data as Linked Data. (Walkthrough Video: https://doi.org/10.5281/zenodo.7018928 )

Content:


	Types of metadata
	Data formats
	Data Models Microscopy Data
	Tools to edit/gather metadata
	ISA Framework
	FDO Framework
	Ontology
	RDF
	JSON-LD
	SPARQL
	Knowledge Graph
	Linked Data
	Smart Data
	...


Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/7018750](https://zenodo.org/records/7018750)

[https://doi.org/10.5281/zenodo.7018750](https://doi.org/10.5281/zenodo.7018750)


---

## Sustainable Data Stewardship

Stefano Della Chiesa

Published 2024-03-25

Licensed CC-BY-4.0



 These slides were presented at the 2. SaxFDM-Beratungsstammtisch and delve into the strategic integration of Research Data Management (RDM) within research organizations. The Leibniz IOER presented an insightful overview of RDM activities and approaches, emphasizing the criticality of embedding RDM strategically within research institutions. The presentation showcases some best practices in RDM implementation through practical examples, offering valuable insights for optimizing data stewardship processes.

Tags: Research Data Management, Data Stewardship

Content type: Slides

[https://zenodo.org/records/10942559](https://zenodo.org/records/10942559)

[https://doi.org/10.5281/zenodo.10942559](https://doi.org/10.5281/zenodo.10942559)


---

## Ten simple rules for making training materials FAIR

Leyla Garcia, Bérénice Batut, Melissa L. Burke, Mateusz Kuzak, Fotis Psomopoulos, et al.

Published 2020-05-21

Licensed CC-BY-4.0



The authors offer trainers some simple rules, to help make their training materials FAIR, enabling others to find, (re)use, and adapt them.

Tags: Metadata, Bioinformatics, FAIR-Principles

Content type: Publication

[https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007854](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007854)


---

## Terminology service for research data management and knowledge discovery in low-temperature plasma physics

Markus M. Becker, Ihda Chaerony Siffa, Roman Baum

Published 2024-12-11

Licensed CC-BY-4.0



Abstract: 
Terminology services (TS) [1,2] play a pivotal role in achieving structured metadata by providing controlled vocabularies and ontologies that standardize the description of data. This is a crucial aspect of research data management (RDM) in all scientific disciplines. In addition, TS facilitate the use of a common vocabulary within a scientific community also in a more general context, e.g. to annotate scientific papers, patents or other content for better discoverability, as envisaged by the Open Research Knowledge Graph (ORKG) [3] or the Patents4Science project [4].&nbsp;
To make use of these opportunities, terminologies, ontologies and knowledge graphs must be developed and made available as TS where they do not yet exist. This step is currently being taken by the research community in low-temperature plasma (LTP) physics. LTP physics explores partially ionized gases and its technological applications. This vibrant field offers innovative solutions for societal challenges, ranging from developing efficient lighting and solar cells to revolutionizing healthcare through plasma medicine. Various activities and projects have been started in the past years to support the RDM in LTP research and development and to facilitate the application of data-driven research methods. These activities are supported in parts by the NFDI4BIOIMAGE consortium, active work in the NFDI section &ldquo;(Meta)data, Terminologies, Provenance&rdquo;, and the basic service Terminology Services 4 NFDI (TS4NFDI) funded by Base4NFDI.&nbsp;
Recently, the ontology Plasma-O [5&ndash;7] for LTP physics has been developed at INP in collaboration with FIZ Karlsruhe &ndash; Leibniz Institute for Information Infrastructure, providing a framework for structuring metadata and building a knowledge graph for scientific information within the field. The present contribution will show how a TS utilizing this resource can support different aspects of RDM and knowledge discovery using concrete examples. The application cases include (i) standardizing data annotation: By providing researchers with a controlled vocabulary of LTP-specific terms and their relationships, ensuring consistent and unambiguous data descriptions; (ii) enabling semantic search: Moving beyond keyword-based searches, TS allow for complex queries based on the relationships between concepts, significantly improving data discoverability; (iii) facilitating data integration: By mapping data from different sources to a common ontology, TS enable seamless integration and analysis of heterogeneous datasets, which is crucial for data-driven research and development. The TS Suite of TS4NFDI with the provided widgets [8] fits perfectly to the requirements of these three application cases and will support the harmonization of metadata in LTP physics. The implementation of a public TS is required to provide the domain-specific metadata in a standardized format and will be instrumental in unlocking the full potential of the TS widgets for RDM and knowledge discovery by LTP researchers. Furthermore, the results can provide insights to other domains on how to apply TS to their specific needs.
&nbsp;The work was supported in parts by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under the National Research Data Infrastructure &ndash; [NFDI46/1] &ndash; 501864659 and project number 496963457 as well as by the Federal Ministry of Education and Research (BMBF), project number 16KOA013A.
References:




[1]


S. Jupp, T. Burdett, C. Leroy, H. Parkinson, &ldquo;A new Ontology Lookup Service at EMBL-EBI&rdquo;, Workshop on Semantic Web Applications and Tools for Life Sciences (2015), https://ceur-ws.org/Vol-1546/paper_29.pdf (accessed: 2024-09-20).




[2]


P. L. Whetzel, N. F. Noy, N. H. Shah, P. R. Alexander, C. Nyulas, T. Tudorache, M. A. Musen, &ldquo;BioPortal: enhanced functionality via new Web services from the National Center for Biomedical Ontology to access and use ontologies in software applications&rdquo;, Nucleic Acids Res. 39 (2011) W541&ndash;W545, https://doi.org/10.1093/nar/gkr469. 




[3]


Open Research Knowledge Graph, https://orkg.org/ (accessed: 2024-09-20).




[4]


Patents4Science &ndash; Establishing an Information Infrastructure for the Use of Patent Knowledge in Science, https://www.patents4science.org/ (accessed: 2024-09-20).




[5]


H. Sack, F. Hoppe, &ldquo;Verbundprojekt: Qualit&auml;tssicherung und Vernetzung von Forschungsdaten in der Plasmatechnologie - QPTDat; Teilvorhaben: Wissensgraph und Ontologieentwicklung zur Vernetzung von Metadaten : Schlussbericht des Teilvorhabens&rdquo;, 2023, https://doi.org/10.2314/KXP:1883436974.




[6]


I. Chaerony Siffa, R. Wagner, L. Vilardell Scholten, M. M. Becker, &ldquo;Semantic Information Management in Low-Temperature Plasma Science and Technology with VIVO&rdquo;, 2024, preprint, https://doi.org/10.48550/arXiv.2409.11065.




[7]


I. Chaerony Siffa, R. Wagner, L. Vilardell Scholten, M. M. Becker, &ldquo;Plasma Ontology and Knowledge Graph Initial Release v0.5.0&rdquo;, 2024, Zenodo, https://doi.org/10.5281/zenodo.13325226. 




[8]


J. Sasse, V. Kneip, R. Baum, P. Zimmermann, J. Darms, J. Schneider, V. Clemens, P. Oladazimi, L. K&uuml;hnel, &ldquo;ts4nfdi/terminology-service-suite: v2.6.0&rdquo;, 2024, Zenodo, https://doi.org/10.5281/zenodo.13692297. 





[https://zenodo.org/records/14381522](https://zenodo.org/records/14381522)

[https://doi.org/10.5281/zenodo.14381522](https://doi.org/10.5281/zenodo.14381522)


---

## Test Dataset for Whole Slide Image Registration

Romain Guiet, Nicolas Chiaruttini

Published 2021-04-12

Licensed CC-BY-4.0



Mouse duodenum fixed in 4% PFA overnight at 4&deg;C, processed for paraffin infiltration using a standard histology procedure and cut at 4 microns were dewaxed, rehydrated, permeabilized with 0.5% Triton X-100 in PBS 1x and stained with Azide - Alexa Fluor 555 (Thermo Fisher) to detect EdU and DAPI for nuclei. The images were taken using a Leica DM5500 microscope with a 40X N.A.1 objective (black&amp;white camera: DFC350FXR2, pixel dimension: 0.161 microns). Next, the slide was unmounted and stained using the fully automated Ventana Discovery xT autostainer (Roche Diagnostics, Rotkreuz, Switzerland). All steps were performed on automate with Ventana solutions. Sections were pretreated with heat using the CC1 solution under mild conditions. The primary rat anti BrDU (clone: BU1/75 (ICR1), Serotec, diluted 1:300) was incubated 1 hour at 37&deg;C. After incubation with a donkey anti rat biotin diluted 1:200 (Jackson ImmunoResearch Laboratories), chromogenic revelation was performed with DabMap kit. The section was counterstained with Harris hematoxylin (J.T. Baker) before a second round of imaging on DM5500 PL Fluotar 40X N.A.1.0 oil (color camera: DFC 320 R2, pixel dimension: 0.1725 microns). Before acquisition, a white-balance as well as a shading correction is performed according to Leica LAS software wizard. The fluorescence and DAB images were converted in ome.tiff multiresolution file with the kheops Fiji Plugin.

Sampled prepared in the EPFL histology core facility by Nathalie M&uuml;ller and Gian-Filippo Mancini.

Associated documents:


	https://c4science.ch/w/bioimaging_and_optics_platform_biop/teaching/dab-intensity/
	https://imagej.net/plugins/bdv/warpy/warpy


This document contains a full QuPath project with an example of registered image.

&nbsp;

[https://zenodo.org/records/5675686](https://zenodo.org/records/5675686)

[https://doi.org/10.5281/zenodo.5675686](https://doi.org/10.5281/zenodo.5675686)


---

## The FAIR Guiding Principles for scientific data management and stewardship

Mark D. Wilkinson, Michel Dumontier, IJsbrand Jan Aalbersberg, Gabrielle Appleton, Myles Axton, et. al

Published 2016-03-15

Licensed CC-BY-4.0



This Comment is the first formal publication of the FAIR Principles, and includes the rationale behind them, and some exemplar implementations in the community.

Tags: FAIR-Principles, Research Data Management

Content type: Publication

[https://www.nature.com/articles/sdata201618](https://www.nature.com/articles/sdata201618)

[https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)


---

## The FAIR guiding principles for data stewardship - fair enough?

Martin Boeckhout, Gerhard A. Zielhuis, Annelien L. Bredenoord

Published 2018-05-17

Licensed CC-BY-4.0



The FAIR guiding principles for research data stewardship (findability, accessibility, interoperability, and reusability) look set to become a cornerstone of research in the life sciences. A critical appraisal of these principles in light of ongoing discussions and developments about data sharing is in order.

Tags: FAIR-Principles, Data Stewardship, Sharing

Content type: Publication

[https://www.nature.com/articles/s41431-018-0160-0](https://www.nature.com/articles/s41431-018-0160-0)


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

## The Open Microscopy Environment (OME) Data Model and XML file - open tools for informatics and quantitative analysis in biological imaging

Ilya G. Goldberg, Chris Allan, jean-marie burel, Doug Creager, Andrea Falconi, et. al

Published 2005-05-03

Licensed CC-BY-4.0



The Open Microscopy Environment (OME) defines a data model and a software implementation to serve as an informatics framework for imaging in biological microscopy experiments, including representation of acquisition parameters, annotations and image analysis results.

Tags: Bioimage Analysis

Content type: Publication

[https://genomebiology.biomedcentral.com/articles/10.1186/gb-2005-6-5-r47](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2005-6-5-r47)

[https://doi.org/10.1186/gb-2005-6-5-r47](https://doi.org/10.1186/gb-2005-6-5-r47)


---

## The Turing Way: Guide for reproducible research

Licensed ['CC-BY-4.0', 'MIT']



A guide which covers topics related to skills, tools and best practices for research reproducibility.

Content type: Book

[https://the-turing-way.netlify.app/reproducible-research/reproducible-research](https://the-turing-way.netlify.app/reproducible-research/reproducible-research)


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

## Thinking data management on different scales

Susanne Kunis

Licensed CC-BY-4.0



Presentation given at PoL BioImage Analysis Symposium Dresden 2023

Tags: Research Data Management, Nfdi4Bioimage

Content type: Slides

[https://zenodo.org/doi/10.5281/zenodo.8329305](https://zenodo.org/doi/10.5281/zenodo.8329305)


---

## Towards Preservation of Life Science Data with NFDI4BIOIMAGE

Robert Haase

Published 2024-09-03

Licensed CC-BY-4.0



This talk will present the initiatives of the NFDI4BioImage consortium aimed at the long-term preservation of life science data. We will discuss our efforts to establish metadata standards, which are crucial for ensuring data reusability and integrity. The development of sustainable infrastructure is another key focus, enabling seamless data integration and analysis in the cloud. We will take a look at how we manage training materials and communicate with our community. Through these actions, NFDI4BioImage seeks to enable FAIR bioimage data management for German researchers, across disciplines and embedded in the international framework.

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/13640979](https://zenodo.org/records/13640979)

[https://doi.org/10.5281/zenodo.13640979](https://doi.org/10.5281/zenodo.13640979)


---

## Towards Transparency and Knowledge Exchange in AI-assisted Data Analysis Code Generation

Robert Haase

Published 2024-10-14

Licensed CC-BY-4.0



The integration of Large Language Models (LLMs) in scientific research presents both opportunities and challenges for life scientists. Key challenges include ensuring transparency in AI-generated content and facilitating efficient knowledge exchange among researchers. These issues arise from the in-transparent nature of AI-driven code generation and the informal sharing of AI insights, which may hinder reproducibility and collaboration. This paper introduces git-bob, an innovative AI-assistant designed to address these challenges by fostering an interactive and transparent collaboration platform within GitHub. By enabling seamless dialogue between humans and AI, git-bob ensures that AI contributions are transparent and reproducible. Moreover, it supports collaborative knowledge exchange, enhancing the interdisciplinary dialogue necessary for cutting-edge life sciences research. The open-source nature of git-bob further promotes accessibility and customization, positioning it as a vital tool in employing LLMs responsibly and effectively within scientific communities.

[https://zenodo.org/records/13928832](https://zenodo.org/records/13928832)

[https://doi.org/10.5281/zenodo.13928832](https://doi.org/10.5281/zenodo.13928832)


---

## Tracking of mitochondria and capturing mitoflashes

Leonid Kostrykin, Diana Chiang Jurado

Published 2024-11-20

Licensed CC-BY-4.0



Tags: Bioinformatics, Bioimage Analysis

Content type: Workflow, Tutorial

[https://training.galaxyproject.org/training-material/topics/imaging/tutorials/detection-of-mitoflashes/tutorial.html#tracking-of-mitochondria-and-capturing-mitoflashes](https://training.galaxyproject.org/training-material/topics/imaging/tutorials/detection-of-mitoflashes/tutorial.html#tracking-of-mitochondria-and-capturing-mitoflashes)


---

## Train-the-Trainer Concept on Research Data Management

Katarzyna Biernacka, Maik Bierwirth, Petra Buchholz, Dominika Dolzycka, Kerstin Helbig, Janna Neumann, Carolin Odebrecht, Cord Wiljes, Ulrike Wuttke

Published 2020-11-04

Licensed CC-BY-4.0



Within the project FDMentor, a German Train-the-Trainer Programme on Research Data Management (RDM) was developed and piloted in a series of workshops. The topics cover many aspects of research data management, such as data management plans and the publication of research data, as well as didactic units on learning concepts, workshop design and a range of didactic methods.

After the end of the project, the concept was supplemented and updated by members of the Sub-Working Group Training/Further Education (UAG Schulungen/Fortbildungen) of the DINI/nestor Working Group Research Data (DINI/nestor-AG Forschungsdaten). The newly published English version of the Train-the-Trainer Concept contains the translated concept, the materials and all methods of the Train-the-Trainer Programme. Furthermore, additional English references and materials complement this version.

Tags: Research Data Management

Content type: Book

[https://zenodo.org/record/4071471](https://zenodo.org/record/4071471)

[https://doi.org/10.5281/zenodo.4071471](https://doi.org/10.5281/zenodo.4071471)


---

## Training Computational Skills in the Age of AI

Robert Haase

Published 2024-11-06

Licensed CC-BY-4.0



Artificial intelligence (AI) and large language models (LLMs) are changing the way we use computers in science. This slide deck introduces ways for using AI and LLMs for making training materials and for exchanging knowledge about how to use AI in joint discussions between humans and LLM-based AI-systems.

[https://zenodo.org/records/14043615](https://zenodo.org/records/14043615)

[https://doi.org/10.5281/zenodo.14043615](https://doi.org/10.5281/zenodo.14043615)


---

## TrendsInMicroscopy2025

Marcelo Zoccoler, Johannes Soltwedel

Published 2025-03-10T13:42:57+00:00

Licensed CC-BY-4.0



Course contents for biapol course at Trends in Microscopy conference 2025

Tags: Bioimage Analysis

Content type: Github Repository

[https://biapol.github.io/TrendsInMicroscopy_2025/](https://biapol.github.io/TrendsInMicroscopy_2025/)

[https://github.com/BiAPoL/TrendsInMicroscopy_2025](https://github.com/BiAPoL/TrendsInMicroscopy_2025)


---

## Using Glittr.org to find, compare and re-use online training materials

Geert van Geest, Yann Haefliger, Monique Zahn-Zabal, Patricia M. Palagi

Licensed CC-BY-4.0



Glittr.org is a platform that aggregates and indexes training materials on computational life sciences from public git repositories, making it easier for users to find, compare, and analyze these resources based on various metrics. By providing insights into the availability of materials, collaboration patterns, and licensing practices, Glittr.org supports adherence to the FAIR principles, benefiting the broader life sciences community.

Tags: Bioimage Analysis, Research Data Management

Content type: Publication, Preprint

[https://www.biorxiv.org/content/10.1101/2024.08.20.608021v1](https://www.biorxiv.org/content/10.1101/2024.08.20.608021v1)


---

## Welcome to BioImage Town

Josh Moore

Licensed CC-BY-4.0



Welcome at NFDI4BIOIMAGE All-Hands Meeting in Düsseldorf, Germany, October 16, 2023

Tags: OMERO, Bioimage Analysis, Nfdi4Bioimage

Content type: Slides

[https://zenodo.org/doi/10.5281/zenodo.10008464](https://zenodo.org/doi/10.5281/zenodo.10008464)


---

## What is Open Data?

Daniel Dietrich, Jonathan Gray, Tim McNamara, Antti Poikola, Rufus Pollock, et al.

Licensed CC-BY-4.0



This handbook is about open data but what exactly is it? In particular what makes open data open, and what sorts of data are we talking about?

Tags: Open Science

Content type: Collection

[http://opendatahandbook.org/guide/en/what-is-open-data/](http://opendatahandbook.org/guide/en/what-is-open-data/)


---

## Who you gonna call? - Data Stewards to the rescue

Vanessa Aphaia Fiona Fuchs, Jens Wendt, Maximilian Müller, Mohsen Ahmadi, Riccardo Massei, Cornelia Wetzker

Published 2024-03-01

Licensed CC-BY-4.0



The Data Steward Team of the NFDI4BIOIMAGE consortium presents themselves and the services (including the Helpdesk) that we offer.

[https://zenodo.org/records/10730424](https://zenodo.org/records/10730424)

[https://doi.org/10.5281/zenodo.10730424](https://doi.org/10.5281/zenodo.10730424)


---

## Workflow for user introduction into microscopy, OMERO and data management at Center for Advanced imaging

Ksenia Krooß, Fuchs, Vanessa Aphaia Fiona, Tom Boissonnet, Stefanie Weidtkamp-Peters

Published 2025-03-07

Licensed CC-BY-4.0



At the Center for Advanced Imaging (CAi) at the Heinrich Heine University D&uuml;sseldorf, Germany, we have established a workflow to guide users through all aspects of bioimaging. The process begins with an initial consultation with our imaging specialists regarding microscopy techniques for their specific project. Users then receive training in microscope operation, ensuring they can handle the equipment effectively. If needed, our specialists also provide support in image analysis. Next, we introduce users to OMERO, highlighting its features and the advantages of using a bioimage data management system. They are then trained to structure and annotate their data within OMERO according to the Recommended Metadata for Biological Images (REMBI), taking their specific research topics into account. As users prepare for data publication, we assist with data organization and repository uploads. Our goal is to educate researchers in managing bioimage data&nbsp;throughout its entire lifecycle, with a strong emphasis on the FAIR (findable, accessible, interoperable, reusable) principles.

[https://zenodo.org/records/14988921](https://zenodo.org/records/14988921)

[https://doi.org/10.5281/zenodo.14988921](https://doi.org/10.5281/zenodo.14988921)


---

## Working Group Charter. RDM Helpdesk Network

Judith Engel, Patrick Helling, Robert Herrenbrück, MarinaLemaire, Hela Mehrtens, Marcus Schmidt, Martha Stellmacher, Lukas Weimer, Cord Wiljes, Wolf Zinke

Published 2024-11-04

Licensed CC-BY-4.0



Support is an essential component of an efficient infrastructure for research data management (RDM). Helpdesks guide researchers through this complex landscape and provide reliable support about all questions regarding research data management, including support for technical services, best practices, requirements of funding organizations and legal topics. In NFDI, most consortia have already established or are planning to establish helpdesks to support their specific communities. On a local level, many institutions have set up RDM helpdesks that provide support for the researchers of their own institution. Additional RDM support services are offered by RDM federal state initiatives, by research data centers, by specialist libraries, by the EOSC, and by providers of RDM-relevant tools. Helpdesks cover a wide range of institutions, disciplines, topics, methodologies and target audiences. However, the individual helpdesks are not yet interconnected and therefore cannot complement one another in an efficient way: Given the wide and constantly increasing complexity of RDM, no single helpdesk can provide the expertise for all potential support requests. Therefore, we see great potential in combining the efforts and resources of the existing RDM helpdesks into an efficient and comprehensive national RDM support network in order to provide optimal and tailored RDM support to all researchers and research-related institutions in Germany and in an international context.

[https://zenodo.org/records/14035822](https://zenodo.org/records/14035822)

[https://doi.org/10.5281/zenodo.14035822](https://doi.org/10.5281/zenodo.14035822)


---

## Zeiss AxioZoom Stage Adapter

Michael Gerlach

Published 2024-06-20

Licensed CC-BY-4.0



A 3D- printable microscope stage adapter for the reproducible accomodation of samples at a Zeiss AxioZoom stereomicroscope.
4 cylindrical anchors are fixed to the glass plate of the stage. The stage adapter is reversibly placed on these anchors.
&nbsp;

[https://zenodo.org/records/7963020](https://zenodo.org/records/7963020)

[https://doi.org/10.5281/zenodo.7963020](https://doi.org/10.5281/zenodo.7963020)


---

## Zeiss AxioZoom Stage Adapter - 12/6Well Plate

Michael Gerlach

Published 2024-06-20

Licensed CC-BY-4.0



A 3D- printable microscope stage adapter for the reproducible accomodation of 6 or 12-well plates at a Zeiss AxioZoom microscope.
4 cylindrical anchors are fixed to the glass plate of the stage. The stage adapter is reversibly placed on these anchors and acommodates a standard Greiner 6- or 12-well plate.

[https://zenodo.org/records/7944877](https://zenodo.org/records/7944877)

[https://doi.org/10.5281/zenodo.7944877](https://doi.org/10.5281/zenodo.7944877)


---

## Zeiss AxioZoom Stage Adapter - EM block holder

Michael Gerlach

Published 2024-06-20

Licensed CC-BY-4.0



A 3D- printable microscope stage adapter for the reproducible accomodation of EM Blocks at a Zeiss AxioZoom microscope.

4 cylindrical anchors are fixed to the glass plate of the stage. The stage adapter is reversibly placed on these anchors and acommodates 70 standard resin EM blocks.

[https://zenodo.org/records/7963006](https://zenodo.org/records/7963006)

[https://doi.org/10.5281/zenodo.7963006](https://doi.org/10.5281/zenodo.7963006)


---

## Zeiss AxioZoom Stage Adapter - Microscope slides

Michael Gerlach

Published 2024-06-21

Licensed CC-BY-4.0



A 3D- printable microscope stage adapter for the reproducible accomodation of microscopic slides at a Zeiss AxioZoom microscope.
4 cylindrical anchors are fixed to the glass plate of the stage. The stage adapter is reversibly placed on these anchors and acommodates 4 standard glass slides.

[https://zenodo.org/records/7945018](https://zenodo.org/records/7945018)

[https://doi.org/10.5281/zenodo.7945018](https://doi.org/10.5281/zenodo.7945018)


---

## [BINA CC] Scalable strategies for a next-generation of FAIR bioimaging

Josh Moore

Published 2024-09-24

Licensed CC-BY-4.0



Presented at https://www.bioimagingnorthamerica.org/events/bina-2024-community-congress/

[https://zenodo.org/records/13831274](https://zenodo.org/records/13831274)

[https://doi.org/10.5281/zenodo.13831274](https://doi.org/10.5281/zenodo.13831274)


---

## [CIDAS] Scalable strategies for a next-generation of FAIR bioimaging

Josh Moore

Published 2025-01-23

Licensed CC-BY-4.0



Talk given at Georg-August-Universit&auml;t G&ouml;ttingen Campus Institute Data Science23rd January 2025
https://www.uni-goettingen.de/en/653203.html

[https://zenodo.org/records/14845059](https://zenodo.org/records/14845059)

[https://doi.org/10.5281/zenodo.14845059](https://doi.org/10.5281/zenodo.14845059)


---

## [CMCB] Scalable strategies for a next-generation of FAIR bioimaging

Josh Moore

Published 2025-01-16

Licensed CC-BY-4.0



CMCB LIFE SCIENCES SEMINARSTechnische Universit&auml;t Dresden16th January 2025
https://tu-dresden.de/cmcb/crtd/news-termine/termine/cmcb-life-sciences-seminar-josh-moore-german-bioimaging-e-v-society-for-microscopy-and-image-analysis-constance
&nbsp;

Tags: Nfdi4Bioimage

[https://zenodo.org/records/14650434](https://zenodo.org/records/14650434)

[https://doi.org/10.5281/zenodo.14650434](https://doi.org/10.5281/zenodo.14650434)


---

## [CORDI 2023] Zarr: A Cloud-Optimized Storage for Interactive Access of Large Arrays

Josh Moore

Licensed CC-BY-4.0



For decades, the sharing of large N-dimensional datasets has posed issues across multiple domains. Interactively accessing terabyte-scale data has previously required significant server resources to properly prepare cropped or down-sampled representations on the fly. Now, a cloud-native chunked format easing this burden has been adopted in the bioimaging domain for standardization. The format — Zarr — is potentially of interest for other consortia and sections of NFDI.

Tags: Research Data Management, Bioimage Analysis, Data Science

Content type: Poster

[https://zenodo.org/doi/10.5281/zenodo.8340247](https://zenodo.org/doi/10.5281/zenodo.8340247)


---

## [Community Meeting 2024] Overview Team Image Data Analysis and Management

Susanne Kunis, Thomas Zobel

Published 2024-03-08

Licensed CC-BY-4.0



Overview of Activities of the Team Image Data Analysis and Management of German BioImaging e.V.
&nbsp;

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/10796364](https://zenodo.org/records/10796364)

[https://doi.org/10.5281/zenodo.10796364](https://doi.org/10.5281/zenodo.10796364)


---

## [Community Meeting 2024] Supporting and financing RDM projects within GerBI

Stefanie Weidtkamp-Peters, Josh Moore, Christian Schmidt, Roland Nitschke, Susanne Kunis, Thomas Zobel

Published 2024-03-28

Licensed CC-BY-4.0



Overview of GerBI RDM projects: why and how?

[https://zenodo.org/records/10889694](https://zenodo.org/records/10889694)

[https://doi.org/10.5281/zenodo.10889694](https://doi.org/10.5281/zenodo.10889694)


---

## [ELMI 2024]  AI's Dirty Little Secret: Without
FAIR Data, It's Just Fancy Math

Josh Moore, Susanne Kunis

Published 2024-05-21

Licensed CC-BY-4.0



Poster presented at the European Light Microscopy Initiative meeting in Liverpool (https://www.elmi2024.org/)

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/11235513](https://zenodo.org/records/11235513)

[https://doi.org/10.5281/zenodo.11235513](https://doi.org/10.5281/zenodo.11235513)


---

## [ELMI 2024] AI's Dirty Little Secret: Without FAIR Data, It's Just Fancy Math

Josh Moore, Susanne Kunis

Licensed CC-BY-4.0



Poster presented at the European Light Microscopy Initiative meeting in Liverpool (https://www.elmi2024.org/)

Tags: Research Data Management, FAIR-Principles, Bioimage Analysis, Nfdi4Bioimage

Content type: Poster

[https://zenodo.org/doi/10.5281/zenodo.11235512](https://zenodo.org/doi/10.5281/zenodo.11235512)


---

## [GBI EOE VII] Five (or ten) must-have items for making IT infrastructure for managing bioimage data

Josh Moore

Published 2024-05-26

Licensed CC-BY-4.0



Presentation made to the GBI Image Data Management Working Group during the 7th Exchange of Experience in Uruguay.

[https://zenodo.org/records/11318151](https://zenodo.org/records/11318151)

[https://doi.org/10.5281/zenodo.11318151](https://doi.org/10.5281/zenodo.11318151)


---

## [GBI EoE IX] NFDI4BIOIMAGE
National Research Data Infrastructure 
for Microscopy and BioImage Analysis

Josh Moore

Published 2024-10-29

Licensed CC-BY-4.0



Presented at https://globalbioimaging.org/exchange-of-experience/exchange-of-experience-ix in Okazaki, Japan.

[https://zenodo.org/records/14001388](https://zenodo.org/records/14001388)

[https://doi.org/10.5281/zenodo.14001388](https://doi.org/10.5281/zenodo.14001388)


---

## [I2K] Scalable strategies for a next-generation of FAIR bioimaging

Josh Moore

Published 2024-10-25

Licensed CC-BY-4.0



or, "OME-Zarr: 'even a talk on formats [can be] interesting'"
Presented at https://events.humantechnopole.it/event/1/

[https://zenodo.org/records/13991322](https://zenodo.org/records/13991322)

[https://doi.org/10.5281/zenodo.13991322](https://doi.org/10.5281/zenodo.13991322)


---

## [N4BI AHM] Welcome to BioImage Town

Josh Moore

Published 2023-10-16

Licensed CC-BY-4.0



Keynote at the NFDI4BIOIMAGE All-Hands Meeting in Düsseldorf, Germany, October 16, 2023.

[https://zenodo.org/records/15031842](https://zenodo.org/records/15031842)

[https://doi.org/10.5281/zenodo.15031842](https://doi.org/10.5281/zenodo.15031842)


---

## [SWAT4HCLS 2023] NFDI4BIOIMAGE: Perspective for a national bioimage standard

Josh Moore, Susanne Kunis

Licensed CC-BY-4.0



Poster presented at Semantic Web Applications and Tools for Health Care and Life Sciences (SWAT4HCLS 2023), Feb 13--16, 2023, Basel, Switzerland. NFDI4BIOIMAGE is a newly established German consortium dedicated to the FAIR representation of biological imaging data. A key deliverable is the definition of a semantically-compatible FAIR image object integrating RDF metadata with web-compatible storage of large n-dimensional binary data in OME-Zarr. We invite feedback from and collaboration with other endeavors during the soon-to-begin 5 year funding period.

Tags: Research Data Management, FAIR-Principles, Nfdi4Bioimage

Content type: Poster

[https://zenodo.org/doi/10.5281/zenodo.7928332](https://zenodo.org/doi/10.5281/zenodo.7928332)


---

## [Short Talk] NFDI4BIOIMAGE - A consortium in the National Research Data Infrastructure

Christian Schmidt

Published 2024-04-10

Licensed CC-BY-4.0



Short Talk about the NFDI4BIOIMAGE consortium presented at the RDM in (Bio-)Medicine Information Event on April 10th, 2024, organized C&sup3;RDM &amp; ZB MED.

[https://zenodo.org/records/10939520](https://zenodo.org/records/10939520)

[https://doi.org/10.5281/zenodo.10939520](https://doi.org/10.5281/zenodo.10939520)


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

## ilastik: interactive machine learning for (bio)image analysis

Anna Kreshuk, Dominik Kutra

Licensed CC-BY-4.0



Tags: Artificial Intelligence, Bioimage Analysis

Content type: Slides

[https://zenodo.org/doi/10.5281/zenodo.4330625](https://zenodo.org/doi/10.5281/zenodo.4330625)


---

## imaris file not read by bfGetReader()

Julien Dubrulle

Published 2025-03-10

Licensed CC-BY-4.0



This file cannot be read by bfGetReader() v8.1.1 on a Windows operating workstation.

[https://zenodo.org/records/15001649](https://zenodo.org/records/15001649)

[https://doi.org/10.5281/zenodo.15001649](https://doi.org/10.5281/zenodo.15001649)


---

## introduction-to-generative-ai

Bruna Piereck, Alexander Botzki

Published 2024-09-27T14:38:51+00:00

Licensed CC-BY-4.0



Course repository for Strategic Use of Generative AI

Tags: Artificial Intelligence

Content type: Github Repository, Tutorial

[https://github.com/vibbits/introduction-to-generative-ai](https://github.com/vibbits/introduction-to-generative-ai)

[https://liascript.github.io/course/?https://raw.githubusercontent.com/vibbits/introduction-to-generative-ai/refs/heads/main/README.md](https://liascript.github.io/course/?https://raw.githubusercontent.com/vibbits/introduction-to-generative-ai/refs/heads/main/README.md)


---

## nextflow-workshop

Tuur Muyldermans, Kris Davie, Alexander, Nicolas Vannieuwkerke, Kobe Lavaerts, Marcel Ribeiro-Dantas, Bruna Piereck, Steff Taelman

Published 2023-03-29T10:40:04+00:00

Licensed CC-BY-4.0



Nextflow workshop materials March 2023

Tags: Workflow, Nextflow

Content type: Github Repository, Tutorial

[https://github.com/vibbits/nextflow-workshop](https://github.com/vibbits/nextflow-workshop)

[https://liascript.github.io/course/?https://raw.githubusercontent.com/vibbits/nextflow-workshop/main/README.md#1](https://liascript.github.io/course/?https://raw.githubusercontent.com/vibbits/nextflow-workshop/main/README.md#1)


---

## re3data.org - registry of Research Data Repositories

Licensed CC-BY-4.0



Re3data is a global registry of research data repositories that covers research data repositories from different academic disciplines. It includes repositories that enable permanent storage of and access to data sets to researchers, funding bodies, publishers, and scholarly institutions.

Tags: Research Data Management

Content type: Website

[https://www.re3data.org/](https://www.re3data.org/)


---

## scikit-learn MOOC

Loïc Estève et al.

Licensed CC-BY-4.0



Machine learning in Python with scikit-learn MOOC

Tags: Bioimage Analysis, Machine Learning

Content type: Github Repository

[https://github.com/INRIA/scikit-learn-mooc](https://github.com/INRIA/scikit-learn-mooc)


---

## training-resources

Christian Tischer, Antonio Politi, Toby Hodges, maulakhan, grinic, bugraoezdemir, Tim-Oliver Buchholz, Elnaz Fazeli, Aliaksandr Halavatyi, Dominik Kutra, Stefania Marcotti, AnniekStok, Felix, jhennies, Severina Klaus, Martin Schorb, Nima Vakili, Sebastian Gonzalez Tirado, Stefan Helfrich, Yi Sun, Ziqiang Huang, Jan Eglinger, Constantin Pape, Joel Lüthi, Matt McCormick, Oane Gros

Published 2020-04-23T07:51:38+00:00

Licensed CC-BY-4.0



Resources for teaching/preparing to teach bioimage analysis

Tags: Bioimageanalysis, Neurobias

Content type: Github Repository

[https://github.com/NEUBIAS/training-resources](https://github.com/NEUBIAS/training-resources)


---

