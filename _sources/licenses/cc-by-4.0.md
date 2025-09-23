# Cc-by-4.0 (410)
## "Management of Microscopy Image Data: An overview of OMERO, BioImage Archive and Image Data Resource"  2025 @ Uni Leipzig

Vellutini, Bruno C., Cuenca, Marina B., Abhijeet Krishna, Alicja Szałapak, Modes, Carl D., Pavel Tomančák

Published 2025-08-15

Licensed CC-BY-4.0



Presentation matherial from the course "Management of Microscopy Image Data: An Overview of OMERO, BioImage Archive and Image Data Resource"&nbsp;helded in Uni Leipzig on the 04/07/2025.
This course is part of the RDM lecture series organized by&nbsp;Dr. Dr. habil. Dagmar Quandt.
Link to the event:
https://fortbildung.uni-leipzig.de/fortbildung.html?id=2436
M. Massei is funded by the Deutsche Forschungsgemeinschaft (DFG) &ndash; project number [NFDI46/1] - 501864659

Tags: Include In Dalia

[https://zenodo.org/records/16880913](https://zenodo.org/records/16880913)

[https://doi.org/10.5281/zenodo.16880913](https://doi.org/10.5281/zenodo.16880913)


---

## "ZENODO und Co." Was bringt und wer braucht ein Repositorium?

Elfi Hesse, Jan-Christoph Deinert, Christian Löschen

Published 2021-01-25

Licensed CC-BY-4.0



Die Online-Veranstaltung fand am 21.01.2021 im Rahmen der SaxFDM-Veranstaltungsreihe &quot;Digital Kitchen - K&uuml;chengespr&auml;che mit SaxFDM&quot; statt. SaxFDM-Sprecherin Elfi Hesse (HTW Dresden) erl&auml;uterte zun&auml;chst Grunds&auml;tzliches zum Thema Repositorien. Anschlie&szlig;end teilten Nutzer (Jan Deinert &ndash; HZDR) und Anbieter (Christian L&ouml;schen &ndash; TU Dresden/ZIH) lokaler Repositorien ihre Erfahrungen mit uns.

Tags: Research Data Management, Include In Dalia

Content type: Slides

[https://zenodo.org/records/4461261](https://zenodo.org/records/4461261)

[https://doi.org/10.5281/zenodo.4461261](https://doi.org/10.5281/zenodo.4461261)


---

## .lif files misbehaving in fiji but fine in LASX

Pamela Young

Published 2025-05-07

Licensed CC-BY-4.0



.lif files misbehaving in fiji but fine in LASX.&nbsp; This data opens fine in LASX but FIJI only likes some of the files.&nbsp; I think it was captured during a poweroutage so may have lived on a temp drive and been recovered when the power came back.&nbsp; LASX uses the .lifext but I don't think FIJI does.&nbsp; I have included it however since it is part of the dataset output from the microscope.

Tags: Exclude From Dalia

[https://zenodo.org/records/15353569](https://zenodo.org/records/15353569)

[https://doi.org/10.5281/zenodo.15353569](https://doi.org/10.5281/zenodo.15353569)


---

## 10 frames of fluorescent particles

Zach Marin, Maohan Su

Published 2024-12-05

Licensed CC-BY-4.0



10 frames of fluorescent particles. They don't do much, but they are a DCIMG version 0x7 file example.

Tags: Exclude From Dalia

[https://zenodo.org/records/14281237](https://zenodo.org/records/14281237)

[https://doi.org/10.5281/zenodo.14281237](https://doi.org/10.5281/zenodo.14281237)


---

## 3D Ground Truth Annotations of Nuclei in 3D Microscopy Volumes

Alain Chen, Liming Wu, Seth Winfree, Kenneth Dunn, Paul Salama, Edward Delp, Teresa Zulueta-Coarasa

Published 2024-12-20

Licensed CC-BY-4.0



This submission contains a set of 3D microscopy volumes of cell nuclei from different species and tissues that have been manually segmented. We also provide synthetically generated 3D microscopy volumes that can be used for training segmentation methods.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://www.ebi.ac.uk/bioimage-archive/galleries/ai/analysed-dataset/S-BIAD1518/](https://www.ebi.ac.uk/bioimage-archive/galleries/ai/analysed-dataset/S-BIAD1518/)


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

Tags: Exclude From Dalia

[https://zenodo.org/records/6645978](https://zenodo.org/records/6645978)

[https://doi.org/10.5281/zenodo.6645978](https://doi.org/10.5281/zenodo.6645978)


---

## 3D light-sheet microscopy data for SELMA3D 2024 challenge - Training subset with annotations

Ying Chen, Johannes C. Paetzold, Ali Erturk, Doris Kaltenecker, Mihail Todorov, Harsharan Singh Bhatia, Shan Zhao, Luciano Höher

Published 2024-06-05

Licensed CC-BY-4.0



This dataset is the training set with annotations for the SELMA3D challenge. The SELMA3D challenge focuses on self-supervised learning for 3D light-sheet microscopy image segmentation. Its objective is to encourage the development of self-supervised learning methods for general segmentation of various structures in 3D light-sheet microscopy images. The dataset comtains 3D image patches of different labeled biological structures in the brain, including blood vessels, c-Fos labeled brain cells involved in neural activity, cell nuclei, and Alzheimers disease plaques. Each patch includes corresponding pixel-wise annotations for the labeled structures.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://www.ebi.ac.uk/bioimage-archive/galleries/ai/analysed-dataset/S-BIAD1196/](https://www.ebi.ac.uk/bioimage-archive/galleries/ai/analysed-dataset/S-BIAD1196/)


---

## 3D nuclei instance segmentation dataset of fluorescence microscopy volumes of C. elegans

Fuhui Long, Hanchuan Peng, Xiao Liu, Stuart K Kim, Eugene Myers, Dagmar Kainmüller, Martin Weigert

Published 2022-02-01

Licensed CC-BY-4.0



The dataset consists of 28 confocal microscopy volumes of C. elegans worms at the L1 stage and&nbsp; corresponding stacks of densely annotated nuclei instance segmentation masks.

* 28 raw images and corresponding masks of average dimension (xyz) 1050 x 140 x 140
* Pixelsize (xyz): 0.116 x 0.116 x 0.122&mu;m
* Microscope: Leica confocal microscopy, 63x oil objective


The original raw data and preliminary annotations were&nbsp; part of the following publication (please cite if you use the dataset):
&nbsp;
Long, F., Peng, H., Liu, X., Kim, S. K., &amp; Myers, E. (2009). A 3D digital atlas of C. elegans and its application to single-cell analyses. Nature methods, 6(9), 667-672.

The nuclei annotation masks were further manually curated by Dagmar Kainmueller (MDC Berlin) for the following publication:

Hirsch, P., &amp; Kainmueller, D. (2020). An auxiliary task for learning nuclei segmentation in 3d microscopy images. In&nbsp;Medical Imaging with Deep Learning&nbsp;(pp. 304-321). PMLR.

We provide the dataset already structured into the train/validation/test split as used by the above as well as the following publications:&nbsp;

Weigert, M., Schmidt, U., Haase, R., Sugawara, K., &amp; Myers, G. (2020). Star-convex polyhedra for 3d object detection and segmentation in microscopy. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (pp. 3666-3673).
&nbsp;

&nbsp;

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/5942575](https://zenodo.org/records/5942575)

[https://doi.org/10.5281/zenodo.5942575](https://doi.org/10.5281/zenodo.5942575)


---

## 6 Steps Towards Reproducible Research

Heidi Seibold

Licensed CC-BY-4.0



A short book with 6 steps that get you closer to making your work reproducible.

Tags: Reproducibility, Research Data Management, Include In Dalia

Content type: Book

[https://zenodo.org/records/12744715](https://zenodo.org/records/12744715)

[https://doi.org/10.5281/zenodo.12744715](https://doi.org/10.5281/zenodo.12744715)


---

## A Cloud-Optimized Storage for Interactive Access of Large Arrays

Josh Moore, Susanne Kunis

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

Content type: Publication, Conference Abstract

[https://doi.org/10.52825/cordi.v1i.285](https://doi.org/10.52825/cordi.v1i.285)


---

## A Glimpse of the Open-Source FLIM Analysis Software Tools FLIMfit, FLUTE and napari-flim-phasor-plotter

Anca Margineanu, Chiara Stringari, Marcelo Zoccoler, Cornelia Wetzker

Published 2024-03-27

Licensed CC-BY-4.0



The presentations introduce open-source software to read in, visualize and analyse fluorescence lifetime imaging microscopy (FLIM) raw data developed for life scientists. The slides were presented at German Bioimaging (GerBI) FLIM Workshop held February 26 to 29 2024 at the Biomedical Center of LMU M&uuml;nchen by Anca Margineanu, Chiara Stringari and Conni Wetzker.&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/10886750](https://zenodo.org/records/10886750)

[https://doi.org/10.5281/zenodo.10886750](https://doi.org/10.5281/zenodo.10886750)


---

## A Hitchhiker's guide through the bio-image analysis software universe

Robert Haase, Elnaz Fazeli, David Legland, Michael Doube, Siân Culley, Ilya Belevich, Eija Jokitalo, Martin Schorb, Anna Klemm, Christian Tischer

Licensed CC-BY-4.0



This article gives an overview about commonly used bioimage analysis software and which aspects to consider when choosing a software for a specific project.

Tags: Bioimage Analysis, Include In Dalia

Content type: Publication

[https://febs.onlinelibrary.wiley.com/doi/full/10.1002/1873-3468.14451](https://febs.onlinelibrary.wiley.com/doi/full/10.1002/1873-3468.14451)


---

## A Perspective on FAIR and Scalable Access to Large Image Data

Julia Thönnißen, Sarah Oliveira, Alexander Oberstrass, Jan-Oliver Kropp, Xiao Gui, Christian Schiffer, Timo Dickscheid

Published 2025-08-04

Licensed CC-BY-4.0



The rapid development of new imaging technologies across scientific domains–especially high-throughput technologies–results in a growing volume of image datasets in the Tera- to Petabyte scale. Efficient visualization and analysis of such massive image resources is critical but remains challenging due to the sheer size of the data, its continuous growth, and the limitations of conventional software tools to address these problems. Tools for visualization, annotation and analysis of large image data are confronted with the fundamental dilemma of balancing computational efficiency and memory requirements. Many tools are unable to process large datasets due to memory constraints, requiring workarounds like downsampling. On the other hand, solutions that can handle large data efficiently often rely on specialized or even proprietary file formats, limiting interoperability with other software. This reflects diverging requirements: storage favours compression for efficiency, analysis demands fast data access, and visualization requires tiled, multi-resolution representations. Lacking a unified approach for these conflicting needs, the operation of large and dynamically evolving image repositories in practice often requires undesirable data conversions and costly data duplication. In addressing these challenges, the bioimaging community increasingly adheres to the FAIR principles [1] through national and international initiatives [2], [3], [4]. For example, the Open Microscopy Environment (OME) fosters standards such as OME-TIFF [5] and its cloud-native successor OME-NGFF [6]; BioFormats [7] and OMERO [8] facilitate metadata-rich data handling across diverse platforms; and BrAinPI [9] provides web-based visualization of images via Neuroglancer [10]. These tools represent important developments towards more efficient and standardized use of bioimaging data. However, for very large and dynamically growing repositories, it is still not feasible to settle on a single standard for a subset of these tools, in particular in the light of very diverging needs for massively parallel processing on HPC systems. Therefore, converting data to a single target format is often not a practical solution. We propose a concept for a modular image delivery service which acts as a middleware between large image data resources and applications, serving image data from a cloud resource in multiple requested representations on demand. The service allows reading data stored in different input file formats, applying coordinate transformations and filtering operations on-the-fly, and serving the results in a range of different output formats and layouts. Building upon a common framework for reading and transforming data, an extensible set of access points connects the service to client applications: Lightweight REST APIs allow web-based mutli-resolution access (e.g., in common formats such as used in Neuroglancer and OpenSeadragon base viewers); mountable filesystem interfaces enable linking the repository to file-oriented solutions (e.g., OMERO, ImageJ); and programmatic access from customizable software tools (e.g., Napari). To provide compatibility with upcoming image data standards like BIDS [11] and minimize conversion efforts, the service is able to dynamically expose standard-conform views into arbitrarily organized datasets. The proposed approach for reading and transforming data on-the-fly eliminates the need for redundant storage and application-specific conversions of datasets, improving workflow efficiency and sustainability. In summary, we advocate for the development of a flexible and extensible image data service that supports large-scale analysis, dynamic transformations, multi-tool interoperability, and compatibility with community standards for large image datasets. This way it supports the FAIR principles, reduces integration barriers, meets the performance demands of modern imaging research, and still fosters the use of existing community developments.

Tags: Include In Dalia

[https://zenodo.org/records/16736220](https://zenodo.org/records/16736220)

[https://doi.org/10.5281/zenodo.16736220](https://doi.org/10.5281/zenodo.16736220)


---

## A deep learning approach to quantify auditory hair cells

Maurizio Cortada, Loïc Sauteur, Michael Lanz, Soledad Levano, Daniel Bodmer

Published 2021-03-09

Licensed CC-BY-4.0



StarDist 2D deep learning model and training dataset.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/4590066](https://zenodo.org/records/4590066)

[https://doi.org/10.5281/zenodo.4590066](https://doi.org/10.5281/zenodo.4590066)


---

## A journey to FAIR microscopy data

Stefanie Weidtkamp-Peters, Janina Hanne, Christian Schmidt

Published 2023-05-03

Licensed CC-BY-4.0



Oral presentation, 32nd MoMAN &quot;From Molecules to Man&quot; Seminar, Ulm, online. Monday February 6th, 2023

Abstract:

Research data management is essential in nowadays research, and one of the big opportunities to accelerate collaborative and innovative scientific projects. To achieve this goal, all our data needs to be FAIR (findable, accessible, interoperable, reproducible). For data acquired on microscopes, however, a common ground for FAIR data sharing is still to be established. Plenty of work on file formats, data bases, and training needs to be performed to highlight the value of data sharing and exploit its potential for bioimaging data.

In this presentation, Stefanie Weidtkamp-Peters will introduce the challenges for bioimaging data management, and the necessary steps to achieve data FAIRification. German BioImaging - GMB e.V., together with other institutions, contributes to this endeavor. Janina Hanne will present how the network of imaging core facilities, research groups and industry partners is key to the German bioimaging community&rsquo;s aligned collaboration toward FAIR bioimaging data. These activities have paved the way for two data management initiatives in Germany: I3D:bio (Information Infrastructure for BioImage Data) and NFDI4BIOIMAGE, a consortium of the National Research Data Infrastructure. Christian Schmidt will introduce the goals and measures of these initiatives to the benefit of imaging scientist&rsquo;s work and everyday practice. &nbsp;

Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

[https://zenodo.org/records/7890311](https://zenodo.org/records/7890311)

[https://doi.org/10.5281/zenodo.7890311](https://doi.org/10.5281/zenodo.7890311)


---

## A mihc mrxs example

Wang

Published 2025-08-27

Licensed CC-BY-4.0



Tags: Exclude From Dalia

[https://zenodo.org/records/16962727](https://zenodo.org/records/16962727)

[https://doi.org/10.5281/zenodo.16962727](https://doi.org/10.5281/zenodo.16962727)


---

## ABIC - Intermediate Fiji Image Analysis Course 2024

Rensu Petrus Theart

Licensed CC-BY-4.0



A structured beginner to intermediate-level course in image analysis using Fiji, developed for ABIC 2024.  It includes a video lecture playlist, course documentation, and participant image files.


Tags: Bioimage Analysis, Image Processing, Teaching Resource, Imagej, Exclude From Dalia

Content type: Workshop, Video, Document

[https://www.youtube.com/playlist?list=PL0RrV4sTNwh2S9Lb7d1TzJWPGgdw_YVnb](https://www.youtube.com/playlist?list=PL0RrV4sTNwh2S9Lb7d1TzJWPGgdw_YVnb)

[https://docs.google.com/document/d/1h-3oJDR7gd_y3tfgN3clPwt2O4g34QRPp_FJ4v2Q7kA/edit?usp=sharing](https://docs.google.com/document/d/1h-3oJDR7gd_y3tfgN3clPwt2O4g34QRPp_FJ4v2Q7kA/edit?usp=sharing)

[https://www.dropbox.com/scl/fi/7njq2wp680vubt6rwhn5f/ParticipantImages.zip?rlkey=pk3kttbsclk69ixxp1yv9j8p3&dl=0](https://www.dropbox.com/scl/fi/7njq2wp680vubt6rwhn5f/ParticipantImages.zip?rlkey=pk3kttbsclk69ixxp1yv9j8p3&dl=0)


---

## Abdominal Imaging Window (AIW) for Intravital Imaging

Michael Gerlach

Published 2024-11-15

Licensed CC-BY-4.0



This upload features a simple model for the creation (Manufacturing/Prototyping) of an abdominal imaging window (AIW) for use in mice intravital microscopy.
Manufacture in titanium for chronic implantation. Measures in mm.

Tags: Exclude From Dalia

[https://zenodo.org/records/14168603](https://zenodo.org/records/14168603)

[https://doi.org/10.5281/zenodo.14168603](https://doi.org/10.5281/zenodo.14168603)


---

## Aberrated Bead Stack

Zach Marin

Published 2024-12-03

Licensed CC-BY-4.0



Bead stack taken on lower path of a 4Pi without deformable mirror corrections. DCIMG examples, not for other purposes.

Tags: Exclude From Dalia

[https://zenodo.org/records/14268554](https://zenodo.org/records/14268554)

[https://doi.org/10.5281/zenodo.14268554](https://doi.org/10.5281/zenodo.14268554)


---

## Abstract - NFDI Basic Service for Data Management Plans

Licensed CC-BY-4.0



The NFDI Basic Service DMP4NFDI supports consortia in developing and providing data management plans (DMP) services for their community.

Tags: Research Data Management, Exclude From Dalia

Content type: Document

[https://base4nfdi.de/images/AbstractDMP4NFDI.pdf](https://base4nfdi.de/images/AbstractDMP4NFDI.pdf)


---

## Accessible Interactive Spatial-Omics Data Visualizations with Vitessce and OMERO

Bortolomeazzi Michele

Published 2025-06-30

Licensed CC-BY-4.0



OMERO is the most used research data management system (RDM) in the bioimaging domain, and has been adopted as a centralized RDM solution by several academic and research institutions. A main reason for this is the ability to directly view and annotate images from a web-based interface. However, this feature of OMERO is currently underpowered for the visualization of very large or multimodal datasets. These datasets, are becoming a more and more common foundation for biological and biomedical studies, due to the recent developments in imaging, and sequencing technologies which enabled their application to spatial-omics. In order to begin to provide this multimodal-data capability to OMERO, we developed omero-vitessce (https://github.com/NFDI4BIOIMAGE/omero-vitessce/tree/main), a new OMERO.web plugin for viewing data stored in OMERO with the Vitessce (http://vitessce.io/) multimodal data viewer. omero-vitessce can be installed as an OMERO.web plugin with PiPy (https://pypi.org/project/omero-vitessce/), and allows users to set up interactive visualizations of their images of cells and tissues through interactive plots which are directly linked to the image. This enables the visual exploration of bioimage-analysis results and of multimodal data such as those generated through spatial-omics experiments. The data visualization is highly customizable and can be configured not only through custom configuration files, but also with the graphical interface provided by the plugin, thus making omero-vitessce a highly user-friendly solution for multimodal data viewing. most biological datasets. We plan to extend the interoperability of omero-vitessce with the OME-NGFF and SpatialData file formats to leverage the efficiency of these cloud optimized formats.

Tags: Nfdi4Bioimage, OMERO, Include In Dalia

[https://zenodo.org/records/15771899](https://zenodo.org/records/15771899)

[https://doi.org/10.5281/zenodo.15771899](https://doi.org/10.5281/zenodo.15771899)


---

## Advancing FAIR Image Analysis in Galaxy: Tools, Workflows, and Training

Chiang Jurado, Diana, Riccardo Massei, Pavankumar Videm, Anup Kumar, Anne Fouilloux, Leonid Kostrykin, Beatriz Serrano-Solano, Björn Grüning

Published 2025-03-06

Licensed CC-BY-4.0



Tags: Include In Dalia

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

Tags: Research Data Management, Licensing, Include In Dalia

Content type: Slides

[https://zenodo.org/records/11472148](https://zenodo.org/records/11472148)

[https://doi.org/10.5281/zenodo.11472148](https://doi.org/10.5281/zenodo.11472148)


---

## An annotated high-content fluorescence microscopy dataset with Hoechst 33342-stained nuclei and manually labelled outlines

Malou Arvidsson, Salma Kazemi Rashed, Sonja Aits

Published 2022-06-17

Licensed CC-BY-4.0



Here we present a benchmarking dataset of fluorescence microscopy images with Hoechst 33342-stained nuclei together with annotations of nuclei, nuclear fragments and micronuclei. Images were randomly selected from an RNA interference screen with a modified U2OS osteosarcoma cell line, acquired on a Thermo Fischer CX7 high-content imaging system at 20x magnification. Labelling was performed by a single annotator and reviewed by a biomedical expert.

The dataset contains 50 images showing over 2000 labelled nuclear objects in total, which is sufficiently large to train well-performing neural networks for instance or semantic segmentation. It is pre-split into training, development and test set, each in a zip file. The dataset should be referred to as Aitslab_bioimaging1. A brief article describing the dataset is also available (Arvidsson M, Kazemi Rashed S, Aits S. 10.1016/j.dib.2022.108769 )

Dataset description:

Fluorescence microscopy images: original .C01 files and files converted to 8-bit .png format (Grayscale)

Annotations: 24-bit .png format (RGB)

Script used to convert C01 to png images:&nbsp;C01_to_png.py file with python code and readme.md file with instructions to run it

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/6657260](https://zenodo.org/records/6657260)

[https://doi.org/10.5281/zenodo.6657260](https://doi.org/10.5281/zenodo.6657260)


---

## An image-based data-driven analysis of cellular architecture in a developing tissue

Jonas Hartmann, Mie Wong, Elisa Gallo, Darren Gilmour

Published 2022-12-13

Licensed CC-BY-4.0



3D zebrafish embryo images with single-cell segmentation and point cloud-based morphometry

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://www.ebi.ac.uk/bioimage-archive/galleries/S-BIAD599-ai.html](https://www.ebi.ac.uk/bioimage-archive/galleries/S-BIAD599-ai.html)


---

## Angebote der NFDI für die Forschung im Bereich Zoologie

Birgitta König-Ries, Robert Haase, Daniel Nüst, Konrad Förstner, Judith Sophie Engel

Published 2024-12-04

Licensed CC-BY-4.0



In diesem Slidedeck geben wir einen Einblick in Angebote und Dienste der Nationalen Forschungsdaten Infrastruktur (NFDI), die Relevant f&uuml;r die Zoologie und angrenzende Disziplinen relevant sein k&ouml;nnten.

Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

[https://zenodo.org/records/14278058](https://zenodo.org/records/14278058)

[https://doi.org/10.5281/zenodo.14278058](https://doi.org/10.5281/zenodo.14278058)


---

## Artificial Blobs and Labels image

Romain

Published 2023-05-10

Licensed CC-BY-4.0



A groovy script to use in Fiji to generate artificial images and labels, with example images.

Tags: Exclude From Dalia

[https://zenodo.org/records/7919117](https://zenodo.org/records/7919117)

[https://doi.org/10.5281/zenodo.7919117](https://doi.org/10.5281/zenodo.7919117)


---

## Astigmatic 4Pi bead stack

Zach Marin, Maohan Su

Published 2024-12-06

Licensed CC-BY-4.0



Bead stack taken on a 4Pi. DCIMG 0x1000000 file with a 4-pixel correction requirement.

Tags: Exclude From Dalia

[https://zenodo.org/records/14287640](https://zenodo.org/records/14287640)

[https://doi.org/10.5281/zenodo.14287640](https://doi.org/10.5281/zenodo.14287640)


---

## Automatic labelling of HeLa "Kyoto" cells using Deep Learning tools

Romain Guiet

Published 2022-02-25

Licensed CC-BY-4.0



Name: Automatic labelling&nbsp;of HeLa &ldquo;Kyoto&rdquo; cells using Deep Learning tools

Data type: Microscopy images from the dataset &ldquo;HeLa &ldquo;Kyoto&rdquo; cells&nbsp;under the scope&rdquo;, Brightfield (BF), Digital Phase Contrast (DPC, either &ldquo;raw&rdquo; or &ldquo;square-rooted&rdquo;), Tubulin and H2B fluorescent channel, paired with their corresponding nuclei or cell/cyto label images.

Labels images: Labels images were generated using the script &ldquo;prepare_trainingDataset_cellpose.ijm&rdquo;.

Briefly, for 5 defined time-points (1,10,50,100,150), channels of interest were duplicated, resaved and :

-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; nuclei label images were obtained using StarDist on H2B channel

-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cell label images were obtained using Cellpose on Tubulin and H2B channels

A quick visual inspection of the resulting label images concluded that they were satisfying enough, despite certainly not being perfect.

Notes :

-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This labelling&nbsp;strategy:

o&nbsp;&nbsp; will not produce 100% accurate labels, but they might be more reproducible than labels generated by humans and are (definitely) much faster to obtain.

o&nbsp;&nbsp; is NOT a recommended way of generating labels images, but for educational purposes.

-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The fluorescent channels are part of the dataset to ease the process of review of the labels and are NOT used for training. We generated the labels from the fluorescent channels to later predict labels from the BF or DPC channels only. As such, the fluorescent channels should not be &ldquo;reused&rdquo; with our labels during training.

File format: .tif (16-bit)

Image size: 540x540 (Pixel size: 0.299 nm)

&nbsp;

NOTE: This dataset uses&nbsp;the &ldquo;HeLa &ldquo;Kyoto&rdquo; cells&nbsp;under the scope&rdquo; &nbsp;dataset (https://doi.org/10.5281/zenodo.6139958) to automatically generate annotations

NOTE: This dataset was used to train cellpose models in the following Zenodo entry&nbsp;https://doi.org/10.5281/zenodo.6140111

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/6140064](https://zenodo.org/records/6140064)

[https://doi.org/10.5281/zenodo.6140064](https://doi.org/10.5281/zenodo.6140064)


---

## BHG2023-OMERO-ARC

Andrea Schrader, Michele Bortolomeazzi, Niraj Kandpal, Torsten Stöter, Kevin Schneider, Peter Zentis, Josh Moore, Jeam-Marie Burel, Tom Boissonnet

Licensed CC-BY-4.0



Repository for documentation during the 2nd de.NBI BioHackathon Germany - 11.-15.12.2023 - OMERO-ARC project (in short: BHG2023-OMERO-ARC)

Tags: Nfdi4Bioimage, Bioinformatics, OMERO, Exclude From Dalia

Content type: Github Repository

[https://github.com/NFDI4BIOIMAGE/BHG2023-OMERO-ARC](https://github.com/NFDI4BIOIMAGE/BHG2023-OMERO-ARC)


---

## BIDS-lecture-2024

Robert Haase

Licensed CC-BY-4.0



Training resources for Students at Uni Leipzig who want to dive into bio-image data science with Python. The material developed here between April and July 2024.

Tags: Bioimage Analysis, Artificial Intelligence, Python, Exclude From Dalia

Content type: Github Repository

[https://github.com/ScaDS/BIDS-lecture-2024/](https://github.com/ScaDS/BIDS-lecture-2024/)


---

## BIOMERO - A scalable and extensible image analysis framework

Torec T. Luik, Rodrigo Rosas-Bertolini, Eric A.J. Reits, Ron A. Hoebe, Przemek M. Krawczyk

Published None

Licensed CC-BY-4.0



The authors introduce BIOMERO (bioimage analysis in OMERO), a bridge connecting OMERO, a renowned bioimaging data management platform, FAIR workflows, and high-performance computing (HPC) environments.

Tags: OMERO, Workflow, Bioimage Analysis, Exclude From Dalia

Content type: Publication

[https://doi.org/10.1016/j.patter.2024.101024](https://doi.org/10.1016/j.patter.2024.101024)


---

## Beads imaged over time

Zach Marin

Published 2025-04-04

Licensed CC-BY-4.0



DCIMG 0x1000000 images of beads over time (30 seconds, 0.03 s exposure).&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/15150937](https://zenodo.org/records/15150937)

[https://doi.org/10.5281/zenodo.15150937](https://doi.org/10.5281/zenodo.15150937)


---

## BigDataProcessor2: A free and open-source Fiji plugin for inspection and processing of TB sized image data

Christian Tischer, Ashis Ravindran, Sabine Reither, Nicolas Chiaruttini, Rainer Pepperkok, Nils Norlin

Licensed CC-BY-4.0



Tags: Research Data Management, Bioimage Analysis, Exclude From Dalia

Content type: Publication

[https://doi.org/10.1093/bioinformatics/btab106](https://doi.org/10.1093/bioinformatics/btab106)


---

## Bio-Image Data Strudel for Workshop on Research Data Management in TU Dresden Core Facilities

Cornelia Wetzker

Published 2023-11-08

Licensed CC-BY-4.0



This presentation gives a short outline of the complexity of data and metadata in the bioimaging universe. It introduces NFDI4BIOIMAGE as a newly formed consortium as part of the German 'Nationale Forschungsdateninfrastruktur' (NFDI) and its goals and tools for data management including its current members on TU Dresden campus. &nbsp;

Tags: Research Data Management, Nfdi4Bioimage, Include In Dalia

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

Tags: Include In Dalia

[https://zenodo.org/records/14001044](https://zenodo.org/records/14001044)

[https://doi.org/10.5281/zenodo.14001044](https://doi.org/10.5281/zenodo.14001044)


---

## Bio-image Analysis Code Generation using bia-bob

Robert Haase

Published 2024-10-09

Licensed CC-BY-4.0



In this presentation I introduce bia-bob, an AI-based code generator that integrates into Jupyter Lab and allows for easy generation of Bio-Image Analysis Python code. It highlights how to get started with using large language models and prompt engineering to get high-quality bio-image analysis code.

Tags: Artificial Intelligence, Bioimage Analysis, Include In Dalia

[https://zenodo.org/records/13908108](https://zenodo.org/records/13908108)

[https://doi.org/10.5281/zenodo.13908108](https://doi.org/10.5281/zenodo.13908108)


---

## Bio-image Analysis with the Help of Large Language Models

Robert Haase

Published 2024-03-13

Licensed CC-BY-4.0



Large Language Models (LLMs) change the way how we use computers. This also has impact on the bio-image analysis community. We can generate code that analyzes biomedical image data if we ask the right prompts. This talk outlines introduces basic principles, explains prompt engineering and how to apply it to bio-image analysis. We also compare how different LLM vendors perform on code generation tasks and which challenges are ahead for the bio-image analysis community.

Tags: Artificial Intelligence, Python, Include In Dalia

Content type: Slides

[https://zenodo.org/records/10815329](https://zenodo.org/records/10815329)

[https://doi.org/10.5281/zenodo.10815329](https://doi.org/10.5281/zenodo.10815329)


---

## Bio-image Data Science

Robert Haase

Licensed CC-BY-4.0



This repository contains training resources for Students at Uni Leipzig who want to dive into bio-image data science with Python.

Tags: Research Data Management, Artificial Intelligence, Bioimage Analysis, Python, Include In Dalia

Content type: Notebook

[https://github.com/ScaDS/BIDS-lecture-2024](https://github.com/ScaDS/BIDS-lecture-2024)


---

## Bio-image Data Science Lectures 2025 @ Uni Leipzig / ScaDS.AI

Robert Haase

Published 2025-07-10

Licensed CC-BY-4.0



These are the PPTx training resources for Students at Uni Leipzig who want to dive into bio-image data science with Python. The material will develop here and in the corresponding&nbsp;github repository between April and July 2025.

Tags: Nfdi4Bioimage, Bioimage Analysis, Artificial Intelligence, Exclude From Dalia

[https://zenodo.org/records/15858127](https://zenodo.org/records/15858127)

[https://doi.org/10.5281/zenodo.15858127](https://doi.org/10.5281/zenodo.15858127)


---

## Bio-image Data Science Lectures @ Uni Leipzig / ScaDS.AI

Robert Haase

Licensed CC-BY-4.0



These are the PPTx training resources for Students at Uni Leipzig who want to dive into bio-image data science with Python. The material developed here between April and July 2024.

Tags: Bioimage Analysis, Artificial Intelligence, Python, Exclude From Dalia

Content type: Slides

[https://zenodo.org/records/12623730](https://zenodo.org/records/12623730)

[https://doi.org/10.5281/zenodo.12623730](https://doi.org/10.5281/zenodo.12623730)


---

## Bio-image analysis, biostatistics, programming and machine learning for computational biology

Anna Poetsch, Biotec Dresden, Marcelo Leomil Zoccoler, Johannes Richard Müller, Robert Haase

Licensed CC-BY-4.0



Tags: Python, Bioimage Analysis, Napari, Include In Dalia

Content type: Notebook

[https://github.com/BiAPoL/Bio-image_Analysis_with_Python](https://github.com/BiAPoL/Bio-image_Analysis_with_Python)


---

## Bio.tools database

Licensed CC-BY-4.0



Tags: Bioinformatics, Exclude From Dalia

Content type: Collection

[https://bio.tools/](https://bio.tools/)


---

## BioFormats Command line (CLI) tools

Published 2024-10-24

Licensed CC-BY-4.0



Bio-Formats is a standalone Java library for reading and writing life sciences image file formats. There are several scripts for using Bio-Formats on the command line, which are listed here.

Tags: Exclude From Dalia

Content type: Documentation

[https://bio-formats.readthedocs.io/en/v8.0.0/users/comlinetools/index.html](https://bio-formats.readthedocs.io/en/v8.0.0/users/comlinetools/index.html)


---

## BioImage Analysis Notebooks

Robert Haase et al.

Licensed ['CC-BY-4.0', 'BSD-3-CLAUSE']



Tags: Python, Bioimage Analysis, Include In Dalia

Content type: Book, Notebook

[https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/intro.html](https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/intro.html)


---

## BioImage Analysis and Superresolution Microscopy Workshop 2023 (at Dartmouth College)

Zuzana Burdíková, Zdeněk Švindrych, Martin Schätz, Jakub Soukup, Pat Robison

Published 2023-06-07

Licensed CC-BY-4.0



The full program is available in the repository (Schedule DMW 2023.rtf) with most of the presentations and all exercises. All exercise files are in ZIP files Data.zip and&nbsp;ThunderSTORM sample data 2023.zip.

Date: June 6-7, 2023
Time: 9am - 5pm
Location: Dartmouth College, 74 College St, Hanover, Kellogg 200
Sponsor: bioMT (Lunch and coffee breaks)

Summary:
The BioImage Analysis and Superresolution Microscopy Workshop 2023 took place at Dartmouth College, offering participants a comprehensive learning experience in the field of bioimage analysis and superresolution microscopy. Over the course of two days, researchers, scientists, and students immersed themselves in cutting-edge microscopy techniques and expanded their knowledge and practical skills.

Day 1 (Tue, June 6):
The workshop began with Zdenek Svindrych providing an overview of microscopy principles, methods, and theoretical foundations. Participants gained insights into image formation in fluorescence microscopes, resolution, and noise. This was followed by an introduction to superresolution microscopy techniques, including Single-Molecule localization Microscopy (STORM, PALM, DNA-PAINT) and Structured Illumination Microscopy (SIM, ISM, Airyscan, SoRa). Zuzana Burdikova then guided attendees through the theoretical aspects of bioimage processing in Fiji, covering image formats, multi-dimensional image analysis, data visualization, and quantitative analysis. Practical sessions allowed participants to apply their knowledge, exploring two-channel colocalization, image filtering, and quantitative measurements in Fiji.

Day 2 (Wed, June 7):
The second day commenced with a remote presentation by SVI.nl, introducing participants to the Huygens deconvolution software used in widefield, confocal, and superresolution microscopy. Zdenek Svindrych demonstrated the practical applications of ThunderSTORM, an ImageJ plug-in for single molecule localization microscopy (SMLM) data analysis and superresolution imaging. The session included an overview of the ThunderSTORM workflow, covering localization, filtering, rendering, and 3D STORM using the astigmatism method. Jakub Soukup explored advanced noise reduction algorithms such as Noise2Void and StarDist. Martin Sch&auml;tz discussed data management strategies.

In the afternoon, participants engaged in practical sessions. Martin Sch&auml;tz presented Ilastik, a versatile software for image classification and segmentation. Pat Robison delivered a scientific lecture on the role of detyrosinated microtubules in contracting cardiomyocytes. Zdenek Svindrych, along with other experts, led a hands-on session on customizing Fiji using the ImageJ Macro language. The day concluded with a practical session on the interactive design of GPU-accelerated image data flow graphs in Fiji, guided by Martin Sch&auml;tz and the workshop team.

Tags: Include In Dalia

[https://zenodo.org/records/8025067](https://zenodo.org/records/8025067)

[https://doi.org/10.5281/zenodo.8025067](https://doi.org/10.5281/zenodo.8025067)


---

## BioImage.IO Chatbot, GloBIAS Seminar

Caterina Fuster-Barcelo

Published 2024-10-02

Licensed CC-BY-4.0



The dynamic field of bioimage analysis continually seeks innovative tools to democratize access to analysis tools and its documentation. The BioImage.IO Chatbot, leveraging state-of-the-art AI technologies including Large Language Models (LLMs) and Retrieval Augmented Generation (RAG), provides an interactive platform that significantly integrates the exploration and application of bioimage analysis tools and models. This seminar will introduce the BioImage.IO Chatbot's capabilities, focusing on how it facilitates access to advanced analysis tools and documentation, allows for the execution of complex models, and enables users to create customized extensions adjusted to specific research needs. In a live demo, attendees will see how to interact with the chatbot and all its assistants and capabilities. Join us to explore how the BioImage.IO Chatbot ca transform your research by making sophisticated analysis more intuitive and accessible.

Tags: Include In Dalia

[https://zenodo.org/records/13880367](https://zenodo.org/records/13880367)

[https://doi.org/10.5281/zenodo.13880367](https://doi.org/10.5281/zenodo.13880367)


---

## Bioimaging workflow based on OMERO, eLabFTW, and Adamant for integrating images with multimodal metadata

Mohsen Ahmadi, Robert Wagner, Sander Bekeschus, Becker, Markus M.

Published 2025-07-29

Licensed CC-BY-4.0



This research data management workflow for bioimaging is designed to bridge the gap between image metadata and experimental / process metadata. By linking images and microscopy-related metadata with broader experimental records, the workflow particularly supports the adoption of the FAIR (Findable, Accessible, Interoperable, Reusable) data principles in interdisciplinary fields where bioimaging is used to analyse treated samples requiring multimodal metadata. A Jupyter Notebook guides the user through the metadata level, data handling level, and data processing level and connects various software components in a modular manner. On the metadata level, microscope-specific metadata are captured using the Micro-Meta App and stored as reusable digital assets. Adamant provides a user interface to collect and process schema-based metadata related to the experiment / treatment procedure. Structured imaging and process metadata are attached to the complete experiment description in eLabFTW. On the data handling level, OMERO serves as the central platform for storing and managing microscopy images together with their metadata retrieved from eLabFTW (workflow with ELN) or directly from JSON files (workflow without ELN). On the data processing level, OMERO supports both automated and manual image analysis either directly via the Jupyter Notebook or FIJI. Due to the modularity of the workflow, the integrated tools can be substituted with equivalent systems based on institutional / user requirements. Whether in teaching or research settings, this workflow supports high-throughput, reproducible imaging workflows, ensuring that data, metadata, and analysis steps remain transparent, interoperable, and reusable across diverse bioimage analysis platforms.

Tags: Nfdi4Bioimage, Exclude From Dalia

[https://zenodo.org/records/16561545](https://zenodo.org/records/16561545)

[https://doi.org/10.5281/zenodo.16561545](https://doi.org/10.5281/zenodo.16561545)


---

## Breast Cancer Nuclei images for DL Training + ZeroCostDL4Mic StarDist Model

Ofra Golani, Vishnu Mohan, Tamar Geiger

Published 2024-05-21

Licensed CC-BY-4.0




Training dataset:Paired microscopy images (fluorescence) and corresponding masks
Microscopy data type: Fluorescence microscopy and masks obtained via manual correction of automatic segmentation with pre-trained StarDist model (see https://github.com/qupath/models/tree/main/stardist)&nbsp;
Cells were imaged using a 20x objective with a 1x camera adapter was used in conjunction with a pco.edge 4.2 4MP camera on Pannoramic SCAN 150 scanner.
Cell type: FFPE tissue sections were sliced from all cancer-containing paraffin blocks
File format: .tif (8-bit for fluorescence and 16-bit for the masks)
&nbsp;
StarDist Model:The StarDist model was generated using the ZeroCostDL4Mic platform (Chamier et al., 2021). This custom StarDist model was trained for 100 epochs using 80 manually annotated paired images (image dimensions: (257, 257)) with a batch size of 2, an augmentation factor of 10 and a mae loss function. The StarDist &ldquo;Versatile fluorescent nuclei&rdquo; model was used as a training starting point. Key python packages used include TensorFlow (v 2.2.0), Keras (v 1.1.2), CSBdeep (v 0.7.2), NumPy (v 1.21.6), Cuda (v 11..1.105). The training was accelerated using a Tesla P100GPU.The model weights can be used in the ZeroCostDL4Mic StarDist 2D notebook or in the StarDist Fiji plugin. a QuPath-compatible model is also provided.
&nbsp;
&nbsp;


Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/11235393](https://zenodo.org/records/11235393)

[https://doi.org/10.5281/zenodo.11235393](https://doi.org/10.5281/zenodo.11235393)


---

## Browsing the Open Microscopy Image Data Resource with Python

Robert Haase

Licensed CC-BY-4.0



Tags: OMERO, Python, Include In Dalia

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

Tags: Include In Dalia

[https://zenodo.org/records/14909526](https://zenodo.org/records/14909526)

[https://doi.org/10.5281/zenodo.14909526](https://doi.org/10.5281/zenodo.14909526)


---

## Building a FAIR image data ecosystem for microscopy communities

Isabel Kemmer, Antje Keppler, Beatriz Serrano-Solano, Arina Rybina, Bugra Özdemir, Johanna Bischof, Ayoub El Ghadraoui, John E. Eriksson, Aastha Mathur

Published 2023-03-31

Licensed CC-BY-4.0



Bioimaging has now entered the era of big data with faster than ever development of complex microscopy technologies leading to increasingly complex datasets. This enormous increase in data size and informational complexity within those datasets has brought with it several difficulties in terms of common and harmonized data handling, analysis and management practices, which are currently hampering the full potential of image data being realized. Here we outline a wide range of efforts and solutions currently being developed by the microscopy community to address these challenges on the path towards FAIR bioimage data. We also highlight how different actors in the microscopy ecosystem are working together, creating synergies that develop new approaches, and how research infrastructures, such as Euro-BioImaging, are fostering these interactions to shape the field.&nbsp;

Tags: Include In Dalia

[https://zenodo.org/records/7788899](https://zenodo.org/records/7788899)

[https://doi.org/10.5281/zenodo.7788899](https://doi.org/10.5281/zenodo.7788899)


---

## Building a National Research Data Infrastructure 
for Microscopy and BioImage Analysis

Josh Moore

Published 2025-06-30

Licensed CC-BY-4.0



Presentation for the BioImagingUK Meeting taking place from 1200 - 1500 BST on Monday 30 June 2025 at mmc2025 https://www.mmc-series.org.uk/meetings-features/bioimaginguk-meeting.html
This pre-congress meeting provides an opportunity for the UK Bioimaging community to discuss priorities and strategies in national infrastructure, technology development, training, careers and ways to share knowledge across different disciplines. The session will consist of short talks from members of the BioImagingUK community and industrial/institute collaboration partners to update on progress, new opportunities and initiatives. There will be interactive Q+A sessions to encourage discussion and enable emerging priorities and ideas to be highlighted.

Tags: Nfdi4Bioimage, Include In Dalia

[https://zenodo.org/records/15756866](https://zenodo.org/records/15756866)

[https://doi.org/10.5281/zenodo.15756866](https://doi.org/10.5281/zenodo.15756866)


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

Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/6140111](https://zenodo.org/records/6140111)

[https://doi.org/10.5281/zenodo.6140111](https://doi.org/10.5281/zenodo.6140111)


---

## Cellpose training data and scripts from "Inhibition of CERS1 in aging skeletal muscle exacerbates age-related muscle impairments"

Martin Wohlwend, Olivier Burri, Johan Auwerx

Published 2024-02-27

Licensed CC-BY-4.0



This Workflow contains all the material necessary to reproduce the results of the QuPath analysis performed in the paper
&nbsp;"Inhibition of CERS1 in aging skeletal muscle exacerbates age-related muscle impairments"
Inside this workflow and dataset, you will find the following folders

QuPath Training Project: A QuPath 0.3.2 project containing all the manual annotations (ground truths) used to train the cellpose model, as well as the script to start the training
QuPath Demo Project: A QuPath 0.3.2 project containing an example image that can be segmented using cellpose, followed by the classification of the CD45 expressing fibers
Training Images and Demo Images: The raw whole slide scanner 20x images needed by the above QuPath projects
Model: The fodler contianing the trained cellpose model
Cellpose Training Folder: The exported raw and ground truth images that the above cellpose model was trained on
Scripts: The QuPath scripts, also located in their respective QuPath projects, that were created for this whole workflow
QC: A Jupyter notebook, based on ZeroCostDL4Mic that computes quality metrics in order to assess the performance of the trained cellpose model. The folder also contains the resulting metrics.

Installation and Use
If you are going to use the QuPath projects, you need a local QuPath Installation https://qupath.github.io/ that is configured to run the QuPath Cellpose Extension https://github.com/BIOP/qupath-extension-cellpose as well as a working Cellpose installation https://github.com/MouseLand/cellpose
Instructions for installation are available from the links above.
After that, you should be able to open the QuPath project, navigate to the "Automate &gt; Project scripts" menu and locate the script you wish to run.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/7041137](https://zenodo.org/records/7041137)

[https://doi.org/10.5281/zenodo.7041137](https://doi.org/10.5281/zenodo.7041137)


---

## Cellpose training data and scripts from "Machine learning for histological annotation and quantification of cortical layers"

Jean Jacquemier, Julie Meystre, Olivier Burri

Published 2024-07-04

Licensed CC-BY-4.0



This Workflow contains all the material necessary to reproduce the cells detection, thanks to the QuPath performed in the paper
&nbsp;"Machine learning for histological annotation and quantification of cortical layers"
Inside this workflow and dataset, you will find the following folders

QuPath Training Project: A QuPath 0.5.0 project containing all the manual annotations (ground truths) used to train the cellpose model, as well as the script to start the training
Training Images and Demo Images: The raw whole slide scanner images needed by the above QuPath project
Model: The fodler containing the trained cellpose model
cellpose-training Folder: The exported raw and ground truth images that the above cellpose model was trained on
Scripts: The QuPath scripts, also located in their respective QuPath projects, that were created for this whole workflow
QC: A Jupyter notebook, based on ZeroCostDL4Mic that computes quality metrics in order to assess the performance of the trained cellpose model. The folder also contains the resulting metrics.

Installation and Use
If you are going to use the QuPath projects, you need a local QuPath Installation https://qupath.github.io/ that is configured to run the QuPath Cellpose Extension https://github.com/BIOP/qupath-extension-cellpose as well as a working Cellpose installation https://github.com/MouseLand/cellpose
Instructions for installation are available from the links above.
After that, you should be able to open the QuPath project, navigate to the "Automate &gt; Project scripts" menu and locate the script you wish to run.
1. train a cell segmentation algorithm in the context of the rat brain Layer&nbsp;Boundaries project&nbsp;
2. trigger cell segmentation from a QuPath project in a semi-automated pipeline

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/12656468](https://zenodo.org/records/12656468)

[https://doi.org/10.5281/zenodo.12656468](https://doi.org/10.5281/zenodo.12656468)


---

## Challenges and opportunities for bio-image analysis core-facilities

Robert Haase

Licensed CC-BY-4.0



Tags: Research Data Management, Bioimage Analysis, Nfdi4Bioimage, Include In Dalia

Content type: Slides

[https://f1000research.com/slides/12-1054](https://f1000research.com/slides/12-1054)


---

## Challenges and opportunities for bioimage analysis core-facilities

Johannes Richard Soltwedel, Robert Haase

Licensed CC-BY-4.0



This article outlines common reasons for founding bioimage analysis core-facilities, services they can provide to fulfill certain need and conflicts of interest that arise from these services.

Tags: Bioimage Analysis, Research Data Management, Include In Dalia

Content type: Publication

[https://onlinelibrary.wiley.com/doi/full/10.1111/jmi.13192](https://onlinelibrary.wiley.com/doi/full/10.1111/jmi.13192)


---

## ChatGPT for Image Analysis

Robert Haase

Published 2024-08-25

Licensed CC-BY-4.0



Large Language Models (LLMs) such as ChatGPT are changing the way we interact with computers, including how we analye microscopy imaging data. In this talk I introduce basic concepts of asking LLMs to write code and how to modify the questions to get the best out of it. For trying out these prompt engineering basics there are additional online resources available: https://scads.github.io/prompt-engineering-basics-2024/intro.html

Tags: Include In Dalia

[https://zenodo.org/records/13371196](https://zenodo.org/records/13371196)

[https://doi.org/10.5281/zenodo.13371196](https://doi.org/10.5281/zenodo.13371196)


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

## Cloud-Native Formats Enable Federated Repositories at Peta-Scale

Josh Moore

Published 2025-09-27

Licensed CC-BY-4.0



Poster presentation for the abstract "Enabling Peta-Scale Federated Repositories through Cloud-Native Formats: Lessons from a fast-paced challenge in the bioimaging community" submitted to 2nd Conference on Research Data Infrastructure (CoRDI) 2025

Tags: Nfdi4Bioimage, Include In Dalia

[https://zenodo.org/records/16911980](https://zenodo.org/records/16911980)

[https://doi.org/10.5281/zenodo.16911980](https://doi.org/10.5281/zenodo.16911980)


---

## Collaborative Working and Version Control with git[hub]

Robert Haase

Published 2024-01-10

Licensed CC-BY-4.0



This slide deck introduces the version control tool git, related terminology and the Github Desktop app for managing files in Git[hub] repositories. We furthermore dive into:* Working with repositories* Collaborative with others* Github-Zenodo integration* Github pages* Artificial Intelligence answering Github Issues

Tags: Nfdi4Bioimage, Globias, Research Data Management, Research Software Management, Include In Dalia

[https://zenodo.org/records/14626054](https://zenodo.org/records/14626054)

[https://doi.org/10.5281/zenodo.14626054](https://doi.org/10.5281/zenodo.14626054)


---

## Collaborative bio-image analysis script editing with git

Robert Haase

Licensed CC-BY-4.0



Introduction to version control using git for collaborative, reproducible script editing.

Tags: Sharing, Research Data Management, Include In Dalia

Content type: Blog Post

[https://focalplane.biologists.com/2021/09/04/collaborative-bio-image-analysis-script-editing-with-git/](https://focalplane.biologists.com/2021/09/04/collaborative-bio-image-analysis-script-editing-with-git/)


---

## Collaborative working and  Version Control with Git[Hub]

Robert Haase

Published 2025-05-10

Licensed CC-BY-4.0



Working together on the internet presents us with new challenges: Who uploaded a file and when? Who contributed to the project when and why? How can content be merged when multiple team members make changes at the same time? The version control tool&nbsp;Git offers a comprehensive solution to these questions. The online platform GitHub.com provides a Git-driven platform that enables effective collaboration. Attendees of this hands-on tutorial will learn:


Introduction to version control with Git[Hub]


Working with Git: Pull requests


Resolving merge conflicts


Artificial intelligence that can respond to GitHub issues



Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

[https://zenodo.org/records/15379632](https://zenodo.org/records/15379632)

[https://doi.org/10.5281/zenodo.15379632](https://doi.org/10.5281/zenodo.15379632)


---

## Combining StarDist and TrackMate example 1 -  Breast cancer cell dataset

Guillaume Jacquemet

Published 2020-09-17

Licensed CC-BY-4.0



Description: Contains a StarDist example training dataset, a test dataset, and the StarDist model generated using ZeroCostDL4Mic (see https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist)

Training dataset: 72 Paired microscopy images (fluorescence) and corresponding masks

Microscopy data type: Fluorescence microscopy (SiR-DNA) and masks obtained via manual segmentation (see https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist for details about the segmentation)

Microscope: Spinning disk confocal microscope with a 20x 0.8 NA objective

Cell type: DCIS.COM Lifeact-RFP cells

File format: .tif (16-bit for fluorescence and 8 and 16-bit for the masks)

Image size: 1024x1024 (Pixel size: 634 nm)

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/4034976](https://zenodo.org/records/4034976)

[https://doi.org/10.5281/zenodo.4034976](https://doi.org/10.5281/zenodo.4034976)


---

## Combining StarDist and TrackMate example 2 -  T cell dataset

Nathan H. Roy, Guillaume Jacquemet

Published 2020-09-17

Licensed CC-BY-4.0



Description: Contains a StarDist example training dataset, a test dataset, and the StarDist model generated using ZeroCostDL4Mic (see https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist)

Training dataset: 209 Paired microscopy images (brightfield) and corresponding masks

Microscopy data type: brightfield microscopy and masks obtained via manual segmentation (see https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist for details about the segmentation)

Microscope: Imaging was done using a 10x phase contrast objective at 37&deg;C on a Zeiss Axiovert 200M microscope equipped with an automated X-Y stage and a Roper EMCCD camera. Time-lapse images were collected every 30 sec for 10 min using SlideBook 6 software (Intelligent Imaging Innovations).

File format: .tif (16-bit for brightfield images and 8 and 16-bit for the masks)

Image size: 1024x1024 (Pixel size: 645 nm)

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/4034929](https://zenodo.org/records/4034929)

[https://doi.org/10.5281/zenodo.4034929](https://doi.org/10.5281/zenodo.4034929)


---

## Combining StarDist and TrackMate example 3 -  Flow chamber dataset

Gautier Follain, Guillaume Jacquemet

Published 2020-09-17

Licensed CC-BY-4.0



Description: Contains a StarDist example training dataset, a test dataset, and the StarDist model generated using ZeroCostDL4Mic (see https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist)

Training dataset: Paired microscopy images (brightfield) and corresponding masks

Microscopy data type: brightfield microscopy and masks obtained via manual segmentation (see https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist for details about the segmentation)

Microscope: Images were acquired with a brightfield microscope (Zeiss Laser-TIRF 3 Imaging System, Carl Zeiss) and a 10X objective.

File format: .tif (8-bit for brightfield images and 8 and 16-bit for the masks)

Image size: 1024x1024 (Pixel size: 650 nm)

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/4034939](https://zenodo.org/records/4034939)

[https://doi.org/10.5281/zenodo.4034939](https://doi.org/10.5281/zenodo.4034939)


---

## Combining the BIDS and ARC Directory Structures for Multimodal Research Data Organization

Torsten Stöter, Tobias Gottschall, Andrea Schrager, Peter Zentis, Monica Valencia-Schneider, Niraj Kandpal, Werner Zuschratter, Astrid Schauss, Timo Dickscheid, Timo Mühlhaus, Dirk von Suchodoletz

Published 2023-09-12

Licensed CC-BY-4.0



Interdisciplinary collaboration and integration of large and diverse datasets are becoming increasingly important. Answering complex research questions requires combining and analysing multimodal datasets. Research data management follows the FAIR principles making data findable, accessible, interoperable, and reusable. However, there are challenges in capturing the entire research cycle and contextualizing data according, not only for the DataPLANT and NFDI4BIOIMAGE communities. To address these challenges, DataPLANT developed a data structure called Annotated Research Context (ARC). The Brain Imaging Data Structure (BIDS) originated from the neuroimaging community extended for microscopic image data. Both concepts provide standardised and file system based data storage structures for organising and sharing research data accompanied with metadata. We exemplarily compare the ARC and BIDS designs and propose structural and metadata mapping.

Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

Content type: Poster

[https://zenodo.org/records/8349563](https://zenodo.org/records/8349563)

[https://doi.org/10.5281/zenodo.8349563](https://doi.org/10.5281/zenodo.8349563)


---

## Conda, Container and Bots - How to Build and Maintain Tool Dependencies in Workflows and Training Materials

Paul Zierep, Sanjay Kumar Srikakulam, Sebastian Schaaf, Bjoern Gruening

Published 2023-09-07

Licensed CC-BY-4.0



The lifecycle of scientific tools comprises the creation of code releases, packages and containers which can be deployed into cloud platforms, such as the Galaxy Project, where they are run and integrated into workflows. The tools and workflows are further used to create training material that benefits a broad community. The need to organize and streamline this tool development lifecycle has led to a sophisticated development and deployment architecture.

Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

Content type: Publication

[https://www.tib-op.org/ojs/index.php/CoRDI/article/view/417](https://www.tib-op.org/ojs/index.php/CoRDI/article/view/417)


---

## Conference Slides - 4th Day of Intravital Microscopy

Dr. Hellen Ishikawa-Ankerhold

Published 2024-11-13

Licensed CC-BY-4.0



Conference Slides for the presentation of GerBI e.V. at the 4th Day of Intravital Microscopy in Leuven, Belgium.
Features Structure, activities and Links to join GerBI e.V.

Tags: Exclude From Dalia

[https://zenodo.org/records/14113714](https://zenodo.org/records/14113714)

[https://doi.org/10.5281/zenodo.14113714](https://doi.org/10.5281/zenodo.14113714)


---

## Crashkurs Forschungsdatenmanagement

Barbara Weiner, Stephan Wünsche, Stefan Kühne, Pia Voigt, Sebastian Frericks, Clemens Hoffmann, Romy Elze, Ronny Gey

Published 2020-04-30

Licensed CC-BY-4.0



Diese Pr&auml;sentation bietet einen Einstieg in alle relevanten Bereiche des Forschungsdatenmanagements an der Universit&auml;t Leipzig. Behandelt werden Grundlagen des Forschungsdatenmanagements, technische, ethische und rechtliche Aspekte sowie die Archivierung und Publikation von Forschungsdaten. Die Pr&auml;sentation enth&auml;lt zahlreiche weiterf&uuml;hrende Links (rot) und Literaturhinweise.

Erg&auml;nzend hierzu wird eine Pr&auml;sentation mit &Uuml;bungsaufgaben angeboten, die helfen soll, das Gelernte zu festigen und in der eigenen Forschungspraxis umzusetzen. Den Aufgaben folgen jeweils eine Antwortfolie sowie deren Aufl&ouml;sung.

Tags: Research Data Management, Include In Dalia

Content type: Slides

[https://zenodo.org/records/3778431](https://zenodo.org/records/3778431)

[https://doi.org/10.5281/zenodo.3778431](https://doi.org/10.5281/zenodo.3778431)


---

## Creating Workflows and Advanced Workflow Options

Licensed CC-BY-4.0



Tags: Workflow, Include In Dalia

Content type: Tutorial, Online Tutorial

[https://galaxyproject.org/learn/advanced-workflow/](https://galaxyproject.org/learn/advanced-workflow/)


---

## Creating a Research Data Management Plan using chatGPT

Robert Haase

Published 2023-11-06

Licensed CC-BY-4.0



In this blog post the author demonstrates how chatGPT can be used to combine a fictive project description with a DMP specification to produce a project-specific DMP.

Tags: Research Data Management, Artificial Intelligence, Include In Dalia

Content type: Blog Post

[https://focalplane.biologists.com/2023/11/06/creating-a-research-data-management-plan-using-chatgpt/](https://focalplane.biologists.com/2023/11/06/creating-a-research-data-management-plan-using-chatgpt/)


---

## Creating open computational curricula

Kari Jordan, Zhian Kamvar, Toby Hodges

Published 2020-12-11

Licensed CC-BY-4.0



In this interactive session, Carpentries team members will guide attendees through three stages of the backward design process to create a lesson development plan for the open source tool of their choosing. Attendees will leave having identified what practical skills they aim to teach (learning objectives), an approach for designing challenge questions (formative assessment), and mechanisms to give and receive feedback.

Tags: Include In Dalia

Content type: Slides

[https://zenodo.org/records/4317149](https://zenodo.org/records/4317149)

[https://doi.org/10.5281/zenodo.4317149](https://doi.org/10.5281/zenodo.4317149)


---

## Cultivating Open Training

Robert Haase

Published 2024-03-14

Licensed CC-BY-4.0



In this SaxFDM Digital Kitchen, I introduced current challenges and potential solutions for openly sharing training materials, softly focusing on bio-image analysis. In this field a lot of training materials circulate in private channels, but openly shared, reusable materials, according to the FAIR-principles, are still rare. Using the CC-BY license and uploading materials to publicly acessible repositories are proposed to fill this gap.

Tags: Open Science, Research Data Management, FAIR-Principles, Bioimage Analysis, Licensing, Include In Dalia

Content type: Slides

[https://zenodo.org/records/10816895](https://zenodo.org/records/10816895)

[https://doi.org/10.5281/zenodo.10816895](https://doi.org/10.5281/zenodo.10816895)


---

## Cultivating Open Training to advance Bio-image Analysis

Robert Haase

Published 2024-04-25

Licensed CC-BY-4.0




These slides introduce current challenges and potential solutions for openly sharing training materials, focusing on bio-image analysis. In this field a lot of training materials circulate in private channels, but openly shared, reusable materials, according to the FAIR-principles, are still rare. Using the CC-BY license and publicly acessible repositories are proposed to fill this gap.


Tags: Research Data Management, Licensing, FAIR-Principles, Include In Dalia

Content type: Slides

[https://zenodo.org/records/11066250](https://zenodo.org/records/11066250)

[https://doi.org/10.5281/zenodo.11066250](https://doi.org/10.5281/zenodo.11066250)


---

## DCIMG dense beads taken in chunks over time

Zach Marin

Published 2025-08-14

Licensed CC-BY-4.0



Two 2000-frame chunks acquired at different times (~40 minutes apart) on a 4Pi widefield, showing some slow sample drift.&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/16875377](https://zenodo.org/records/16875377)

[https://doi.org/10.5281/zenodo.16875377](https://doi.org/10.5281/zenodo.16875377)


---

## DL4MicEverywhere

Iván Hidalgo, et al.

Licensed CC-BY-4.0



Tags: Bioimage Analysis, Exclude From Dalia

Content type: Notebook, Collection

[https://github.com/HenriquesLab/DL4MicEverywhere](https://github.com/HenriquesLab/DL4MicEverywhere)


---

## DNG in BioFormat opens in wrong resolution

Michael

Published 2025-07-15

Licensed CC-BY-4.0



Tags: Exclude From Dalia

[https://zenodo.org/records/15933943](https://zenodo.org/records/15933943)

[https://doi.org/10.5281/zenodo.15933943](https://doi.org/10.5281/zenodo.15933943)


---

## Data Carpentry for Biologists

Licensed ['CC-BY-4.0', 'MIT']



Tags: Include In Dalia

Content type: Tutorial, Code

[https://datacarpentry.org/semester-biology/](https://datacarpentry.org/semester-biology/)


---

## Data life cycle

ELIXIR (2021) Research Data Management Kit

Licensed CC-BY-4.0



In this section, information is organised according to the stages of the research data life cycle.

Tags: Data Life Cycle, Research Data Management, Exclude From Dalia

Content type: Collection, Website, Online Tutorial

[https://rdmkit.elixir-europe.org/data_life_cycle](https://rdmkit.elixir-europe.org/data_life_cycle)


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

## DataPLANT knowledge base

Published 2022-12-14

Licensed CC-BY-4.0



Explore fundamental topics on research data management (RDM), how DataPLANT implements these aspects to support plant researchers with RDM tools and services, read guides and manuals or search for some teaching materials.

Tags: Research Data Management, Dataplant, Include In Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/14769820](https://zenodo.org/records/14769820)

[https://doi.org/10.5281/zenodo.14769820](https://doi.org/10.5281/zenodo.14769820)


---

## Datenmanagement

Robert Haase

Published 2024-04-14

Licensed CC-BY-4.0



In dieser Data Management Session wird der Lebenszyklus von Daten n&auml;her beleuchtet. Wie entstehen Daten, was passiert mit ihnen, wenn sie verarbeitet werden? Wem geh&ouml;ren die Daten und wer ist daf&uuml;r verantwortlich, sie zu ver&ouml;ffentlichen, zu archivieren und gegebenenfalls wiederzuverwenden? Wir werden einen Datenmanagementplan in Gruppenarbeit entwerfen, ggf. mit Hilfe von ChatGPT.

Tags: Research Data Management, Include In Dalia

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

Tags: Research Data Management, Include In Dalia

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

Tags: Research Data Management, Include In Dalia

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

Tags: Research Data Management, Include In Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/5101351](https://zenodo.org/records/5101351)

[https://doi.org/10.5281/zenodo.5101351](https://doi.org/10.5281/zenodo.5101351)


---

## Deep learning segmentation projects of FIB-SEM dataset of U2-OS cell

Belevich Ilya, Eija Jokitalo

Published 2023-10-26

Licensed CC-BY-4.0



This submission includes ground truth datasets that were used to segment the nuclear envelope (NE), mitochondria, endoplasmic reticulum (ER) and Golgi from a human bone osteosarcoma epithelial cell (U2-OS) imaged using focused-ion beam scanning electron microscopy (FIB-SEM).The full FIB-SEM dataset is deposited to EMPIAR (https://www.ebi.ac.uk/empiar, EMPIAR-11746).&nbsp;

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/10043461](https://zenodo.org/records/10043461)

[https://doi.org/10.5281/zenodo.10043461](https://doi.org/10.5281/zenodo.10043461)


---

## DeepBacs – Bacillus subtilis fluorescence segmentation dataset

Séamus Holden, Mia Conduit

Published 2021-10-05

Licensed CC-BY-4.0



Training and test images of live B. subtilis cells expressing FtsZ-GFP for the task of segmentation.

Additional information can be found on this github wiki.

The example shows the fluorescence widefield image of live B. subtilis cells expressing FtsZ-GFP and the manually annotated segmentation mask.

&nbsp;

Data type: Paired fluorescence and segmented mask images

Microscopy data type: 2D widefield images (fluorescence)&nbsp;

Microscope: Custom-built 100x inverted microscope bearing a 100x TIRF objective (Nikon CFI Apochromat TIRF 100XC Oil); images were captured on a Prime BSI sCMOS camera (Teledyne Photometrics)

Cell type: B. subtilis strain SH130 grown under agarose pads

File format: .tiff (8-bit) or .png (8-bit)

For segmented masks, binary masks are used for training of CARE/U-Net models, 8-bit .tif ROI maps for training of StarDist models and .png images for training of pix2pix models

Image size: 1024 x 1024 px&sup2; (Pixel size: 65 nm)

Image preprocessing: Images were denoised using PureDenoise and resulting 32-bit images were converted into 8-bit images after normalizing to 1% and 99.98% percentiles. Images were manually annotated using the Labkit Fiji plugin

&nbsp;

Author(s): Mia Conduit1,2, S&eacute;amus Holden1,3

Contact email: Seamus.Holden@newcastle.ac.uk

&nbsp;

Affiliation:

1) Centre for Bacterial Cell Biology, Biosciences Institute, Newcastle University, NE2 4AX UK

2) ORCID: 0000-0002-7169-907X

&nbsp;

&nbsp;Associated publications: Whitley et al., 2021, Nature Communications, https://doi.org/10.15252/embj.201696235

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/5550968](https://zenodo.org/records/5550968)

[https://doi.org/10.5281/zenodo.5550968](https://doi.org/10.5281/zenodo.5550968)


---

## DeepBacs – Escherichia coli bright field segmentation dataset

Christoph Spahn, Mike Heilemann

Published 2021-10-05

Licensed CC-BY-4.0



Training and test images of live E. coli cells imaged under bright field for the task of segmentation.

Additional information can be found on this github wiki.

The example shows a bright field image of live E. coli cells and the manually annotated segmentation mask.

&nbsp;

Data type: Paired bright field and segmented mask images&nbsp;

Microscopy data type: 2D bright field images recorded at 1 min interval

Microscope: Nikon Eclipse Ti-E equipped with an Apo TIRF 1.49NA 100x oil immersion objective

Cell type: E. coli MG1655 wild type strain (CGSC #6300).

File format: .tif (8-bit)

Image size: 1024 x 1024 px&sup2; (79 nm / pixel), 19/15 individual frames (training/test dataset)

1024 x 1024 px&sup2; (79 nm / pixel), 9 regions of interest with 80 frames @ 1 min time interval (live-cell time series)

Image preprocessing: Raw images were recorded in 16-bit mode (image size 512 x 512 px&sup2; @ 158 nm/px). Images were upscaled with a factor of 2 (no interpolation) to enable generation of higher-quality segmentation masks. Two sets of mask images are provided: RoiMaps for instance segmentation using e.g. StarDist or binary images for CARE or U-Net.


Author(s): Christoph Spahn1,2, Mike Heilemann1,3

Contact email: christoph.spahn@mpi-marburg.mpg.de

&nbsp;

Affiliation(s):&nbsp;

1) Institute of Physical and Theoretical Chemistry, Max-von-Laue Str. 7, Goethe-University Frankfurt, 60439 Frankfurt, Germany

2) ORCID: 0000-0001-9886-2263&nbsp;

3) ORCID: 0000-0002-9821-3578

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/5550935](https://zenodo.org/records/5550935)

[https://doi.org/10.5281/zenodo.5550935](https://doi.org/10.5281/zenodo.5550935)


---

## DeepBacs – Mixed segmentation dataset and StarDist model

Christoph Spahn, Mike Heilemann, Séamus Holden, Mia Conduit, Pereira, Pedro Matos, Mariana Pinho

Published 2021-10-05

Licensed CC-BY-4.0



Mixed training and test images of S. aureus, E. coli and B. subtilis for cell segmentation using StarDist, as well as the trained StarDist model.

Additional information can be found on this github wiki.

&nbsp;

Data type: Paired bright field / fluorescence and segmented mask images

Microscopy data type: 2D widefield images; DIC and fluorescence for S. aureus, bright field images for E. coli, and fluorescence images for B. subtilis

Microscopes:&nbsp;

S. aureus:&nbsp;

GE HealthCare Deltavision OMX system (with temperature and humidity control, 37&deg;C) equipped with an Olympus 60x 1.42NA Oil immersion objective and 2 PCO Edge 5.5 sCMOS cameras (one for DIC, one for fluorescence)

E.coli:

Nikon Eclipse Ti-E equipped with an Apo TIRF 1.49NA 100x oil immersion objective

B. subtilis:

Custom-built 100x inverted microscope bearing a 100x TIRF objective (Nikon CFI Apochromat TIRF 100XC Oil); images were captured on a Prime BSI sCMOS camera (Teledyne Photometrics)

&nbsp;

Cell types: S. aureus strain JE2, E. coli MG1655 (CGSC #6300) and B. subtilis strain SH130; all grown under agarose pads

File format: .tif (8-bit and 16-bit)

Image size: 512 x 512 px&sup2; @ 80 nm pixel size (S. aureus); 1024 x 1024 px&sup2; @ 79 nm pixel size (E. coli); 1024 x 1024 px&sup2; @ 65 nm pixel size (B. subtilis)

Image preprocessing:&nbsp;

S. aureus:

Raw images were manually annotated by drawing ellipses in the NR fluorescence image and segmented images were created using the LOCI plugin (&ldquo;ROI Map&rdquo;). For training, images and masks were quartered into four 256 x 256 px&sup2; patches.

E. coli:

Raw images were recorded in 16-bit mode (image size 512x512 px&sup2; @ 158 nm/px). Images were upscaled with a factor of 2 (no interpolation) to enable generation of higher-quality segmentation masks.

B. subtilis:

Images were denoised using PureDenoise and resulting 32-bit images were converted into 8-bit images after normalizing to 1% and 99.98% percentiles. Images were manually annotated using the Labkit Fiji plugin

&nbsp;

StarDist model:

The StarDist 2D model was generated using the ZeroCostDL4Mic platform (Chamier et al., 2021). It was trained from scratch for 200 epochs (120 steps/epoch) on 155 paired image patches (image dimensions: (1024, 1024), patch size: (256,256)) with a batch size of 4, 10% validation data, 64 rays on grid 2, a learning rate of 0.0003 and a mae loss function, using the StarDist 2D ZeroCostDL4Mic notebook (v 1.12.2). Key python packages used include tensorflow (v 0.1.12), Keras (v 2.3.1), csbdeep (v 0.6.1), numpy (v 1.19.5), cuda (v 11.0.221). The training was accelerated using a Tesla P100GPU. The dataset was augmented by a factor of 3.

&nbsp;

The model weights can be used in the ZeroCostDL4Mic StarDist 2D notebook, the StarDist Fiji plugin or the TrackMate Fiji plugin (v7+).

&nbsp;

Author(s): Christoph Spahn1,2, Mike Heilemann1,3, Mia Conduit4, S&eacute;amus Holden4,5, Pedro Matos Pereira6,7, Mariana Pinho6,8

Contact email: christoph.spahn@mpi-marburg.mpg.de, Seamus.Holden@newcastle.ac.uk, pmatos@itqb.unl.pt and mgpinho@itqb.unl.pt

&nbsp;

Affiliation(s):&nbsp;

1) Institute of Physical and Theoretical Chemistry, Max-von-Laue Str. 7, Goethe-University Frankfurt, 60439 Frankfurt, Germany

2) ORCID: 0000-0001-9886-2263&nbsp;

3) ORCID: 0000-0002-9821-3578

4) Centre for Bacterial Cell Biology, Biosciences Institute, Newcastle University, NE2 4AX UK

5) ORCID: 0000-0002-7169-907X

6) Bacterial Cell Biology, Instituto de Tecnologia Qu&iacute;mica e Biol&oacute;gica Ant&oacute;nio Xavier, Universidade Nova de Lisboa, Oeiras, Portugal

7) ORCID: 0000-0002-1426-9540

8) ORCID: 0000-0002-7132-8842

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/5551009](https://zenodo.org/records/5551009)

[https://doi.org/10.5281/zenodo.5551009](https://doi.org/10.5281/zenodo.5551009)


---

## DeepBacs – Staphylococcus aureus widefield segmentation dataset

Pereira, Pedro Matos, Mariana Pinho

Published 2021-10-05

Licensed CC-BY-4.0



Training and test images of live S. aureus cells for the task of cell segmentation.

Additional information can be found in the github wiki.

The example shows the bright field and Nile Red fluorescence image of live S. aureus cells, as well as the manually annotated segmentation mask.

&nbsp;

Data type: Paired DIC/fluorescence and segmented mask images

Microscopy data type: 2D widefield images (DIC and fluorescence)

Microscope:&nbsp; GE HealthCare Deltavision OMX system (with temperature and humidity control, 37&deg;C) equipped with an Olympus 60x 1.42NA Oil immersion objective and 2 PCO Edge 5.5 sCMOS cameras (one for DIC, one for fluorescence)

Cell type: S. aureus strain JE2 grown under agarose pads

File format: .tif (16-bit)

Image size: 512 x 512 px&sup2; (80 nm/px)
Image preprocessing: Raw images were manually annotated by drawing ellipses in the NR fluorescence image and segmented images were created using the LOCI plugin (&ldquo;ROI Map&rdquo;). For training, images and masks were quartered into four 256 x 256 px&sup2; patches.

&nbsp;

Author(s): Pedro Matos Pereira1,2, Mariana Pinho1,3

Contact email: pmatos@itqb.unl.pt and mgpinho@itqb.unl.pt

&nbsp;

Affiliation:&nbsp;

1) Bacterial Cell Biology, Instituto de Tecnologia Qu&iacute;mica e Biol&oacute;gica Ant&oacute;nio Xavier, Universidade Nova de Lisboa, Oeiras, Portugal

2) ORCID: https://orcid.org/0000-0002-1426-9540

3) ORCID: https://orcid.org/0000-0002-7132-8842

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/5550933](https://zenodo.org/records/5550933)

[https://doi.org/10.5281/zenodo.5550933](https://doi.org/10.5281/zenodo.5550933)


---

## Developing (semi)automatic analysis pipelines and technological solutions for metadata annotation and management in high-content screening (HCS) bioimaging

Riccardo Massei, Stefan Scholz, Wibke Busch, Thomas Schnike, Hannes Bohring, Jan Bumberger

Licensed CC-BY-4.0



High-content screening (HCS) bioimaging automates the imaging and analysis of numerous biological samples, generating extensive metadata that is crucial for effective image management and interpretation. Efficiently handling this complex data is essential to implementing FAIR principles and realizing HCS's full potential for scientific discoveries.

Tags: Bioimage Analysis, Exclude From Dalia

Content type: Poster

[https://doi.org/10.5281/zenodo.8434325](https://doi.org/10.5281/zenodo.8434325)


---

## Developing a Training Strategy

Robert Haase

Published 2024-11-08

Licensed CC-BY-4.0



When training people in topics such as programming, bio-image analysis or data science, it makes sense to define a training strategy with a wider perspective than just trainees needs. This slide deck gives insights into aspects to consider when defining a training strategy. It considers funder's interests, financial aspects, metrics / goals, steps towards sustainability and opportunities for outreach and for founding future collaborations.

Tags: Nfdi4Bioimage, Artificial Intelligence, Include In Dalia

[https://zenodo.org/records/14053758](https://zenodo.org/records/14053758)

[https://doi.org/10.5281/zenodo.14053758](https://doi.org/10.5281/zenodo.14053758)


---

## Developing open-source software for bioimage analysis: opportunities and challenges

Florian Levet, Anne E. Carpenter, Kevin W. Eliceiri, Anna Kreshuk, Peter Bankhead, Robert Haase

Licensed CC-BY-4.0



This article outlines common challenges and practices when developing open-source software for bio-image analysis.

Tags: Neubias, Include In Dalia

Content type: Publication

[https://f1000research.com/articles/10-302](https://f1000research.com/articles/10-302)


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

## Development of a platform for advanced optics education, training and prototyping

Nadine Utz, Sabine Reither, Ruth Hans, Christian Feldhaus

Published 2023-10-05

Licensed CC-BY-4.0



In bio-medical research we often need to combine a broad range of expertise to run complex experiments and analyse and interpret their results. Also, it is desirable that all stakeholders of a project understand all parts of the experiment and analysis to draw and support the right conclusions. For imaging experiments this usually requires a basic understanding of the underlying physics. This has not necessarily been part of the professional training of all stakeholders, e.g. biologists or data scientists. Therefore an affordable platform for easily demonstrating and explaining imaging principles would be desirable.
Building up on a commercially available STEM Optics kit we developed extensions with widely available and affordable components to demonstrate advanced imaging techniques like e.g. confocal, lightsheet, OPT, spectral imaging. All models are quick and easy to build, yet demonstrate the important physical principles each imaging technique is based on.
Further use cases for this kit are training courses, demonstrations for imaging newbies when designing an experiment and outreach activities but also basic level prototyping.

Tags: Include In Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/5996883](https://zenodo.org/records/5996883)

[https://doi.org/10.5281/zenodo.5996883](https://doi.org/10.5281/zenodo.5996883)


---

## EDAM-bioimaging - The ontology of bioimage informatics operations, topics, data, and formats

Matúš Kalaš et al.

Licensed CC-BY-4.0



EDAM-bioimaging is an extension of the EDAM ontology, dedicated to bioimage analysis, bioimage informatics, and bioimaging.

Tags: Ontology, Bioimage Analysis, Exclude From Dalia

Content type: Poster

[https://hal.science/hal-02267597/document](https://hal.science/hal-02267597/document)


---

## EDAM-bioimaging: The ontology of bioimage informatics operations, topics, data, and formats (update 2020)

Matúš Kalaš, Laure Plantard, Joakim Lindblad, Martin Jones, Nataša Sladoje, Moritz A Kirschmann, Anatole Chessel, Leandro Scholz, Fabianne Rössler, Laura Nicolás Sáenz, Estibaliz Gómez de Mariscal, John Bogovic, Alexandre Dufour, Xavier Heiligenstein, Dominic Waithe, Marie-Charlotte Domart, Matthia Karreman, Raf Van de Plas, Robert Haase, David Hörl, Lassi Paavolainen, Ivana Vrhovac Madunić, Dean Karaica, Arrate Muñoz-Barrutia, Paula Sampaio, Daniel Sage, Sebastian Munck, Ofra Golani, Josh Moore, Florian Levet, Jon Ison, Alban Gaignard, Hervé Ménager, Chong Zhang, Kota Miura, Julien Colombelli, Perrine Paul-Gilloteaux

Licensed CC-BY-4.0



Tags: Metadata, Include In Dalia

Content type: Publication, Poster

[https://f1000research.com/posters/9-162](https://f1000research.com/posters/9-162)


---

## Effect of local topography on cell division of Staphylococci sp.

Sorzabal Bellido, Ioritz, Luca Barbieri, Beckett, Alison J., Prior, Ian A., Arturo Susarrey-Arce, Tiggelaar, Roald M., Jo Forthergill, Rasmita Raval, Diaz Fernandez, Yuri A.

Published 2021-05-16

Licensed CC-BY-4.0



Dataset.zip

This dataset includes the raw and annotated images used to train a Stardist 2D deep learning model for segmentation of surface attached S.aureus as described in Effect of local topography on cell division of Staphylococci sp.

&nbsp;

Stardist2d_Model.zip

Stardist 2D deep learning model for segmentation of surface attached S.aureus, obtained using the StarDist 2D ZeroCostDL4Mic notebook (v 1.12.3).

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/4765599](https://zenodo.org/records/4765599)

[https://doi.org/10.5281/zenodo.4765599](https://doi.org/10.5281/zenodo.4765599)


---

## Efficiently starting institutional research data management

Katarzyna Biernacka, Katrin Cortez, Kerstin Helbig

Published 2019-10-15

Licensed CC-BY-4.0



Researchers are increasingly often confronted with research data management (RDM) topics during their work. Higher education institutions therefore begin to offer services for RDM at some point to give support and advice. However, many groundbreaking decisions have to be made at the very beginning of RDM services. Priorities must be set and policies formulated. Likewise, the staff must first be qualified in order to provide advice and adequately deal with the manifold problems awaiting.
The FDMentor project has therefore bundled the expertise of five German universities with different experiences and levels of RDM knowledge to jointly develop strategies, roadmaps, guidelines, and open access training material. Humboldt-Universit&auml;t zu Berlin, Freie Universit&auml;t Berlin, Technische Universit&auml;t Berlin, University of Potsdam, and European University Viadrina Frankfurt (Oder) have worked together on common solutions that are easy to adapt. With funding of the German Federal Ministry of Education and Research, the collaborative project addressed four problem areas: strategy development, legal issues, policy development, and competence enhancement. The aim of the project outcomes is to provide other higher education institutions with the best possible support for the efficient introduction of research data management. Therefore, all project results are freely accessible under the CC-BY 4.0 international license. The early involvement of the community in the form of workshops and the collection of feedback has proven its worth: the FDMentor strategies, roadmaps, guidelines, and training materials are applied and adapted beyond the partner universities.

Tags: Research Data Management, Include In Dalia

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

Tags: Research Data Management, Data Protection, Include In Dalia

Content type: Slides

[https://zenodo.org/records/4748510](https://zenodo.org/records/4748510)

[https://doi.org/10.5281/zenodo.4748510](https://doi.org/10.5281/zenodo.4748510)


---

## End-to-End Tissue Microarray Image Analysis with Galaxy-ME

Cameron Watson, Allison Creason

Published 2023-02-14

Licensed CC-BY-4.0



This tutorial will demonstrate how to use the Galaxy multiplex imaging tools to process and analyze publicly available TMA test data provided by MCMICRO (Figure 1); however, the majority of the steps in this tutorial are the same for both TMAs and WSIs and notes are made throughout the tutorial where processing of these two imaging types diverge.

Tags: Galaxy, Multiplex Imaging, Include In Dalia

Content type: Tutorial

[https://training.galaxyproject.org/training-material/topics/imaging/tutorials/multiplex-tissue-imaging-TMA/tutorial.html#end-to-end-tissue-microarray-image-analysis-with-galaxy-me](https://training.galaxyproject.org/training-material/topics/imaging/tutorials/multiplex-tissue-imaging-TMA/tutorial.html#end-to-end-tissue-microarray-image-analysis-with-galaxy-me)


---

## Erstellung und Realisierung einer institutionellen Forschungsdaten-Policy

Uli Hahn, Kerstin Helbig, Gerald Jagusch, Jessica Rex

Published  2018-10-22

Licensed CC-BY-4.0



Die vorliegende Empfehlung sowie die zugehörigen Erfahrungsberichte geben einen Überblick über die verschiedenen Möglichkeiten der Gestaltung einer Forschungsdatenmanagement Policy sowie Wege zu deren Erstellung.

Tags: Research Data Management, Include In Dalia

Content type: Publication

[https://bausteine-fdm.de/article/view/7945](https://bausteine-fdm.de/article/view/7945)

[https://doi.org/10.17192/bfdm.2018.1.7945](https://doi.org/10.17192/bfdm.2018.1.7945)


---

## Euro-BioImaging  Scientific Ambassadors Program

Beatriz Serrano-Solano

Published 2023-07-25

Licensed CC-BY-4.0



Graduation presentation for the 7th cohort of the Open Seeds mentoring &amp; training program for Open Science ambassadors. The project presented is called &quot;Euro-BioImaging &nbsp;Scientific Ambassadors Program&quot;.

Tags: Exclude From Dalia

[https://zenodo.org/records/8182154](https://zenodo.org/records/8182154)

[https://doi.org/10.5281/zenodo.8182154](https://doi.org/10.5281/zenodo.8182154)


---

## Euro-BioImaging - EVOLVE Deliverable 6.2 - Landscape analysis of existing training resources for the Nodes

Euro-BioImaging ERIC

Published 2025-09-03

Licensed CC-BY-4.0



Horizon Europe funded EVOLVE Deliverable 6.2 - Landscape analysis of existing training resources for the Nodes
This version has&nbsp;not yet been reviewed or approved by the European Commission&nbsp;and is made publicly available for transparency and early community feedback.
A final, EC-approved version will be published when available.
This document presents a strategic analysis of training resources for Euro-BioImaging Nodes, assessing bothNode-organized and global opportunities. By analyzing Node-organized and externally available trainingcourses, alongside insights from recent surveys and training bursary applications, this report provides afoundation for strengthening the training framework of Euro-BioImagingDelivering high-quality imaging services relies on continuous skill development, particularly as scientificadvancements and technological innovations reshape the imaging landscape.&nbsp;

Tags: Include In Dalia

[https://zenodo.org/records/17048377](https://zenodo.org/records/17048377)

[https://doi.org/10.5281/zenodo.17048377](https://doi.org/10.5281/zenodo.17048377)


---

## Euro-BioImaging Annual Report 2020

Euro-BioImaging ERIC

Published 2025-07-23

Licensed CC-BY-4.0



Euro-BioImaging ERIC is the European landmark research infrastructure for biological and biomedical imaging as recognized by the European Strategy Forum on Research Infrastructures (ESFRI). Euro-BioImaging is the gateway to world-class imaging facilities across Europe. This document is the Euro-BioImaging Annual Report for the year 2020.

Tags: Exclude From Dalia

[https://zenodo.org/records/16357209](https://zenodo.org/records/16357209)

[https://doi.org/10.5281/zenodo.16357209](https://doi.org/10.5281/zenodo.16357209)


---

## Euro-BioImaging Annual Report 2021

Euro-BioImaging ERIC

Published 2022-06-30

Licensed CC-BY-4.0



Euro-BioImaging ERIC is the European landmark research infrastructure for biological and biomedical imaging as recognized by the European Strategy Forum on Research Infrastructures (ESFRI). Euro-BioImaging is the gateway to world-class imaging facilities across Europe. This document is the Euro-BioImaging Annual Report for the year 2021.

Tags: Exclude From Dalia

[https://zenodo.org/records/16357461](https://zenodo.org/records/16357461)

[https://doi.org/10.5281/zenodo.16357461](https://doi.org/10.5281/zenodo.16357461)


---

## Euro-BioImaging Annual Report 2023

Euro-BioImaging ERIC

Published 2024-06-30

Licensed CC-BY-4.0



Euro-BioImaging ERIC is the European landmark research infrastructure for biological and biomedical imaging as recognized by the European Strategy Forum on Research Infrastructures (ESFRI). Euro-BioImaging is the gateway to world-class imaging facilities across Europe. This document is the Euro-BioImaging Annual Report for the year 2023.

Tags: Exclude From Dalia

[https://zenodo.org/records/16323251](https://zenodo.org/records/16323251)

[https://doi.org/10.5281/zenodo.16323251](https://doi.org/10.5281/zenodo.16323251)


---

## Euro-BioImaging Annual Report 2024

Euro-BioImaging ERIC

Published 2025-06-30

Licensed CC-BY-4.0



Euro-BioImaging ERIC is the European landmark research infrastructure for biological and biomedical imaging as recognized by the European Strategy Forum on Research Infrastructures (ESFRI). Euro-BioImaging is the gateway to world-class imaging facilities across Europe. This document is the Euro-BioImaging Annual Report for the year 2024.

Tags: Exclude From Dalia

[https://zenodo.org/records/16761197](https://zenodo.org/records/16761197)

[https://doi.org/10.5281/zenodo.16761197](https://doi.org/10.5281/zenodo.16761197)


---

## Euro-BioImaging ERIC Annual Report 2022

Euro-BioImaging ERIC

Published 2023-07-14

Licensed CC-BY-4.0



Euro-BioImaging ERIC is the European landmark research infrastructure for biological and biomedical imaging as recognized by the European Strategy Forum on Research Infrastructures (ESFRI). Euro-BioImaging is the gateway to world-class imaging facilities across Europe. This document is the Euro-BioImaging Annual Report for the year 2022.

Tags: Exclude From Dalia

[https://zenodo.org/records/8146412](https://zenodo.org/records/8146412)

[https://doi.org/10.5281/zenodo.8146412](https://doi.org/10.5281/zenodo.8146412)


---

## Euro-BioImaging's Guide to FAIR BioImage Data - Practical Tasks

Isabel Kemmer, Euro-BioImaging ERIC

Published 2024-06-04

Licensed CC-BY-4.0



Hands-on exercises on FAIR Bioimage Data from the interactive online workshop "Euro-BioImaging's Guide to FAIR BioImage Data 2024" (https://www.eurobioimaging.eu/news/a-guide-to-fair-bioimage-data-2024/).&nbsp; Types of tasks included: FAIR characteristics of a real world dataset Data Management Plan (DMP) Journal Policies on FAIR data sharing Ontology search Metadata according to REMBI scheme (Image from: Sarkans, U., Chiu, W., Collinson, L. et al. REMBI: Recommended Metadata for Biological Images&mdash;enabling reuse of microscopy data in biology. Nat Methods 18, 1418&ndash;1422 (2021). https://doi.org/10.1038/s41592-021-01166-8) Matching datasets to bioimage repositories Browsing bioimage repositories

Tags: Bioimage Analysis, FAIR-Principles, Research Data Management, Include In Dalia

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

Tags: Bioimage Analysis, FAIR-Principles, Research Data Management, Exclude From Dalia

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


Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

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


Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/14014252](https://zenodo.org/records/14014252)

[https://doi.org/10.5281/zenodo.14014252](https://doi.org/10.5281/zenodo.14014252)


---

## Expansion and fluctuations-enhanced microscopy for nanoscale molecular profiling of cells and tissues - Data processing manual

Dominik Kylies, Heil, Hannah S., Vesga, Arturo G., Del Rosario, Mario, Maria Schwerk, Malte Kuehl, Wong, Milagros N., Victor Puelles, Ricardo Henriques

Published 2023/2024

Licensed CC-BY-4.0



Here we provide test datasets and a training manual for the parameter optimization with eSRRF.&nbsp;
The training manual will guide users through an eSRRF paramenter optimization routine and quantiative image quality assesment with both, the ImagJ-Plugin NanoJ-eSRRF (Chapter 1) and the python implementation NanoPyx-eSRRF (Chapter 2). By showcasing the optimization routine on three differnt test dataset (Chapter 3), providing intermediate results and expected outcome, the users can eaisily learn how to find the optimal processing parameters for eSRRF processing.
Three samples are provided to showcase the eSRRF reconstruction process:
1. Microtubules sample: Set01_DNA-PAINT_Microtubules.tif
DNA-PAINT microscopy measurement of immunolabeled microtubules in fixed COS-7 cells, showing 0.121 localizations per frame and &micro;m^2 (data published in Laine and Heil et al.)
108x90 pixels, 500 frames, pixel size: 160 nm&nbsp;
2. Kidney sample: Set02_KidneySDNephrinExM.tif
ExM of human kidney biopsies stained with nephrin (data published in Kylies et al.)
150x150 pixels, 200 frames, pixel size: 102 nm&nbsp;
3. Single emitters simulation: Set03_simulation_groundTruth_2p5Sigma - Fluorescence stack_Avg5.tif
Simulated individual molecules emitting placed on concentric rings with radii increasing by 220 nm steps. On each ring the molecules are separated by 57.5, 115, 173, 230, 288 and 345 nm, respectively (data published in&nbsp;Laine and Heil et al.)
33x33 pixels, 100 frames, pixel size: 100 nm&nbsp;
4. Test dataset for drift/vibration correction: Set04_ExSRRF_eSRRF_vibration_correction_practice_dataset.tif
EsM of human kidney biopsies stained with nephrin (data published in Kylies et al.)
100x100 pixels, 200 frames, pixel size: 102 nm
5. Test dataset for photobleaching: Set05_Photobleaching.tif
ExM of 120 nm Nanorulers (data published in Kylies et al.)
150x150 pixels, 75 frames, pixel size: 64 nm
&nbsp;
Jupyter-Notebook: ridge_detection.ipynb
With this notebook qantitative image analyis of sturctures resolved with ExSRRF can be performed.
Such as:

calculation of the target structure density.&nbsp;
identifying areas with high inter-ridge spacing by maping the distance to the nearest ridge based on Euclidean distance transform.&nbsp;
measuring the spatial uniformity of the structure of interest by&nbsp;examining the distribution of the local densities and the distances to the nearest ridge.&nbsp;


Tags: Include In Dalia

[https://zenodo.org/records/13897937](https://zenodo.org/records/13897937)

[https://doi.org/10.5281/zenodo.13897937](https://doi.org/10.5281/zenodo.13897937)


---

## Explainable AI for Computer Vision

Robert Haase

Published 2025-03-09

Licensed CC-BY-4.0



In this slide deck we learn about the basics of Explainable Artificial Intelligence with a soft focus on Computer Vision. We take a deeper dive in one method: Gradient Class Activation Maps.
Releated exercise materials are available online: https://haesleinhuepf.github.io/xai/

Tags: Nfdi4Bioimage, Bioimage Analysis, Artificial Intelligence, Include In Dalia

[https://zenodo.org/records/14996127](https://zenodo.org/records/14996127)

[https://doi.org/10.5281/zenodo.14996127](https://doi.org/10.5281/zenodo.14996127)


---

## FAIR BioImage Data

Licensed CC-BY-4.0



Tags: Research Data Management, Fair, Bioimage Analysis, Exclude From Dalia

Content type: Collection, Video

[https://www.youtube.com/watch?v=8zd4KTy-oYI&list=PLW-oxncaXRqU4XqduJzwFHvWLF06PvdVm](https://www.youtube.com/watch?v=8zd4KTy-oYI&list=PLW-oxncaXRqU4XqduJzwFHvWLF06PvdVm)


---

## FAIR High Content Screening in Bioimaging

Rohola Hosseini, Matthijs Vlasveld, Joost Willemse, Bob van de Water, Sylvia E. Le Dévédec, Katherine J. Wolstencroft

Published 2023-07-17

Licensed CC-BY-4.0



The authors show the utility of Minimum Information for High Content Screening Microscopy Experiments (MIHCSME) for High Content Screening (HCS) data using multiple examples from the Leiden FAIR Cell Observatory, a Euro-Bioimaging flagship node for high content screening and the pilot node for implementing FAIR bioimaging data throughout the Netherlands Bioimaging network.

Tags: FAIR-Principles, Metadata, Research Data Management, Exclude From Dalia

Content type: Publication

[https://www.nature.com/articles/s41597-023-02367-w](https://www.nature.com/articles/s41597-023-02367-w)


---

## FAIR Priciples

Licensed CC-BY-4.0



In 2016, the ‘FAIR Guiding Principles for scientific data management and stewardship’ were published in Scientific Data. The authors intended to provide guidelines to improve the Findability, Accessibility, Interoperability, and Reuse of digital assets.

Tags: FAIR-Principles, Data Stewardship, Research Data Management, Include In Dalia

Content type: Collection

[https://www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)


---

## FAIRy deep-learning for bioImage analysis

Estibaliz Gómez de Mariscal

Licensed CC-BY-4.0



Introduction to FAIR deep learning. Furthermore, tools to deploy trained DL models (deepImageJ), easily train and evaluate them (ZeroCostDL4Mic and DeepBacs) ensure reproducibility (DL4MicEverywhere), and share this technology in an open-source and reproducible manner (BioImage Model Zoo) are introduced.

Tags: Artificial Intelligence, FAIR-Principles, Bioimage Analysis, Include In Dalia

Content type: Slides

[https://f1000research.com/slides/13-147](https://f1000research.com/slides/13-147)


---

## FAQ Künstliche Intelligenz und gute wissenschaftliche Praxis

Katrin Frisch

Published 2024-11-06

Licensed CC-BY-4.0



Diese FAQ versammeln Fragen, die uns h&auml;ufig im Zusammenhang mit k&uuml;nstlicher Intelligenz (KI) und guter wissenschaftlicher Praxis (GWP) erreichen. Die Antworten sollen bei der Orientierung in einem schnelllebigen Thema helfen, ohne dabei pr&auml;skriptiv zu sein. Sie stellen keine offizielle Positionierung des Ombudsman f&uuml;r die Wissenschaft (OfdW) dar, sondern beschreiben den Status Quo und ordnen bereits bestehende Empfehlungen aus Sicht der GWP ein, identifizieren L&uuml;cken und verweisen auf weiterf&uuml;hrende Literatur. Diese FAQ-Sammlung richtet sich prim&auml;r an Forschende. F&uuml;r die Nutzung von KI in der Lehre und in studentischen (Qualifikations-)Arbeiten sind i.d.R. universit&auml;re KI-Richtlinien, angepasste Pr&uuml;fungsordnungen und Selbstst&auml;ndigkeitserkl&auml;rungen sowie Entscheidungen individueller Lehrpersonen ma&szlig;geblich. Daher werden eventuelle Besonderheiten von KI in der Lehre und in Pr&uuml;fungsangelegenheiten in diesen FAQ nicht besprochen.

Tags: Include In Dalia

[https://zenodo.org/records/14045172](https://zenodo.org/records/14045172)

[https://doi.org/10.5281/zenodo.14045172](https://doi.org/10.5281/zenodo.14045172)


---

## Fiber and vessel dataset for segmentation and characterization

Saqib Qamar, Baba, Abu Imran, Stèphane Verger, Magnus Andersson

Published 2024-05-03

Licensed CC-BY-4.0



This repository hosts a comprehensive collection of datasets used to develop an innovative deep learning model designed to enhance the segmentation and characterization of macerated fibers and vessel forms in microscopy images. Included in the deposit are raw images, alongside meticulously prepared training and validation datasets. We present an automated segmentation approach that utilizes the one-stage YOLOv8 model, which has been specifically adapted to process high-resolution microscopy images up to 32640 x 25920 pixels. Our model excels in cell detection and segmentation, demonstrating exceptional proficiency.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/10913446](https://zenodo.org/records/10913446)

[https://doi.org/10.5281/zenodo.10913446](https://doi.org/10.5281/zenodo.10913446)


---

## File Naming Convention Worksheet

Kristin Briney

Published 2020-06-02

Licensed CC-BY-4.0



This worksheet walks researchers through the process of creating a file naming convention for a group of files. This process includes: choosing metadata, encoding and ordering the metadata, adding version information, and properly formatting the file names. Two versions of the worksheet are available: a Caltech Library branded version and a generic editable version.

Tags: Research Data Management, Include In Dalia

Content type: Worksheet

[https://authors.library.caltech.edu/records/mmnpf-cez11](https://authors.library.caltech.edu/records/mmnpf-cez11)


---

## Finding and using publicly available data

Anna Swan

Published 2024-01-01

Licensed CC-BY-4.0



Sharing knowledge and data in the life sciences allows us to learn from each other and built on what others have discovered. This collection of online courses brings together a variety of training, covering topics such as biocuration, open data, restricted access data and finding publicly available data, to help you discover and make the most of publicly available data in the life sciences.

Tags: Open Science, Teaching, Sharing, Include In Dalia

Content type: Collection, Tutorial, Video

[https://www.ebi.ac.uk/training/online/courses/finding-using-public-data/](https://www.ebi.ac.uk/training/online/courses/finding-using-public-data/)


---

## Forschungsdaten.org

Licensed CC-BY-4.0



Research Data Management Wiki in German

Tags: Research Data Management, Include In Dalia

Content type: Collection

[https://www.forschungsdaten.org/](https://www.forschungsdaten.org/)


---

## Forschungsdatenmanagement zukunftsfest gestalten – Impulse für die   Strukturevaluation der Nationalen Forschungsdateninfrastruktur (NFDI)

Steuerungsgremium Allianz-Schwerpunkt, Alexander von Humboldt Foundation, Deutsche Forschungsgemeinschaft, Fraunhofer Society, German Rectors' Conference, Leibniz Association, German National Academy of Sciences Leopoldina, German Academic Exchange Service, Helmholtz Association of German Research Centres, Max Planck Society

Published 2024-11-04

Licensed CC-BY-4.0



Arbeitspapier des Steuerungsgremiums des Allianz-Schwerpunkts "Digitalit&auml;t in der Wissenschaft"

Tags: Exclude From Dalia

[https://zenodo.org/records/14032908](https://zenodo.org/records/14032908)

[https://doi.org/10.5281/zenodo.14032908](https://doi.org/10.5281/zenodo.14032908)


---

## From Cells to Pixels: Bridging Biologists and  Image Analysts Through a Common Language

Elnaz Fazeli, Haase Robert, Doube Michael, Miura Kota, Legland David

Published 2024-08-16

Licensed CC-BY-4.0



Bioimaging has transformed our understanding of biological processes, yet extracting&nbsp;meaningful information from complex datasets remains a challenge, particularly for&nbsp;early career scientists. This paper proposes a simplified, systematic approach to&nbsp;bioimage analysis, focusing on categorizing commonly observed structures and&nbsp;shapes, and providing relevant analysis methods. Our approach includes illustrative&nbsp;examples and a visual flowchart, enabling researchers to define analysis objectives&nbsp;clearly. By understanding the diversity of bioimage structures and aligning them with&nbsp;appropriate analysis approaches, the framework empowers researchers to navigate&nbsp;bioimage datasets more efficiently. It also aims to foster a common language between&nbsp;researchers and analysts, thereby enhancing mutual understanding and facilitating&nbsp;effective communication.

Tags: Include In Dalia

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

Tags: Research Data Management, Include In Dalia

Content type: Slides

[https://zenodo.org/records/11548617](https://zenodo.org/records/11548617)

[https://doi.org/10.5281/zenodo.11548617](https://doi.org/10.5281/zenodo.11548617)


---

## From bioimaging projects to communities - GloBIAS BIA Seminar Series

Aastha Mathur, Euro-BioImaging ERIC

Published 2025-07-29

Licensed CC-BY-4.0



This presentaiton sumarises Euro-BioImaging ERIC services, focussing on their Image Data Services. It briefly presents processes and challenges in image anlaysis service provison and introduces some supporting tools. It also emphasises the roll of community initiatives and networks in providing solutions and support towards Image data management and analysis. This presentaiton was part of the GloBIAS BioImage Analysis Seminar Series.
Date of presentation: 2025-07-24

Tags: Include In Dalia

[https://zenodo.org/records/16573999](https://zenodo.org/records/16573999)

[https://doi.org/10.5281/zenodo.16573999](https://doi.org/10.5281/zenodo.16573999)


---

## Galaxy Training

Published None

Licensed CC-BY-4.0



Collection of tutorials developed and maintained by the worldwide Galaxy community.

Tags: Bioimage Analysis, Data Analysis, Exclude From Dalia

Content type: Collection, Tutorial

[https://training.galaxyproject.org/](https://training.galaxyproject.org/)


---

## Galaxy meets OMERO! Overview on the Galaxy OMERO-suite and Vizarr Viewer

Riccardo Massei, Matthias Bernt, Beatriz Serrano-Solano, Lucille Lopez-Delisle, Jan Bumberger, Björn Grüning, Leonid Kostrykin

Published 2025-03-05

Licensed CC-BY-4.0



Tags: Include In Dalia

[https://zenodo.org/records/14975462](https://zenodo.org/records/14975462)

[https://doi.org/10.5281/zenodo.14975462](https://doi.org/10.5281/zenodo.14975462)


---

## Generative artificial intelligence for bio-image analysis

Robert Haase

Licensed CC-BY-4.0



Tags: Python, Bioimage Analysis, Artificial Intelligence, Include In Dalia

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

Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/13807114](https://zenodo.org/records/13807114)

[https://doi.org/10.5281/zenodo.13807114](https://doi.org/10.5281/zenodo.13807114)


---

## Getting started with Mambaforge and Python

Mara Lampert

Licensed CC-BY-4.0



Tags: Python, Conda, Mamba, Include In Dalia

Content type: Blog Post

[https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html)


---

## Getting started with Python: intro and set-up a conda environment

Riccardo Massei

Published 2024-10-09

Licensed CC-BY-4.0



YMIA python event 2024
Presentation :&nbsp; "Getting started with Python: intro and set-up a conda environment with Dr. Riccardo Massei"

Tags: Include In Dalia

[https://zenodo.org/records/13908480](https://zenodo.org/records/13908480)

[https://doi.org/10.5281/zenodo.13908480](https://doi.org/10.5281/zenodo.13908480)


---

## GloBIAS in-person workshop 2024

Christa Walther

Published 2025-04-07

Licensed CC-BY-4.0



This document reports on the first in-person workshop supported by GloBIAS. Each session has its own chapter provided by the people chairing the sessions, summarising the outputs achieved.&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/15168241](https://zenodo.org/records/15168241)

[https://doi.org/10.5281/zenodo.15168241](https://doi.org/10.5281/zenodo.15168241)


---

## Ground-truth cell body segmentation used for Starfinity training

Yuhan Wang, Martin Weigert, Uwe Schmidt, Stephan Saalfeld, Eugene W. Myers, Tim Wang, Karel Svoboda, Mark Eddison, Greg Fleishman, Shengjin Xu, Fredrick E. Henry, Andrew L. Lemire, Hui Yang, Konrad Rokicki, Cristian Goina, Eugene W Myers, Wyatt Korff, Scott M. Sternson, Paul W. Tillberg

Published 2021-03-05

Licensed CC-BY-4.0



Accurate segmentation of volumetric fluorescence image data has been a long-standing challenge and it can considerably degrade the accuracy of multiplexed fluorescence in situ hybridization (FISH) analysis. To overcome this challenge, we developed a deep learning-based automatic 3D segmentation algorithm, called Starfinity. It first predicts its cell center probability and its radial distances to the nearest cell borders for each pixel. It then aggregates pixel affinity maps from the densely predicted distances and applies a watershed segmentation on the affinity maps using the thresholded center probability as seeds.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://janelia.figshare.com/articles/dataset/Ground-truth_cell_body_segmentation_used_for_Starfinity_training/13624268](https://janelia.figshare.com/articles/dataset/Ground-truth_cell_body_segmentation_used_for_Starfinity_training/13624268)


---

## Guidance for Developing a Research Data Management (RDM) Policy

Published 2017

Licensed CC-BY-4.0



This document provides the essential elements of a Research Data Management (RDM) Policy and is part of the LEARN Toolkit containing the Model Policy for Research Data Management (RDM) at Research Institutions/Institutes.

Tags: Research Data Management, Include In Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/13739137](https://zenodo.org/records/13739137)

[https://doi.org/10.5281/zenodo.13739137](https://doi.org/10.5281/zenodo.13739137)


---

## Gut Analysis Toolbox: Training data and 2D models for segmenting enteric neurons, neuronal subtypes and ganglia

Luke Sorensen, Ayame Saito, Sabrina Poon, Myat Noe Han, Adam Humenick, Peter Neckel, Keith Mutunduwe, Christie Glennan, Narges Mahdavian, Simon JH Brookes, Rachel M McQuade, Jaime PP Foong, Sebastian K. King, Estibaliz  Gómez-de-Mariscal, Arrate Muñoz-Barrutia, Robert Haase, Simona Carbone, Nicholas A. Veldhuis, Daniel P. Poole, Pradeep Rajasekhar

Published 2025-05-01

Licensed CC-BY-4.0



This upload is associated with the software, Gut Analysis Toolbox&nbsp;(GAT).
If you use it please cite:
Sorensen et al.&nbsp;Gut Analysis Toolbox: Automating quantitative analysis of enteric neurons.&nbsp;J Cell Sci&nbsp;2024; jcs.261950. doi:&nbsp;https://doi.org/10.1242/jcs.261950
The upload contains StarDist models for segmenting enteric neurons in 2D, enteric neuronal subtypes in 2D and FPN+ResNet101 model for enteric ganglia in 2D in gut wholemount tissue. GAT is implemented in Fiji, but the models can be used in any software that supports StarDist and the use of 2D UNet models.&nbsp;The files here also consist of&nbsp;Python notebooks (Google Colab), training and test data as well as reports on model performance.
Note: The enteric ganglia model is has been updated to v3 which uses pytorch and is a different architecture (FPN+ResNet101).
The model files are located in the respective folders as zip files. The folders have also been zipped:

Neuron (Hu; StarDist&nbsp;model):

Main folder: 2D_enteric_neuron_model_QA.zip
StarDist Model File:2D_enteric_neuron_v4_1.zip&nbsp;
DeepImageJ compatible model: 2D_enteric_neuron.bioimage.io.model.zip (used currently in GAT)


Neuronal subtype (StarDist&nbsp;model):&nbsp;

Main folder: 2D_enteric_neuron_subtype_model_QA.zip
Model File: 2D_enteric_neuron_subtype_v4.zip
DeepImageJ compatible model: 2D_enteric_neuron_subtype.bioimage.io.model.zip (used currently in GAT)


Enteric ganglia (2D FPN_ResNet101; Use in FIJI with&nbsp;deepImageJ)

Main folder: 2D_enteric_ganglia_v3_training.zip
Model File: 2D_Ganglia_RGB_v3.bioimage.io.model.zip (used currently in GAT)



For the all models, files included are:

Model for segmenting cells or ganglia in 2D FIJI. StarDist or 2D UNet.
Training and Test datasets used for training.
Google Colab notebooks used for training and quality assurance (ZeroCost DL4Mic notebooks).
Python notebook and code for training ganglia model with QA.
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

Additional images for new ganglia model:

Hamnett, R., Dershowitz, L. B., Sampathkumar, V., Wang, Z., Gomez-Frittelli, J., De Andrade, V., Kasthuri, N., Druckmann, S. and Kaltschmidt, J. A. (2022b). Regional cytoarchitecture of the adult and developing mouse enteric nervous system. Curr. Biol. 32, 4483-4492.e5.

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

Tags: Exclude From Dalia

[https://zenodo.org/records/15314214](https://zenodo.org/records/15314214)

[https://doi.org/10.5281/zenodo.15314214](https://doi.org/10.5281/zenodo.15314214)


---

## HPA Nucleus Segmentation (DPNUnet)

Hao Xu, Wei Ouyang

Published 2023-03-02

Licensed CC-BY-4.0



Download RDF Package

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/7690494](https://zenodo.org/records/7690494)

[https://doi.org/10.5281/zenodo.7690494](https://doi.org/10.5281/zenodo.7690494)


---

## HT1080WT cells embedded in 3D collagen type I matrices - manual annotations for cell instance segmentation and tracking

Estibaliz Gómez-de-Mariscal, Hasini Jayatilaka, Denis Wirtz, Arrate Muñoz-Barrutia

Published 2021-12-13

Licensed CC-BY-4.0



Human fibrosarcoma HT1080WT (ATCC) cells at low cell densities embedded in 3D collagen type I matrices [1]. The time-lapse videos were recorded every 2 minutes for 16.7 hours and covered a field of view of 1002 pixels &times; 1004 pixels with a pixel size of 0.802 &mu;m/pixel The videos were pre-processed to correct frame-to-frame drift artifacts, resulting in a final size of 983 pixels &times; 985 pixels pixels.

Hasini Jayatilaka, Anjil Giri, Michelle Karl, Ivie Aifuwa, Nicholaus J Trenton, Jude M Phillip, Shyam Khatau, and Denis Wirtz. EB1 and cytoplasmic dynein mediate protrusion dynamics for efficient 3-dimensional cell migration. FASEB J., 32(3):1207&ndash;1221, 2018. ISSN 0892-6638. doi: 10.1096/fj.201700444RR.

Further information about how to use this data is given in&nbsp;https://github.com/esgomezm/microscopy-dl-suite-tf

This dataset is provided together with the following preprint and if you use it, we would like to kindly ask you to cite it properly:

Estibaliz G&oacute;mez-de-Mariscal, Hasini Jayatilaka, &Ouml;zg&uuml;n &Ccedil;i&ccedil;ek, Thomas Brox, Denis Wirtz, Arrate Mu&ntilde;oz-Barrutia, *Search for temporal cell segmentation robustness in phase-contrast microscopy videos*, arXiv 2021 (arXiv:2112.08817)

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/5979761](https://zenodo.org/records/5979761)

[https://doi.org/10.5281/zenodo.5979761](https://doi.org/10.5281/zenodo.5979761)


---

## Hackaton Results - Conversion of KNIME image analysis workflows to Galaxy

Riccardo Massei

Published 2024-03-07

Licensed CC-BY-4.0



Results of the project "Conversion of KNIME image analysis workflows to Galaxy" during the Hackathon "Image Analysis in Galaxy" (Freiburg 26 Feb - 01 Mar 2024)
&nbsp;

Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/6139958](https://zenodo.org/records/6139958)

[https://doi.org/10.5281/zenodo.6139958](https://doi.org/10.5281/zenodo.6139958)


---

## High throughput & automated data analysis and data management workflow with Cellprofiler and OMERO

Sarah Weischer, Jens Wendt, Thomas Zobel

Licensed CC-BY-4.0



In this workshop a fully integrated data analysis solutions employing OMERO and commonly applied image analysis tools (e.g., CellProfiler, Fiji) using existing python interfaces (OMERO Python language bindings, ezOmero, Cellprofiler Python API) is presented.

Tags: OMERO, Data Analysis, Bioimage Analysis, Include In Dalia

Content type: Collection

[https://zenodo.org/doi/10.5281/zenodo.8139353](https://zenodo.org/doi/10.5281/zenodo.8139353)


---

## Highlights from the 2016-2020 NEUBIAS training schools for Bioimage Analysts: a success story and key asset for analysts and life scientists

Gabriel G. Martins, Fabrice P. Cordelières, Julien Colombelli, Rocco D’Antuono, Ofra Golani, Romain Guiet, Robert Haase, Anna H. Klemm, Marion Louveaux, Perrine Paul-Gilloteaux, Jean-Yves Tinevez, Kota Miura

Published 2021

Licensed CC-BY-4.0



Tags: Bioimage Analysis, Neubias, Include In Dalia

Content type: Publication

[https://f1000research.com/articles/10-334/v1](https://f1000research.com/articles/10-334/v1)


---

## Hitchhiking through a diverse Bio-image Analysis Software Universe

Robert Haase

Published 2022-07-22

Licensed CC-BY-4.0



Overview about decision making and how to influence decisions in the bio-image analysis software context.

Tags: Bioimage Analysis, Exclude From Dalia

Content type: Slides, Presentation

[https://f1000research.com/slides/11-746](https://f1000research.com/slides/11-746)

[https://doi.org/10.7490/f1000research.1119026.1](https://doi.org/10.7490/f1000research.1119026.1)


---

## Human DAB staining Axioscan BF 20x

Mario Garcia

Published 2024-05-21

Licensed CC-BY-4.0



Human brain tissue with DAB immunostaining. Image acquired by BF microscopy in&nbsp; Zeiss Axioscan at 20x.&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/11234863](https://zenodo.org/records/11234863)

[https://doi.org/10.5281/zenodo.11234863](https://doi.org/10.5281/zenodo.11234863)


---

## I3D:bio's OMERO training material: Re-usable, adjustable, multi-purpose slides for local user training

Christian Schmidt, Michele Bortolomeazzi, Tom Boissonnet, Carsten Fortmann-Grote, Julia Dohle, Peter Zentis, Niraj Kandpal, Susanne Kunis, Thomas Zobel, Stefanie Weidtkamp-Peters, Elisa Ferrando-May

Published 2023-11-13

Licensed CC-BY-4.0



The open-source software OME Remote Objects (OMERO) is a data management software that allows storing, organizing, and annotating bioimaging/microscopy data. OMERO has become one of the best-known systems for bioimage data management in the bioimaging community. The Information Infrastructure for BioImage Data (I3D:bio) project facilitates the uptake of OMERO into research data management (RDM) practices at universities and research institutions in Germany. Since the adoption of OMERO into researchers' daily routines requires intensive training, a broad portfolio of training resources for OMERO is an asset. On top of using the OMERO guides curated by the Open Microscopy Environment Consortium (OME) team, imaging core facility staff at institutions where OMERO is used often prepare additional material tailored to be applicable for their own OMERO instances. Based on experience gathered in the Research Data Management for Microscopy group (RDM4mic) in Germany, and in the use cases in the I3D:bio project, we created a set of reusable, adjustable, openly available slide decks to serve as the basis for tailored training lectures, video tutorials, and self-guided instruction manuals directed at beginners in using OMERO. The material is published as an open educational resource complementing the existing resources for OMERO contributed by the community.

Tags: OMERO, Research Data Management, Nfdi4Bioimage, I3Dbio, Include In Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/11637422](https://zenodo.org/records/11637422)

[https://doi.org/10.5281/zenodo.11637422](https://doi.org/10.5281/zenodo.11637422)


---

## If you license it, it’ll be harder to steal it. Why we should license our work

Robert Haase

Licensed CC-BY-4.0



Blog post about why we should license our work and what is important when choosing a license.

Tags: Licensing, Research Data Management, Include In Dalia

Content type: Blog Post

[https://focalplane.biologists.com/2023/05/06/if-you-license-it-itll-be-harder-to-steal-it-why-we-should-license-our-work/](https://focalplane.biologists.com/2023/05/06/if-you-license-it-itll-be-harder-to-steal-it-why-we-should-license-our-work/)


---

## Image Analysis Training Resources

Licensed CC-BY-4.0



Tags: Neubias, Bioimage Analysis, Include In Dalia

Content type: Book

[https://neubias.github.io/training-resources/](https://neubias.github.io/training-resources/)


---

## Image Analysis in Healthcare - The Current Landscape, Trends, and Collaborative Opportunities

Martin Schätz, Pérez Koldenkova, Vadim

Published 2025-09-09

Licensed CC-BY-4.0



Workshop presentation from XXXIV Foro de Investigaci&oacute;n en Salud 2025.

Tags: Include In Dalia

[https://zenodo.org/records/17080219](https://zenodo.org/records/17080219)

[https://doi.org/10.5281/zenodo.17080219](https://doi.org/10.5281/zenodo.17080219)


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

Tags: Include In Dalia

[https://zenodo.org/records/14944040](https://zenodo.org/records/14944040)

[https://doi.org/10.5281/zenodo.14944040](https://doi.org/10.5281/zenodo.14944040)


---

## Image Processing with Python

Mark Meysenburg, Toby Hodges, Dominik Kutra, Erin Becker, David Palmquist, et al.

Licensed CC-BY-4.0



This lesson shows how to use Python and scikit-image to do basic image processing.

Tags: Bioimage Analysis, Python, Include In Dalia

Content type: Tutorial, Workflow

[https://datacarpentry.org/image-processing/key-points.html](https://datacarpentry.org/image-processing/key-points.html)


---

## Image Repository Decision Tree - Where do I deposit my imaging data

Isabel Kemmer, Feriel Romdhane, Euro-BioImaging ERIC

Published 2025-05-15

Licensed CC-BY-4.0



Depositing data in quality data repositories is one crucial step towards FAIR (Findable, Accessible, Interoperable, and Reusable) data. Accordingly, Euro-BioImaging strongly encourages sharing scientific imaging data in established, thematic repositories.&nbsp;
To guide you in the selection of appropriate repositories, we have created an overview of available repositories for different types of image data, including their scope and requirements. This decision tree guides you through questions about your data and directs you to the correct repository, and/or provides instructions for further processing to meet the critera of the repositories.&nbsp;
Three seperate trees are provided for different classes of imaging data: open bioimage data, preclinical data, and human imaging data. These versions with three trees can be used for web-view. Update: also the editable versions in powerpoint format (.pptx) are now provided. Please be aware that opening the versions with another program might lead to shifted formatting.
Update: we now also provide ready-to-print versions designed to be printed on A3 format. One page shows the open bioimaging data tree and one page combines the preclinical and human imaging data trees. Also the editable versions of these are provided.

Tags: Include In Dalia

[https://zenodo.org/records/15425770](https://zenodo.org/records/15425770)

[https://doi.org/10.5281/zenodo.15425770](https://doi.org/10.5281/zenodo.15425770)


---

## ImageJ Bioformats 8.3.0 Importer Incorrectly Reading ND2 Metadata

Snyder, Erika, Erika Thomas, Erika T.

Published 2025-08-21

Licensed CC-BY-4.0



Hi all,I was referred to this community from the Image.sc Forum original post: https://forum.image.sc/t/imagej-bioformats-importer-incorrectly-reading-metadata/115943
I have an ND2 file, 3 color channels, 2 positions in the well, and 81 timepoints. However, when I open this as I normally would in ImageJ as a hyperstack, the stack interpretation is totally incorrect. It is including my Z-positions as frames in the timelapse. Even when I open the series for the positions independently, images from the other series will appear within it. I am running Bioformats 8.3.0.&nbsp;
I have tried swapping dimensions. That did not work. I have tried creating substacks to parse out one series from the other, this also did not work.
The only thing I can think of that is different from before is that I was previously aquiring z-stacks with our MCL nanodrive Piezo, and we had to have that serviced so in the meantime I used the Ti2 eclipse camera drive for z-stack aquisiton. I have opened the metadata to compare aquisitions between the two, and the stack order appears exactly the same, although Bioformats has no problem reading the metadata for aquisitions with the Piezo. I have also opened this file in NIS elements viewer, and all the information for the stacks appears correctly, so I dont think aquisitions is the issue.
I have also tried opening this file on multiple computers with multiple versions of imageJ, and the issue persists.
Any advice would be greatly appreciated I am panicking a bit because this is a few months worth of data I am suddenly not able to analyze.&nbsp;
Please let me know if there's anything else needed to help figure this out.&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/16921650](https://zenodo.org/records/16921650)

[https://doi.org/10.5281/zenodo.16921650](https://doi.org/10.5281/zenodo.16921650)


---

## ImageJ tool for percentage estimation of pneumonia in lungs

Martin Schätz, Olga Rubešová, Jan Mareš, Alan Spark

Published 2025-07-07

Licensed CC-BY-4.0



The software tool is developed on demand of Radiological Department of Faculty Hospital of Kr&aacute;lovsk&eacute; Vinohrady, with the aim to provide a tool to estimate the percentage of pneumonia (or COVID-19 presence) in lungs. Paper&nbsp;Estimation of Covid-19 lungs damage based on computer tomography images analysis presenting the tool is available on F1000reserach&nbsp;DOI: 10.12688/f1000research.109020.1. The underlying dataset is published in Zenodo (DOI:10.5281/zenodo.5805939).&nbsp;One of the challenges was to design a tool that would be available without complicated install procedures and would process data in a reasonable time even on office computers. For this reason, 8-bit and 16-bit version of the tool exists. The FIJI software (or ImageJ with Bio-Formats plugin installed) was selected as the best candidate. Examples of use and tutorials are available at GitHub.&nbsp;
The third version includes an intra-variabilty analysis, containing evaluation both for percentage and score metrics.
Underlying data:DOI:10.5281/zenodo.5805939The first five datasets are analyzed using this tool, with results and parameters to repeat the analysis in results_csv.csv or results.xlsx.
Contributions:Martin SCH&Auml;TZ:&nbsp; &nbsp; &nbsp; &nbsp;Coding, tool testing, data curation, data set analysisOlga RUBE&Scaron;OV&Aacute;:&nbsp; &nbsp; Code review, tutorial preparation, tool testing, data set analysisJan MARE&Scaron;:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Tool testing, data set analysis, funding acquisitionAlan SPARK:&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Tool testing
The work was funded by the Ministry of Education, Youth and Sports by grant &lsquo;Development of Advanced Computational Algorithms for evaluating post-surgery rehabilitation&rsquo; number LTAIN19007. The work was also supported from the grant of Specific university research &ndash; grant No FCHI 2022-001.
&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/15827771](https://zenodo.org/records/15827771)

[https://doi.org/10.5281/zenodo.15827771](https://doi.org/10.5281/zenodo.15827771)


---

## Images acquired with Zeiss Sigma 300 - Images with low magnification are corrently not handeled correctly

Johannes Preußner

Published 2025-08-07

Licensed CC-BY-4.0



When using bioformats the images are not scaled correctly. The problem arises with low magnifications where the lengths in the metadata are given in &micro;m (not in nm). Attached are two pictures. Only with the picture with the ending &ldquo;Correct_scale_bar&rdquo; the import is working correctly. One issue might be that the metadata information of the images are stored in iso-8859-1&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/16760282](https://zenodo.org/records/16760282)

[https://doi.org/10.5281/zenodo.16760282](https://doi.org/10.5281/zenodo.16760282)


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

Tags: Exclude From Dalia

[https://zenodo.org/records/14777242](https://zenodo.org/records/14777242)

[https://doi.org/10.5281/zenodo.14777242](https://doi.org/10.5281/zenodo.14777242)


---

## Increasing the FAIRness of electron microscopy data in life and material science research

Cornelia Wetzker

Published 2025-08-31

Licensed CC-BY-4.0



The poster introduces the consortium NFDI4BIOIMAGE and presents tools of research data management in microscopy to increase the FAIRness of data at the Microscopy Conference in Karlsruhe 2025. On site, it is presented in booth 57 for joint introduction of the national research data infrastructure (NFDI) consortia matWERK, FAIRmat and NFDI4BIOIMAGE.
C.W. is funded by the German consortium NFDI4BIOIMAGE (Deutsche Forschungsgemeinschaft, grant number NFDI 46/1, project number 501864659).

Tags: Nfdi4Bioimage, Include In Dalia

[https://zenodo.org/records/17014253](https://zenodo.org/records/17014253)

[https://doi.org/10.5281/zenodo.17014253](https://doi.org/10.5281/zenodo.17014253)


---

## Insights and Impact From Five Cycles of Essential Open Source Software for Science

Kate Hertweck, Carly Strasser, Dario Taraborelli

Licensed CC-BY-4.0



Open source software (OSS) is essential for advancing scientific discovery, particularly in biomedical research, yet funding to support these vital tools has been limited. The Chan Zuckerberg Initiative's Essential Open Source Software for Science (EOSS) program has significantly contributed to this field by providing $51.8 million in funding over five years to support the maintenance, growth, and community engagement of critical OSS tools. The program has impacted scientific OSS projects by improving their technical outputs, community building, and sustainability practices, and fostering collaborations within the OSS community. Additionally, EOSS funding has enhanced diversity, equity, and inclusion within the OSS community, although changes in principal investigator demographics were not observed. The funded projects have had a substantial impact on biomedical research by improving the usability and accessibility of scientific software, which has led to increased adoption and advancements in various biomedical fields.

Tags: Open Source Software, Funding, Sustainability, Exclude From Dalia

Content type: Publication

[https://zenodo.org/records/11201216](https://zenodo.org/records/11201216)

[https://doi.org/10.5281/zenodo.11201216](https://doi.org/10.5281/zenodo.11201216)


---

## Insights from Acquiring Open Medical Imaging  Datasets for Foundation Model Development

Stefan Dvoretskii

Published 2024-04-10

Licensed CC-BY-4.0



Tags: Exclude From Dalia

[https://zenodo.org/records/11503289](https://zenodo.org/records/11503289)

[https://doi.org/10.5281/zenodo.11503289](https://doi.org/10.5281/zenodo.11503289)


---

## Insights from Acquiring Open Medical Imaging Datasets for Foundation Model Development

Stefan Dvoretskii

Published 2024-04-10

Licensed CC-BY-4.0



Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/12699637](https://zenodo.org/records/12699637)

[https://doi.org/10.5281/zenodo.12699637](https://doi.org/10.5281/zenodo.12699637)


---

## Interactive Bioimage Analysis Workflow with CLIJ (@EABIAS 2025 training event)

Wei-Chen Chu

Published 2025-03-23

Licensed CC-BY-4.0



Presentation file used in the EABIAS training event:&nbsp;EABIAS/2025-ImageJ-Micro-Image-Analysis-and-Programming_Taipei (Lesson_04)Video Recording (in Mandarin): https://www.youtube.com/watch?v=uheSMSENnzE

Tags: Include In Dalia

[https://zenodo.org/records/15070246](https://zenodo.org/records/15070246)

[https://doi.org/10.5281/zenodo.15070246](https://doi.org/10.5281/zenodo.15070246)


---

## Interactive Image Data Flow Graphs

Martin Schätz

Published 2022-10-17

Licensed CC-BY-4.0



The slides were presented during the Macro programming with ImageJ workshop (https://www.16mcm.cz/programme/#workshops) which was part of the&nbsp;16th Multinational Congress on Microscopy. It is a collection and &quot;reshuffle&quot; of slides originally made by Robert Haase on topics from Image Analysis in general up to&nbsp;User-friendly GPU-accelerated bio-image analysis and CLIJ2.

Tags: Include In Dalia

[https://zenodo.org/records/7215114](https://zenodo.org/records/7215114)

[https://doi.org/10.5281/zenodo.7215114](https://doi.org/10.5281/zenodo.7215114)


---

## Internal ALM BioImage Analysis workshop 2023

Martin Schätz, Maria Azevedo, Paula Sampaio

Published 2023-11-03

Licensed CC-BY-4.0



Internal ALM BioImage Analysis Workshop 2023OverviewThe Internal ALM BioImage Analysis Workshop 2023, organized by the Advanced Light Microscopy i3S scientific platform, was a comprehensive 2.5-day internal workshop dedicated to open-source BioImage Analysis. The event combined informative presentations with hands-on sessions, utilizing the EMBL Bioimage Analysis Desktop (BAND) Platform. The used sources for datasets and presentations are in Notes.Workshop ProgramDay 1: Foundations of BioImage AnalysisIntroduction to Research Data Management [00i3S_Data_Management_2023_MP_Slido]: An exploration of data management, naming conventions, and ethical considerations in BioImage Analysis and image manipulation. Referencing content from the NEUBIASAcademy@Home Webinar: "In Defense of Image Data &amp; Analysis Integrity."Interactive Image Data Flow Graphs with CLIJ2 in FIJI [01i3S_Interactive Image Data Flow Graphs]: A hands-on session introducing CLIJ2 in FIJI, with a focus on practical applications. Relevant datasets were explored during the presentation, and are described in notes.Day 2: Advanced Techniques in BioImage AnalysisNoise2Void Denoising with CSBdeep in FIJI [02i3S_IMCF_noise2void_EN] : Exploring the Noise2Void denoising approach using the CSBdeep FIJI plugin, with hands-on examples using data from the juglab/n2v GitHub repository.StarDist for Fluorescence Nuclei Segmentation [03i3S_schatzm_stardist_21] : An introduction to StarDist through the FIJI StarDist plugin, with hands-on experience using the BBBC004 dataset.Introduction to Napari 2023 [04i3S_Introduction to Napari 2023] : A hands-on session introducing Napari and its connection with CLIJ2. The datasets used were detailed in the presentation.Ilastik Pixel Classification and BioImage Model Zoo [05i3S_schatzm_Ilastik_woHandOn_PixObj_2023]: Hands-on exploration of Ilastik with a focus on pixel and object classification. Neural networks from the BioImage Model Zoo were also introduced.BioImage Model Zoo Possibilities [06i3S_BioImageModelZoo-Kreshuk]: An overview of the concept of BioImage Model Zoo and its potential applications.DeepImageJ Plugin with Hands-on on Stardist and Unet NNs [07i3S_deepImageJ-Gomez_de_Mariscal]: Introduction to the deepImageJ plugin, capable of utilizing models from the BioImage Model Zoo. The hands-on session focused on Stardist and Unet Neural Networks.Day 3: Practical Applications and Advanced TrainingHands-on with Ilastik Neural Networks: Utilizing BioImage Model Zoos, participants engaged in hands-on exercises using the Ilastik Multicut method from the AdvanceImageAnalysisEMBO2023 GitHub repository.Hands-on with Cellpose 2.0: Practical sessions included applying pre-trained models with the Simple Visual Cellpose Cheat Sheet. Participants also had the opportunity to train new models using original Cellpose datasets and larger data from BBBC019 and BBBC003 datasets.&nbsp;This workshop would not be possible without the previous excellent work of many people involved in the Network of European BioImage Analysts - NEUBIAS and without my attendance at the EMBO Practical Course Advanced methods in bioimage analysis .

Tags: Include In Dalia

[https://zenodo.org/records/10205578](https://zenodo.org/records/10205578)

[https://doi.org/10.5281/zenodo.10205578](https://doi.org/10.5281/zenodo.10205578)


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

Tags: Exclude From Dalia

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

Tags: Nfdi4Bioimage, Exclude From Dalia

[https://zenodo.org/records/14832855](https://zenodo.org/records/14832855)

[https://doi.org/10.5281/zenodo.14832855](https://doi.org/10.5281/zenodo.14832855)


---

## Introduction to Bioimage Analysis

Pete Bankhead

Licensed CC-BY-4.0



Tags: Python, Imagej, Bioimage Analysis, Include In Dalia

Content type: Book, Notebook

[https://bioimagebook.github.io/index.html](https://bioimagebook.github.io/index.html)


---

## Introduction to High Performance Computing for Life Scientists

Julien Sindt

Published 2021-03-22

Licensed CC-BY-4.0



This course introduces life science researchers to high-performance computing (HPC), covering essential concepts and providing hands-on experience using the UK’s ARCHER2 supercomputing service. It aims to help participants understand how HPC can benefit their research and prepare them to use it effectively for tasks like biomolecular simulation.

Tags: High Performance Computing, Include In Dalia

Content type: Github Repository

[https://epcced.github.io/20210322-intro-hpc-life-scientists/](https://epcced.github.io/20210322-intro-hpc-life-scientists/)


---

## Introduction to OMERO - Frankfurt - online

Michele Bortolomeazzi, Tom Boissonnet

Published 2025-04-05

Licensed CC-BY-4.0



These slides were presented during an online introductory session to OMERO for the UB Frankfurt.
The two-hour session consisted of a first part highlighting the benefits that image data management brings to the lab. The second part showcased image analysis workflows with a Fiji macro and a Python notebook.
&nbsp;

Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

[https://zenodo.org/records/15152576](https://zenodo.org/records/15152576)

[https://doi.org/10.5281/zenodo.15152576](https://doi.org/10.5281/zenodo.15152576)


---

## Introduction to Research Data Management and Open Research

Shanmugasundaram

Published 2024-05-17

Licensed CC-BY-4.0



Introduction to RDM primarily for researchers. Can be seen as primer to all other materials in this catalogue.

Tags: Research Data Management, Open Science, Include In Dalia

Content type: Slides

[https://zenodo.org/records/4778265](https://zenodo.org/records/4778265)

[https://doi.org/10.5281/zenodo.4778265](https://doi.org/10.5281/zenodo.4778265)


---

## JIPipe Spring Course (JSC) 2025: Workshop Recordings, Slides, Homework, and Materials

Ruman Gerst, Zoltán Cseresnyés, Marc Thilo Figge

Published 2025-05-12:T13:37:00+00:00

Licensed CC-BY-4.0



The course gives a basic introduction into microscopy, optics, and image analysis. This is followed by interactive tutorials that explain the basics of creating fully automated image analysis workflows in JIPipe using a simple blobs analysis and intermediate-level quantification of LSFM kidney images. JIPipe-specific features including annotation-guided batch processing, organization with graph compartments, expressions and path processing, and project-wide metadata and parameters are also established. Finally, an advanced real-world pipeline is showcased with detailed guidance through the individual components that include integrations of Cellpose and TrackMate.

Tags: Nfdi4Bioimage, Jipipe, Bioimage Analysis, Include In Dalia

Content type: Workshop, Video, Tutorial, Slides

[https://doi.org/10.5281/zenodo.15373555](https://doi.org/10.5281/zenodo.15373555)


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

Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

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

Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

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

Tags: Exclude From Dalia

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


Tags: Research Data Management, FAIR-Principles, Git, Zenodo, Include In Dalia

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

Tags: Include In Dalia

[https://zenodo.org/records/14729452](https://zenodo.org/records/14729452)

[https://doi.org/10.5281/zenodo.14729452](https://doi.org/10.5281/zenodo.14729452)


---

## LEO: Linking ELN with OMERO

Escobar Diaz Guerrero, Rodrigo

Published 2024-05-08

Licensed CC-BY-4.0



First updates of LEO (Linking ELN with OMERO)

Tags: Exclude From Dalia

[https://zenodo.org/records/11146807](https://zenodo.org/records/11146807)

[https://doi.org/10.5281/zenodo.11146807](https://doi.org/10.5281/zenodo.11146807)


---

## LMRG Image Analysis Study - FISH datasets

Kristopoher Kubow, Thomas Pengo

Published 2022-05-18

Licensed CC-BY-4.0



Original image files, label (ground truth) files, and PSF files used in the ABRF Light Microscopy Research Group (LMRG) image analysis study. Simulated 3D confocal fluorescence images of sub-diffraction punctate staining (fluorescence in situ hybridization (FISH) in C. elegans).

See https://github.com/ABRFLMRG/image-analysis-study for more details.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/6560910](https://zenodo.org/records/6560910)

[https://doi.org/10.5281/zenodo.6560910](https://doi.org/10.5281/zenodo.6560910)


---

## LMRG Image Analysis Study - nuclei datasets

Kristopher Kubow, Thomas Pengo

Published 2022-05-18

Licensed CC-BY-4.0



Original image files, label (ground truth) files, and PSF files used in the ABRF Light Microscopy Research Group (LMRG) image analysis study. Simulated 3D widefield fluorescence images of nuclei.

See https://github.com/ABRFLMRG/image-analysis-study for more details.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/6560759](https://zenodo.org/records/6560759)

[https://doi.org/10.5281/zenodo.6560759](https://doi.org/10.5281/zenodo.6560759)


---

## LSM example J. Dubrulle

Salama Lab Fred Hutchinson Cancer Center

Published 2024-12-17

Licensed CC-BY-4.0



Tags: Exclude From Dalia

[https://zenodo.org/records/14510432](https://zenodo.org/records/14510432)

[https://doi.org/10.5281/zenodo.14510432](https://doi.org/10.5281/zenodo.14510432)


---

## LZ4-compressed Imaris ims example datasets.

Marco Stucchi

Published 2024-11-21

Licensed CC-BY-4.0



The files contained in this repository are cropped versions of Imaris demo images compressed with LZ4.

Tags: Exclude From Dalia

[https://zenodo.org/records/14197622](https://zenodo.org/records/14197622)

[https://doi.org/10.5281/zenodo.14197622](https://doi.org/10.5281/zenodo.14197622)


---

## Large Language Models: An Introduction for Life Scientists

Robert Haase

Published 2024-12-12

Licensed CC-BY-4.0



This slide deck introduces Large Language Models to an audience of life-scientists. We first dive into terminology: Different kinds of Language Models and what they can be used for. The remaining slides are optional slides to allow us to dive deeper into topics such as tools for using LLMs in Science, Quality Assurance, Techniques such as Retrieval Augmented Generation and Prompt Engineering.

Tags: Globias, Artificial Intelligence, Include In Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/6646128](https://zenodo.org/records/6646128)

[https://doi.org/10.5281/zenodo.6646128](https://doi.org/10.5281/zenodo.6646128)


---

## Laser perturbation imaging data for: Patterned invagination prevents mechanical instability during gastrulation

Vellutini, Bruno C., Cuenca, Marina B., Abhijeet Krishna, Alicja Szałapak, Modes, Carl D., Pavel Tomančák

Published 2025-07-14

Licensed CC-BY-4.0



This repository contains the imaging data for the laser perturbation experiments of the manuscript:
Vellutini BC, Cuenca MB, Krishna A, Szałapak A, Modes CD, Tomanč&aacute;k P.&nbsp;Patterned embryonic invagination evolved in response to mechanical instability. bioRxiv (2023) doi:10.1101/2023.03.30.534554
Please refer to the main repository for more information:&nbsp;https://doi.org/10.5281/zenodo.7781947

Tags: Exclude From Dalia

[https://zenodo.org/records/15876646](https://zenodo.org/records/15876646)

[https://doi.org/10.5281/zenodo.15876646](https://doi.org/10.5281/zenodo.15876646)


---

## Learning and Training Bio-image Analysis in the Age of AI

Robert Haase

Published 2025-04-07

Licensed CC-BY-4.0



The advent of large language models (LLMs) such as ChatGPT changes the way we analyse images. We ask LLMs to generate code, apply it to images and spend less time on learning implementation details. This also has impact on how we learn image analysis. While coding skills are still required, we can use LLMs to explain code, make proposals how to analyse the images and yet still decide how the analysis is done.

Tags: Include In Dalia

[https://zenodo.org/records/15165424](https://zenodo.org/records/15165424)

[https://doi.org/10.5281/zenodo.15165424](https://doi.org/10.5281/zenodo.15165424)


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

Tags: Include In Dalia

[https://zenodo.org/records/11445843](https://zenodo.org/records/11445843)

[https://doi.org/10.5281/zenodo.11445843](https://doi.org/10.5281/zenodo.11445843)


---

## Leitlinie? Grundsätze? Policy? Richtlinie? – Forschungsdaten-Policies an deutschen Universitäten

Bea Hiemenz, Monika Kuberek

Published 2018-07-13

Licensed CC-BY-4.0



As a methodological approach, research data policies of German universities are collected and evaluated, and compared to international recommendations on research data policies.

Tags: Research Data Management, FAIR-Principles, Exclude From Dalia

Content type: Publication

[https://www.o-bib.de/bib/article/view/2018H2S1-13](https://www.o-bib.de/bib/article/view/2018H2S1-13)


---

## Life Science Competence Centres: Open by Design

Romain David, Nektarios Liaskos, Arina Rybina, Christos Arvanitidis, Anne-Sophie Bage, Carvajal-Vallejos, Patricia K., Sudeep Das, De Pascalis, Francesca, Dorothea Dörr, Katrina Exter, Petr Holub, Gurwitz, Kim Tamara, Fabio Liberante, Philippe Lieutaud, Allyson Lister, Joaquin Lopez, Bénédicte Madon, Marzia Massimi, Rafaele Matteoni, Maria Mîrza, Sarah Morgan, Bugra Oezdemir, Maria Panagiotopoulou, Christina Pavloudi, P. Melo, Ana M., Susanna-Assunta Sansone, Harald Schwalbe, Beatriz Serrano-Solano, Sorzano, Carlos Oscar, Emilio Urbinati, Jing Tang, Jonathan Tedds, Gary Saunders, Jonathan Ewbank

Published 2025-07

Licensed CC-BY-4.0



Preprint in submission process to GigaScience journal
Abstract:
European Life Science Research Infrastructures (LS-RIs), one of the five major RI Science Clusters in Europe, were established to provide access to cutting-edge technologies to the scientific community. Individually, and collectively as the LS-RI cluster, they contribute to the development of the European Open Science Cloud (EOSC), under the aegis of the EOSC Federation. They are actively involved in the design and implementation of Competence Centres (CCs). These aim to increase the accessibility of domain-specific knowledge and tools, enhance interoperability, facilitate sharing and harmonisation of procedures, and promote Open Science and FAIR (Findable, Accessible, Interoperable, Reusable) practices. In this paper, we report a landscape mapping of the existing resources that formed the basis for the construction of CCs. We describe the possible design of CCs and their articulation with the LS-RIs. We focus on community-based ideas and recommendations to increase the potential of CCs to address long-standing challenges in sustainability, governance, scalability, and interoperability of Open Science within EOSC and the European Research Area (ERA) more generally.This paper provides a description of the nascent LS CCs, built following a survey of needs and services of existing LS-RI communities. When fully implemented, the LS CCs will serve as dynamic hubs to foster innovation, contribute to the EOSC&rsquo;s future FAIR web of data, and support ongoing developments of the EOSC Federation. They will act as drivers of collaborative and impactful LS research in Europe and beyond. We explore the underlying challenges, and propose solutions, to ensure that the establishment of CCs will add value to the LS RI community, and to the EOSC, in a sustainable way.

Tags: Exclude From Dalia

[https://zenodo.org/records/15798751](https://zenodo.org/records/15798751)

[https://doi.org/10.5281/zenodo.15798751](https://doi.org/10.5281/zenodo.15798751)


---

## Lightsheet and in situ imaging data for: Patterned invagination prevents mechanical instability during gastrulation

Vellutini, Bruno C., Cuenca, Marina B., Abhijeet Krishna, Alicja Szałapak, Modes, Carl D., Pavel Tomančák

Published 2025-07-14

Licensed CC-BY-4.0



This repository contains the lightsheet and in situ hybridization imaging data for the manuscript:
Vellutini BC, Cuenca MB, Krishna A, Szałapak A, Modes CD, Tomanč&aacute;k P.&nbsp;Patterned embryonic invagination evolved in response to mechanical instability. bioRxiv (2023) doi:10.1101/2023.03.30.534554
Please refer to the main repository for more information:&nbsp;https://doi.org/10.5281/zenodo.7781947

Tags: Exclude From Dalia

[https://zenodo.org/records/15876638](https://zenodo.org/records/15876638)

[https://doi.org/10.5281/zenodo.15876638](https://doi.org/10.5281/zenodo.15876638)


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

Tags: Exclude From Dalia

[https://zenodo.org/records/1472859](https://zenodo.org/records/1472859)

[https://doi.org/10.5281/zenodo.1472859](https://doi.org/10.5281/zenodo.1472859)


---

## Linked (Open) Data for Microbial Population Biology

Carsten Fortmann-Grote

Published 2024-03-12

Licensed CC-BY-4.0



Tags: Exclude From Dalia

[https://zenodo.org/records/10808486](https://zenodo.org/records/10808486)

[https://doi.org/10.5281/zenodo.10808486](https://doi.org/10.5281/zenodo.10808486)


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

Tags: Include In Dalia

[https://zenodo.org/records/6523649](https://zenodo.org/records/6523649)

[https://doi.org/10.5281/zenodo.6523649](https://doi.org/10.5281/zenodo.6523649)


---

## LyNSeC: Lymphoma Nuclear Segmentation and Classification

Naji Hussein, Büttner Reinhard, Simon Adrian, Eich Marie-Lisa, Lohneis Philipp, Bozek Katarzyna

Published 2023-06-21

Licensed CC-BY-4.0



Over the last years, there has been large progress in automated segmentation and classification methods in histological whole slide images (WSIs) stained with hematoxylin and eosin (H&amp;E). Current state-of-the-art techniques are based on diverse datasets of H&amp;E-stained WSIs of different types of predominantly solid cancer. However, there is a lack of publicly available annotated datasets of lymphoma, which is why we generated a labeled diffuse large B-cell lymphoma dataset and denoted it LyNSeC (lymphoma nuclear segmentation and classification). LyNSeC comprises three subsets: LyNSeC 1 consists of 379 IHC images of size 512 x 512 pixels at 40x magnification. In the images, we annotated the contours of each cell nuclei and the cell class: marker-positive or marker-negative.

In total, LyNSeC 1 contains 87,316 annotated cell nuclei of four different cases, with 48,171 of them assigned the class negative and 39,145 positive. We included three markers in this dataset showing visually different staining patterns: cluster of differentiation 3 (CD3), Ki67 as a marker of proliferation, and erythroblast transformation-specific (EST)-related gene (ERG).

LyNSeC 2 and 3 contain H&amp;E-stained images of 70 different patients. LyNSeC 2 consists of 280 images and LyNSeC 3 of 40 images of size 512 x 512 pixels at 40x magnification. 65,479 and 8,452 nuclei were annotated in LyNSeC 2 and 3, respectively. In LyNSeC 3, the nuclei were also assigned a class label (tumor and non-tumor). 3,747 nuclei were identified as tumors and 4,705 as non-tumors.

In the annotation procedure, the contours of the H&amp;E images (LyNSeC 2 and LyNSeC 3) were annotated by two pathologists and by two students (trained by the pathologists). Annotation of the cell classes in LyNSeC 3 was done by the pathologists only. LyNSeC 1 was annotated by the two students who were additionally trained to annotate the contours and to distinguish marker-positive and marker-negative cells. The pathologists inspected and (if necessary) adjusted the LyNSeC 3 annotations.

The files are uploaded in &#39;.npy&#39; format. The files of LyNSeC 1 (x_l1.npy) and LyNSeC 3&nbsp;(x_l3.npy) contain five channels, respectively: the first three are the RGB channels of the images, channel 4 contains the instance maps, and channel 5 the class type maps (for LyNSeC 1 a pixel value of 1 corresponds to the class negative and 2 to the class positive, whereas in LyNSeC 3 1 corresponds to the class non-tumor and 2 to the class tumor). The files of LyNSeC 2 (x_l2.npy) have 4 channels (without the class type map).

Additionally, we also make our HoVer-Net-based pre-trained nuclei segmentation and classification models available (he.tar for H&amp;E images and ihc.tar for IHC images).

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/8065174](https://zenodo.org/records/8065174)

[https://doi.org/10.5281/zenodo.8065174](https://doi.org/10.5281/zenodo.8065174)


---

## Making the most of bioimaging data through interdisciplinary interactions

Virginie Uhlmann, Matthew Hartley, Josh Moore, Erin Weisbart, Assaf Zaritsky

Published 2024-10-23

Licensed CC-BY-4.0



Tags: Bioimage Analysis, Open Science, Microscopy, Include In Dalia

Content type: Publication

[https://journals.biologists.com/jcs/article/137/20/jcs262139/362478/Making-the-most-of-bioimaging-data-through](https://journals.biologists.com/jcs/article/137/20/jcs262139/362478/Making-the-most-of-bioimaging-data-through)


---

## Making your package available on conda-forge

Kevin Yamauchi

Licensed CC-BY-4.0



Tags: Deployment, Python, Include In Dalia

Content type: Documentation

[https://kevinyamauchi.github.io/open-image-data/how_tos/conda_forge_packaging.html](https://kevinyamauchi.github.io/open-image-data/how_tos/conda_forge_packaging.html)


---

## Managing Scientific Python environments using Conda, Mamba and friends

Robert Haase

Licensed CC-BY-4.0



Tags: Python, Conda, Mamba, Include In Dalia

Content type: Blog Post

[https://focalplane.biologists.com/2022/12/08/managing-scientific-python-environments-using-conda-mamba-and-friends/](https://focalplane.biologists.com/2022/12/08/managing-scientific-python-environments-using-conda-mamba-and-friends/)


---

## Masterclasses from the Euro-Bioimaging EVOLVE Mentoring programme 2025

Euro-BioImaging ERIC

Published 2025-06-26

Licensed CC-BY-4.0



EVOLVE Mentoring Masterclasses
Description:This series captures the class guides of the 2025 masterclasses from Euro‑BioImaging's EVOLVE Mentoring Program.
Included Masterclasses:

Peter O&rsquo;Toole &ndash; &ldquo;Entrepreneurship &amp; Leadership in Imaging Core Facilities&rdquo;&nbsp;Peter O&rsquo;Toole, President of the Royal Microscopical Society and Director of the Bioscience Technology Facility (University of York), kicks off the series with a deep dive into entrepreneurial leadership. He highlights how to balance science, business, and technology, emphasizing stakeholder engagement, staff investment, cross-training, and using social media to boost visibility and unlock funding.
Ilaria Testa &ndash; &ldquo;Interdisciplinary Science, SMART Microscopy &amp; Team Building&rdquo;&nbsp;Professor Ilaria Testa (SciLifeLab &amp; KTH) reflects on her transition from physics to super-resolution microscopy and team leadership. Her session underscores the power of crossing disciplinary boundaries, mentorship, and innovation in live-cell imaging .
Daphna Link‑Sourani &ndash; &ldquo;Leadership, Facility Management &amp; Work‑Life Balance&rdquo;&nbsp;Dr. Daphna Link‑Sourani (Technion Human MRI Research Center) challenges hierarchical notions of leadership, advocating instead for integrity, empathy, and strategic vision. She draws on her experience establishing an MRI facility to discuss crisis management, user engagement, and balancing career demands.
Muriel Mari &ndash; &ldquo;Women in Science: Normalizing, Supporting &amp; Leading"&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Dr. Muriel Mari (Aarhus University) leads a powerful reflection on gender equity in science. Her masterclass goes beyond barriers&mdash;focusing on cultural shifts, inclusive leadership, and redefining success. She encourages institutions and individuals alike to move from tokenism to transformative support, and to recognize the diverse paths women take in STEM.
Sylvia E. Le D&eacute;v&eacute;dec &ndash; &ldquo;Image Data Management &amp; FAIR Core Facilities&rdquo;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Dr. Sylvia Le D&eacute;v&eacute;dec (Leiden University) discusses how to integrate FAIR data principles in imaging core facilities. Drawing on her experience with high-content imaging and Open Science advocacy, she outlines actionable steps toward sustainable, reusable, and accessible data workflows.

Why Archive These Sessions?These masterclasses offer invaluable insights for core facility managers, imaging scientists, and team leaders in life sciences. They blend hands-on leadership strategies, technical facility growth advice, and real-world experience&mdash;making them essential viewing for professionals and institutions aiming to build sustainable, people-centred imaging infrastructures.

Tags: Exclude From Dalia

[https://zenodo.org/records/15837532](https://zenodo.org/records/15837532)

[https://doi.org/10.5281/zenodo.15837532](https://doi.org/10.5281/zenodo.15837532)


---

## Measuring reporter activity domain in EPI aggregates and Gastruloids.ijm

Romain Guiet, Olivier Burri, Mehmet Girgin, Matthias Lutolf

Published 2022-12-07

Licensed CC-BY-4.0



This imagej macro analyses the reporter intensity activity and expression domain in EPI aggregates and Gastruloids.

Tags: Exclude From Dalia

[https://zenodo.org/records/7409423](https://zenodo.org/records/7409423)

[https://doi.org/10.5281/zenodo.7409423](https://doi.org/10.5281/zenodo.7409423)


---

## Meeting in the Middle: Towards Successful Multidisciplinary Bioimage Analysis Collaboration

Anjalie Schlaeppi, Wilson Adams, Robert Haase, Jan Huisken, Ryan B. MacDonald, Kevin W. Eliceiri, Elisabeth C. Kugler

Licensed CC-BY-4.0



Tags: Bioimage Analysis, Include In Dalia

Content type: Publication

[https://www.frontiersin.org/articles/10.3389/fbinf.2022.889755/full](https://www.frontiersin.org/articles/10.3389/fbinf.2022.889755/full)


---

## MemBrain-seg training data

Lorenz Lamm

Published 2023-03-16

Licensed CC-BY-4.0



This dataset contains training data for segmenting membranes in cryo-electron tomograms.

More details will follow.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/7739793](https://zenodo.org/records/7739793)

[https://doi.org/10.5281/zenodo.7739793](https://doi.org/10.5281/zenodo.7739793)


---

## Memorandum of Understanding of NFDI consortia from Earth-, Chemical and Life Sciences to support a network called the Geo-Chem-Life Science Helpdesk Cluster

Lars Bernard, Maike Brück, Christian Busse, Judith Engel, Jan Eufinger, Frank Ewert, Juliane Fluck, Konrad Förstner, Julia Fürst, Holger Gauza, Klaus Getzlaff, Glöckner, Frank Oliver, Johannes Hunold, Oliver Koepler, Ksenia Krooß, Birte Lindstädt, McHardy, Alice C., Hela Mehrtens, Elena Rey-Mazon, Marcus Schmidt, Isabel Schober, Annett Schröter, Oliver Stegle, Christoph Steinbeck, Feray Steinhart, von Suchodoletz, Dirk, Stefanie Weidtkamp-Peters, Jens Wendt, Conni Wetzker

Published 2025-04-02

Licensed CC-BY-4.0



In a Memorandum of Understanding, the undersigned consortia agree to work together to enhance their support capabilities (helpdesks) to meet the needs of interdisciplinary research in&nbsp;Earth-, Chemical and Life Sciences.

Tags: Exclude From Dalia

[https://zenodo.org/records/15065070](https://zenodo.org/records/15065070)

[https://doi.org/10.5281/zenodo.15065070](https://doi.org/10.5281/zenodo.15065070)


---

## Metadata Annotation Workflow for OMERO with Tabbles

Wendt Jens

Published 2023-09-04

Licensed CC-BY-4.0



Short presentation given at at PoL BioImage Analysis Symposium Dresden 2023

Tags: Exclude From Dalia

[https://zenodo.org/records/8314968](https://zenodo.org/records/8314968)

[https://doi.org/10.5281/zenodo.8314968](https://doi.org/10.5281/zenodo.8314968)


---

## Metadata in Bioimaging

Josh Moore, Susanne Kunis

Published 2025-03-25

Licensed CC-BY-4.0



Presentation given to the Search &amp; Harvesting workgroup of the Metadata section of NFDI on March 25th, 2025

Tags: Nfdi4Bioimage, Exclude From Dalia

[https://zenodo.org/records/15083018](https://zenodo.org/records/15083018)

[https://doi.org/10.5281/zenodo.15083018](https://doi.org/10.5281/zenodo.15083018)


---

## Methods in bioimage analysis

Christian Tischer

Licensed CC-BY-4.0



Tags: Bioimage Analysis, Include In Dalia

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


Tags: Bioimage Analysis, Artificial Intelligence, Exclude From Dalia

Content type: Slides

[https://zenodo.org/records/11265038](https://zenodo.org/records/11265038)

[https://doi.org/10.5281/zenodo.11265038](https://doi.org/10.5281/zenodo.11265038)


---

## Microscopy data analysis: machine learning and the BioImage Archive

Andrii Iudin, Anna Foix-Romero, Anna Kreshuk, Awais Athar, Beth Cimini, Dominik Kutra, Estibalis Gomez de Mariscal, Frances Wong, Guillaume Jacquemet, Kedar Narayan, Martin Weigert, Nodar Gogoberidze, Osman Salih, Petr Walczysko, Ryan Conrad, Simone Weyend, Sriram Sundar Somasundharam, Suganya Sivagurunathan, Ugis Sarkans

Licensed CC-BY-4.0



The Microscopy data analysis: machine learning and the BioImage Archive course, which focused on introducing programmatic approaches used in the analysis of bioimage data via the BioImage Archive, ran in May 2023.

Tags: Bioimage Analysis, Python, Artificial Intelligence, Include In Dalia

Content type: Video, Slides

[https://www.ebi.ac.uk/training/materials/microscopy-data-analysis-machine-learning-and-the-bioimage-archive-materials/](https://www.ebi.ac.uk/training/materials/microscopy-data-analysis-machine-learning-and-the-bioimage-archive-materials/)


---

## Microscopy-BIDS - An Extension to the Brain Imaging Data Structure for Microscopy Data

Marie-Hélène Bourget, Lee Kamentsky, Satrajit S. Ghosh, Giacomo Mazzamuto, Alberto Lazari, et al.

Published 2022-04-19

Licensed CC-BY-4.0



The Brain Imaging Data Structure (BIDS) is a specification for organizing, sharing, and archiving neuroimaging data and metadata in a reusable way.

Tags: Research Data Management, Exclude From Dalia

Content type: Publication

[https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.871228/full](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.871228/full)


---

## Model and simulations for: Patterned invagination prevents mechanical instability during gastrulation

Abhijeet Krishna, Alicja Szałapak, Vellutini, Bruno C., Cuenca, Marina B., Pavel Tomančák, Modes, Carl D.

Published 2025-07-14

Licensed CC-BY-4.0



This repository contains the code and simulations for the manuscript:
Vellutini BC, Cuenca MB, Krishna A, Szałapak A, Modes CD, Tomanč&aacute;k P.&nbsp;Patterned embryonic invagination evolved in response to mechanical instability. bioRxiv (2023) doi:10.1101/2023.03.30.534554
Please refer to the main repository for more information:&nbsp;https://doi.org/10.5281/zenodo.7781947

Tags: Exclude From Dalia

[https://zenodo.org/records/15869598](https://zenodo.org/records/15869598)

[https://doi.org/10.5281/zenodo.15869598](https://doi.org/10.5281/zenodo.15869598)


---

## Modeling community standards for metadata as templates makes data FAIR

Mark A Musen, Martin J O'Connor, Erik Schultes, Marcos Martínez-Romero, Josef Hardi, John Graybeal

Published 2022-11-12

Licensed CC-BY-4.0



The authors have developed a model for scientific metadata, and they have made that model usable by both CEDAR and FAIRware. The approach shows that a formal metadata model can standardize reporting guidelines and that it can enable separate software systems to assist (1) in the authoring of standards-adherent metadata and (2) in the evaluation of existing metadata.

Tags: Data Stewardship, FAIR-Principles, Metadata, Exclude From Dalia

Content type: Publication

[https://pubmed.ncbi.nlm.nih.gov/36371407/](https://pubmed.ncbi.nlm.nih.gov/36371407/)

[https://www.nature.com/articles/s41597-022-01815-3](https://www.nature.com/articles/s41597-022-01815-3)


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

## Morphological analysis of neural cells with WEKA and SNT Fiji plugins

Daniel Waiger

Published 2022-07-14

Licensed CC-BY-4.0



A simple workflow to detect Soma and neurite paths, from light microscopy&nbsp;datasets.

Using open-source tools for beginners.

Tags: Include In Dalia

[https://zenodo.org/records/6834214](https://zenodo.org/records/6834214)

[https://doi.org/10.5281/zenodo.6834214](https://doi.org/10.5281/zenodo.6834214)


---

## Multi-Template-Matching for object-detection (slides)

Laurent Thomas

Published 2022-05-16

Licensed CC-BY-4.0



This presentations describes Multi-Template-Matching, a novel method extending on template-matching for object-detection in images.

The project was part of the PhD project of Laurent Thomas between 2017 and 2020, under supervision of Jochen Gehrig. The project was hosted at ACQUIFER Imaging with collaboration of the medical university of Heidelberg, and part of the ImageInLife Horizon2020 ITN (PhD program).&nbsp;

Tags: Include In Dalia

[https://zenodo.org/records/6554166](https://zenodo.org/records/6554166)

[https://doi.org/10.5281/zenodo.6554166](https://doi.org/10.5281/zenodo.6554166)


---

## Multiplexed histology of COVID-19 post-mortem lung samples - CONTROL CASE 1 FOV1

Anna Pascual Reguant, Ronja Mothes, Helena Radbruch, Anja E. Hauser

Published 2022-12-16

Licensed CC-BY-4.0



Image-based data set of a post-mortem lung sample from a non-COVID-related pneumonia donor (CONTROL CASE 1, FOV1)

Each image shows the same field of view (FOV), sequentially stained with the depicted fluorescence-labelled antibodies, including surface proteins, intracellular proteins and transcription factors. Images contain 2024 x 2024 pixels and are generated using an inverted wide-field fluorescence microscope with a 20x objective, a lateral resolution of 325 nm and an axial resolution above 5 &micro;m. Images have&nbsp;been normalized and intensities adjusted.

Tags: Exclude From Dalia

[https://zenodo.org/records/7447491](https://zenodo.org/records/7447491)

[https://doi.org/10.5281/zenodo.7447491](https://doi.org/10.5281/zenodo.7447491)


---

## Multiplexed tissue imaging - tools and approaches

Agustín Andrés Corbat, OmFrederic, Jonas Windhager, Kristína Lidayová

Licensed CC-BY-4.0



Material for the I2K 2024 "Multiplexed tissue imaging - tools and approaches" workshop

Tags: Bioimage Analysis, Include In Dalia

Content type: Github Repository, Slides, Workshop

[https://github.com/BIIFSweden/I2K2024-MTIWorkshop](https://github.com/BIIFSweden/I2K2024-MTIWorkshop)

[https://docs.google.com/presentation/d/1R9-4lXAmTYuyFZpTMDR85SjnLsPZhVZ8/edit#slide=id.p1](https://docs.google.com/presentation/d/1R9-4lXAmTYuyFZpTMDR85SjnLsPZhVZ8/edit#slide=id.p1)


---

## My Journey Through Bioimage Analysis Teaching Methods From Classroom to Cloud

Elnaz Fazeli

Published 2024-02-19

Licensed CC-BY-4.0



In these slides I introducemy journey through teaching bioimage analysis courses in different formats, from in person courses to online material. I have an overview of different training formats and comparing these for different audiences.&nbsp;

Tags: Teaching, Include In Dalia

Content type: Slides

[https://zenodo.org/records/10679054](https://zenodo.org/records/10679054)

[https://doi.org/10.5281/zenodo.10679054](https://doi.org/10.5281/zenodo.10679054)


---

## NFDI4BIOIMAGE

Carsten Fortmann-Grote

Published 2024-04-22

Licensed CC-BY-4.0



This presentation was given at the 2nd MPG-NFDI Workshop on April 18th.

Tags: Exclude From Dalia

[https://zenodo.org/records/11031747](https://zenodo.org/records/11031747)

[https://doi.org/10.5281/zenodo.11031747](https://doi.org/10.5281/zenodo.11031747)


---

## NFDI4BIOIMAGE - National Research Data Infrastructure for Microscopy and BioImage Analysis - Online Kick-Off 2023

Stefanie Weidtkamp-Peters

Licensed CC-BY-4.0



NFDI4BIOIMAGE core mission, bioimage data challenge, task areas, FAIR bioimage workflows.

Tags: Research Data Management, FAIR-Principles, Bioimage Analysis, Nfdi4Bioimage, Include In Dalia

Content type: Slides

[https://doi.org/10.5281/zenodo.8070038](https://doi.org/10.5281/zenodo.8070038)

[https://zenodo.org/records/8070038](https://zenodo.org/records/8070038)


---

## NFDI4BIOIMAGE - National Research Data Infrastructure for Microscopy and BioImage Analysis [conference talk: The Pelagic Imaging Consortium meets Helmholtz Imaging, 5.10.2023, Hamburg]

Riccardo Massei

Licensed CC-BY-4.0



NFDI4BIOIMAGE is a consortium within the framework of the National Research Data Infrastructure (NFDI) in Germany. In this talk, the consortium and the contribution to the work programme by the Helmholtz Centre for Environmental Research (UFZ) in Leipzig are outlined.

Tags: Research Data Management, Bioimage Analysis, Nfdi4Bioimage, Exclude From Dalia

Content type: Slides

[https://zenodo.org/doi/10.5281/zenodo.8414318](https://zenodo.org/doi/10.5281/zenodo.8414318)


---

## NFDI4BIOIMAGE - National Research Data Infrastructure for Microscopy and Bioimage Analysis

NFDI4BIOIMAGE Consortium

Published 2024-08-07

Licensed CC-BY-4.0



Bioimaging refers to a collection of methods to visualize the internal structures and mechanisms of living organisms. The fundamental tool, the microscope, has enabled seminal discoveries like that of the cell as the smallest unit of life, and continues to expand our understanding of biological processes. Today, we can follow the interaction of single molecules within nanoseconds in a living cell, and the development of complete small organisms like fish and flies over several days starting from the fertilized egg. Each image pixel encodes multiple spatiotemporal and spectral dimensions, compounding the massive volume and complexity of bioimage data. Proper handling of this data is indispensable for analysis and its lack has become a growing hindrance for the many disciplines of the life and biomedical sciences relying on bioimaging. No single domain has the expertise to tackle this bottleneck alone.
As a method-specific consortium, NFDI4BIOMAGE seeks to address these issues, enabling bioimaging data to be shared and re-used like they are acquired, i.e., independently of disciplinary boundaries. We will provide solutions for exploiting the full information content of bioimage data and enable new discoveries through sharing and re-analysis. Our RDM strategy is based on a robust needs analysis that derives not only from a community survey but also from over a decade of experience in German BioImaging, the German Society for Microscopy and Image Analysis. It considers the entire lifecycle of bioimaging data, from acquisition to archiving, including analysis and enabling re-use. A foundational element of this strategy is the definition of a common, cloud-compatible, and interoperable digital object that bundles binary images with their descriptive and provenance metadata. With members from plant biology to neuroscience, NFDI4BIOIMAGE will champion the standardization of bioimage data to create a framework that answers discipline-specific needs while ensuring communication and interoperability with data types and RDM systems across domains. Integration of bioimage data with, e.g., omics data as the basis for spatial omics, holds great promise for fields such as cancer medicine. Unlocking the full potential of bioimage data will rely on the development and broad availability of exceptional analysis tools and training sets. NFDI4BIOIMAGE will make these accessible and usable including cutting-edge AI-based methods in scalable cloud environments. NFDI4BIOIMAGE intersects with multiple NFDI consortia, most prominently with GHGA for linking image and genomics data and with DataPLANT on the definition of FAIR data objects. Last but not least, NFDI4BIOIMAGE is internationally well connected and represents the opportunity for German scientists to keep path with and have a voice in several international initiatives focusing on the FAIRification of bioimage data as one of the main challenges for the advancement of knowledge in the life and biomedical sciences.

Tags: Include In Dalia

[https://zenodo.org/records/13168693](https://zenodo.org/records/13168693)

[https://doi.org/10.5281/zenodo.13168693](https://doi.org/10.5281/zenodo.13168693)


---

## NFDI4BIOIMAGE Calendar April 2025

Martin Zurowietz, Nattkemper, Tim W.

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar April 2025.
This image shows the BIIGLE image and video annotation tool, which is a web-based software for collaborative research on large imaging datasets [1, 2]. It offers tools for manual and computer-assisted annotation, quality control and the collaboration on custom taxonomies to describe objects. BIIGLE is freely available and can be installed in cloud environments, a local network or on mobile platforms during research expeditions. A public instance can be found at biigle.de.
The annotated image shows the coastline of Fernandina Island, Galapagos, which is the habitat of the Galapagos Marine Iguana (Amblyrhynchus cristatus). The image is a large mosaic that was stitched together from many individual images captured by a drone. The green annotations marking the iguanas were machine-generated as part of a feasibility study for the automatic analysis of the data in the project Iguanas from Above [3, 4].
[1] Langenk&auml;mper, D., Zurowietz, M., Schoening, T., &amp; Nattkemper, T. W. (2017). BIIGLE 2.0-browsing and annotating large marine image collections. Frontiers in Marine Science, 4, 83. https://doi.org/10.3389/fmars.2017.00083
[2] Zurowietz, M., &amp; Nattkemper, T. W. (2021). Current trends and future directions of large scale image and video annotation: Observations from four years of BIIGLE 2.0. Frontiers in Marine Science, 8, 760036. https://doi.org/10.3389/fmars.2021.760036
[3] Varela-Jaramillo, A., Rivas-Torres, G., Guayasamin, J. M., Steinfartz, S., &amp; MacLeod, A. (2023). A pilot study to estimate the population size of endangered Gal&aacute;pagos marine iguanas using drones. Frontiers in Zoology, 20(1), 4. https://doi.org/10.1186/s12983-022-00478-5
[4] https://iguanasfromabove.com




Project


Iguanas from Above




Location


Fernandina Island, Galapagos




Organism


Amblyrhynchus cristatus




Drone model


DJI Mavic 2 Pro




Camera


Hasselblad L1D-20c




Size


26,545 &times; 20,894 px




Mosaic algorithm


Agisoft Metashape Professional v.1.6




Submitted via NFDI4Biodiversity





Tags: Exclude From Dalia

[https://zenodo.org/records/16980661](https://zenodo.org/records/16980661)

[https://doi.org/10.5281/zenodo.16980661](https://doi.org/10.5281/zenodo.16980661)


---

## NFDI4BIOIMAGE Calendar August 2025

Haowen Jiang, Claire Chalopin

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar August 2025.
This image illustrates tissue oxygen saturation in the hand, calculated using various computer-assisted methods and based on hyperspectral and multispectral imaging. The purpose of this image is to compare the perfusion parameters (3 and 4) obtained with multispectral cameras delivering relatively less spectral information but capable of real-time imaging against the perfusion parameters (2) obtained with a hyperspectral medical system delivering large spectral information but not capable of real-time imaging. The picture shows that deep learning methods (4) perform better than classical methods (3) that are not based on artificial intelligence. It lays the groundwork for future real-time quantitative assessment of perfusion during organ transplantation surgeries.
Image Metadata (using REMBI template):




Study




Study description


Quantification of tissue reperfusion using real-time spectral imaging and deep learning




Study type


Study on volunteers




Study Component




Imaging method


(1) RGB imaging
(2) Hyperspectral imaging
(3) and (4) Multispectral imaging




Image component description


(1) RGB image of the hand under normal perfusion.
(2) Perfusion parameter map computed based on hyperspectral imaging (100 spectral bands between 500 and 1000 nm). High perfusion values are represented in red, low perfusion values in blue.
(3) Perfusion parameter map computed based on multispectral imaging (31 spectral bands between 460 and 850 nm) and using the spectral bands that are available but that are less than in (2). Therefore, the result in (3) looks very different from the result in (2).
(4) Perfusion parameter map computed based on multispectral imaging and using a deep neural network. The result in (4) looks similar to the result in (2).




Biosample




Biological entity


Hand




Organism


Homo sapiens




Image data




Image resolution hyperspectral imaging


Spatial Resolution: 480*640 pixels
Spectral Resolution: 500 nm-1000 nm, 100 bands, 5 nm




Image resolution multispectral imaging


Spatial Resolution: 1088*2048 pixels
Spectral Resolution: 16 bands in 460-600 nm; 15 bands in 600-850 nm




Image mode


Reflectance




Submitted via NFDI4BIOIMAGE





Tags: Exclude From Dalia

[https://zenodo.org/records/16993059](https://zenodo.org/records/16993059)

[https://doi.org/10.5281/zenodo.16993059](https://doi.org/10.5281/zenodo.16993059)


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

## NFDI4BIOIMAGE Calendar December 2025

Kira Müntjes, Kerstin Schipper

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar December 2025.
The microscopic image shows yeast cells of the fungal model Ustilago maydis that produce single cell oil at nitrogen-starvation conditions. The genetically engineered cells are packed with oil droplets that were visualized by BODIPY staining. The study was conducted in the framework of the BioSC project "NextVegOil".
Image Metadata (using REMBI template):




Study




Study type


Visualisation of microbial oil in the fungus Ustilago maydis




Study Component




Imaging method


Wide field whole organism microscopy




Biosample




Biological entity


Ustilago maydis




Organism


Yeast cells (sporidia)




Identity


Ustilago maydis MB215 cyp1&Delta;emt1&Delta; (published in https://doi.org/10.1128/AEM.71.6.3033-3040.2005)




Intrinsic variable


Glycolipid production has been ablated by genetic engineering




Extrinsic variable


BODIPY (4,4-Difluoro-1,3,5,7,8-Pentamethyl-4-Bora-3a,4a-Diaza-s-Indacene 493/503) staining




Experimental variables 


Cultivation time




Specimen




Location within biosample


Overview image with yeast cells from liquid culture at nitrogen-starvation condition




Preparation method


Living cells attached to agarose mounts




Signal/contrast mechanism


Differential interference contrast and fluorescence




Channel 1 - content


DIC




Channel 1 - biological entity


Intact yeast cells 




Channel 2 - content


BODIPY 493/503




Channel 2 - biological entity


Intracellular lipid droplets




Image acquisition




Instrument attributes


Zeiss Axio Observer.Z1; Prime BSI express; solid-state laser 488 nm




Submitted via NFDI4BIOIMAGE





Tags: Exclude From Dalia

[https://zenodo.org/records/16993955](https://zenodo.org/records/16993955)

[https://doi.org/10.5281/zenodo.16993955](https://doi.org/10.5281/zenodo.16993955)


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





Tags: Exclude From Dalia

[https://zenodo.org/records/16980217](https://zenodo.org/records/16980217)

[https://doi.org/10.5281/zenodo.16980217](https://doi.org/10.5281/zenodo.16980217)


---

## NFDI4BIOIMAGE Calendar July 2025

Pilar Lörzing, Denis Iliasov, Michael Schlierf, Thorsten Mascher

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar July 2025.
The sample was provided through a collaboration with the group of Thorsten Mascher at TU Dresden. Aim of this project is to explore the cellular autofluorescence patterns in Streptomyces using advanced imaging techniques.&nbsp;Streptomyces coelicolor are multicellular, mycelial bacteria that grow as vegetative hyphae. The use of confocal microscopy in this project was crucial for optically sectioning these filamentous cells, enabling the resolution of their cellular autofluorescence patterns with a high signal-to-noise ratio, which allowed us to visualize the 3D arrangement of the hyphae.
Image Metadata (using REMBI template):




Study




Study type


Characterization of the intrinsic autofluorescence in filamentous actinobacteria




Study Component




Imaging method


Spinning Disk Confocal Microscopy




Biosample




Biological entity


Hyphae




Organism


Streptomyces coelicolor M600




Intrinsic variable


Plasmid free derivative of the wild type strain




Experimental variables


Live-Cell imaging




Specimen




Preparation method


S. coelicolor was grown in maltose-yeast extract-malt extract (MYM) medium with tap and deionized water (1:1) and supplemented with 0.2 mL R2 trace element solution per 100 mL. Cultures were inoculated from spore suspension and grown for 18 hours at 28 &deg;C. 2 &micro;l cell suspension was immobilized on 1% agarose pads and covered with a cleaned coverslip (1.5H).




Channel 1 - content


Cellular autofluorescence




Channel 1 - biological entity


S. coelicolor hyphae




Image acquisition




Instrument attributes


Imaging was performed using a Nikon Ti-E Spinning Disk microscope with 100x objective and 1.5x tube lens. Fluorescence was excited with a 488 nm laser and emission light was filtered using a dual band filter 433/530 HC. An Andor Ixon Ultra 888 EMCCD camera was used for detection. 




Image acquisition parameter


Z-stacks of confocal images with 0.2 &micro;m step size




Image data




Type


Maximum intensity projection of individual z-stacks




Format &amp; compression


TIFF




Dimension extents


x: 1024 y: 1024 z: 28 px




Size description


x: 63.12 y: 63.12 z: 5.6 &micro;m




Pixel/voxel size description


x: 86 y: 86 z: 200 nm




Submitted via NFDI4BIOIMAGE





Tags: Exclude From Dalia

[https://zenodo.org/records/16992904](https://zenodo.org/records/16992904)

[https://doi.org/10.5281/zenodo.16992904](https://doi.org/10.5281/zenodo.16992904)


---

## NFDI4BIOIMAGE Calendar June 2025

Kevin Warstat

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar June 2025.
This illustration compares two orthomosaics generated from UAV imagery. On the left, a true-color RGB orthomosaic is displayed, accompanied by three smaller orthomosaic images above it, each representing the red, green, and blue bands, vividly colored to highlight their significance. On the right, a corresponding NDVI orthomosaic of the same field is shown, with two images above it illustrating the red and near-infrared bands used as input. All images are processed products from structure from motion modelling.




Title


Crop spectra




Research project


PhenoRob (EXC 2070)




Recording date


2023-07-11




Location


Campus Klein-Altendorf, 53359 Rheinbach, Germany




Sensor platform


DJI Matrice 600 Pro




Sensors


Sony alpha 7 mark IV RGB
MicaSense RedEdge-MX Dual multispectral camera




Submitted via FAIRagro





Tags: Exclude From Dalia

[https://zenodo.org/records/16992716](https://zenodo.org/records/16992716)

[https://doi.org/10.5281/zenodo.16992716](https://doi.org/10.5281/zenodo.16992716)


---

## NFDI4BIOIMAGE Calendar March 2025

Michael Schwarz

Published 2025-09-11

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


Submitted via NFDI4BIOIMAGE
&nbsp;



&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/17098115](https://zenodo.org/records/17098115)

[https://doi.org/10.5281/zenodo.17098115](https://doi.org/10.5281/zenodo.17098115)


---

## NFDI4BIOIMAGE Calendar May 2025

Stefanie Lück

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar May 2025.
The microscopy image captures the interaction between the barley cv. Golden Promise and the barley powdery mildew fungus Blumeria&nbsp;graminis&nbsp;f.sp.&nbsp;hordei, observed 48 hours post-inoculation. The fungus was stained with Coomassie dye, enhancing its visibility against the barley leaves. The leaves were prepared and fixed onto slides, followed by scanning with a Zeiss Axio Scan Z.1 microscope scanner using a 5x objective lens.
The upper section of the image displays the hyphal colonies, which were automatically segmented, highlighting the fungal structures (black) against the plant tissue (white). The lower section presents a machine learning-based analysis where a Convolutional Neural Network (CNN) was employed to predict the fungal structures. Here, the red bounding boxes show the outer boundaries of detected objects, while the green contours precisely trace the segmented hyphae, illustrating the effectiveness of the segmentation and prediction processes.
Image Metadata (using MIAPPE template):




Investigation information




Investigation Title


Analysis of Hordeum vulgare cv. Golden promise infected with Blumeria graminis f. sp. hordei (causative for barley powdery mildew)




Objective


To study the interaction between Hordeum vulgare and Blumeria graminis f. sp. hordei using advanced imaging techniques and automated image analysis.




Study information




Study Title


Microscopy imaging and analysis of barley powdery mildew infection on Hordeum vulgare cv. Golden promise




Study Type


Microscopy-based phenotyping experiment




Study Description


The study involves imaging barley leaves inoculated with Blumeria graminis f. sp. hordei, followed by automated segmentation and CNN-based prediction of fungal structures.




Plant material




Plant Species


Hordeum vulgare 




Cultivar


Golden promise




Experimental design




Experiment Type


Fungal inoculation and microscopy imaging




Inoculation Details


Barley leaves were inoculated with Blumeria graminis f. sp. hordei.




Time post-inoculation


48 hours




Imaging information




Microscopy type


Brightfield microscopy




Staining method


Coomassie stain for fungal structures




Microscope


Zeiss Axio Scan Z.1




Objective Lens


5x




Image Format


Zeiss CZI file




Image analysis information




Segmentation method


Automated segmentation of hyphal colonies




Image analysis software


BluVision Micro software




Prediction method


Convolutional Neural Network (CNN) for fungal structure detection




Upper image


Shows binary image with hyphal colonies (black) and background (white).




Lower image


Displays CNN predictions with red bounding boxes marking detected objects and green contours outlining segmented hyphae.




Submitted via NFDI4Biodiversity





Tags: Exclude From Dalia

[https://zenodo.org/records/16991961](https://zenodo.org/records/16991961)

[https://doi.org/10.5281/zenodo.16991961](https://doi.org/10.5281/zenodo.16991961)


---

## NFDI4BIOIMAGE Calendar November 2025

Jadranka Macas

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar November 2025.
The image shows a perivascular accumulation of perivascular B cells, T cells and plasma cells in a human brain tumor. These structures, also known as tertiary lymphoid structures, are sites of lymphocyte clonal expansion and plasma cell formation. The study aims to determine the clinical relevance and immunological function of tertiary lymphoid structures in human primary brain tumors.
Image Metadata (using REMBI template):




Study




Study type


Immunomonitoring study in human oncology




Study Component




Imaging method


COMET&trade; highplex seq-IF staining and scanning system, HORIZON&trade; Viewer (Lunaphore Technologies, SA)




Biosample




Biological entity


Tertiary lymphoid structure in glioblastoma




Organism


Homo sapiens




Specimen




Location within biosample


Tumor (glioblastoma)




Preparation method


FFPE sample, automatic sequential-IF using COMET&trade; (Lunaphore Technologies, SA)




Signal/contrast mechanism


HORIZON&trade; Viewer (Lunaphore Technologies, SA)




Channel 1 - content


Alexa Fluor Plus 555, red




Channel 1 - biological entity


CD20 - B-cells




Channel 2 - content


Alexa Fluor Plus 647, green




Channel 2 - biological entity


CD3 - T-cells




Channel 3 - content


Alexa Fluor Plus 555, white




Channel 3 - biological entity


CD163 - anti-inflammatory macrophages (M2-like) 




Channel 4 - content


Alexa Fluor Plus 647, magenta




Channel 4 - biological entity


MZB-1 - Marginal zone B and B1 cell-specific protein, MEDA-7 - plasma cells, memory B-cells




Channel 5 - content


Alexa Fluor Plus 647, orange




Channel 5 - biological entity


NF- Neurofilament - intermediate filaments around the axons




Channel 6- content


Alexa Fluor Plus 555, cyan




Channel 6 - biological entity


GAP43 - Neuromodulin, neuronal growth-associated protein 43 - neurons




Channel 7 - content


Alexa Fluor Plus 555, blue




Channel 7 - biological entity


vWF - von-Willebrand-Factor - endothelial cells




Image acquisition




Instrument attributes


COMET&trade; highplex seq-IF staining and scanning system v.1.1.1.0 (Lunaphore Technologies, SA)




Image acquisition parameters


COMET&trade; acquisition software&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 




Image data




Pixel size


0.23 &micro;m/pixel




Image size


Width 11986 pixels - 2.76 mmHeight 11514 pixels - 2.65 mm




Pixel bit depth


16-bit&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




Channel information


Displayed are 7 markers out of the highplex IF-panel; number of channels 43 (including autofluorescence)




Submitted via NFDI4Immuno





Tags: Exclude From Dalia

[https://zenodo.org/records/16993649](https://zenodo.org/records/16993649)

[https://doi.org/10.5281/zenodo.16993649](https://doi.org/10.5281/zenodo.16993649)


---

## NFDI4BIOIMAGE Calendar October 2025

Vivien Joisten-Rosenthal

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar October 2025.
As part of the MibiNet SFB 1535 project (https://www.sfb1535.hhu.de), this lichen was collected in the Northern Eifel region, between Blankenheim and Schmidtheim in Germany. Lichens are among the most successful examples of complex mutualistic symbiosis, where a fungus (mycobiont) forms an association with one or more photosynthetic organisms (photobionts), including green algae and/or cyanobacteria. Based on ITS analysis, the lichen shown has been identified as Peltigera neckeri. Lichens of the genus Peltigera are classified as cyanolichens due to their symbiotic association with a cyanobacterial photobiont of the genus Nostoc. The image shows the lichen's blue-gray thallus when wet, after its collection on a mossy stone.




Research project


MibiNet SFB 1535 Project B02




Recording date; time


2023-10-28; 12:21 CEST




Location


Northern Eifel, between Blankenheim and Schmidtheim, Germany




Environmental conditions


Cloudy, slightly rainy




Temperature


14&deg;C




Organism


Peltigera neckeri




Organism attribute


Cyanolichen, foliose




Mycobiont


Peltigera




Photobiont


Nostoc




Substrate


Moss




Camera


Apple iPhone 12




Objective


iPhone 12 back dual wide camera 4.2mm f/1.6




Size


4,032 x 3,024 px




Submitted via NFDI4BIOIMAGE





Tags: Exclude From Dalia

[https://zenodo.org/records/16993297](https://zenodo.org/records/16993297)

[https://doi.org/10.5281/zenodo.16993297](https://doi.org/10.5281/zenodo.16993297)


---

## NFDI4BIOIMAGE Calendar September 2025

Heidi Faber-Zuschratter, Torsten Stöter, Werner Zuschratter, Roland Hartig, Markus Wilke

Published 2025-09-15

Licensed CC-BY-4.0



Image from the NFDI4BIOIMAGE Calendar September 2025.
The scanning electron micrograph shows the approach of T-lymphocytes (Jurkat cells; cyan) to an antigen-presenting B cell (Raji cell; yellow) in the center. The image was taken as part of the research work of the CRC 854, which focused on molecular processes that regulate inter- and intracellular communication within the immune system.
Image Metadata (using REMBI template):




Study




Study description


Ultrastructure of the immune synapse




Study type


Research project within DFG CRC 854 (Molecular organisation of cellular communication within the immune system)




Study Component




Imaging method


Scanning Electron Microscopy




Biosample




Biological entity


Jurkat cell line E6.1 and Raji B cell lymphoma cell line




Organism


Homo sapiens




Identity


Z21_A1




Specimen




Preparation method


Cell lines were maintained in RPMI 1640 medium supplemented with 10% fetal calf serum (FCS; PAN Biotech), stable L-glutamine, penicillin (50 U/ml), and streptomycin (50 mg/ml) (Biochrom) in humidified 5% CO2 at 37&deg;C. E6.1 cells were mixed at a 1:1 ratio with Raji B cells that had been pulsed with SEE (bacterial SAG staphylococcal enterotoxin E). After 10 min cells were plated on poly-L-lysine&ndash;covered slides at room temperature for 5 min and fixed for 10 min in PBS (pH 7.4) containing 1.5% PFA and 0.025% glutaraldehyde. Cryo-drying by critical point dryer (Leica EM CPD300) followed by sputtering with gold.




Signal/contrast mechanism


Detected secondary electrons




Channel 1 - content


Jurkat cell line E6.1 (artificial color table, cyan)




Channel 1 - biological entity


Surface of Jurkat cells 




Channel 2 - content


Raji B cell lymphoma cell line (artificial color table, yellow)




Channel 2 - biological entity


Surface of a Raji B cell 




Image acquisition




Instrument attributes


FEI XL30 FEG ESEM




Image acquisition parameters


10 keV, Magnification 6500 x, Scale bar: 2 &micro;m




Submitted via NFDI4BIOIMAGE





Tags: Exclude From Dalia

[https://zenodo.org/records/16993178](https://zenodo.org/records/16993178)

[https://doi.org/10.5281/zenodo.16993178](https://doi.org/10.5281/zenodo.16993178)


---

## NFDI4BIOIMAGE data management illustrations by Henning Falk

NFDI4BIOIMAGE Consortium

Published 2024-11-29

Licensed CC-BY-4.0



These illustrations were contracted by the Heinrich Heine University D&uuml;sseldorf in the frame of the consortium NFDI4BIOIMAGE from Henning Falk for the purpose of education and public outreach. The illustrations are free to use under a CC-BY 4.0 license.AttributionPlease include an attribution similar to: "Data annoation matters", NFDI4BIOIMAGE Consortium (2024): NFDI4BIOIMAGE data management illustrations by Henning Falk, Zenodo,&nbsp;https://doi.org/10.5281/zenodo.14186100, is used under a CC-BY 4.0 license. Modifications to this illustration include cropping.
&nbsp;

Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

[https://zenodo.org/records/14186101](https://zenodo.org/records/14186101)

[https://doi.org/10.5281/zenodo.14186101](https://doi.org/10.5281/zenodo.14186101)


---

## NFDI4BIOIMAGE: Perspective for a national bioimaging standard

Josh Moore, Susanne Kunis

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage, Exclude From Dalia

Content type: Publication

[https://ceur-ws.org/Vol-3415/paper-27.pdf](https://ceur-ws.org/Vol-3415/paper-27.pdf)


---

## NFDI4Bioimage - TA3-Hackathon - UoC-2023 (Cologne Hackathon)

Mohamed M. Abdrabbou, Mehrnaz Babaki, Tom Boissonnet, Michele Bortolomeazzi, Eik Dahms, Vanessa A. F. Fuchs, Moritz Hoevels, Niraj Kandpal, Christoph Möhl, Joshua A. Moore, Astrid Schauss, Andrea Schrader, Torsten Stöter, Julia Thönnißen, Monica Valencia-S., H. Lukas Weil, Jens Wendt and Peter Zentis

Licensed CC-BY-4.0



Tags: Arc, Dataplant, Hackathon, Nfdi4Bioimage, OMERO, Python, Research Data Management, Exclude From Dalia

Content type: Event, Publication, Documentation

[https://github.com/NFDI4BIOIMAGE/Cologne-Hackathon-2023](https://github.com/NFDI4BIOIMAGE/Cologne-Hackathon-2023)

[https://doi.org/10.5281/zenodo.10609770](https://doi.org/10.5281/zenodo.10609770)


---

## NFDI4Bioimage - TA3-Hackathon - UoC-2023 (Cologne-Hackathon-2023, GitHub repository)

Mohamed Abdrabbou, Mehrnaz Babaki, Tom Boissonnet, Michele Bortolomeazzi, Eik Dahms, Vanessa Fuchs, A. F. Moritz Hoevels, Niraj Kandpal, Christoph Möhl, Joshua A. Moore, Astrid Schauss, Andrea Schrader, Torsten Stöter, Julia Thönnißen, Monica Valencia-S., H. Lukas Weil, Jens Wendt, Peter Zentis

Licensed CC-BY-4.0



This repository documents the first NFDI4Bioimage - TA3-Hackathon - UoC-2023 (Cologne Hackathon), where topics like 'Interoperability', 'REMBI / Mapping', and 'Neuroglancer (OMERO / zarr)' were explored through collaborative discussions and workflow sessions, culminating in reports that bridge NFDI4Bioimage to DataPLANT. Funded by various DFG initiatives, this event emphasized documentation and use cases, contributing preparatory work for future interoperability projects at the 2nd de.NBI BioHackathon in Bielefeld.

Tags: Research Data Management, FAIR-Principles, Bioimage Analysis, Nfdi4Bioimage, Exclude From Dalia

Content type: Github Repository

[https://zenodo.org/doi/10.5281/zenodo.10609770](https://zenodo.org/doi/10.5281/zenodo.10609770)


---

## NFDI4Bioimage Calendar 2024 October; original image

Christian Jüngst, Peter Zentis

Published 2024-09-25

Licensed CC-BY-4.0



Raw microscopy image from the NFDI4Bioimage calendar October 2024

Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/14937632](https://zenodo.org/records/14937632)

[https://doi.org/10.5281/zenodo.14937632](https://doi.org/10.5281/zenodo.14937632)


---

## Navigating the Bioimage Analysis Landscape: Understanding the Community  and its Collaborative Dynamics

Martin Schätz

Published 2024-06-28

Licensed CC-BY-4.0



Presented as a part of:
Mexican Bioimaging Workshops 9: Fundamentos de Microscop&iacute;a &ldquo;Microscop&iacute;a en la Salud&rdquo;
Workshop on light microscopyJune 26th to 28th, 2024
Outreach 9June 29th, 2024
Expanding Global Access to BioimagingConnecting the Mexican Bioimaging Community

Tags: Include In Dalia

[https://zenodo.org/records/12584729](https://zenodo.org/records/12584729)

[https://doi.org/10.5281/zenodo.12584729](https://doi.org/10.5281/zenodo.12584729)


---

## Nd2 does not open in Fiji Bio_formats 8.1.1

Jaramillo Carlos

Published 2025-06-02

Licensed CC-BY-4.0



this file is a .nd2 image of a pollen grain taken with a Nikon 80i.&nbsp; It is in RGB and it is a stack of hundreds of Z layers

Tags: Exclude From Dalia

[https://zenodo.org/records/15579371](https://zenodo.org/records/15579371)

[https://doi.org/10.5281/zenodo.15579371](https://doi.org/10.5281/zenodo.15579371)


---

## Nd2 does not open in Fiji Bio_formats 8.1.1 (additional files)

Jonatan Bustos

Published 2025-05-23

Licensed CC-BY-4.0



This dataset contains 4 .nd2 image files of pollen grains captured using a Nikon 80i microscope. The files include both the original full-frame images and cropped Regions of Interest (ROIs) extracted from them. All images are in RGB format and include multiple Z-stack layers.

Tags: Exclude From Dalia

[https://zenodo.org/records/15493140](https://zenodo.org/records/15493140)

[https://doi.org/10.5281/zenodo.15493140](https://doi.org/10.5281/zenodo.15493140)


---

## Nd2 does not open in Fiji Bio_formats 8.1.1 (on Windows)

Loïc Sauteur

Published 2025-07-31

Licensed CC-BY-4.0



Related to github issue: https://github.com/ome/bioformats/issues/3517
&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/16628927](https://zenodo.org/records/16628927)

[https://doi.org/10.5281/zenodo.16628927](https://doi.org/10.5281/zenodo.16628927)


---

## New Kid on the (NFDI) Block: NFDI4BIOIMAGE  - A National Initiative for FAIR Data Management in Bioimaging and Bioimage Analysis

Cornelia Wetzker

Published 2024-10-29

Licensed CC-BY-4.0



The poster introduces the consortium NFDI4BIOIMAGE with its central objectives, provides an overview of challenges in bioimage data handling, sharing and analysis and lists support options by the consortium through its data stewardship team.
It is part of the work of the German consortium NFDI4BIOIMAGE funded by the Deutsche Forschungsgemeinschaft (DFG grant number NFDI 46/1, project number 501864659) and has been presented at the conference FDM@Campus held in G&ouml;ttingen September 23-25, 2024.

Tags: Exclude From Dalia

[https://zenodo.org/records/14006558](https://zenodo.org/records/14006558)

[https://doi.org/10.5281/zenodo.14006558](https://doi.org/10.5281/zenodo.14006558)


---

## Nextflow: Scalable and reproducible scientific workflows

Floden Evan, Di Tommaso Paolo

Published 2020-12-17

Licensed CC-BY-4.0



Nextflow is an open-source workflow management system that prioritizes portability and reproducibility. It enables users to develop and seamlessly scale genomics workflows locally, on HPC clusters, or in major cloud providers&rsquo; infrastructures. Developed since 2014 and backed by a fast-growing community, the Nextflow ecosystem is made up of users and developers across academia, government and industry. It counts over 1M downloads and over 10K users worldwide.

Tags: Workflow Engine, Exclude From Dalia

Content type: Slides

[https://zenodo.org/records/4334697](https://zenodo.org/records/4334697)

[https://doi.org/10.5281/zenodo.4334697](https://doi.org/10.5281/zenodo.4334697)


---

## NuInsSeg

Amirreza Mahbod, Christine Polak, Katharina Feldmann, Rumsha Khan, Katharina Gelles, Georg Dorffner, Ramona Woitek, Sepideh Hatamikia, Isabella Ellinger

Published 2024-05-14

Licensed CC-BY-4.0



A Fully Annotated Dataset for Nuclei Instance Segmentation in H&E-Stained Images

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://www.kaggle.com/datasets/ipateam/nuinsseg](https://www.kaggle.com/datasets/ipateam/nuinsseg)


---

## OME Documentation

Licensed CC-BY-4.0



Tags: OMERO, Include In Dalia

Content type: Documentation

[https://www.openmicroscopy.org/docs/](https://www.openmicroscopy.org/docs/)


---

## OME-NGFF: a next-generation file format for expanding bioimaging data-access strategies

Josh Moore, Chris Allan, Sébastien Besson, Jean-Marie Burel, Erin Diel, David Gault, Kevin Kozlowski, Dominik Lindner, Melissa Linkert, Trevor Manz, Will Moore, Constantin Pape, Christian Tischer, Jason R. Swedlow

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

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

Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

[https://zenodo.org/records/14234608](https://zenodo.org/records/14234608)

[https://doi.org/10.5281/zenodo.14234608](https://doi.org/10.5281/zenodo.14234608)


---

## OMExcavator: a tool for exporting and connecting  Bioimaging-specific metadata in wider knowledge graphs

Stefan Dvoretskii, Klaus Maier-Hein, Marco Nolden, Christian Schmidt, Michele Bortolomeazzi, Josh Moore

Published 2025-05-15

Licensed CC-BY-4.0



Tags: Include In Dalia

[https://zenodo.org/records/15423904](https://zenodo.org/records/15423904)

[https://doi.org/10.5281/zenodo.15423904](https://doi.org/10.5281/zenodo.15423904)


---

## OMExcavator: a tool for exporting and connecting domain-specific metadata in a wider knowledge graph

Stefan Dvoretskii, Michele Bortolomeazzi, Marco Nolden, Christian Schmidt, Klaus Maier-Hein, Josh Moore

Published 2025-02-21

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage, Exclude From Dalia

[https://zenodo.org/records/15268798](https://zenodo.org/records/15268798)

[https://doi.org/10.5281/zenodo.15268798](https://doi.org/10.5281/zenodo.15268798)


---

## Omero-tools

Johannes Soltwedel

Licensed CC-BY-4.0



This repository contains a collection of tools for working with OMERO. Such tools can be working with the OMERO command line interface to transfer datasets between repositories, etc.

Tags: OMERO, Bioimage Analysis, Exclude From Dalia

Content type: Github Repository

[https://biapol.github.io/omero-tools/](https://biapol.github.io/omero-tools/)


---

## Open Image Data Handbook

Kevin Yamauchi

Licensed CC-BY-4.0



Tags: Neubias, Research Data Management, Napari, Python, Bioimage Analysis, Include In Dalia

Content type: Book, Notebook

[https://kevinyamauchi.github.io/open-image-data/intro.html](https://kevinyamauchi.github.io/open-image-data/intro.html)


---

## Open Micoscropy Environment (OME) Youtube Channel

Published None

Licensed CC-BY-4.0



OME develops open-source software and data format standards for the storage and manipulation of biological microscopy data

Tags: Open Source Software, Exclude From Dalia

Content type: Video, Collection

[https://www.youtube.com/@OpenMicroscopyEnvironment](https://www.youtube.com/@OpenMicroscopyEnvironment)


---

## Open Science, Sharing & Licensing

Robert Haase

Published 2024-04-18

Licensed CC-BY-4.0



Wir tauchen ein in die Welt der Open Science und definieren Begriffe wie Open Source, Open Access und die FAIR-Prinzipien (Findable, Accessible, Interoperable and Reuasable). Wir diskutieren, wie diese Methoden der [wissenschaftlichen] Kommunikation und des Datenmanagements die Welt ver&auml;ndern und wie wir sie praktisch in unsere Arbeit integrieren k&ouml;nnen. Dabei spielen Aspekte wie Copyright und Lizenzierung eine wichtige Rolle.

Tags: Research Data Management, Open Access, FAIR-Principles, Licensing, Include In Dalia

Content type: Slides

[https://zenodo.org/records/10990107](https://zenodo.org/records/10990107)

[https://doi.org/10.5281/zenodo.10990107](https://doi.org/10.5281/zenodo.10990107)


---

## Open Source Platform for Scalable Multi-Purpose Virtual Desktop Infrastructures

Michael Scherle, Rafael Gieschke, Isabela Mocanu, Björn Grüning, von Suchodoletz, Dirk

Published 2025-09-12

Licensed CC-BY-4.0



Data and access to it are central to each NFDI consortium. However, moving data&nbsp;around is often impractical&mdash;it may be too large, sensitive, or restricted by agreements&nbsp;with, e.g., the funding provider, and copying introduces duplication, versioning issues,&nbsp;and loss of provenance. Rather than bringing data to the researcher, a Desktop-as-a-Service (DaaS) approach can offer researchers interactive, high-performance access in a secure and efficient manner. Driven by the need for seamless workflows and&nbsp;efficient data handling in NFDI4BIOIMAGE, we present a DaaS approach that is&nbsp;broadly applicable across NFDI. It supports diverse use cases, such as standardized&nbsp;virtual training environments for distributed participants (like required in DataPLANT), remote visualization of large-scale HPC datasets, and secure access to sensitive&nbsp;data (BERD)&mdash;all without the overhead of local machine setup and maintenance.

Tags: Exclude From Dalia

[https://zenodo.org/records/17103962](https://zenodo.org/records/17103962)

[https://doi.org/10.5281/zenodo.17103962](https://doi.org/10.5281/zenodo.17103962)


---

## Open source AI Tools for bioimage analysis workshop (2024) @ICOB, Academia Sinica, Taiwan

Wei-Chen Chu

Published 2024-08-09

Licensed CC-BY-4.0



Presentation file used in the &nbsp;Open source AI Tools for bioimage analysis workshop @ICOB, Academia Sinica, Taiwan (2024)Introduce ilastik, StarDist, Cellpose, Segment Anything Model (SAM), and how to use it briefly.
Full video recording (in Chinese) is available on YouTube: https://youtu.be/KqwssouW0G0
This document is part III of the previous document:Chu, W.-C. (2024). Bioimage Analysis with FIJI /ImageJ &amp; Friends workshop (2024) @ICOB, Academia Sinica, Taiwan. Zenodo. https://doi.org/10.5281/zenodo.12803966

Tags: Bioimage Analysis, Include In Dalia

[https://zenodo.org/records/13284351](https://zenodo.org/records/13284351)

[https://doi.org/10.5281/zenodo.13284351](https://doi.org/10.5281/zenodo.13284351)


---

## Optimisation and Validation of a Swarm Intelligence based Segmentation Algorithm for low Contrast Positron Emission Tomography

Robert Haase

Published 2014-04-01

Licensed CC-BY-4.0



In the field of radiooncological research, individualised therapy is one of the hot topics at the moment. As a key aspect biologically-adapted therapy is discussed. Therapy adaption based on biological parameters&nbsp;may include tomographic imaging to determine biological properties of the tumour. One often invoked&nbsp;imaging modality is positron emission tomography (PET) using the tracer [18F]-fluoromisonidazole&nbsp;(FMISO) for hypoxia imaging. Hypoxia imaging is of interest, because hypoxic tumours are known to be radiorestistant. Even further, patients with hypoxic tumours have worse prognosis compared to patients&nbsp;with normoxic tumours. Thus, hypoxia imaging appears promising for radiotherapy treatment adaption.&nbsp;For example, volumetric analysis of FMISO PET could deliver additional hypoxia target volumes, which&nbsp;may be irradiated with higher radiation doses to improve the therapeutic effect. However, limited contrast&nbsp;between target volume and background in FMISO PET images interferes image analysis.Established&nbsp;methods for target volume delineation in PET do not allow determination of reliable contours in FMISO PET. To tackle this aspect, this thesis focusses on an earlier developed swarm intelligence based&nbsp;segmentation algorithm for FMISO PET and rather, its optimisation and validation in a clinically relevant&nbsp;setting. In this setting, clinical FMISO PET images were used which were acquired as part of a clinical&nbsp;trial performed at the Clinic and Policlinic for Radiation Therapy and Radiooncology of the University&nbsp;Hospital Carl Gustav Carus Dresden. The segmentation algorithm was applied to these imaging data&nbsp;sets and optimised using a cross-validation approach incorporating reference contours from experienced&nbsp;observers who outlined FMISO PET positive volumes manually. Afterwards, the performance of the algorithm&nbsp;and the properties of the resulting contours were studied in more detail. The algorithm was shown&nbsp;to deliver contours which were similar to manually-created contours to a degree like manually-created&nbsp;contours were similar to each other. Thus, the application of the algorithm in clinical research is recommended&nbsp;to eliminate inter-observer-variabilities. Finally, it was shown that repeated FMISO PET imaging&nbsp;before and shortly after the beginning of combined radiochemotherapy lead to manually-created contours&nbsp;with significantly higher variations than the variations of automatically-created contours using the&nbsp;proposed algorithm. Increased contour similarity in subsequently acquired imaging data highlights the&nbsp;observer-independence of the algorithm. While several observers outline different volumes, in identical&nbsp;data sets as well as in subsequent imaging data sets, the algorithm outlines more stable volumes in both&nbsp;cases. Thus, increased contour reproducibility is reached by automation of the delineation process by&nbsp;the proposed algorithm.&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/7209862](https://zenodo.org/records/7209862)

[https://doi.org/10.5281/zenodo.7209862](https://doi.org/10.5281/zenodo.7209862)


---

## Optimized cranial window implantation for subcellular and functional imaging in vivo

Ben Vermaercke

Published 2025-01-13

Licensed CC-BY-4.0



Intravital workshop 15/11/2024

Tags: Exclude From Dalia

[https://zenodo.org/records/14641777](https://zenodo.org/records/14641777)

[https://doi.org/10.5281/zenodo.14641777](https://doi.org/10.5281/zenodo.14641777)


---

## Overview of the Galaxy OMERO-suite - Upload images and metadata in OMERO using Galaxy

Riccardo Massei, Björn Grüning

Published 2024-12-02

Licensed CC-BY-4.0



Tags: OMERO, Galaxy, Metadata, Nfdi4Bioimage, Include In Dalia

Content type: Tutorial, Framework, Workflow

[https://training.galaxyproject.org/training-material/topics/imaging/tutorials/omero-suite/tutorial.html](https://training.galaxyproject.org/training-material/topics/imaging/tutorials/omero-suite/tutorial.html)


---

## Parallelization and heterogeneous computing: from pure CPU to GPU-accelerated image processing

Robert Haase

Licensed CC-BY-4.0



Tags: Include In Dalia

Content type: Slides

[https://f1000research.com/slides/11-1171](https://f1000research.com/slides/11-1171)

[https://doi.org/10.7490/f1000research.1119154.1](https://doi.org/10.7490/f1000research.1119154.1)


---

## Parhyale 3D segmentation dataset

Frederike Alwes, Ko Sugawara, Michalis Averof

Published 2023-08-11

Licensed CC-BY-4.0



The Parhyale 3D Segmentation dataset consists of 50 timepoints (TP01-TP50) of 3D images (512x512x34), where the manual annotations can be found at discrete 6 timepoints (at TP01, TP11, TP21, TP31, TP41 and TP50).

For further&nbsp;details, see README&nbsp;file.

This version fixes&nbsp;the duplicated label IDs found in the previous version of label files. This version ensures that each instance has a unique ID. Thanks to&nbsp;Jackson Borchardt for reporting that error.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/8252039](https://zenodo.org/records/8252039)

[https://doi.org/10.5281/zenodo.8252039](https://doi.org/10.5281/zenodo.8252039)


---

## Photonic data analysis in 2050

Oleg Ryabchykov, Shuxia Guo, Thomas Bocklitz

Licensed CC-BY-4.0



Photonic data analysis, combining imaging, spectroscopy, machine learning, and computer science, requires flexible methods and interdisciplinary collaborations to advance. Essential developments include standardizing data infrastructure for comparability, optimizing data-driven models for complex investigations, and creating techniques to handle limited or unbalanced data and device variations.

Tags: FAIR-Principles, Machine Learning, Research Data Management, Include In Dalia

Content type: Publication

[https://doi.org/10.1016/j.vibspec.2024.103685](https://doi.org/10.1016/j.vibspec.2024.103685)


---

## Platynereis EM training data

Constantin Pape

Published 2020-02-19

Licensed CC-BY-4.0



Training data for Convolutional Neural Networks used in the publication Whole-body integration of gene expression and single-cell morphology. We provide training data for segmenting structures in the SerialBlockface Electron Microscopy data-set containing a complete 6 day old Platynereis dumerilii larva, in particular for:
- cell membranes: 9 training blocks @ resolution 20x20x25 nm. Based on initial training data provided by https://ariadne.ai/.
- cilia: 3 training and 2 validation blocks @ resolution 20x20x25 nm.
- cuticle: 5 training blocks @ resolution 40x40x50 nm.
- nuclei: 12 training blocks @ resolution 80x80x100 nm. Based on initial training data provided by https://ariadne.ai/.

For details on how to use this data for training, see https://github.com/platybrowser/platybrowser-backend/tree/master/segmentation.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/3675220](https://zenodo.org/records/3675220)

[https://doi.org/10.5281/zenodo.3675220](https://doi.org/10.5281/zenodo.3675220)


---

## Platynereis dumerilii full-length transcriptome of developmental stages

Vellutini, Bruno C., Mette Handberg-Thorsager, Pavel Tomancak

Published 2024-11-29

Licensed CC-BY-4.0



To generate a high-quality full-length transcriptome for the annelid&nbsp;Platynereis dumerilii, we collected samples from representative developmental stages, from unfertilized eggs to 5 days post-fertilization. Each sample consisted of a bulk mix from 1 to 5 batches of embryos fertilized by different parents. We incubated all batches at 18 degrees Celsius until the desired time point, then collected the embryos into a clean tube and snap-froze them in liquid nitrogen with as little seawater as possible. The samples were stored at -80 degrees Celsius until RNA extraction. We extracted total RNA from the samples using a Trizol protocol. After measuring the RNA concentration with NanoDrop, we created a bulk RNA mix by combining 1 &micro;L from each sample into a new tube. We gave the sample to the Sequencing and Genotyping facility of the Max Planck Institute of Molecular Cell Biology and Genetics, who ran aliquots of this bulk mix through a Bioanalyzer and gel electrophoresis. They found no evidence of RNA degradation. From this sample, they prepared PacBio Iso-Seq libraries using the Express Template Prep Kit 2.0 and sequenced full-length transcripts on a SMRT 8M Cell for 30 hours using a PacBio Sequel II System. They processed the raw movie subreads with SMRT Analysis software, following the Iso-Seq v3 workflow to generate representative circular consensus sequences, demultiplex and remove primers, trim poly(A) tails, and remove concatemers. After transcript clustering and merging, the resulting dataset contained 176,122 polished high-quality isoforms. Using Cogent, we removed redundant isoforms and obtained a dataset with 117,524 transcripts. From this, we generated a dataset containing only the longest isoform for each gene, with 70,003 sequences in total. We calculated descriptive metrics using Transrate. To estimate their completeness, we used BUSCO for metazoa and obtained a score of 85%. Finally, we annotated the longest-isoform dataset using EnTAP. About 85% of the transcripts have a coding sequence. We obtained annotations for 67% of the sequences, while 33% have remained unannotated.
Datasets



file name
file size (zipped)
sequences
description


0-Pdum_workflow.zip (folder)
3.40 GB
-
entire pipeline with notebook entries and analyses


1-Pdum_hq_isoforms.zip (fasta)
180.30 MB
176,122
polished high-quality isoforms from CCS


2-Pdum_co_isoforms.zip (fasta)
70.68 MB
117,524
non-redundant polished high-quality isoforms


3-Pdum_co_longest.zip (fasta)
54.85 MB
70,003
longest of non-redundant polished high-quality isoforms


4-Pdum_co_longest_annotations.zip (tsv)
34.37 MB
70,003 (46,635 annotated)
annotations for longest-isoform dataset



&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/14250773](https://zenodo.org/records/14250773)

[https://doi.org/10.5281/zenodo.14250773](https://doi.org/10.5281/zenodo.14250773)


---

## PoL Bio-Image Analysis Training School on GPU-Accelerated Image Analysis

Stephane Rigaud, Brian Northan, Till Korten, Neringa Jurenaite, Apurv Deepak Kulkarni, Peter Steinbach, Sebastian Starke, Johannes Soltwedel, Marvin Albert, Robert Haase

Licensed CC-BY-4.0



This repository hosts notebooks, information and data for the GPU-Accelerated Image Analysis Track of the PoL Bio-Image Analysis Symposium.

Tags: Gpu, Clesperanto, Dask, Python, Include In Dalia

Content type: Notebook

[https://github.com/BiAPoL/PoL-BioImage-Analysis-TS-GPU-Accelerated-Image-Analysis/](https://github.com/BiAPoL/PoL-BioImage-Analysis-TS-GPU-Accelerated-Image-Analysis/)


---

## Practical Guide to the International Alignment of Research Data Management - Extended Edition

Licensed CC-BY-4.0



Tags: Include In Dalia

Content type: Book

[https://www.scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/](https://www.scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/)

[https://doi.org/10.5281/zenodo.4915861](https://doi.org/10.5281/zenodo.4915861)


---

## Practical considerations for data exploration in quantitative cell biology

Joanna W. Pylvänäinen, Hanna Grobe, Guillaume Jacquemet

Published 2025-04-07

Licensed CC-BY-4.0



This article emphasizes the importance of structured, hands-on data exploration in quantitative cell biology, offering practical advice for analyzing bioimage datasets. It also highlights how generative AI and large language models can enhance and streamline data workflows for more reliable and transparent research.

Tags: Bioimage Analysis, Data Exploration, Include In Dalia

Content type: Publication

[https://journals.biologists.com/jcs/article/138/7/jcs263801/367617/Practical-considerations-for-data-exploration-in](https://journals.biologists.com/jcs/article/138/7/jcs263801/367617/Practical-considerations-for-data-exploration-in)


---

## Preprint: "Be Sustainable", Recommendations for FAIR Resources in Life Sciences research: EOSC-Life's Lessons

Romain David, Arina Rybina, Jean-Marie Burel, Jean-Karim Heriche, Pauline Audergon, Jan-Willem Boiten, Frederik Coppens, Sara Crockett, Exter Katrina, Sven Fahrener, Maddalena Fratelli, Carole Goble, Philipp Gormanns, Tobias Grantner, Bjorn Gruning, Kim Tamara Gurwitz, John Hancock, Henriette Harmse, Petr Holub, Nick Juty, Geoffrey Karnbach, Emma Karoune, Antje Keppler, Jessica Klemeier, Carla Lancelotti, Jean-Luc Legras, L. Allyson Lister, Dario Livio Longo, Rebecca Ludwig, Benedicte Madon, Marzia Massimi, Vera Matser, Rafaele Matteoni, Mayrhofer Michaela Th., Christian Ohmann, Maria Panagiotopoulou, Helen Parkinson, Isabelle Perseil, Claudia Pfander, Roland Pieruschka, Michael Raess, Andreas Rauber, Audrey S. Richard, Paolo Romano, Antonio Rosato, Alex Sanchez-Pla, Susanna-Assunta Sansone, Ugis Sarkans, Beatriz Serrano-Solano, Jing Tang, Ziaurrehman Tanoli, Jonathan Tedds, Harald Wagener, Martin Weise, Hans V. Westerhoff, Rudolf Wittner, Jonathan Ewbank, Niklas Blomberg, Philip Gribbon

Published 2023-09-12

Licensed CC-BY-4.0



"Be SURE - Be SUstainable REcommendations"The main goals and challenges for the Life Science (LS) communities in the Open Science framework are to increase reuse and sustainability of data resources, software tools, and workflows, especially in large-scale data-driven research and computational analyses. Here, we present key findings, procedures, effective measures and recommendations for generating and establishing sustainable LS resources based on the collaborative, cross-disciplinary work done within the EOSC-Life (European Open Science Cloud for Life Sciences) consortium. Bringing together 13 European LS Research Infrastructures (RIs), it has laid the foundation for an open, digital space to support biological and medical research. Using lessons learned from 27 selected projects, we describe the organisational, technical, financial and legal/ethical challenges that represent the main barriers to sustainability in the life sciences. We show how EOSC-Life provides a model for sustainable FAIR data management, including solutions for sensitive- and industry-related resources, by means of cross-disciplinary training and best practices sharing. Finally, we illustrate how data harmonisation and collaborative work facilitate interoperability of tools, data, solutions and lead to a better understanding of concepts, semantics and functionalities in the life sciences.IN PRESS EMBO Journal:&nbsp;https://www.embopress.org/journal/14602075&nbsp;AVAILABLE SOON at : https://doi.org/10.15252/embj.2023115008&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/8338931](https://zenodo.org/records/8338931)

[https://doi.org/10.5281/zenodo.8338931](https://doi.org/10.5281/zenodo.8338931)


---

## ProdgerLab-StarDist-HIV Target Cell Training Set

Zhongtian Shao

Published 2023-06-28

Licensed CC-BY-4.0



40 annotated immunofluorescence microscopy images (600 microns x 600 microns) of foreskin tissue stained for CD3/CD4/CCR5/Nuclei. These images were used to train StarDist models used for the identification of HIV Target Cells in foreskin tissue section scans.&nbsp;

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/8091914](https://zenodo.org/records/8091914)

[https://doi.org/10.5281/zenodo.8091914](https://doi.org/10.5281/zenodo.8091914)


---

## Prompt Engineering, Agentic Workflows and Multi-modal Large Language Models

Robert Haase

Published 2025-01-19

Licensed CC-BY-4.0



In these two slide-decks we explore applications of large language models. In the first slide deck we dive into prompt engineering, function calling and how to build agentic workflows. In the second slide-deck we explore multi-modal large language models focusing on vision language models and image generation models.&nbsp;

Tags: Include In Dalia

[https://zenodo.org/records/14692037](https://zenodo.org/records/14692037)

[https://doi.org/10.5281/zenodo.14692037](https://doi.org/10.5281/zenodo.14692037)


---

## PygamePrompts

Lea Kabjesz, Lea Gihlein, Mara Lampert, FPGro

Published 2025-08-12T11:36:36+00:00

Licensed CC-BY-4.0



A collection of workshop materials for exploring prompting techniques by building a Snake game in Cursor.  

Tags: Include In Dalia

Content type: Github Repository

[https://github.com/kaabl/PygamePrompts](https://github.com/kaabl/PygamePrompts)


---

## QI 2024 Analysis Lab Manual

Beth Cimini, Florian Jug, QI 2024

Licensed CC-BY-4.0



This book contains the quantitative analysis labs for the QI CSHL course, 2024

Tags: Python, Include In Dalia

Content type: Notebook

[https://bethac07.github.io/qi_2024_analysis_lab_manual/intro.html](https://bethac07.github.io/qi_2024_analysis_lab_manual/intro.html)


---

## QM Course Lectures on Bio-Image Analysis with napari 2024

Marcelo Leomil Zoccoler

Licensed CC-BY-4.0



In these lectures, we will explore ways to analyze microscopy images with Python and visualize them with napari, an nD viewer open-source software. The analysis will be done in Python mostly using the scikit-image, pyclesperanto and apoc libraries, via Jupyter notebooks. We will also explore some napari plugins as an interactive and convenient alternative way of performing these analysis, especially the napari-assistant, napari-apoc and napari-flim-phasor-plotter plugins.

Tags: Napari, Python, Include In Dalia

Content type: Notebook

[https://zoccoler.github.io/QM_Course_Bio_Image_Analysis_with_napari_2024](https://zoccoler.github.io/QM_Course_Bio_Image_Analysis_with_napari_2024)


---

## QUAREP-LiMi: A community-driven initiative to establish guidelines for quality assessment and reproducibility for instruments and images in light microscopy

Glyn Nelson, Ulrike Boehme, et al.

Licensed CC-BY-4.0



Tags: Quareo-Limi, Include In Dalia

Content type: Publication

[https://onlinelibrary.wiley.com/doi/10.1111/jmi.13041](https://onlinelibrary.wiley.com/doi/10.1111/jmi.13041)


---

## QuPath: Open source software for analysing (awkward) images

Peter Bankhead

Published 2020-12-16

Licensed CC-BY-4.0



Slides from the CZI/EOSS online meeting in December 2020.

Tags: Bioimage Analysis, Include In Dalia

Content type: Slides

[https://zenodo.org/records/4328911](https://zenodo.org/records/4328911)

[https://doi.org/10.5281/zenodo.4328911](https://doi.org/10.5281/zenodo.4328911)


---

## RDF as a bridge to domain-platforms like OMERO, or There and back again.

Josh Moore, Andra Waagmeester, Kristina Hettne, Katherine Wolstencroft, Susanne Kunis

Licensed CC-BY-4.0



In 2005, the first version of OMERO stored RDF natively. However, just a year after the 1.0 release of RDF, performance considerations led to the development of a more traditional SQL approach for OMERO. A binary protocol makes it possible to query and retrieve metadata but the resulting information cannot immediately be combined with other sources. This is the adventure of rediscovering the benefit of RDF triples as a -- if not the -- common exchange mechanism.

Tags: Research Data Management, FAIR-Principles, Bioimage Analysis, Exclude From Dalia

Content type: Slides

[https://zenodo.org/doi/10.5281/zenodo.10687658](https://zenodo.org/doi/10.5281/zenodo.10687658)


---

## RDM Starter Kit

GO FAIR

Licensed CC-BY-4.0



This page is supposed to serve as a Starter Kit for research data management (RDM). It lists resources designed to help researchers get started to organize their data.

Tags: Research Data Management, Include In Dalia

Content type: Website

[https://www.go-fair.org/resources/rdm-starter-kit/](https://www.go-fair.org/resources/rdm-starter-kit/)


---

## RDM4Mic Presentations

Licensed CC-BY-4.0



Tags: Research Data Management, Exclude From Dalia

Content type: Collection

[https://github.com/German-BioImaging/RDM4mic/tree/master/presentations](https://github.com/German-BioImaging/RDM4mic/tree/master/presentations)


---

## RDMKit Training Resources

Licensed CC-BY-4.0



Tags: Research Data Management, Include In Dalia

Content type: Collection

[https://rdmkit.elixir-europe.org/all_training_resources](https://rdmkit.elixir-europe.org/all_training_resources)


---

## RESEARCH DATA MANAGEMENT on Campus and in NFDI4BIOIMAGE

Cornelia Wetzker, Michael Schlierf

Published 2024-08-29

Licensed CC-BY-4.0



The poster is part of the work of the German consortium NFDI4BIOIMAGE funded by the Deutsche Forschungsgemeinschaft (DFG grant number NFDI 46/1, project number 501864659).

Tags: Exclude From Dalia

[https://zenodo.org/records/13684187](https://zenodo.org/records/13684187)

[https://doi.org/10.5281/zenodo.13684187](https://doi.org/10.5281/zenodo.13684187)


---

## Rechtsfragen bei Open Science - Ein Leitfaden

Till Kreutzer, Henning Lahmann

Published 2021-05-25

Licensed CC-BY-4.0



Die Digitalisierung ermöglicht eine offene Wissenschaft (Open Science). Diese hat viele Aspekte, insbesondere den freien Zugang zu wissenschaftlichen Veröffentlichungen und Materialien (Open Access), transparente Begutachtungsverfahren (Open Peer Review) oder quelloffene Technologien (Open Source). Das Programm Hamburg Open Science (Laufzeit 2018–2020) unterstützt unter anderem den Kulturwandel in der Wissenschaft. In diesem Kontext entstand der nun vorliegende Leitfaden, der das rechtliche Umfeld greifbar machen soll. Der Leitfaden erarbeitet die betroffenen Rechtsgebiete zunächst systematisch. Im zweiten Teil werden rechtliche Fragen zu Open Science beantwortet, die direkt aus den Universitäten und Bibliotheken kommen.

Tags: Open Science, Open Access, Copyright, Include In Dalia

Content type: Book

[https://hup.sub.uni-hamburg.de/oa-pub/catalog/book/205](https://hup.sub.uni-hamburg.de/oa-pub/catalog/book/205)


---

## Reconstructed images of a 2DSIM multiposition acquisition.

Louis Romette

Published 2025-02-19

Licensed CC-BY-4.0



Acquired with an Nikon SIM, in 2D-SIM mode at 488nm of excitation with 30% laser power and 200ms of exposition.&nbsp; Fluorescence is a knocked-in mStayGold-&beta;2Spectrin. Cells are rat hippocampal neurons &agrave; DIV 3. The file is a reconstructed multiposition acquisition (10 positions). Uploaded to show a probable issue with Bio-Formats in Fiji, where SIM reconstrcuted multipositions files open like static noise.&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/14893791](https://zenodo.org/records/14893791)

[https://doi.org/10.5281/zenodo.14893791](https://doi.org/10.5281/zenodo.14893791)


---

## Report on a pilot study:  Implementation of OMERO for  microscopy data management

Silke Tulok, Gunar Fabig, Andy Vogelsang, Thomas Kugel, Thomas Müller-Reichert

Published 2023-11-10

Licensed CC-BY-4.0



The Core Facility Cellular Imaging (CFCI) at the Faculty of Medicine Carl Gustav Carus (TU Dresden) is currently running a pilot project for testing the use and handling of the OMERO software. This is done together with interested users of the imaging facility and a research group. Currently, we are pushing forward this pilot study on a small scale without any data steward. Our experiences argue so far for giving data management issues into the hands of dedicated personnel not fully involved in research projects. As funding agencies will ask for higher and higher standards for implementing FAIRdata principles in the future, this will be a releva

Tags: Include In Dalia

[https://zenodo.org/records/10103316](https://zenodo.org/records/10103316)

[https://doi.org/10.5281/zenodo.10103316](https://doi.org/10.5281/zenodo.10103316)


---

## Repository for: Combinatorial Wnt signaling landscape during brachiopod anteroposterior patterning

Vellutini, Bruno C., Martín-Durán, José M., Aina Børve, Andreas Hejnol

Published 2024-08-16

Licensed CC-BY-4.0



This repository contains the data and analyses for the manuscript:
Vellutini, B. C., Mart&iacute;n-Dur&aacute;n, J. M., B&oslash;rve, A. &amp; Hejnol, A.&nbsp;Combinatorial Wnt signaling landscape during brachiopod anteroposterior patterning.&nbsp;BMC Biol. 22, 1&ndash;23 (2024).&nbsp;https://doi.org/10.1186/s12915-024-01988-w
The source is maintained at&nbsp;https://github.com/bruvellu/terebratalia-wnts.

Tags: Exclude From Dalia

[https://zenodo.org/records/13338425](https://zenodo.org/records/13338425)

[https://doi.org/10.5281/zenodo.13338425](https://doi.org/10.5281/zenodo.13338425)


---

## Reproducible Bio-Image Analysis using Python, Napari, Jupyter and AI

Robert Haase

Published 2025-09-09

Licensed CC-BY-4.0



In this slide deck we learn how to write reproducible bio-image analysis code in Jupyter notebooks. Goal is not just to have code running elsewhere reproducibly, but also enabling others to understand workflows to enable them reproducing the analysis also in their mind and potentially other tools. Additionally we cover how to generate Jupyter notebooks from Napari and using artificial intelligence, namely bia-bob.

Tags: Nfdi4Bioimage, Bioimage Analysis, Include In Dalia

[https://zenodo.org/records/17085991](https://zenodo.org/records/17085991)

[https://doi.org/10.5281/zenodo.17085991](https://doi.org/10.5281/zenodo.17085991)


---

## Research Data Management

Robert Haase

Published 2025-09-22

Licensed CC-BY-4.0



This slides covers aspects of research data management (RDM) and open science such as the RDM life cylce, FAIR principles, sharing data on Zenodo, rights and duties of scientists in the RDM context.

[https://zenodo.org/records/17174207](https://zenodo.org/records/17174207)

[https://doi.org/10.5281/zenodo.17174207](https://doi.org/10.5281/zenodo.17174207)


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

Tags: Research Data Management, Include In Dalia

Content type: Slides

[https://zenodo.org/record/6602101](https://zenodo.org/record/6602101)

[https://doi.org/10.5281/zenodo.6602101](https://doi.org/10.5281/zenodo.6602101)


---

## Research Data Managemet and how not to get overwhelmed with data

Martin Schätz

Published 2023-09-23

Licensed CC-BY-4.0



Research data management and how not to get overwhelmed with data presentation is an overview of bioimage analysis with a focus on the basics for data management planning, FAIR principles, and how to practically organize folders and prepares naming convention. The presentation includes an overview of metadata, Creative Common licenses, and a sum up of electronic laboratory notebooks. The last two slides go through how all of that works in practice in open access core microscopy facility.

Tags: Include In Dalia

[https://zenodo.org/records/8372703](https://zenodo.org/records/8372703)

[https://doi.org/10.5281/zenodo.8372703](https://doi.org/10.5281/zenodo.8372703)


---

## Research Data Reusability - Conceptual Foundations, Barriers and Enabling Technologies

Costantino Thanos

Published 2017-01-09

Licensed CC-BY-4.0



This article discusses various aspects of data reusability in the context of scientific research, including technological, legal, and policy frameworks.

Tags: Research Data Management, Open Science, Data Protection, Exclude From Dalia

Content type: Publication

[https://www.mdpi.com/2304-6775/5/1/2](https://www.mdpi.com/2304-6775/5/1/2)


---

## Research data management for bioimaging - the 2021 NFDI4BIOIMAGE community survey

Christian Schmidt, Janina Hanne, Josh Moore, Christian Meesters, Elisa Ferrando-May, et al.

Published 2022-09-20

Licensed CC-BY-4.0



As an initiative within Germany's National Research Data Infrastructure, the authors conducted this community survey in summer 2021 to assess the state of the art of bioimaging RDM and the community needs.

Tags: Research Data Management, Exclude From Dalia

Content type: Publication

[https://f1000research.com/articles/11-638/v2](https://f1000research.com/articles/11-638/v2)


---

## Research data management for bioimaging: the 2021 NFDI4BIOIMAGE community survey

Christian Schmidt, Janina Hanne, Josh Moore, Christian Meesters, Elisa Ferrando-May, Stefanie Weidtkamp-Peters, members of the NFDI4BIOIMAGE initiative

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

Content type: Publication

[https://f1000research.com/articles/11-638](https://f1000research.com/articles/11-638)


---

## Root tissue segmentation dataset

Julian Wanner, Kuhn Cuellar, Luis, Friederike Wanke

Published 2022-01-12

Licensed CC-BY-4.0



The PHDFM dataset is composed of fluorescence microscopy images of root tissue samples from A. thaliana, using the ratiometric fluorescent indicator 8‐hydroxypyrene‐1,3,6‐trisulfonic acid trisodium salt (HPTS). This semantic segmentation training dataset consists of 2D microscopy images (the brightfield channel for excitation at 405 nm), each containing a segmentation mask as an additional image channel (manually annotated by plant biologists). The segmentation masks classify pixels into the following 5 labels with the corresponding IDs: background (0), root tissue (1), early elongation zone (2), late elongation zone (3), and meristematic zone (4).

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/5841376](https://zenodo.org/records/5841376)

[https://doi.org/10.5281/zenodo.5841376](https://doi.org/10.5281/zenodo.5841376)


---

## Round Table Workshop 1 - Sample Stabilization in intravital Imaging

Michael Gerlach, Hans-Ulrich Fried, Christiane Peuckert

Published 2024-11-14

Licensed CC-BY-4.0



Notes from a round table workshop on the 4th Day of Intravital Microscopy in Leuven, Belgium.
Contains hands-on tips, tricks and schemes to improve sample stability during various models of Intravital Miroscopy.

Tags: Exclude From Dalia

[https://zenodo.org/records/14161289](https://zenodo.org/records/14161289)

[https://doi.org/10.5281/zenodo.14161289](https://doi.org/10.5281/zenodo.14161289)


---

## Round Table Workshop 2 - Correction of Drift and Movement

Dr. Hellen Ishikawa-Ankerhold, Max Nobis

Published 2024-11-14

Licensed CC-BY-4.0



Session 2 of a round table workshop. Features description of image processing methods useful in intravital imaging to compensate for the motion of living tissue.

Tags: Exclude From Dalia

[https://zenodo.org/records/14161633](https://zenodo.org/records/14161633)

[https://doi.org/10.5281/zenodo.14161633](https://doi.org/10.5281/zenodo.14161633)


---

## Running Deep-Learning Scripts in the BiA-PoL Omero Server

Marcelo Zoccoler

Licensed CC-BY-4.0



Tags: Python, Artificial Intelligence, Bioimage Analysis, Include In Dalia

Content type: Blog Post

[https://biapol.github.io/blog/marcelo_zoccoler/omero_scripts/readme.html](https://biapol.github.io/blog/marcelo_zoccoler/omero_scripts/readme.html)


---

## STEDYCON OBF dataset with simulated intensity and complex stacks for bioformats MR #4362

Nils Gladitz

Published 2025-09-02

Licensed CC-BY-4.0



Tags: Exclude From Dalia

[https://zenodo.org/records/17039369](https://zenodo.org/records/17039369)

[https://doi.org/10.5281/zenodo.17039369](https://doi.org/10.5281/zenodo.17039369)


---

## SWC/GCNU Software Skills

Licensed CC-BY-4.0



Computational skills training at the UCL Sainsbury Wellcome Centre and Gatsby Computational Neuroscience Unit, delivered by members of the Neuroinformatics Unit.

Tags: Include In Dalia

Content type: Collection, Online Course, Video, Tutorial

[https://software-skills.neuroinformatics.dev/index.html](https://software-skills.neuroinformatics.dev/index.html)


---

## Sample data for PR#4284 (https://github.com/ome/bioformats/pull/4284)

Jürgen Bohl

Published 2025-03-04

Licensed CC-BY-4.0



With this file the problem addressed in PR#4284 can be reproduced: when runningbfconvert -series 4 -channel 0 2025_01_27__0007_offline_Zen_3_9_5.czi output.png
the result is garbled.

Tags: Exclude From Dalia

[https://zenodo.org/records/14968770](https://zenodo.org/records/14968770)

[https://doi.org/10.5281/zenodo.14968770](https://doi.org/10.5281/zenodo.14968770)


---

## Segmentation of Nuclei in Histopathology Images by deep regression of the distance map

Naylor Peter Jack, Walter Thomas, Laé Marick, Reyal Fabien

Published 2018-02-16

Licensed CC-BY-4.0



This dataset has been annonced in our accepted paper &quot;Segmentation of Nuclei in Histopathology Images by deep regression of the distance map&quot; in Transcation on Medical Imaging on the 13th of August.
This dataset consists of 50 annotated images, divided into 11 patients.

&nbsp;

v1.1 (27/02/19): Small corrections to a few pixel that were labelled nuclei but weren&#39;t.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/2579118](https://zenodo.org/records/2579118)

[https://doi.org/10.5281/zenodo.2579118](https://doi.org/10.5281/zenodo.2579118)


---

## Segmenting cells in a spheroid in 3D using 2D StarDist within TrackMate

Jean-Yves Tinevez, Joanna W. Pylvänäinen, Guillaume Jacquemet

Published 2021-08-19

Licensed CC-BY-4.0



3D image of cells in a spheroid, imaged on a confocal microscope, used in a tutorial to demonstrate how to hack TrackMate to segment cells in 3D using the 2D segmentation algorithms it ships.

Image by Guillaume Jacquemet.

For more details see&nbsp;https://imagej.net/plugins/trackmate/trackmate-stardist#generation-of-3d-labels-by-tracking-2d-labels-using-trackmate

&nbsp;

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/5220610](https://zenodo.org/records/5220610)

[https://doi.org/10.5281/zenodo.5220610](https://doi.org/10.5281/zenodo.5220610)


---

## Setting up an institutional OMERO environment for bioimage data: Perspectives from both facility staff and users

Anett Jannasch, Silke Tulok, Chukwuebuka William Okafornta, Thomas Kugel, Michele Bortolomeazzi, Tom Boissonnet, Christian Schmidt, Andy Vogelsang

Published 2024-09-14

Licensed CC-BY-4.0



Modern bioimaging core facilities at research institutions are essential for managing and maintaining high-end instruments, providing training and support for researchers in experimental design, image acquisition and data analysis. 

Tags: Nfdi4Bioimage, OMERO, Bioimage Analysis, Exclude From Dalia

Content type: Publication

[https://onlinelibrary.wiley.com/doi/10.1111/jmi.13360](https://onlinelibrary.wiley.com/doi/10.1111/jmi.13360)


---

## Sharing and licensing material

Robert Haase

Licensed CC-BY-4.0



Introduction to sharing resources online and licensing

Tags: Sharing, Research Data Management, Include In Dalia

Content type: Slides

[https://f1000research.com/slides/10-519](https://f1000research.com/slides/10-519)


---

## Sharing research data with Zenodo

Robert Haase

Licensed CC-BY-4.0



Blog post about how to share data using zenodo.org

Tags: Sharing, Research Data Management, Include In Dalia

Content type: Blog Post

[https://focalplane.biologists.com/2023/02/15/sharing-research-data-with-zenodo/](https://focalplane.biologists.com/2023/02/15/sharing-research-data-with-zenodo/)


---

## Single-cell approach dissecting agr quorum sensing dynamics in Staphylococcus aureus

Julian Bär

Published 2024-02-28

Licensed CC-BY-4.0



Training data for the two StarDist2D models and the DeLTA 2.0 2D tracking model used in the publication on&nbsp;bioarxiv. The trained stardist models are included in the respective zip files of the training data. mm: mother-machine; cc: connected chamber. Each of them contains two folders, img and seg_label. They contain matching pairs of phasecontrast images (img) and label images (seg_label).&nbsp;
&nbsp;
tracking_set_subset.zip contains the training data for the DeLTA tracking model following the default folder structure. We used custom weight functions to create the training weight maps in the folder wei. The folder wei_bck contains weights generated with the original function.
The unet_pads_tracking.hdf5 is the retrained tracking model used in the associated publication.
See associated GitHub repository for example code on how to use the models for segmentation and tracking.
The four numbered zip files contain the data used to create all figures displaying image analysis output.
Abstract:
Staphylococcus aureus both colonizes humans and causes severe virulent infections. Virulence is regulated by the agr quorum sensing system and its autoinducing peptide (AIP), with dynamics at the single-cell level across four agr-types &ndash; each defined by distinct AIP sequences and capable of cross-inhibition &ndash; remaining elusive. Employing microfluidics, time-lapse microscopy, and deep-learning image analysis, we uncovered significant differences in AIP sensitivity among agr-types. We observed bimodal agr activation, attributed to intergenerational phenotypic stability and influenced by AIP concentration. Upon AIP stimulation, agr‑III showed AIP insensitivity, while agr‑II exhibited increased sensitivity and prolonged generation time. Beyond expected cross-inhibition of agr‑I by heterologous AIP‑II and ‑III, the presumably cross-activating AIP‑IV also inhibited agr‑I. Community interactions across different agr-type pairings revealed four main patterns: stable or switched dominance, and delayed or stable dual activation, influenced by community characteristics. These insights underscore the potential of personalized treatment strategies considering virulence and genetic diversity.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/10720439](https://zenodo.org/records/10720439)

[https://doi.org/10.5281/zenodo.10720439](https://doi.org/10.5281/zenodo.10720439)


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

Tags: Include In Dalia

[https://zenodo.org/records/10839310](https://zenodo.org/records/10839310)

[https://doi.org/10.5281/zenodo.10839310](https://doi.org/10.5281/zenodo.10839310)


---

## So geschlossen wie nötig, so offen wie möglich - Datenschutz beim Umgang mit Forschungsdaten

Pia Voigt

Published 2024-05-30

Licensed CC-BY-4.0



Der Umgang mit personenbezogenen Daten stellt Forschende oft vor rechtliche Herausforderungen: Unter welchen Bedingungen d&uuml;rfen personenbezogene Daten verarbeitet werden? Welche Voraussetzungen m&uuml;ssen erf&uuml;llt sein und welche Strategien k&ouml;nnen angewendet werden, um Daten sicher speichern, verarbeiten, teilen und aufbewahren zu k&ouml;nnen? Mit Hilfe dieses Foliensatzes erhalten Sie Einblicke in datenschutzrechtliche Aspekte beim Umgang mit Ihren Forschungsdaten.&nbsp;

Tags: Research Data Management, Data Protection, FAIR-Principles, Include In Dalia

Content type: Slides

[https://zenodo.org/records/11396199](https://zenodo.org/records/11396199)

[https://doi.org/10.5281/zenodo.11396199](https://doi.org/10.5281/zenodo.11396199)


---

## SpatialData: an open and universal data framework for spatial omics

Luca Marconato, Giovanni Palla, Kevin A Yamauchi, Isaac Virshup, Elyas Heidari, Tim Treis, Marcella Toth, Rahul Shrestha, Harald Vöhringer, Wolfgang Huber, Moritz Gerstung, Josh Moore, Fabian J Theis, Oliver Stegle

Licensed CC-BY-4.0



Tags: Python, Exclude From Dalia

Content type: Publication, Preprint

[https://www.biorxiv.org/content/10.1101/2023.05.05.539647v1.abstract](https://www.biorxiv.org/content/10.1101/2023.05.05.539647v1.abstract)


---

## Stackview sliceplot example data

Robert Haase

Published 2024-11-03

Licensed CC-BY-4.0



This is a dataset of PNG images of [Bio-Image Data Science teaching slides](https://zenodo.org/records/12623730). The png_umap.yml file contains a list of all images and a dimensionality reduced embedding (Uniform Manifold Approximation Projection, UMAP) made using OpenAI's text-embedding-ada-002 model.
A notebook for visualizing this data is published here: https://github.com/haesleinhuepf/stackview/blob/main/docs/sliceplot.ipynb

Tags: Exclude From Dalia

[https://zenodo.org/records/14030307](https://zenodo.org/records/14030307)

[https://doi.org/10.5281/zenodo.14030307](https://doi.org/10.5281/zenodo.14030307)


---

## StarDist Adipocyte Segmentation Training data, Training Notebook and Model

Sarkis Rita, Naveiras Olaia, Burri Olivier, Weigert Martin, De Leval Laurence

Published 2022-08-17

Licensed CC-BY-4.0



Data from H&amp;E human bone marrow whole slide scanner images used in the paper: &quot;MarrowQuant 2.0: a digital pathology workflow assisting bone marrow evaluation in clinical and experimental hematology&quot; (https://doi.org/10.21203/rs.3.rs-1860140/v1)

&nbsp;

292 image patches

Ground truth were manually annotated using QuPath and split into 263 images for training and 29 for validation.

Training in StarDist was done on a Windows 10 PC with an RTX 2080 GPU. The requirements file for installing a Python 3.7 environment to run the attached notebooks is provided (stardist-val.txt).

The StarDist model configuration can be found in the Jupyter Notebook :

Adipocyte Training.ipynb

Model validation and metrics can be performed by running the notebook after finishing the Adipocyte Training notebook.

Quality Control.ipynb

&nbsp;

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/7003909](https://zenodo.org/records/7003909)

[https://doi.org/10.5281/zenodo.7003909](https://doi.org/10.5281/zenodo.7003909)


---

## StarDist model and data for the segmentation of Yersinia enterocolitica cells in widefield images

Christoph Spahn, Andreas Diepold, Francesca Ermoli

Published 2024-05-02

Licensed CC-BY-4.0



Dataset and StarDist model for the segmentation of Yersinia enterocolitica cells
This dataset and StarDist model are part of the publication "Active downregulation of the type III secretion system at higher local cell densities promotes Yersinia replication and dissemination".
It contains the dataset that was used for training the provided StarDist model using ZeroCostDL4Mic.
Data:
Yersinia enterocolitica cells were spotted on an agarose pad (1.5% low melting agarose (Sigma-Aldrich) in minimal medium, 1% Casamino acids, 5 mM EGTA, &nbsp;glass depression slides (Marienfeld)). For imaging, a Deltavision Elite Optical Sectioning Microscope equipped with a UPlanSApo 100&times;/1.40 oil objective (Olympus) and an EDGE sCMOS_5.5 camera (Photometrics) was used. Z-stacks with 9 slices (∆z = 0.15 &micro;m) per fluorescence channel were acquired and &nbsp;5 slices were selected for network training. Images were annotated in Fiji using the Freehand selection tool, and brightlight and mask images were quartered to obtain the final dataset of 300 paired images. 260 images were used for training, while 40 images were used to test model performance.
Model:
The StarDist 2D model was trained from scratch for 100 epochs on 300 paired image patches (image dimensions: (480 x 480 px&sup2;), patch size: (480 x 480 px&sup2;)) with a batch size of 4 and a mae loss function, using the StarDist 2D ZeroCostDL4Mic notebook (v 1) (von Chamier &amp; Laine et al., 2020). Grid parameter was set to 2 and the number of rays to 120. The model was trained with an initial learning rate of 0.0003 using a 80/20 train/test split. The dataset was augmented 4-fold by flipping and rotation.
Key python packages used include tensorflow (v 0.1.12), Keras (v2.3.1), csbdeep (v 0.7.2), numpy (v 1.21.6), cuda (v 11.1.105Build cuda_11.1.TC455_06.29190527_0). The training was accelerated using a Tesla T4 GPU.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/11105050](https://zenodo.org/records/11105050)

[https://doi.org/10.5281/zenodo.11105050](https://doi.org/10.5281/zenodo.11105050)


---

## StarDist_AsPC1_Lifeact

Gautier Follain, Sujan Ghimire, Joanna Pylvänäinen, Johanna Ivaska, Guillaume Jacquemet

Published 2024-08-29

Licensed CC-BY-4.0



This repository includes a StarDist deep learning model designed for segmenting AsPC1 cells labeled with Lifeact from fluorescence microscopy images. The model distinguishes individual AsPC1 cells within clusters and separates them from the background. The model was trained on a small dataset and achieved an Intersection over Union (IoU) score of 0.884 and an F1 Score of 0.967, indicating high accuracy in cell segmentation.
Specifications


Model: StarDist for segmenting AsPC1 cells in fluorescence microscopy images


Training Dataset:



Number of Images: 10 paired fluorescence microscopy images and label masks


Microscope: Spinning disk confocal microscope (3i CSU-W1) with a 20x objective, NA 0.8


Data Type: Fluorescence microscopy images of the AsPC1 Lifeact channel with manually segmented masks


File Format: TIFF (.tif)



Fluorescence Images: 16-bit


Masks: 8-bit



Image Size: 1024 x 1024 pixels (Pixel size: 0.6337 x 0.6337 &micro;m&sup2;)



Model Capabilities:



Segment AsPC1 Cells: Detects individual AsPC1 cells from a cluster and separates them from the background


Measure Intensity: Enables measurement of CD44, ICAM1, ICAM2, or Fibronectin intensity under individual cells in respective channels



Performance:



Average IoU: 0.884


Average F1 Score: 0.967



Model Training: Conducted using ZeroCostDL4Mic (https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki)



Reference
Fast label-free live imaging reveals key roles of flow dynamics and CD44-HA interaction in cancer cell arrest on endothelial monolayers

Gautier&nbsp;Follain,&nbsp;Sujan&nbsp;Ghimire,&nbsp;Joanna W.&nbsp;Pylv&auml;n&auml;inen,&nbsp;Monika&nbsp;Vaitkevičiūtė,&nbsp;Diana&nbsp;Wurzinger,&nbsp;Camilo&nbsp;Guzm&aacute;n,&nbsp;James RW&nbsp;Conway,&nbsp;Michal&nbsp;Dibus,&nbsp;Sanna&nbsp;Oikari,&nbsp;Kirsi&nbsp;Rilla,&nbsp;Marko&nbsp;Salmi,&nbsp;Johanna&nbsp;Ivaska,&nbsp;Guillaume&nbsp;Jacquemet
bioRxiv&nbsp;2024.09.30.615654;&nbsp;doi:&nbsp;https://doi.org/10.1101/2024.09.30.615654
&nbsp;

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/13442128](https://zenodo.org/records/13442128)

[https://doi.org/10.5281/zenodo.13442128](https://doi.org/10.5281/zenodo.13442128)


---

## StarDist_BF_Monocytes_dataset

Gautier Follain, Sujan Ghimire, Joanna Pylvänäinen, Johanna Ivaska, Guillaume Jacquemet

Published 2024-01-26

Licensed CC-BY-4.0



This repository includes a StarDist deep learning model and its training and validation datasets for detecting mononucleated cells perfused over an endothelial cell monolayer. The model was trained on 27 manually annotated images and achieved an average F1 Score of 0.941. The dataset and model are helpful for biomedical research, especially in studying interactions between mononucleated and endothelial cells.
Specifications


Model: StarDist for mononucleated cell detection on endothelial cells


Training Dataset:



Number of Images: 27 paired brightfield microscopy images and label masks


Microscope: Nikon Eclipse Ti2-E, 20x objective


Data Type: Brightfield microscopy images with manually segmented masks


File Format: TIFF (.tif)



Brightfield Images: 16-bit


Masks: 8-bit



Image Size: 1024 x 1022 pixels (Pixel size: 650 nm)



Training Parameters:



Epochs: 400


Patch Size: 992 x 992 pixels


Batch Size: 2



Performance:



Average F1 Score: 0.941


Average IoU: 0.831



Model Training: Conducted using ZeroCostDL4Mic (https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki)


Reference
Fast label-free live imaging reveals key roles of flow dynamics and CD44-HA interaction in cancer cell arrest on endothelial monolayers
Gautier&nbsp;Follain,&nbsp;Sujan&nbsp;Ghimire,&nbsp;Joanna W.&nbsp;Pylv&auml;n&auml;inen,&nbsp;Monika&nbsp;Vaitkevičiūtė,&nbsp;Diana&nbsp;Wurzinger,&nbsp;Camilo&nbsp;Guzm&aacute;n,&nbsp;James RW&nbsp;Conway,&nbsp;Michal&nbsp;Dibus,&nbsp;Sanna&nbsp;Oikari,&nbsp;Kirsi&nbsp;Rilla,&nbsp;Marko&nbsp;Salmi,&nbsp;Johanna&nbsp;Ivaska,&nbsp;Guillaume&nbsp;Jacquemet
bioRxiv&nbsp;2024.09.30.615654;&nbsp;doi: https://doi.org/10.1101/2024.09.30.615654

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/10572200](https://zenodo.org/records/10572200)

[https://doi.org/10.5281/zenodo.10572200](https://doi.org/10.5281/zenodo.10572200)


---

## StarDist_BF_Neutrophil_dataset

Gautier Follain, Sujan Ghimire, Joanna Pylvänäinen, Johanna Ivaska, Guillaume Jacquemet

Published 2024-01-26

Licensed CC-BY-4.0



This repository includes a StarDist deep learning model and its training and validation datasets for detecting neutrophils perfused over an endothelial cell monolayer. The model was trained on 36 manually annotated images, achieving an average F1 Score of 0.969. The dataset and model are intended for use in biomedical research, particularly for analyzing interactions between neutrophils and endothelial cells.
Specifications


Model: StarDist for neutrophil detection on endothelial cells


Training Dataset:



Number of Images: 36 paired brightfield microscopy images and label masks


Microscope: Nikon Eclipse Ti2-E, 20x objective


Data Type: Brightfield microscopy images with manually segmented masks


File Format: TIFF (.tif)



Brightfield Images: 16-bit


Masks: 8-bit



Image Size: 1024 x 1022 pixels (Pixel size: 650 nm)



Training Parameters:



Epochs: 400


Patch Size: 992 x 992 pixels


Batch Size: 2



Performance:



Average F1 Score: 0.969


Average IoU: 0.914



Model Training: Conducted using ZeroCostDL4Mic (https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki)



Reference
Fast label-free live imaging reveals key roles of flow dynamics and CD44-HA interaction in cancer cell arrest on endothelial monolayers

Gautier&nbsp;Follain,&nbsp;Sujan&nbsp;Ghimire,&nbsp;Joanna W.&nbsp;Pylv&auml;n&auml;inen,&nbsp;Monika&nbsp;Vaitkevičiūtė,&nbsp;Diana&nbsp;Wurzinger,&nbsp;Camilo&nbsp;Guzm&aacute;n,&nbsp;James RW&nbsp;Conway,&nbsp;Michal&nbsp;Dibus,&nbsp;Sanna&nbsp;Oikari,&nbsp;Kirsi&nbsp;Rilla,&nbsp;Marko&nbsp;Salmi,&nbsp;Johanna&nbsp;Ivaska,&nbsp;Guillaume&nbsp;Jacquemet
bioRxiv&nbsp;2024.09.30.615654;&nbsp;doi:&nbsp;https://doi.org/10.1101/2024.09.30.615654

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/10572231](https://zenodo.org/records/10572231)

[https://doi.org/10.5281/zenodo.10572231](https://doi.org/10.5281/zenodo.10572231)


---

## StarDist_BF_cancer_cell_dataset_10x

Gautier Follain, Sujan Ghimire, Joanna Pylvänäinen, Johanna Ivaska, Guillaume Jacquemet

Published 2024-08-12

Licensed CC-BY-4.0



This repository includes a StarDist deep learning model and its training dataset designed for segmenting cancer cells perfused over an endothelial cell monolayer captured at 10x magnification. The model was trained on 77 manually annotated images, with the dataset being computationally augmented during training by a factor of 8. The model was trained for 500 epochs and achieved an average F1 Score of 0.968, indicating high accuracy in segmenting cancer cells on endothelial cells.
Specifications


Model: StarDist for cancer cell segmentation on endothelial cells (10x magnification)


Training Dataset:



Number of Images: 77 paired brightfield microscopy images and label masks


Augmented Dataset: Computational augmentation by a factor of 8 during training


Microscope: Nikon Eclipse Ti2-E, 10x objective


Data Type: Brightfield microscopy images with manually segmented masks


File Format: TIFF (.tif)



Brightfield Images: 16-bit


Masks: 8-bit or 16-bit



Image Size: 1024 x 1022 pixels (pixel size: 1.3148 &mu;m)



Training Parameters:



Epochs: 500


Patch Size: 992 x 992 pixels


Batch Size: 2



Performance:



Average F1 Score: 0.968


Average IoU: 0.882



Model Training: Conducted using ZeroCostDL4Mic (https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki)



Reference
Fast label-free live imaging reveals key roles of flow dynamics and CD44-HA interaction in cancer cell arrest on endothelial monolayers

Gautier&nbsp;Follain,&nbsp;Sujan&nbsp;Ghimire,&nbsp;Joanna W.&nbsp;Pylv&auml;n&auml;inen,&nbsp;Monika&nbsp;Vaitkevičiūtė,&nbsp;Diana&nbsp;Wurzinger,&nbsp;Camilo&nbsp;Guzm&aacute;n,&nbsp;James RW&nbsp;Conway,&nbsp;Michal&nbsp;Dibus,&nbsp;Sanna&nbsp;Oikari,&nbsp;Kirsi&nbsp;Rilla,&nbsp;Marko&nbsp;Salmi,&nbsp;Johanna&nbsp;Ivaska,&nbsp;Guillaume&nbsp;Jacquemet
bioRxiv&nbsp;2024.09.30.615654;&nbsp;doi:&nbsp;https://doi.org/10.1101/2024.09.30.615654

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/13304399](https://zenodo.org/records/13304399)

[https://doi.org/10.5281/zenodo.13304399](https://doi.org/10.5281/zenodo.13304399)


---

## StarDist_BF_cancer_cell_dataset_20x

Gautier Follain, Sujan Ghimire, Joanna Pylvänäinen, Johanna Ivaska, Guillaume Jacquemet

Published 2024-01-26

Licensed CC-BY-4.0



This repository contains a StarDist deep learning model and its training and validation datasets designed for segmenting cancer cells perfused over an endothelial cell monolayer captured at 20x magnification. Using computational methods, the initial dataset of 20 manually annotated images was augmented to 160 paired images. The model was trained over 400 epochs and achieved an average F1 Score of 0.921, demonstrating high accuracy in cell segmentation tasks.
Specifications


Model: StarDist for cancer cell segmentation on endothelial cells (20x magnification)


Training Dataset:



Number of Original Images: 20 paired brightfield microscopy images and label masks


Microscope: Nikon Eclipse Ti2-E, 20x objective


Data Type: Brightfield microscopy images with manually segmented masks


File Format: TIFF (.tif)



Brightfield Images: 16-bit


Masks: 8-bit



Image Size: 1024 x 1022 pixels (Pixel size: 650 nm)



Training Parameters:



Epochs: 400


Patch Size: 992 x 992 pixels


Batch Size: 2



Performance:



Average F1 Score: 0.921


Average IoU: 0.793



Model Training: Conducted using ZeroCostDL4Mic (https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki)


&nbsp;

Reference
Fast label-free live imaging reveals key roles of flow dynamics and CD44-HA interaction in cancer cell arrest on endothelial monolayers

Gautier&nbsp;Follain,&nbsp;Sujan&nbsp;Ghimire,&nbsp;Joanna W.&nbsp;Pylv&auml;n&auml;inen,&nbsp;Monika&nbsp;Vaitkevičiūtė,&nbsp;Diana&nbsp;Wurzinger,&nbsp;Camilo&nbsp;Guzm&aacute;n,&nbsp;James RW&nbsp;Conway,&nbsp;Michal&nbsp;Dibus,&nbsp;Sanna&nbsp;Oikari,&nbsp;Kirsi&nbsp;Rilla,&nbsp;Marko&nbsp;Salmi,&nbsp;Johanna&nbsp;Ivaska,&nbsp;Guillaume&nbsp;Jacquemet
bioRxiv&nbsp;2024.09.30.615654;&nbsp;doi:&nbsp;https://doi.org/10.1101/2024.09.30.615654

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/10572122](https://zenodo.org/records/10572122)

[https://doi.org/10.5281/zenodo.10572122](https://doi.org/10.5281/zenodo.10572122)


---

## StarDist_Fluorescent_cells

Gautier Follain, Sujan Ghimire, Joanna Pylvänäinen, Johanna Ivaska, Guillaume Jacquemet

Published 2024-01-26

Licensed CC-BY-4.0



This repository includes a StarDist deep learning model and its training and validation datasets for detecting fluorescently labeled cancer cells perfused over an endothelial cell monolayer. The model was trained on 66 images labeled with CellTrace and demonstrated high accuracy, achieving an average F1 Score of 0.877. The dataset and the trained model can be used for biomedical image analysis, particularly in cancer research.
Specifications


Model: StarDist for cancer cell detection


Training Dataset:



Number of Images: 66 paired fluorescent microscopy images and label masks


Microscope: Nikon Eclipse Ti2-E, 10x objective


Data Type: Fluorescent microscopy images with manually segmented masks


File Format: TIFF (.tif)



Brightfield Images: 16-bit


Masks: 8-bit



Image Size: 1024 x 1024 pixels (Pixel size: 1.3205 &mu;m)



Training Parameters:



Epochs: 200


Patch Size: 1024 x 1024 pixels


Batch Size: 2



Performance:



Average F1 Score: 0.877


Average IoU: 0.646



Model Training: Conducted using ZeroCostDL4Mic (https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki)



Reference
Fast label-free live imaging reveals key roles of flow dynamics and CD44-HA interaction in cancer cell arrest on endothelial monolayers

Gautier&nbsp;Follain,&nbsp;Sujan&nbsp;Ghimire,&nbsp;Joanna W.&nbsp;Pylv&auml;n&auml;inen,&nbsp;Monika&nbsp;Vaitkevičiūtė,&nbsp;Diana&nbsp;Wurzinger,&nbsp;Camilo&nbsp;Guzm&aacute;n,&nbsp;James RW&nbsp;Conway,&nbsp;Michal&nbsp;Dibus,&nbsp;Sanna&nbsp;Oikari,&nbsp;Kirsi&nbsp;Rilla,&nbsp;Marko&nbsp;Salmi,&nbsp;Johanna&nbsp;Ivaska,&nbsp;Guillaume&nbsp;Jacquemet
bioRxiv&nbsp;2024.09.30.615654;&nbsp;doi:&nbsp;https://doi.org/10.1101/2024.09.30.615654

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/10572310](https://zenodo.org/records/10572310)

[https://doi.org/10.5281/zenodo.10572310](https://doi.org/10.5281/zenodo.10572310)


---

## StarDist_HUVEC_nuclei_dataset

Gautier Follain, Sujan Ghimire, Joanna Pylvänäinen, Johanna Ivaska, Guillaume Jacquemet

Published 2024-02-05

Licensed CC-BY-4.0



This repository contains a StarDist deep learning model and its training and validation datasets for segmenting endothelial nuclei while ignoring cancer cells. The cancer cells were perfused over an endothelial cell monolayer. The initial dataset consisted of 17 images, where cancer cell nuclei were manually removed after segmentation with the StarDist Versatile Nuclei model. This dataset was augmented to 68 paired images using computational techniques like rotation and flipping. The model was trained for 200 epochs, achieving an average F1 Score of 0.976, demonstrating high accuracy in segmenting endothelial nuclei while excluding cancer cells.
Specifications


Model: StarDist for segmenting endothelial nuclei while ignoring cancer cells


Training Dataset:



Number of Original Images: 17 paired predictions of nuclei and label images


Augmented Dataset: Expanded to 68 paired images using rotation and flipping


Source Image Generation: Generated using a pix2pix model trained to predict nuclei from brightfield images of cancer cells on top of an endothelium (DOI: 10.5281/zenodo.10617532)


Target Image Generation: Masks obtained via manual segmentation


File Format: TIFF (.tif)



Brightfield Images: 8-bit


Masks: 8-bit



Image Size: 1024 x 1022 pixels (uncalibrated)



Training Parameters:



Epochs: 200


Patch Size: 1024 x 1024 pixels


Batch Size: 2



Performance:



Average F1 Score: 0.976


Average IoU: 0.927



Model Training: Conducted using ZeroCostDL4Mic (https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki)



Reference
Fast label-free live imaging reveals key roles of flow dynamics and CD44-HA interaction in cancer cell arrest on endothelial monolayers

Gautier&nbsp;Follain,&nbsp;Sujan&nbsp;Ghimire,&nbsp;Joanna W.&nbsp;Pylv&auml;n&auml;inen,&nbsp;Monika&nbsp;Vaitkevičiūtė,&nbsp;Diana&nbsp;Wurzinger,&nbsp;Camilo&nbsp;Guzm&aacute;n,&nbsp;James RW&nbsp;Conway,&nbsp;Michal&nbsp;Dibus,&nbsp;Sanna&nbsp;Oikari,&nbsp;Kirsi&nbsp;Rilla,&nbsp;Marko&nbsp;Salmi,&nbsp;Johanna&nbsp;Ivaska,&nbsp;Guillaume&nbsp;Jacquemet
bioRxiv&nbsp;2024.09.30.615654;&nbsp;doi: https://doi.org/10.1101/2024.09.30.615654

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/10617532](https://zenodo.org/records/10617532)

[https://doi.org/10.5281/zenodo.10617532](https://doi.org/10.5281/zenodo.10617532)


---

## StarDist_TumorCell_nuclei

Gautier Follain, Sujan Ghimire, Joanna Pylvänäinen, Johanna Ivaska, Guillaume Jacquemet

Published 2024-08-29

Licensed CC-BY-4.0



This repository contains a StarDist deep learning model designed for segmenting tumor cell nuclei from the DAPI channel in fluorescence microscopy images while excluding HUVEC nuclei. The model was trained to accurately detect individual tumor cell nuclei for subsequent measurement of CD44, ICAM1, ICAM2, or Fibronectin intensity around or under the nuclei. The model achieved an Intersection over Union (IoU) score of 0.558 and an F1 Score of 0.793, reflecting its capability to distinguish tumor cell nuclei from HUVEC nuclei.
Specifications


Model: StarDist for segmenting tumor cell nuclei from the DAPI fluorescence channel


Training Dataset:



Number of Images: 48 paired fluorescence microscopy images and label masks


Microscope: Spinning disk confocal microscope (3i CSU-W1) with a 20x objective, NA 0.8


Data Type: Fluorescence microscopy images of the DAPI channel with manually segmented masks


File Format: TIFF (.tif)



Fluorescence Images: 16-bit


Masks: 8-bit



Image Size: 920 x 920 pixels (Pixel size: 0.6337 x 0.6337 &micro;m&sup2;)



Model Capabilities:



Segment Tumor Cell Nuclei: Detects individual tumor cell nuclei in the DAPI channel while distinguishing them from HUVEC nuclei


Measure Intensity: Enables measurement of CD44, ICAM1, ICAM2, or Fibronectin intensity around or under tumor cell nuclei in respective channels



Performance:



Average IoU: 0.558


Average F1 Score: 0.793



Model Training: Conducted using ZeroCostDL4Mic (https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki)



Reference
Fast label-free live imaging reveals key roles of flow dynamics and CD44-HA interaction in cancer cell arrest on endothelial monolayers

Gautier&nbsp;Follain,&nbsp;Sujan&nbsp;Ghimire,&nbsp;Joanna W.&nbsp;Pylv&auml;n&auml;inen,&nbsp;Monika&nbsp;Vaitkevičiūtė,&nbsp;Diana&nbsp;Wurzinger,&nbsp;Camilo&nbsp;Guzm&aacute;n,&nbsp;James RW&nbsp;Conway,&nbsp;Michal&nbsp;Dibus,&nbsp;Sanna&nbsp;Oikari,&nbsp;Kirsi&nbsp;Rilla,&nbsp;Marko&nbsp;Salmi,&nbsp;Johanna&nbsp;Ivaska,&nbsp;Guillaume&nbsp;Jacquemet
bioRxiv&nbsp;2024.09.30.615654;&nbsp;doi:&nbsp;https://doi.org/10.1101/2024.09.30.615654
&nbsp;

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/13443221](https://zenodo.org/records/13443221)

[https://doi.org/10.5281/zenodo.13443221](https://doi.org/10.5281/zenodo.13443221)


---

## Stardist model and training dataset for automated tracking of MDA-MB-231 and BT20 cells

Hussein Al-Akhrass, Johanna Ivaska, Guillaume Jacquemet

Published 2021-05-26

Licensed CC-BY-4.0



StarDist Model:
The StarDist model was generated using the ZeroCostDL4Mic platform (Chamier et al., 2021). This custom StarDist model was trained for 300 epochs using 46 manually annotated paired images (image dimensions: (1024, 1024)) with a batch size of 2, an augmentation factor of 4 and a mae loss function. The StarDist &ldquo;Versatile fluorescent nuclei&rdquo; model was used as a training starting point. Key python packages used include TensorFlow (v 0.1.12), Keras (v 2.3.1), CSBdeep (v 0.6.1), NumPy (v 1.19.5), Cuda (v 11.0.221). The training was accelerated using a Tesla P100GPU.
The model weights can be used in the ZeroCostDL4Mic StarDist 2D notebook or in the StarDist Fiji plugin.

StarDist Training dataset:
Paired microscopy images (fluorescence) and corresponding masks

Microscopy data type: Fluorescence microscopy (SiR-DNA) and masks obtained via manual segmentation (see https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist for details about the segmentation)

Cells were imaged using a 20x Nikon CFI Plan Apo Lambda objective (NA 0.75) one frame every 10 minutes for 16h.

Cell type: MDA-MB-231 cells and BT20 cells

File format: .tif (16-bit for fluorescence and 8 and 16-bit for the masks)

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/4811213](https://zenodo.org/records/4811213)

[https://doi.org/10.5281/zenodo.4811213](https://doi.org/10.5281/zenodo.4811213)


---

## Stardist_MiaPaCa2_from_CD44

Gautier Follain, Sujan Ghimire, Joanna Pylvänäinen, Johanna Ivaska, Guillaume Jacquemet

Published 2024-08-29

Licensed CC-BY-4.0



This repository contains a StarDist deep learning model designed for segmenting MiaPaCa2 cells from the CD44 channel in fluorescence microscopy images. The model is capable of accurately segmenting individual MiaPaCa2 cells while excluding HUVECs. Trained on a small dataset, the model achieved an Intersection over Union (IoU) score of 0.884 and an F1 Score of 0.950, indicating high precision in cell segmentation.
Specifications


Model: StarDist for segmenting MiaPaCa2 cells from the CD44 fluorescence channel


Training Dataset:



Number of Images: 8 paired fluorescence microscopy images and label masks


Microscope: Spinning disk confocal microscope (3i CSU-W1) with a 20x objective, NA 0.8


Data Type: Fluorescence microscopy images of the CD44 channel, obtained after immunofluorescence staining with primary and secondary antibodies and manually segmented masks


File Format: TIFF (.tif)



Fluorescence Images: 16-bit


Masks: 8-bit



Image Size: 920 x 920 pixels (Pixel size: 0.6337 x 0.6337 &micro;m&sup2;)



Model Capabilities:



Segment MiaPaCa2 Cells: Accurately detects individual MiaPaCa2 cells while ignoring HUVECs


Measure CD44 Intensity: Allows for the measurement of CD44 intensity around MiaPaCa2 cells, specifically from the CD44 channel



Performance:



Average IoU: 0.884


Average F1 Score: 0.950



Model Training: Conducted using ZeroCostDL4Mic (https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki)



Reference
Fast label-free live imaging reveals key roles of flow dynamics and CD44-HA interaction in cancer cell arrest on endothelial monolayers

Gautier&nbsp;Follain,&nbsp;Sujan&nbsp;Ghimire,&nbsp;Joanna W.&nbsp;Pylv&auml;n&auml;inen,&nbsp;Monika&nbsp;Vaitkevičiūtė,&nbsp;Diana&nbsp;Wurzinger,&nbsp;Camilo&nbsp;Guzm&aacute;n,&nbsp;James RW&nbsp;Conway,&nbsp;Michal&nbsp;Dibus,&nbsp;Sanna&nbsp;Oikari,&nbsp;Kirsi&nbsp;Rilla,&nbsp;Marko&nbsp;Salmi,&nbsp;Johanna&nbsp;Ivaska,&nbsp;Guillaume&nbsp;Jacquemet
bioRxiv&nbsp;2024.09.30.615654;&nbsp;doi:&nbsp;https://doi.org/10.1101/2024.09.30.615654

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/13442877](https://zenodo.org/records/13442877)

[https://doi.org/10.5281/zenodo.13442877](https://doi.org/10.5281/zenodo.13442877)


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


Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

[https://zenodo.org/records/7018750](https://zenodo.org/records/7018750)

[https://doi.org/10.5281/zenodo.7018750](https://doi.org/10.5281/zenodo.7018750)


---

## Sustainable Data Stewardship

Stefano Della Chiesa

Published 2024-03-25

Licensed CC-BY-4.0



 These slides were presented at the 2. SaxFDM-Beratungsstammtisch and delve into the strategic integration of Research Data Management (RDM) within research organizations. The Leibniz IOER presented an insightful overview of RDM activities and approaches, emphasizing the criticality of embedding RDM strategically within research institutions. The presentation showcases some best practices in RDM implementation through practical examples, offering valuable insights for optimizing data stewardship processes.

Tags: Research Data Management, Data Stewardship, Include In Dalia

Content type: Slides

[https://zenodo.org/records/10942559](https://zenodo.org/records/10942559)

[https://doi.org/10.5281/zenodo.10942559](https://doi.org/10.5281/zenodo.10942559)


---

## SynapseNet Training Data

Constantin Pape

Published 2024-12-01

Licensed CC-BY-4.0



This dataset contains room-temperature single-axis TEM tomograms from Schaffer collateral and mossy fiber synapses in organotypic hippocampal slices.&nbsp;The tomograms were published in the two studies [1, 2]. The data was re-used for training deep neural networks to segment different synaptic structures in electron micrographs in [3].&nbsp;For the tomograms, organotypic slices were prepared from the hippocampi of neonatal mice according to the interface protocol55 and vitrified after 28 days in vitro in culture medium supplemented with 20% (w/v) bovine serum albumin using an HPM100 (Leica) high-pressure freezing device. The dataset also contains 23 tomograms resulting from chemically-fixed material, which were also published in (Maus et al., 2020). For these tomograms, wild-type animals at postnatal day 28 were transcardially perfused under deep anesthesia, first with 0.9% sodium chloride solution, and then one of two fixatives (Fixative 1: Ice-cold 4% paraformaldehyde, 2.5% glutaraldehyde in 0.1 M phosphate buffer16; Fixative 2: 37&deg; C 2% paraformaldehyde, 2.5% glutaraldehyde, 2 mM CaCl2, in 0.1 M cacodylate buffer56). Brains were rinsed and sectioned coronally through the dorsal hippocampus in an ice-cold 0.1 M phosphate buffer using a VT 1200S vibratome (Leica) (step size 100 &micro;m; amplitude 1.5 mm, speed 0.1 mm/sec). Hippocampal CA3 subregions were excised using a 1.5 mm diameter biopsy punch and high-pressure frozen on the same day in 20% (w/v) bovine serum albumin using an HPM100 (Leica) high-pressure freezing device. For both sample preparations, automated freeze-substitution was performed. Tomograms were collected using a 200 kV JEM-2100 (JEOL) transmission electron microscope equipped with an 11 MP Orius SC1000 CCD camera (Gatan). Tilt-series (tilt range +/- 60&deg;; 1&deg; angular increments) were acquired at 30 000x magnification using SerialEM58. Tomographic reconstructions were generated using weighted back-projection with etomo.The data is organized into two different subfolders for data with annotations for "vesicles" and "active_zones". Each of these subfolders is further subdivided into "train" and "test" folders, which containtomograms for the two different sample preparations in "chemical_fixation" and "single_axis_tem".Each tomogram and the corresponding annotation is stored as a hdf5 file, containing the following internal datasets:- raw: The tomogram data.- labels/vesicles: Annotations for the synaptic vesicles, annotated with IMOD, further postprocessed and then exported to instance masks. (for tomograms in "vesicles")- labels/AZ: Annotations for the active zone, annotated with IMOD and exported to binary masks.
[1] Imig et al., The Morphological and Molecular Nature of Synaptic Vesicle Priming at Presynaptic Active Zones, Neuron, 2014, DOI:10.1016/j.neuron.2014.10.009[2] Maus et al., Ultrastructural Correlates of Presynaptic Functional Heterogeneity in Hippocampal Synapses, Cell Reports, 2020, DOI: 10.1016/j.celrep.2020.02.083[3] Muth, Moschref et al., 2024, Preprint to be published

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/14330011](https://zenodo.org/records/14330011)

[https://doi.org/10.5281/zenodo.14330011](https://doi.org/10.5281/zenodo.14330011)


---

## TNBC

Naylor Peter Jack, Walter Thomas, Laé Marick, Reyal Fabien

Published 2018-02-16

Licensed CC-BY-4.0



Involves an annotated large number of cells, including normal epithelial and myoepithelial breast cells (localized in ducts and lobules), invasive carcinomatous cells, fibroblasts, endothelial cells, adipocytes, macrophages and inflammatory cells (lymphocytes and plasmocytes). In total, our data set consists of 50 images with a total of 4022 annotated cells, the maximum number of cells in one sample is 293 and the minimum number of cells in one sample is 5, with an average of 80 cells per sample and a high standard deviation of 58. The annotation was performed by three experts: an expert pathologist and two trained research fellows. Each sample was annotated by one of the annotators, checked by another one and in case of disagreement, a consensus was established by discussion among the 3 experts.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://paperswithcode.com/dataset/tnbc](https://paperswithcode.com/dataset/tnbc)


---

## Ten simple rules for making training materials FAIR

Leyla Garcia, Bérénice Batut, Melissa L. Burke, Mateusz Kuzak, Fotis Psomopoulos, et al.

Published 2020-05-21

Licensed CC-BY-4.0



The authors offer trainers some simple rules, to help make their training materials FAIR, enabling others to find, (re)use, and adapt them.

Tags: Metadata, Bioinformatics, FAIR-Principles, Include In Dalia

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





Tags: Exclude From Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/5675686](https://zenodo.org/records/5675686)

[https://doi.org/10.5281/zenodo.5675686](https://doi.org/10.5281/zenodo.5675686)


---

## Test data for Bioformats Issue #4366

Ivo Alxneit

Published 2025-09-22

Licensed CC-BY-4.0



[https://zenodo.org/records/17176730](https://zenodo.org/records/17176730)

[https://doi.org/10.5281/zenodo.17176730](https://doi.org/10.5281/zenodo.17176730)


---

## The FAIR Guiding Principles for scientific data management and stewardship

Mark D. Wilkinson, Michel Dumontier, IJsbrand Jan Aalbersberg, Gabrielle Appleton, Myles Axton, et. al

Published 2016-03-15

Licensed CC-BY-4.0



This Comment is the first formal publication of the FAIR Principles, and includes the rationale behind them, and some exemplar implementations in the community.

Tags: FAIR-Principles, Research Data Management, Exclude From Dalia

Content type: Publication

[https://www.nature.com/articles/sdata201618](https://www.nature.com/articles/sdata201618)

[https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)


---

## The FAIR guiding principles for data stewardship - fair enough?

Martin Boeckhout, Gerhard A. Zielhuis, Annelien L. Bredenoord

Published 2018-05-17

Licensed CC-BY-4.0



The FAIR guiding principles for research data stewardship (findability, accessibility, interoperability, and reusability) look set to become a cornerstone of research in the life sciences. A critical appraisal of these principles in light of ongoing discussions and developments about data sharing is in order.

Tags: FAIR-Principles, Data Stewardship, Sharing, Exclude From Dalia

Content type: Publication

[https://www.nature.com/articles/s41431-018-0160-0](https://www.nature.com/articles/s41431-018-0160-0)


---

## The Information Infrastructure for BioImage Data (I3D:bio) project to advance FAIR microscopy data management for the community

Christian Schmidt, Michele Bortolomeazzi, Tom Boissonnet, Julia Dohle, Tobias Wernet, Janina Hanne, Roland Nitschke, Susanne Kunis, Karen Bernhardt, Stefanie Weidtkamp-Peters, Elisa Ferrando-May

Published 2024-03-04

Licensed CC-BY-4.0



Research data management (RDM) in microscopy and image analysis is a challenging task. Large files in proprietary formats, complex N-dimensional array structures, and various metadata models and formats can make image data handling inconvenient and difficult. For data organization, annotation, and sharing, researchers need solutions that fit everyday practice and comply with the FAIR (Findable, Accessible, Interoperable, Reusable) principles. International community-based efforts have begun creating open data models (OME), an open file format and translation library (OME-TIFF, Bio-Formats), data management software platforms, and microscopy metadata recommendations and annotation tools. Bringing these developments into practice requires support and training. Iterative feedback and tool&nbsp;improvement is needed to foster practical adoption by the scientific&nbsp;community. The Information Infrastructure for BioImage Data (I3D:bio) project&nbsp;works on guidelines, training resources, and practical assistance for FAIR&nbsp;microscopy RDM adoption with a focus on the management platform OMERO&nbsp;and metadata annotations.

Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

[https://zenodo.org/records/10805204](https://zenodo.org/records/10805204)

[https://doi.org/10.5281/zenodo.10805204](https://doi.org/10.5281/zenodo.10805204)


---

## The Open Microscopy Environment (OME) Data Model and XML file - open tools for informatics and quantitative analysis in biological imaging

Ilya G. Goldberg, Chris Allan, Jean-Marie Burel, Doug Creager, Andrea Falconi, et. al

Published 2005-05-03

Licensed CC-BY-4.0



The Open Microscopy Environment (OME) defines a data model and a software implementation to serve as an informatics framework for imaging in biological microscopy experiments, including representation of acquisition parameters, annotations and image analysis results.

Tags: Bioimage Analysis, Exclude From Dalia

Content type: Publication

[https://genomebiology.biomedcentral.com/articles/10.1186/gb-2005-6-5-r47](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2005-6-5-r47)

[https://doi.org/10.1186/gb-2005-6-5-r47](https://doi.org/10.1186/gb-2005-6-5-r47)


---

## The Turing Way: Guide for reproducible research

Licensed ['CC-BY-4.0', 'MIT']



A guide which covers topics related to skills, tools and best practices for research reproducibility.

Tags: Include In Dalia

Content type: Book

[https://the-turing-way.netlify.app/reproducible-research/reproducible-research](https://the-turing-way.netlify.app/reproducible-research/reproducible-research)


---

## The crucial role of bioimage analysts in scientific research and publication

Beth A. Cimini, Peter Bankhead, Rocco D' Antuono, Elnaz Fazeli, Julia Fernandez-Rondriguez, Caterina Fuster-Barcelo, Robert Haase, Helena Klara Jambor, Martin L. Jones, Florian Jug, Anna H. Klemm, Anna Kreshuk, Stefania Marcotti, Gabriel G. Martins, Sara Mc Ardle, Kota Miura, Arrate Muñoz-Barrutia, Laura C. Murphy, Michael S. Nelson, Simon F. Nørrelykke, Perrine Paul-Gilloteaux, Thomas Pengo, Joanna W. Pylvänäinen, Lior Pytowski, Arianna Ravera, Annika Reinke, Yousr Rekik, Caterina Strambio-De-Castillia, Daniel Thédié, Virginie Uhlmann, Oliver Umney, Laura Wiggins, Kevin W. Eliceiri

Published 2024-10-30

Licensed CC-BY-4.0



Bioimage analysis (BIA), a crucial discipline in biological research, overcomes the limitations of subjective analysis in microscopy through the creation and application of quantitative and reproducible methods. The establishment of dedicated BIA support within academic institutions is vital to improving research quality and efficiency and can significantly advance scientific discovery. However, a lack of training resources, limited career paths and insufficient recognition of the contributions made by bioimage analysts prevent the full realization of this potential. This Perspective – the result of the recent The Company of Biologists Workshop ‘Effectively Communicating Bioimage Analysis’, which aimed to summarize the global BIA landscape, categorize obstacles and offer possible solutions – proposes strategies to bring about a cultural shift towards recognizing the value of BIA by standardizing tools, improving training and encouraging formal credit for contributions

Tags: Bioimage Analysis, Include In Dalia

Content type: Publication

[https://journals.biologists.com/jcs/article/137/20/jcs262322/362545/The-crucial-role-of-bioimage-analysts-in](https://journals.biologists.com/jcs/article/137/20/jcs262322/362545/The-crucial-role-of-bioimage-analysts-in)


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

## Thinking data management on different scales

Susanne Kunis

Licensed CC-BY-4.0



Presentation given at PoL BioImage Analysis Symposium Dresden 2023

Tags: Research Data Management, Nfdi4Bioimage, Include In Dalia

Content type: Slides

[https://zenodo.org/doi/10.5281/zenodo.8329305](https://zenodo.org/doi/10.5281/zenodo.8329305)


---

## Towards Preservation of Life Science Data with NFDI4BIOIMAGE

Robert Haase

Published 2024-09-03

Licensed CC-BY-4.0



This talk will present the initiatives of the NFDI4BioImage consortium aimed at the long-term preservation of life science data. We will discuss our efforts to establish metadata standards, which are crucial for ensuring data reusability and integrity. The development of sustainable infrastructure is another key focus, enabling seamless data integration and analysis in the cloud. We will take a look at how we manage training materials and communicate with our community. Through these actions, NFDI4BioImage seeks to enable FAIR bioimage data management for German researchers, across disciplines and embedded in the international framework.

Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

[https://zenodo.org/records/13640979](https://zenodo.org/records/13640979)

[https://doi.org/10.5281/zenodo.13640979](https://doi.org/10.5281/zenodo.13640979)


---

## Towards Transparency and Knowledge Exchange in AI-assisted Data Analysis Code Generation

Robert Haase

Published 2024-10-14

Licensed CC-BY-4.0



The integration of Large Language Models (LLMs) in scientific research presents both opportunities and challenges for life scientists. Key challenges include ensuring transparency in AI-generated content and facilitating efficient knowledge exchange among researchers. These issues arise from the in-transparent nature of AI-driven code generation and the informal sharing of AI insights, which may hinder reproducibility and collaboration. This paper introduces git-bob, an innovative AI-assistant designed to address these challenges by fostering an interactive and transparent collaboration platform within GitHub. By enabling seamless dialogue between humans and AI, git-bob ensures that AI contributions are transparent and reproducible. Moreover, it supports collaborative knowledge exchange, enhancing the interdisciplinary dialogue necessary for cutting-edge life sciences research. The open-source nature of git-bob further promotes accessibility and customization, positioning it as a vital tool in employing LLMs responsibly and effectively within scientific communities.

Tags: Exclude From Dalia

[https://zenodo.org/records/13928832](https://zenodo.org/records/13928832)

[https://doi.org/10.5281/zenodo.13928832](https://doi.org/10.5281/zenodo.13928832)


---

## Towards open and standardised imaging data: an introduction to Bio-Formats, OME-TIFF, and OME-Zarr

Josh Moore

Published 2025-05-28

Licensed CC-BY-4.0



https://www.ebi.ac.uk/training/events/towards-open-and-standardised-imaging-data-introduction-bio-formats-ome-tiff-and-ome-zarr/
Microscopy and bioimaging technologies are fundamental tools for exploring biological systems, generating large, multidimensional datasets rich in experimental detail. However, the bioimaging community has historically faced major challenges around data handling: vendor-specific proprietary formats, fragmented metadata storage, and increasingly large dataset sizes that outstrip traditional storage and computing solutions.
In this webinar, key open technologies developed by the Open Microscopy Environment (OME) to address these challenges were presented. Specifically, the Bio-Formats library for accessing diverse proprietary file formats, the OME-TIFF standard for archival data storage, and the OME-Zarr format for cloud-native, scalable bioimaging workflows were presented.

Tags: Nfdi4Bioimage, Include In Dalia

[https://zenodo.org/records/15479606](https://zenodo.org/records/15479606)

[https://doi.org/10.5281/zenodo.15479606](https://doi.org/10.5281/zenodo.15479606)


---

## Tracking of mitochondria and capturing mitoflashes

Leonid Kostrykin, Diana Chiang Jurado

Published 2024-11-20

Licensed CC-BY-4.0



Tags: Bioinformatics, Bioimage Analysis, Include In Dalia

Content type: Workflow, Tutorial

[https://training.galaxyproject.org/training-material/topics/imaging/tutorials/detection-of-mitoflashes/tutorial.html#tracking-of-mitochondria-and-capturing-mitoflashes](https://training.galaxyproject.org/training-material/topics/imaging/tutorials/detection-of-mitoflashes/tutorial.html#tracking-of-mitochondria-and-capturing-mitoflashes)


---

## Train-the-Trainer Concept on Research Data Management

Katarzyna Biernacka, Maik Bierwirth, Petra Buchholz, Dominika Dolzycka, Kerstin Helbig, Janna Neumann, Carolin Odebrecht, Cord Wiljes, Ulrike Wuttke

Published 2020-11-04

Licensed CC-BY-4.0



Within the project FDMentor, a German Train-the-Trainer Programme on Research Data Management (RDM) was developed and piloted in a series of workshops. The topics cover many aspects of research data management, such as data management plans and the publication of research data, as well as didactic units on learning concepts, workshop design and a range of didactic methods.

After the end of the project, the concept was supplemented and updated by members of the Sub-Working Group Training/Further Education (UAG Schulungen/Fortbildungen) of the DINI/nestor Working Group Research Data (DINI/nestor-AG Forschungsdaten). The newly published English version of the Train-the-Trainer Concept contains the translated concept, the materials and all methods of the Train-the-Trainer Programme. Furthermore, additional English references and materials complement this version.

Tags: Research Data Management, Include In Dalia

Content type: Book

[https://zenodo.org/record/4071471](https://zenodo.org/record/4071471)

[https://doi.org/10.5281/zenodo.4071471](https://doi.org/10.5281/zenodo.4071471)


---

## Training Computational Skills in the Age of AI

Robert Haase

Published 2024-11-06

Licensed CC-BY-4.0



Artificial intelligence (AI) and large language models (LLMs) are changing the way we use computers in science. This slide deck introduces ways for using AI and LLMs for making training materials and for exchanging knowledge about how to use AI in joint discussions between humans and LLM-based AI-systems.

Tags: Nfdi4Bioimage, Artificial Intelligence, Include In Dalia

[https://zenodo.org/records/14043615](https://zenodo.org/records/14043615)

[https://doi.org/10.5281/zenodo.14043615](https://doi.org/10.5281/zenodo.14043615)


---

## Training set of microscopy images for Dietler et al. Nature Communications 2020

Nicola Dietler, Matthias Minder, Vojislav Gligorovski, Economou, Augoustina Maria, Joly, Denis Alain Henri Lucien, Ahmad Sadeghi, Chan, Chun Hei Michael, Mateusz Kozinski, Martin Weigert, Anne-Florence Bitbol, Rahi, Sahand Jamal

Published 2021-12-07

Licensed CC-BY-4.0



Training set of microscopy images for Dietler et al. Nature Communications 2020

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/5765648](https://zenodo.org/records/5765648)

[https://doi.org/10.5281/zenodo.5765648](https://doi.org/10.5281/zenodo.5765648)


---

## TrendsInMicroscopy2025

Marcelo Zoccoler, Johannes Soltwedel

Published 2025-03-10T13:42:57+00:00

Licensed CC-BY-4.0



Course contents for biapol course at Trends in Microscopy conference 2025

Tags: Bioimage Analysis, Exclude From Dalia

Content type: Github Repository

[https://biapol.github.io/TrendsInMicroscopy_2025/](https://biapol.github.io/TrendsInMicroscopy_2025/)

[https://github.com/BiAPoL/TrendsInMicroscopy_2025](https://github.com/BiAPoL/TrendsInMicroscopy_2025)


---

## Using Glittr.org to find, compare and re-use online training materials

Geert van Geest, Yann Haefliger, Monique Zahn-Zabal, Patricia M. Palagi

Licensed CC-BY-4.0



Glittr.org is a platform that aggregates and indexes training materials on computational life sciences from public git repositories, making it easier for users to find, compare, and analyze these resources based on various metrics. By providing insights into the availability of materials, collaboration patterns, and licensing practices, Glittr.org supports adherence to the FAIR principles, benefiting the broader life sciences community.

Tags: Bioimage Analysis, Research Data Management, Exclude From Dalia

Content type: Publication, Preprint

[https://www.biorxiv.org/content/10.1101/2024.08.20.608021v1](https://www.biorxiv.org/content/10.1101/2024.08.20.608021v1)


---

## Vision Language Models for Bio-image Data Science

Robert Haase

Published 2025-06-25

Licensed CC-BY-4.0



In this talk, I demonstrate potential use-cases for vision-language models (VLM) in bio-image data science, focusing on how to analyse microscopy image data. It covers these use-cases:

cell counting
bounding-box segmentation
image descriptions
VLMs guessing which algorithm to use for processing
Data analysis code generation
Answering github issues&nbsp;

The talk also points at a number of VLM-based open-source tools which start reshaping the scientific bio-image data science domain:

bia-bob
unprompted
git-bob
napari-chatgpt
bioimage.io chatbot


Tags: Nfdi4Bioimage, Bioimage Analysis, Artificial Intelligence, Include In Dalia

[https://zenodo.org/records/15735577](https://zenodo.org/records/15735577)

[https://doi.org/10.5281/zenodo.15735577](https://doi.org/10.5281/zenodo.15735577)


---

## Volumetric segmentation of biological cells and subcellular structures for optical diffraction tomography images - dataset

Martyna Mazur, Wojciech Krauze

Published 2023-06-16

Licensed CC-BY-4.0



This dataset includes 4&nbsp;files with segmentation results for 4&nbsp;different ODT reconstructions of SH-SY5Y neuroblastoma cell. The segmentation results contain:


	3D binary masks of biological cells obtained through Cellpose [1] and ODT-SAS;
	3D binary masks of organelles: nucleoli and lipid structures (LS) obtained through slice-by-slice manual segmentation&nbsp;and ODT-SAS.


All files are .*mat files.

The files REC_SH-SY5Y_1.mat,&nbsp;REC_SH-SY5Y_2.mat and&nbsp;REC_SH-SY5Y_3.mat&nbsp;consist of 7 variables:

RECON &ndash;&nbsp;tomographic reconstruction of SH-SY5Y neuroblastoma cell;
n_imm &ndash;&nbsp;refractive index of object immersion medium;
dx &ndash;&nbsp;object space sample size in XY [\(\mu m\)];
rayXY &ndash;&nbsp;xy-coordinates of illumination vectors;

maskManual &ndash;&nbsp;table with manually determined 3D binary masks of organelles;
maskCellpose &ndash;&nbsp;3D binary mask of biological cell obtained through Cellpose;
maskODTSAS &ndash;&nbsp;table with 3D binary masks of biological cell and their organelles obtained through ODT-SAS.

File REC_SH-SY5Y_4.mat&nbsp;includes masks for the ODT-SAS and Cellpose segmentation of three closely packed cells and consists of 5 variables: RECON, n_imm, dx, maskCellpose and maskODTSAS.

Access a particular 3D binary mask from &#39;maskManual&#39; and &#39;maskODTSAS&#39; tables, using the following names: &#39;Cell&#39;, &#39;Nucleoli&#39;, &#39;LS&#39;.
For example:

cellMask = maskODTSAS.Cell{1};


[1] Stringer, C., Wang, T., Michaelos, M., &amp; Pachitariu, M. (2021). Cellpose: a generalist algorithm for cellular segmentation. Nature methods, 18(1), 100-106.

&nbsp;

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/8188948](https://zenodo.org/records/8188948)

[https://doi.org/10.5281/zenodo.8188948](https://doi.org/10.5281/zenodo.8188948)


---

## WHAT NOT TO DO WHEN CREATING A DATA MANAGEMENT PLAN (DMP)

Georgia Koutentaki, Martin Schätz, Jan Vališ

Published 2025-05-14

Licensed CC-BY-4.0



Tags: Include In Dalia

[https://zenodo.org/records/15402904](https://zenodo.org/records/15402904)

[https://doi.org/10.5281/zenodo.15402904](https://doi.org/10.5281/zenodo.15402904)


---

## Welcome to BioImage Town

Josh Moore

Licensed CC-BY-4.0



Welcome at NFDI4BIOIMAGE All-Hands Meeting in Düsseldorf, Germany, October 16, 2023

Tags: OMERO, Bioimage Analysis, Nfdi4Bioimage, Exclude From Dalia

Content type: Slides

[https://zenodo.org/doi/10.5281/zenodo.10008464](https://zenodo.org/doi/10.5281/zenodo.10008464)


---

## What is Open Data?

Daniel Dietrich, Jonathan Gray, Tim McNamara, Antti Poikola, Rufus Pollock, et al.

Licensed CC-BY-4.0



This handbook is about open data but what exactly is it? In particular what makes open data open, and what sorts of data are we talking about?

Tags: Open Science, Include In Dalia

Content type: Collection

[http://opendatahandbook.org/guide/en/what-is-open-data/](http://opendatahandbook.org/guide/en/what-is-open-data/)


---

## When Data Doesn't Fit

Josh Moore

Published 2025-09-11

Licensed CC-BY-4.0



Presented at "International Symposium on Integrative Bioinformatics", Gatersleben Research Conference Series&nbsp;from&nbsp;September 10&ndash;12, 2025, &nbsp;https://meetings.ipk-gatersleben.de/grc-ib2025/

Tags: Include In Dalia

[https://zenodo.org/records/17087096](https://zenodo.org/records/17087096)

[https://doi.org/10.5281/zenodo.17087096](https://doi.org/10.5281/zenodo.17087096)


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

## Workflow for user introduction into microscopy, OMERO and data management at Center for Advanced imaging

Ksenia Krooß, Fuchs, Vanessa Aphaia Fiona, Tom Boissonnet, Stefanie Weidtkamp-Peters

Published 2025-03-07

Licensed CC-BY-4.0



At the Center for Advanced Imaging (CAi) at the Heinrich Heine University D&uuml;sseldorf, Germany, we have established a workflow to guide users through all aspects of bioimaging. The process begins with an initial consultation with our imaging specialists regarding microscopy techniques for their specific project. Users then receive training in microscope operation, ensuring they can handle the equipment effectively. If needed, our specialists also provide support in image analysis. Next, we introduce users to OMERO, highlighting its features and the advantages of using a bioimage data management system. They are then trained to structure and annotate their data within OMERO according to the Recommended Metadata for Biological Images (REMBI), taking their specific research topics into account. As users prepare for data publication, we assist with data organization and repository uploads. Our goal is to educate researchers in managing bioimage data&nbsp;throughout its entire lifecycle, with a strong emphasis on the FAIR (findable, accessible, interoperable, reusable) principles.

Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

[https://zenodo.org/records/14988921](https://zenodo.org/records/14988921)

[https://doi.org/10.5281/zenodo.14988921](https://doi.org/10.5281/zenodo.14988921)


---

## Working Group Charter. RDM Helpdesk Network

Judith Engel, Patrick Helling, Robert Herrenbrück, MarinaLemaire, Hela Mehrtens, Marcus Schmidt, Martha Stellmacher, Lukas Weimer, Cord Wiljes, Wolf Zinke

Published 2024-11-04

Licensed CC-BY-4.0



Support is an essential component of an efficient infrastructure for research data management (RDM). Helpdesks guide researchers through this complex landscape and provide reliable support about all questions regarding research data management, including support for technical services, best practices, requirements of funding organizations and legal topics. In NFDI, most consortia have already established or are planning to establish helpdesks to support their specific communities. On a local level, many institutions have set up RDM helpdesks that provide support for the researchers of their own institution. Additional RDM support services are offered by RDM federal state initiatives, by research data centers, by specialist libraries, by the EOSC, and by providers of RDM-relevant tools. Helpdesks cover a wide range of institutions, disciplines, topics, methodologies and target audiences. However, the individual helpdesks are not yet interconnected and therefore cannot complement one another in an efficient way: Given the wide and constantly increasing complexity of RDM, no single helpdesk can provide the expertise for all potential support requests. Therefore, we see great potential in combining the efforts and resources of the existing RDM helpdesks into an efficient and comprehensive national RDM support network in order to provide optimal and tailored RDM support to all researchers and research-related institutions in Germany and in an international context.

Tags: Exclude From Dalia

[https://zenodo.org/records/14035822](https://zenodo.org/records/14035822)

[https://doi.org/10.5281/zenodo.14035822](https://doi.org/10.5281/zenodo.14035822)


---

## Zarr - A Cloud-Optimized Storage for Interactive Access of Large Arrays

Josh Moore, Susanne Kunis

Published 2023-09-07

Licensed CC-BY-4.0



For decades, the sharing of large N-dimensional datasets has posed issues across multiple domains. Interactively accessing terabyte-scale data has previously required significant server resources to properly prepare cropped or down-sampled representations on the fly. Now, a cloud-native chunked format easing this burden has been adopted in the bioimaging domain for standardization. The format — Zarr — is potentially of interest for other consortia and sections of NFDI.

Tags: Nfdi4Bioimage, Bioimage Analysis, Exclude From Dalia

Content type: Publication

[https://www.tib-op.org/ojs/index.php/CoRDI/article/view/285](https://www.tib-op.org/ojs/index.php/CoRDI/article/view/285)


---

## Zeiss AxioZoom Stage Adapter

Michael Gerlach

Published 2024-06-20

Licensed CC-BY-4.0



A 3D- printable microscope stage adapter for the reproducible accomodation of samples at a Zeiss AxioZoom stereomicroscope.
4 cylindrical anchors are fixed to the glass plate of the stage. The stage adapter is reversibly placed on these anchors.
&nbsp;

Tags: Exclude From Dalia

[https://zenodo.org/records/7963020](https://zenodo.org/records/7963020)

[https://doi.org/10.5281/zenodo.7963020](https://doi.org/10.5281/zenodo.7963020)


---

## Zeiss AxioZoom Stage Adapter - 12/6Well Plate

Michael Gerlach

Published 2024-06-20

Licensed CC-BY-4.0



A 3D- printable microscope stage adapter for the reproducible accomodation of 6 or 12-well plates at a Zeiss AxioZoom microscope.
4 cylindrical anchors are fixed to the glass plate of the stage. The stage adapter is reversibly placed on these anchors and acommodates a standard Greiner 6- or 12-well plate.

Tags: Exclude From Dalia

[https://zenodo.org/records/7944877](https://zenodo.org/records/7944877)

[https://doi.org/10.5281/zenodo.7944877](https://doi.org/10.5281/zenodo.7944877)


---

## Zeiss AxioZoom Stage Adapter - EM block holder

Michael Gerlach

Published 2024-06-20

Licensed CC-BY-4.0



A 3D- printable microscope stage adapter for the reproducible accomodation of EM Blocks at a Zeiss AxioZoom microscope.

4 cylindrical anchors are fixed to the glass plate of the stage. The stage adapter is reversibly placed on these anchors and acommodates 70 standard resin EM blocks.

Tags: Exclude From Dalia

[https://zenodo.org/records/7963006](https://zenodo.org/records/7963006)

[https://doi.org/10.5281/zenodo.7963006](https://doi.org/10.5281/zenodo.7963006)


---

## Zeiss AxioZoom Stage Adapter - Microscope slides

Michael Gerlach

Published 2024-06-21

Licensed CC-BY-4.0



A 3D- printable microscope stage adapter for the reproducible accomodation of microscopic slides at a Zeiss AxioZoom microscope.
4 cylindrical anchors are fixed to the glass plate of the stage. The stage adapter is reversibly placed on these anchors and acommodates 4 standard glass slides.

Tags: Exclude From Dalia

[https://zenodo.org/records/7945018](https://zenodo.org/records/7945018)

[https://doi.org/10.5281/zenodo.7945018](https://doi.org/10.5281/zenodo.7945018)


---

## ZeroCostDL4Mic - Stardist 2D example training and test dataset (light)

Johanna Jukkala, Guillaume Jacquemet

Published 2023-05-19

Licensed CC-BY-4.0



Name: ZeroCostDL4Mic - Stardist 2D example training and test dataset (light)

(see&nbsp;our Wiki&nbsp;for details)

Data type: Paired microscopy images (fluorescence) and corresponding masks

Microscopy data type: Fluorescence microscopy (SiR-DNA) and masks obtained via manual segmentation (see&nbsp;https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist&nbsp;for details about the segmentation)

Microscope: Spinning disk confocal microscope with a 20x 0.8 NA objective

Cell type: DCIS.COM LifeAct-RFP cells

File format: .tif (16-bit for fluorescence and 8 and 16-bit for the masks)

Image size: 1024x1024 (Pixel size: 634 nm)

&nbsp;

Author(s): Johanna Jukkala1,2&nbsp;and Guillaume Jacquemet1,2

Contact email: guillaume.jacquemet@abo.fi

Affiliation&nbsp;:&nbsp;

1) Faculty of Science and Engineering, Cell Biology, &Aring;bo Akademi University, 20520 Turku, Finland

2) Turku Bioscience Centre, University of Turku and &Aring;bo Akademi University, FI-20520 Turku, Finland

Funding bodies: G.J. was supported by grants awarded by the Academy of Finland, the Sigrid Juselius Foundation and &Aring;bo Akademi University Research Foundation (CoE CellMech) and by Drug Discovery and Diagnostics strategic funding to &Aring;bo Akademi University.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/7949940](https://zenodo.org/records/7949940)

[https://doi.org/10.5281/zenodo.7949940](https://doi.org/10.5281/zenodo.7949940)


---

## ZeroCostDL4Mic - Stardist example training and test dataset

Johanna Jukkala, Guillaume Jacquemet

Published 2020-03-17

Licensed CC-BY-4.0



Name: ZeroCostDL4Mic - Stardist example training and test dataset

(see our Wiki for details)

&nbsp;

Data type: Paired microscopy images (fluorescence) and corresponding masks

Microscopy data type: Fluorescence microscopy (SiR-DNA) and masks obtained via manual segmentation (see https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist for details about the segmentation)

Microscope: Spinning disk confocal microscope with a 20x 0.8 NA objective

Cell type: DCIS.COM LifeAct-RFP cells

File format: .tif (16-bit for fluorescence and 8 and 16-bit for the masks)

Image size: 1024x1024 (Pixel size: 634 nm)

&nbsp;

Author(s): Johanna Jukkala1,2 and Guillaume Jacquemet1,2

Contact email: guillaume.jacquemet@abo.fi

Affiliation :&nbsp;

1) Faculty of Science and Engineering, Cell Biology, &Aring;bo Akademi University, 20520 Turku, Finland

2) Turku Bioscience Centre, University of Turku and &Aring;bo Akademi University, FI-20520 Turku, Finland

&nbsp;

Associated publications: Unpublished

Funding bodies: G.J. was supported by grants awarded by the Academy of Finland, the Sigrid Juselius Foundation and &Aring;bo Akademi University Research Foundation (CoE CellMech) and by Drug Discovery and Diagnostics strategic funding to &Aring;bo Akademi University.

Tags: Ai-Ready, Exclude From Dalia

Content type: Data

[https://zenodo.org/records/3715492](https://zenodo.org/records/3715492)

[https://doi.org/10.5281/zenodo.3715492](https://doi.org/10.5281/zenodo.3715492)


---

## [BINA CC] Scalable strategies for a next-generation of FAIR bioimaging

Josh Moore

Published 2024-09-24

Licensed CC-BY-4.0



Presented at https://www.bioimagingnorthamerica.org/events/bina-2024-community-congress/

Tags: Exclude From Dalia

[https://zenodo.org/records/13831274](https://zenodo.org/records/13831274)

[https://doi.org/10.5281/zenodo.13831274](https://doi.org/10.5281/zenodo.13831274)


---

## [CIDAS] Scalable strategies for a next-generation of FAIR bioimaging

Josh Moore

Published 2025-01-23

Licensed CC-BY-4.0



Talk given at Georg-August-Universit&auml;t G&ouml;ttingen Campus Institute Data Science23rd January 2025
https://www.uni-goettingen.de/en/653203.html

Tags: Nfdi4Bioimage, Include In Dalia

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

Tags: Nfdi4Bioimage, Include In Dalia

[https://zenodo.org/records/14650434](https://zenodo.org/records/14650434)

[https://doi.org/10.5281/zenodo.14650434](https://doi.org/10.5281/zenodo.14650434)


---

## [CORDI 2023] Zarr: A Cloud-Optimized Storage for Interactive Access of Large Arrays

Josh Moore

Licensed CC-BY-4.0



For decades, the sharing of large N-dimensional datasets has posed issues across multiple domains. Interactively accessing terabyte-scale data has previously required significant server resources to properly prepare cropped or down-sampled representations on the fly. Now, a cloud-native chunked format easing this burden has been adopted in the bioimaging domain for standardization. The format — Zarr — is potentially of interest for other consortia and sections of NFDI.

Tags: Research Data Management, Bioimage Analysis, Data Science, Exclude From Dalia

Content type: Poster

[https://zenodo.org/doi/10.5281/zenodo.8340247](https://zenodo.org/doi/10.5281/zenodo.8340247)


---

## [Community Meeting 2024] Overview Team Image Data Analysis and Management

Susanne Kunis, Thomas Zobel

Published 2024-03-08

Licensed CC-BY-4.0



Overview of Activities of the Team Image Data Analysis and Management of German BioImaging e.V.
&nbsp;

Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

[https://zenodo.org/records/10796364](https://zenodo.org/records/10796364)

[https://doi.org/10.5281/zenodo.10796364](https://doi.org/10.5281/zenodo.10796364)


---

## [Community Meeting 2024] Supporting and financing RDM projects within GerBI

Stefanie Weidtkamp-Peters, Josh Moore, Christian Schmidt, Roland Nitschke, Susanne Kunis, Thomas Zobel

Published 2024-03-28

Licensed CC-BY-4.0



Overview of GerBI RDM projects: why and how?

Tags: Exclude From Dalia

[https://zenodo.org/records/10889694](https://zenodo.org/records/10889694)

[https://doi.org/10.5281/zenodo.10889694](https://doi.org/10.5281/zenodo.10889694)


---

## [ELMI 2024]  AI's Dirty Little Secret: Without
FAIR Data, It's Just Fancy Math

Josh Moore, Susanne Kunis

Published 2024-05-21

Licensed CC-BY-4.0



Poster presented at the European Light Microscopy Initiative meeting in Liverpool (https://www.elmi2024.org/)

Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

[https://zenodo.org/records/11235513](https://zenodo.org/records/11235513)

[https://doi.org/10.5281/zenodo.11235513](https://doi.org/10.5281/zenodo.11235513)


---

## [ELMI 2024] AI's Dirty Little Secret: Without FAIR Data, It's Just Fancy Math

Josh Moore, Susanne Kunis

Licensed CC-BY-4.0



Poster presented at the European Light Microscopy Initiative meeting in Liverpool (https://www.elmi2024.org/)

Tags: Research Data Management, FAIR-Principles, Bioimage Analysis, Nfdi4Bioimage, Include In Dalia

Content type: Poster

[https://zenodo.org/doi/10.5281/zenodo.11235512](https://zenodo.org/doi/10.5281/zenodo.11235512)


---

## [ELMI2025] Bridging communities with OME-Zarr

Christian Schmidt, Aastha Mathur, Josh Moore

Published 2025-06-04

Licensed CC-BY-4.0



Presented at ELMI2025
&nbsp;
https://www.embl.org/about/info/course-and-conference-office/events/elmi2025/

Tags: Nfdi4Bioimage, Include In Dalia

[https://zenodo.org/records/15393592](https://zenodo.org/records/15393592)

[https://doi.org/10.5281/zenodo.15393592](https://doi.org/10.5281/zenodo.15393592)


---

## [ELMI2025] The Road to OME-Zarr 1.0

Josh Moore

Published 2025-06-05

Licensed CC-BY-4.0



Presented at https://www.embl.org/about/info/course-and-conference-office/events/elmi2025/
&nbsp;
Abstract
For over 20 years, the Open Microscopy Environment (OME) has developed tools and specifications to support bioimaging data sharing. Technologies such as Bio-Formats, OMERO, and OME-TIFF have helped researchers manage the growing size, complexity, and acquisition rates of imaging datasets. However, with increasing mandates for research data management, such as the Nelson memo in the United States, and the shift toward cloud-native workflows, the bioimaging community faces new challenges in ensuring scalable and FAIR data infrastructure.
In 2024, following expanding community engagement, the focus of the Next-Generation File Format (NGFF) community was on building consensus around a Request for Comments (RFC) process. This collaborative effort has laid the foundation for future refinements and wider adoption. In parallel, we hosted the &ldquo;OME2024 NGFF Challenge," bringing together over the course of just four months hundreds of terabytes of data in a first prototype of federated image hosting, showcasing the power of OME-Zarr for handling large-scale, distributed datasets.
In 2025, we are set to take a major step toward a stable FAIR solution with OME-Zarr 1.0. This milestone marks a crucial phase towards an international standard, providing an open, cloud-optimized, and scalable solution for handling terabyte- and petabyte-scale imaging data. The 1.0 release will introduce long-awaited transforms, enabling robust support for multimodal datasets, followed by collections and an extensibility mechanism to accommodate evolving scientific needs. These additions emphasize a solid foundation on which future capabilities can be built while providing the stability needed for broader adoption of the format. This presentation will outline the path to 1.0, including community-driven refinements, vendor engagement to ensure complete metadata representation, and alignment with global bioimaging initiatives. As imaging data continues to grow in scale and complexity, consensus-driven evolution of infrastructure will be key to ensuring a truly FAIR future for bioimaging.
&nbsp;

Tags: Nfdi4Bioimage, Include In Dalia

[https://zenodo.org/records/15597856](https://zenodo.org/records/15597856)

[https://doi.org/10.5281/zenodo.15597856](https://doi.org/10.5281/zenodo.15597856)


---

## [ELMI2025] Workshop: FAIR101 - Navigating FAIR data from principles to practice

Isabel Kemmer, Euro-BioImaging ERIC

Published 2025-06-12

Licensed CC-BY-4.0



&nbsp;This workshop was held at the ELMI Meeting 2025 in Heidelberg (https://www.embl.org/about/info/course-and-conference-office/events/elmi2025/).
Abstract
FAIR 101 - Navigating FAIR data from principles to practice
Isabel Kemmer, Euro-BioImaging ERIC
This workshop will introduce the FAIR principles in the context of bioimaging data. Designed for researchers working across scales and technologies of biological and biomedical imaging, the session will address the unique challenges posed by complex, multidimensional bioimaging datasets. With the aim of providing simple yet impactful steps for a smooth start to the FAIR journey we will explore the features and benefits of FAIR data through interactive exercises and discussions - from metadata annotation and data management planning to repository selection. By the end of the workshop, you will feel more confident in applying the FAIR concepts and be prepared to improve your imaging workflows to make your precious data even more valuable.

Tags: Include In Dalia

[https://zenodo.org/records/15647102](https://zenodo.org/records/15647102)

[https://doi.org/10.5281/zenodo.15647102](https://doi.org/10.5281/zenodo.15647102)


---

## [GBI EOE VII] Five (or ten) must-have items for making IT infrastructure for managing bioimage data

Josh Moore

Published 2024-05-26

Licensed CC-BY-4.0



Presentation made to the GBI Image Data Management Working Group during the 7th Exchange of Experience in Uruguay.

Tags: Include In Dalia

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

Tags: Exclude From Dalia

[https://zenodo.org/records/14001388](https://zenodo.org/records/14001388)

[https://doi.org/10.5281/zenodo.14001388](https://doi.org/10.5281/zenodo.14001388)


---

## [I2K] Scalable strategies for a next-generation of FAIR bioimaging

Josh Moore

Published 2024-10-25

Licensed CC-BY-4.0



or, "OME-Zarr: 'even a talk on formats [can be] interesting'"
Presented at https://events.humantechnopole.it/event/1/

Tags: Include In Dalia

[https://zenodo.org/records/13991322](https://zenodo.org/records/13991322)

[https://doi.org/10.5281/zenodo.13991322](https://doi.org/10.5281/zenodo.13991322)


---

## [N4BI AHM] Welcome to BioImage Town

Josh Moore

Published 2023-10-16

Licensed CC-BY-4.0



Keynote at the NFDI4BIOIMAGE All-Hands Meeting in Düsseldorf, Germany, October 16, 2023.

Tags: Nfdi4Bioimage, Exclude From Dalia

[https://zenodo.org/records/15031842](https://zenodo.org/records/15031842)

[https://doi.org/10.5281/zenodo.15031842](https://doi.org/10.5281/zenodo.15031842)


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

## [SWAT4HCLS 2023] NFDI4BIOIMAGE: Perspective for a national bioimage standard

Josh Moore, Susanne Kunis

Licensed CC-BY-4.0



Poster presented at Semantic Web Applications and Tools for Health Care and Life Sciences (SWAT4HCLS 2023), Feb 13--16, 2023, Basel, Switzerland. NFDI4BIOIMAGE is a newly established German consortium dedicated to the FAIR representation of biological imaging data. A key deliverable is the definition of a semantically-compatible FAIR image object integrating RDF metadata with web-compatible storage of large n-dimensional binary data in OME-Zarr. We invite feedback from and collaboration with other endeavors during the soon-to-begin 5 year funding period.

Tags: Research Data Management, FAIR-Principles, Nfdi4Bioimage, Include In Dalia

Content type: Poster

[https://zenodo.org/doi/10.5281/zenodo.7928332](https://zenodo.org/doi/10.5281/zenodo.7928332)


---

## [Short Talk] NFDI4BIOIMAGE - A consortium in the National Research Data Infrastructure

Christian Schmidt

Published 2024-04-10

Licensed CC-BY-4.0



Short Talk about the NFDI4BIOIMAGE consortium presented at the RDM in (Bio-)Medicine Information Event on April 10th, 2024, organized C&sup3;RDM &amp; ZB MED.

Tags: Exclude From Dalia

[https://zenodo.org/records/10939520](https://zenodo.org/records/10939520)

[https://doi.org/10.5281/zenodo.10939520](https://doi.org/10.5281/zenodo.10939520)


---

## [Webinar] A journey to FAIR bioimage data

Stefanie Weidtkamp-Peters, Tom Boissonnet, Christian Schmidt

Published 2025-07-03

Licensed CC-BY-4.0



Presentation slides from an EMBL-EBI Webinar Talk within the webinar series:
"How to organise and share my imaging data? - Multimodal data management for marine biologists, environmental scientists and imaging specialists"
&nbsp;
Abstract / Description
Bioimaging is a pervasive and indispensable methodological approach in the life and biomedical sciences. Due to the development of new technologies and the easier access to compute resources, bioimaging experiments have become a big data discipline, facing the same challenges as other omics technologies within the life sciences. However, to fully exploit the potential of bioimage data, it is necessary to make the data FAIR. In this webinar we will present viable solutions for storing, processing, analysing, and, first and foremost, sharing bioimaging data. We will introduce services provided to the scientific community, that are dealing with various aspects of the bioimage data life cycle such as:
- Where to get support for bioimage data management- Local bioimage data management: OMERO and beyond- Annotation of bioimage data: metadata, ontologies, REMBI etc- Linking your image data with experimental protocols and analysis results- Large data living in the cloud: ome.zarr- Publication of bioimage data
Who is this course for?
This webinar is suitable for marine biologists and environmental scientists collecting samples from the natural environment, generating, visualising, annotating and analysing large, multimodal datasets such as imaging data, and sharing their data by submitting them to public data repositories. The webinar will support you to set up an efficient data flow that is aligned with FAIR principles.
This event is part of a webinar series&nbsp;organised by the&nbsp;STANDFLOW&nbsp;project, an initiative supported by EMBL&rsquo;s&nbsp;Planetary biology Transversal Theme. STANDFLOW is about a collaborative effort towards creating a standardised data management workflow. The project primarily utilises imaging data derived from samples collected through the&nbsp;TREC&nbsp;(Traversing European Coastlines) and the&nbsp;Roscoff Culture Collection. For details on all topics covered in this series and registration information, please visit the following link:&nbsp;How to organise and share my imaging data?: Multimodal data management for marine biologists, and environmental scientists and imaging specialists
Outcomes
By the end of the webinar you will be able to:&nbsp;

Find resources and support for bioimage data management
Get started with bioimage data annotation
Identify the dos and don'ts for bioimage data publication

&nbsp;
(taken from: https://www.ebi.ac.uk/training/events/journey-fair-bioimage-data/)

Tags: Nfdi4Bioimage, Fair Principles, Research Data Management, Include In Dalia

[https://zenodo.org/records/15796252](https://zenodo.org/records/15796252)

[https://doi.org/10.5281/zenodo.15796252](https://doi.org/10.5281/zenodo.15796252)


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


Tags: Nfdi4Bioimage, Research Data Management, Exclude From Dalia

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

Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

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

Tags: Include In Dalia

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









Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

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

Tags: Nfdi4Bioimage, Research Data Management, Include In Dalia

[https://zenodo.org/records/13861026](https://zenodo.org/records/13861026)

[https://doi.org/10.5281/zenodo.13861026](https://doi.org/10.5281/zenodo.13861026)


---

## ilastik: interactive machine learning for (bio)image analysis

Anna Kreshuk, Dominik Kutra

Licensed CC-BY-4.0



Tags: Artificial Intelligence, Bioimage Analysis, Exclude From Dalia

Content type: Slides

[https://zenodo.org/doi/10.5281/zenodo.4330625](https://zenodo.org/doi/10.5281/zenodo.4330625)


---

## imaris file not read by bfGetReader()

Julien Dubrulle

Published 2025-03-10

Licensed CC-BY-4.0



This file cannot be read by bfGetReader() v8.1.1 on a Windows operating workstation.

Tags: Exclude From Dalia

[https://zenodo.org/records/15001649](https://zenodo.org/records/15001649)

[https://doi.org/10.5281/zenodo.15001649](https://doi.org/10.5281/zenodo.15001649)


---

## introduction-to-generative-ai

Bruna Piereck, Alexander Botzki

Published 2024-09-27T14:38:51+00:00

Licensed CC-BY-4.0



Course repository for Strategic Use of Generative AI

Tags: Artificial Intelligence, Include In Dalia

Content type: Github Repository, Tutorial

[https://github.com/vibbits/introduction-to-generative-ai](https://github.com/vibbits/introduction-to-generative-ai)

[https://liascript.github.io/course/?https://raw.githubusercontent.com/vibbits/introduction-to-generative-ai/refs/heads/main/README.md](https://liascript.github.io/course/?https://raw.githubusercontent.com/vibbits/introduction-to-generative-ai/refs/heads/main/README.md)


---

## nextflow-workshop

Tuur Muyldermans, Kris Davie, Alexander, Nicolas Vannieuwkerke, Kobe Lavaerts, Marcel Ribeiro-Dantas, Bruna Piereck, Steff Taelman

Published 2023-03-29T10:40:04+00:00

Licensed CC-BY-4.0



Nextflow workshop materials March 2023

Tags: Workflow, Nextflow, Include In Dalia

Content type: Github Repository, Tutorial

[https://github.com/vibbits/nextflow-workshop](https://github.com/vibbits/nextflow-workshop)

[https://liascript.github.io/course/?https://raw.githubusercontent.com/vibbits/nextflow-workshop/main/README.md#1](https://liascript.github.io/course/?https://raw.githubusercontent.com/vibbits/nextflow-workshop/main/README.md#1)


---

## qupath-workshop

Antoine A. Ruzette, dependabot[bot]

Published 2025-01-16T14:05:02+00:00

Licensed CC-BY-4.0



Materials supporting the QuPath workshop at Harvard Medical School.

Tags: Notebook, Slides, Collection, Include In Dalia

Content type: Github Repository

[https://github.com/HMS-IAC/qupath-workshop](https://github.com/HMS-IAC/qupath-workshop)


---

## re3data.org - registry of Research Data Repositories

Licensed CC-BY-4.0



Re3data is a global registry of research data repositories that covers research data repositories from different academic disciplines. It includes repositories that enable permanent storage of and access to data sets to researchers, funding bodies, publishers, and scholarly institutions.

Tags: Research Data Management, Exclude From Dalia

Content type: Website

[https://www.re3data.org/](https://www.re3data.org/)


---

## scikit-learn MOOC

Loïc Estève et al.

Licensed CC-BY-4.0



Machine learning in Python with scikit-learn MOOC

Tags: Bioimage Analysis, Machine Learning, Include In Dalia

Content type: Github Repository

[https://github.com/INRIA/scikit-learn-mooc](https://github.com/INRIA/scikit-learn-mooc)


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

