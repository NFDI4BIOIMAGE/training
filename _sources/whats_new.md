# Recently added (10)
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

## Developing a Training Strategy

Robert Haase

Published 2024-11-08

Licensed CC-BY-4.0



When training people in topics such as programming, bio-image analysis or data science, it makes sense to define a training strategy with a wider perspective than just trainees needs. This slide deck gives insights into aspects to consider when defining a training strategy. It considers funder's interests, financial aspects, metrics / goals, steps towards sustainability and opportunities for outreach and for founding future collaborations.

[https://zenodo.org/records/14053758](https://zenodo.org/records/14053758)

[https://doi.org/10.5281/zenodo.14053758](https://doi.org/10.5281/zenodo.14053758)


---

## Gut Analysis Toolbox

Luke Sorensen, Ayame Saito, Sabrina Poon, Noe Han, Myat, Ryan Hamnett, Peter Neckel, Adam Humenick, Keith Mutunduwe, Christie Glennan, Narges Mahdavian, JH Brookes, Simon, M McQuade, Rachel, PP Foong, Jaime, Estibaliz Gómez-de-Mariscal, Muñoz Barrutia, Arrate, Kaltschmidt, Julia A., King, Sebastian K., Robert Haase, Simona Carbone, A. Veldhuis, Nicholas, P. Poole, Daniel, Pradeep Rajasekhar

Published 2025-02-23

Licensed BSD-3-CLAUSE



Full Changelog: https://github.com/pr4deepr/GutAnalysisToolbox/compare/v0.7...v1.0
Skip versions to 1.0
Fixed major bugs:

Use deepImageJ to run Stardist models, due to issue with tensorflow in Fiji
Fixed ganglia model to be compatible with new versions of deepImageJ
Updated all scripts to accommodate for new deepImageJ workflow
Added macros to generate user dialog when running GAT for first time


[https://zenodo.org/records/14913673](https://zenodo.org/records/14913673)

[https://doi.org/10.5281/zenodo.14913673](https://doi.org/10.5281/zenodo.14913673)


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

## LauLauThom/MaskFromRois-Fiji: v1.0.1 - better handle "cancel"

Laurent Thomas, Pierre Trehin

Published 2025-02-24

Licensed MIT



Also re-uploaded the compiled FilenameGetter.py$class to the update site, to fix https://github.com/LauLauThom/MaskFromRois-Fiji/issues/7

[https://zenodo.org/records/14917722](https://zenodo.org/records/14917722)

[https://doi.org/10.5281/zenodo.14917722](https://doi.org/10.5281/zenodo.14917722)


---

## Reconstructed images of a 2DSIM multiposition acquisition.

Louis Romette

Published 2025-02-19

Licensed CC-BY-4.0



Acquired with an Nikon SIM, in 2D-SIM mode at 488nm of excitation with 30% laser power and 200ms of exposition.&nbsp; Fluorescence is a knocked-in mStayGold-&beta;2Spectrin. Cells are rat hippocampal neurons &agrave; DIV 3. The file is a reconstructed multiposition acquisition (10 positions). Uploaded to show a probable issue with Bio-Formats in Fiji, where SIM reconstrcuted multipositions files open like static noise.&nbsp;

[https://zenodo.org/records/14893791](https://zenodo.org/records/14893791)

[https://doi.org/10.5281/zenodo.14893791](https://doi.org/10.5281/zenodo.14893791)


---

## Training Computational Skills in the Age of AI

Robert Haase

Published 2024-11-06

Licensed CC-BY-4.0



Artificial intelligence (AI) and large language models (LLMs) are changing the way we use computers in science. This slide deck introduces ways for using AI and LLMs for making training materials and for exchanging knowledge about how to use AI in joint discussions between humans and LLM-based AI-systems.

[https://zenodo.org/records/14043615](https://zenodo.org/records/14043615)

[https://doi.org/10.5281/zenodo.14043615](https://doi.org/10.5281/zenodo.14043615)


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

## datenbiene

Torsten Stöter

Published 2025-02-02T18:50:20+00:00

Licensed GNU GENERAL PUBLIC LICENSE V3.0





Tags: Research Data Management

Content type: Github Repository, Software

[https://github.com/tstoeter/datenbiene](https://github.com/tstoeter/datenbiene)


---

## omero-arc

Christoph Moehl, Peter Zentis, Niraj Kandpal

Published 2023-12-18T16:11:04+00:00

Licensed GNU GENERAL PUBLIC LICENSE V3.0



Library to export OMERO projects to ARC repositories

Tags: OMERO, Research Data Management

Content type: Github Repository, Software

[https://github.com/cmohl2013/omero-arc](https://github.com/cmohl2013/omero-arc)


---

