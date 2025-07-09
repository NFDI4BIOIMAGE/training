# Constantin pape (10)
## Collection of teaching material for deep learning for (biomedical) image analysis

Constantin Pape

Licensed MIT



Tags: Artificial Intelligence, Bioimage Analysis

[https://github.com/constantinpape/dl-teaching-resources](https://github.com/constantinpape/dl-teaching-resources)


---

## DL@MBL 2021 Exercises

Jan Funke, Constantin Pape, Morgan Schwartz, Xiaoyan

Licensed UNKNOWN



Tags: Artificial Intelligence, Bioimage Analysis

Content type: Slides, Notebook

[https://github.com/JLrumberger/DL-MBL-2021](https://github.com/JLrumberger/DL-MBL-2021)


---

## EMBL Deep Learning course 2021/22 exercises and materials

Martin Weigert, Constantin Pape

Licensed UNKNOWN



Tags: Python, Artificial Intelligence

Content type: Notebook

[https://github.com/kreshuklab/teaching-dl-course-2022](https://github.com/kreshuklab/teaching-dl-course-2022)


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

## OME-NGFF: a next-generation file format for expanding bioimaging data-access strategies

Josh Moore, Chris Allan, Sébastien Besson, jean-marie burel, Erin Diel, David Gault, Kevin Kozlowski, Dominik Lindner, Melissa Linkert, Trevor Manz, Will Moore, Constantin Pape, Christian Tischer, Jason R. Swedlow

Licensed CC-BY-4.0



Tags: Nfdi4Bioimage, Research Data Management

Content type: Publication

[https://www.nature.com/articles/s41592-021-01326-w](https://www.nature.com/articles/s41592-021-01326-w)


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

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/3675220](https://zenodo.org/records/3675220)

[https://doi.org/10.5281/zenodo.3675220](https://doi.org/10.5281/zenodo.3675220)


---

## SynapseNet Training Data

Constantin Pape

Published 2024-12-01

Licensed CC-BY-4.0



This dataset contains room-temperature single-axis TEM tomograms from Schaffer collateral and mossy fiber synapses in organotypic hippocampal slices.&nbsp;The tomograms were published in the two studies [1, 2]. The data was re-used for training deep neural networks to segment different synaptic structures in electron micrographs in [3].&nbsp;For the tomograms, organotypic slices were prepared from the hippocampi of neonatal mice according to the interface protocol55 and vitrified after 28 days in vitro in culture medium supplemented with 20% (w/v) bovine serum albumin using an HPM100 (Leica) high-pressure freezing device. The dataset also contains 23 tomograms resulting from chemically-fixed material, which were also published in (Maus et al., 2020). For these tomograms, wild-type animals at postnatal day 28 were transcardially perfused under deep anesthesia, first with 0.9% sodium chloride solution, and then one of two fixatives (Fixative 1: Ice-cold 4% paraformaldehyde, 2.5% glutaraldehyde in 0.1 M phosphate buffer16; Fixative 2: 37&deg; C 2% paraformaldehyde, 2.5% glutaraldehyde, 2 mM CaCl2, in 0.1 M cacodylate buffer56). Brains were rinsed and sectioned coronally through the dorsal hippocampus in an ice-cold 0.1 M phosphate buffer using a VT 1200S vibratome (Leica) (step size 100 &micro;m; amplitude 1.5 mm, speed 0.1 mm/sec). Hippocampal CA3 subregions were excised using a 1.5 mm diameter biopsy punch and high-pressure frozen on the same day in 20% (w/v) bovine serum albumin using an HPM100 (Leica) high-pressure freezing device. For both sample preparations, automated freeze-substitution was performed. Tomograms were collected using a 200 kV JEM-2100 (JEOL) transmission electron microscope equipped with an 11 MP Orius SC1000 CCD camera (Gatan). Tilt-series (tilt range +/- 60&deg;; 1&deg; angular increments) were acquired at 30 000x magnification using SerialEM58. Tomographic reconstructions were generated using weighted back-projection with etomo.The data is organized into two different subfolders for data with annotations for "vesicles" and "active_zones". Each of these subfolders is further subdivided into "train" and "test" folders, which containtomograms for the two different sample preparations in "chemical_fixation" and "single_axis_tem".Each tomogram and the corresponding annotation is stored as a hdf5 file, containing the following internal datasets:- raw: The tomogram data.- labels/vesicles: Annotations for the synaptic vesicles, annotated with IMOD, further postprocessed and then exported to instance masks. (for tomograms in "vesicles")- labels/AZ: Annotations for the active zone, annotated with IMOD and exported to binary masks.
[1] Imig et al., The Morphological and Molecular Nature of Synaptic Vesicle Priming at Presynaptic Active Zones, Neuron, 2014, DOI:10.1016/j.neuron.2014.10.009[2] Maus et al., Ultrastructural Correlates of Presynaptic Functional Heterogeneity in Hippocampal Synapses, Cell Reports, 2020, DOI: 10.1016/j.celrep.2020.02.083[3] Muth, Moschref et al., 2024, Preprint to be published

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/14330011](https://zenodo.org/records/14330011)

[https://doi.org/10.5281/zenodo.14330011](https://doi.org/10.5281/zenodo.14330011)


---

## Training Deep Learning Models for Vision - Compact Course

Constantin Pape, Adrian Wolny

Licensed UNKNOWN



Tags: Artificial Intelligence, Bioimage Analysis

[https://github.com/constantinpape/training-deep-learning-models-for-vison](https://github.com/constantinpape/training-deep-learning-models-for-vison)


---

## i2k-2020-s3-zarr-workshop

Constantin Pape, Christian Tischer

Licensed UNKNOWN



Tags: Python, Big Data

Content type: Github Repository

[https://github.com/tischi/i2k-2020-s3-zarr-workshop](https://github.com/tischi/i2k-2020-s3-zarr-workshop)


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

