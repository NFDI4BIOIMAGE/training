# Recently added (10)
## Accessible Interactive Spatial-Omics Data Visualizations with Vitessce and OMERO

Bortolomeazzi Michele

Published 2025-06-30

Licensed CC-BY-4.0



OMERO is the most used research data management system (RDM) in the bioimaging domain, and has been adopted as a centralized RDM solution by several academic and research institutions. A main reason for this is the ability to directly view and annotate images from a web-based interface. However, this feature of OMERO is currently underpowered for the visualization of very large or multimodal datasets. These datasets, are becoming a more and more common foundation for biological and biomedical studies, due to the recent developments in imaging, and sequencing technologies which enabled their application to spatial-omics. In order to begin to provide this multimodal-data capability to OMERO, we developed omero-vitessce (https://github.com/NFDI4BIOIMAGE/omero-vitessce/tree/main), a new OMERO.web plugin for viewing data stored in OMERO with the Vitessce (http://vitessce.io/) multimodal data viewer. omero-vitessce can be installed as an OMERO.web plugin with PiPy (https://pypi.org/project/omero-vitessce/), and allows users to set up interactive visualizations of their images of cells and tissues through interactive plots which are directly linked to the image. This enables the visual exploration of bioimage-analysis results and of multimodal data such as those generated through spatial-omics experiments. The data visualization is highly customizable and can be configured not only through custom configuration files, but also with the graphical interface provided by the plugin, thus making omero-vitessce a highly user-friendly solution for multimodal data viewing. most biological datasets. We plan to extend the interoperability of omero-vitessce with the OME-NGFF and SpatialData file formats to leverage the efficiency of these cloud optimized formats.

[https://zenodo.org/records/15771899](https://zenodo.org/records/15771899)

[https://doi.org/10.5281/zenodo.15771899](https://doi.org/10.5281/zenodo.15771899)


---

## Bio-image Data Science Lectures 2025 @ Uni Leipzig / ScaDS.AI

Robert Haase

Published 2025-07-02

Licensed CC-BY-4.0



These are the PPTx training resources for Students at Uni Leipzig who want to dive into bio-image data science with Python. The material will develop here and in the corresponding&nbsp;github repository between April and July 2025.

[https://zenodo.org/records/15793536](https://zenodo.org/records/15793536)

[https://doi.org/10.5281/zenodo.15793536](https://doi.org/10.5281/zenodo.15793536)


---

## Building a National Research Data Infrastructure 
for Microscopy and BioImage Analysis

Josh Moore

Published 2025-06-30

Licensed CC-BY-4.0



Presentation for the BioImagingUK Meeting taking place from 1200 - 1500 BST on Monday 30 June 2025 at mmc2025 https://www.mmc-series.org.uk/meetings-features/bioimaginguk-meeting.html
This pre-congress meeting provides an opportunity for the UK Bioimaging community to discuss priorities and strategies in national infrastructure, technology development, training, careers and ways to share knowledge across different disciplines. The session will consist of short talks from members of the BioImagingUK community and industrial/institute collaboration partners to update on progress, new opportunities and initiatives. There will be interactive Q+A sessions to encourage discussion and enable emerging priorities and ideas to be highlighted.

[https://zenodo.org/records/15756866](https://zenodo.org/records/15756866)

[https://doi.org/10.5281/zenodo.15756866](https://doi.org/10.5281/zenodo.15756866)


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


[https://zenodo.org/records/13897937](https://zenodo.org/records/13897937)

[https://doi.org/10.5281/zenodo.13897937](https://doi.org/10.5281/zenodo.13897937)


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

[https://zenodo.org/records/15827771](https://zenodo.org/records/15827771)

[https://doi.org/10.5281/zenodo.15827771](https://doi.org/10.5281/zenodo.15827771)


---

## Interactive Bioimage Analysis Workflow with CLIJ (@EABIAS 2025 training event)

Wei-Chen Chu

Published 2025-03-23

Licensed CC-BY-4.0



Presentation file used in the EABIAS training event:&nbsp;EABIAS/2025-ImageJ-Micro-Image-Analysis-and-Programming_Taipei (Lesson_04)Video Recording (in Mandarin): https://www.youtube.com/watch?v=uheSMSENnzE

[https://zenodo.org/records/15070246](https://zenodo.org/records/15070246)

[https://doi.org/10.5281/zenodo.15070246](https://doi.org/10.5281/zenodo.15070246)


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

[https://zenodo.org/records/15747344](https://zenodo.org/records/15747344)

[https://doi.org/10.5281/zenodo.15747344](https://doi.org/10.5281/zenodo.15747344)


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


[https://zenodo.org/records/15735577](https://zenodo.org/records/15735577)

[https://doi.org/10.5281/zenodo.15735577](https://doi.org/10.5281/zenodo.15735577)


---

## WHAT NOT TO DO WHEN CREATING A DATA MANAGEMENT PLAN (DMP)

Georgia Koutentaki, Martin Schätz, Jan Vališ

Published 2025-05-14

Licensed CC-BY-4.0



[https://zenodo.org/records/15402904](https://zenodo.org/records/15402904)

[https://doi.org/10.5281/zenodo.15402904](https://doi.org/10.5281/zenodo.15402904)


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

[https://zenodo.org/records/15796252](https://zenodo.org/records/15796252)

[https://doi.org/10.5281/zenodo.15796252](https://doi.org/10.5281/zenodo.15796252)


---

