# Recently added (10)
## CellBinDB: A Large-Scale Multimodal Annotated Dataset

Can Shi, Jinghong Fan, Zhonghan Deng, Huanlin Liu, Qiang Kang, Yumei Li, Jing Guo, Jingwen Wang, Jinjiang Gong, Sha Liao, Ao Chen, Ying Zhang, Mei Li

Published 2024-11-20

Licensed CC-ZERO



CellBinDB is a large-scale, multimodal annotated dataset for cell segmentation. It contains 1,044 annotated microscope images and 109,083 cell annotations, covering four staining types: DAPI, ssDNA, H&amp;E, and mIF. CellBinDB contains samples from two species, human and mouse, covering more than 30 histologically different tissue types, including disease-related tissues. The images in CellBinDB come from two sources: 844 mouse images from internal experiments and 200 human images from the open access platform 10x Genomics. We annotated all images in CellBinDB and provide two types of image annotations: semantic and instance masks. A xlsx file is attached to record the detailed information of each image.
In addition, we provide the images and annotations of nine other widely used publicly available cell segmentation datasets downloaded from their original sources, retaining their original formats for ease of use.&nbsp;
The file 'mixed_licenses.txt' contains the original accessions of the public datasets used in our project and their associated licenses. Please refer to these links for more information about each dataset and its licensing terms, and use it according to the specifications.

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/15370205](https://zenodo.org/records/15370205)

[https://doi.org/10.5281/zenodo.15370205](https://doi.org/10.5281/zenodo.15370205)


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

Tags: Ai-Ready

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

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/12656468](https://zenodo.org/records/12656468)

[https://doi.org/10.5281/zenodo.12656468](https://doi.org/10.5281/zenodo.12656468)


---

## Deep learning training data (JOVE)

Jessica Heebner, Carson Purnell, Ryan Hylton, Mike Marsh, Michael Grillo, Matt Swulius

Published 2022-11-18

Licensed CC-ZERO



Cryo-electron tomography (cryo-ET) allows researchers to image cells in their native, hydrated state at the highest resolution currently possible. However, the technique has several limitations that make analyzing the data it generates time-intensive and difficult. Hand-segmenting a single tomogram can take hours to days of human effort, but the microscope can easily generate 50 or more tomograms a day. Current deep learning segmentation programs for cryo-ET do exist but are limited to segmenting one structure at a time. Here multi-slice U-Net convolutional neural networks are trained and applied to automatically segment multiple structures simultaneously within cryo-tomograms. With proper preprocessing, these networks can be robustly inferred to many tomograms without the need for training individual networks for each tomogram. This workflow dramatically improves the speed with which cryo-electron tomograms can be analyzed by cutting segmentation time down to under 30 min in most cases. Further, segmentations can be used to improve the accuracy of filament tracing within a cellular context and to rapidly extract coordinates for subtomogram averaging.

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/7335439](https://zenodo.org/records/7335439)

[https://doi.org/10.5061/dryad.rxwdbrvct](https://doi.org/10.5061/dryad.rxwdbrvct)


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

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/5979761](https://zenodo.org/records/5979761)

[https://doi.org/10.5281/zenodo.5979761](https://doi.org/10.5281/zenodo.5979761)


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

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/8065174](https://zenodo.org/records/8065174)

[https://doi.org/10.5281/zenodo.8065174](https://doi.org/10.5281/zenodo.8065174)


---

## Melanoma Histopathology Dataset with Tissue and Nuclei Annotations

Mark Schuiveling

Published 2025-03-19

Licensed CC-ZERO



Description:
This dataset is designed for development of deep learning models for segmentation of nuclei and tissue in melanoma H&amp;E stained histopathology. Existing nuclei segmentation models that are trained on non-melanoma specific datasets have low performance due to the ability of melanocytes to mimic other cell types, whereas existing melanoma specific models utilize older, sub-optimal techniques. Moreover, these models do not provide tissue annotations necessary for determining the localization of tumor-infiltrating lymphocytes, which may hold value for predictive and prognostic tasks. To address this, we created a melanoma specific dataset with nuclei and tissue annotations.&nbsp;
Methodology:
Sample Collection:
Regions of interest (ROIs) were sampled from H&amp;E stained slides of 103 primary melanoma specimens and 102 metastatic melanoma specimens, scanned using a Hamamatsu scanner at 40&times; magnification (0.23 &mu;m per pixel). All slides were obtained from regular diagnostic procedures.From each specimen, a 40&times; magnified ROI of 1024&times;1024 pixels was selected for annotation. Additionally, a context ROI of 5120&times;5120 pixels was sampled to provide information about the broader context for the annotation process. Selection was performed by a trained medical expert (M.S.) and subsequently verified by a dermatopathologist (W.B.). Manual ROI selection ensured the inclusion of diverse tissue and nuclei types.
Annotation Process:

Nuclei segmentationNuclei segmentations were generated using Hover-Net pretrained on the PanNuke dataset. Manual annotation adjustments were performed by author M.S. using QuPath, with the following nuclei categories: tumor, stroma, vascular endothelium, histiocyte, melanophage, lymphocyte, plasma cell, neutrophil, apoptotic cell, and epithelium. All annotations were reviewed and corrected, where needed, by a dermatopathologist (W.B.).
Tissue segmentationTissue segmentations were created manually using QuPath by M.S., with the following categories: tumor, stroma, epidermis, necrosis, blood vessel, and background. Annotations were reviewed and corrected, where needed, by a dermatopathologist (W.B.).

Quality Control: To assess the reliability of the annotations, intra- and interobserver agreement (by pathologist G.B.) were determined on 12 randomly selected ROIs.

Nuclei segmentationThe intraobserver overall precision was 84.89%, with a recall of 86.45%, and an F1 score of 85.66%. Interobserver overall precision was 80.34%, with a recall of 80.62%, and an F1 score of 80.20%. These results are based on the sum of all true positive, false positive, and false negative counts for the 12 ROIs.
Tissue segmentationThe DICE score was determined on the same 12 randomly selected ROIs. The average intraobserver DICE score was 0.90, and the interobserver DICE score was also 0.90.

&nbsp;
Version 3:Removed sample "training_set_metastatic_roi_103" due to inconsistencies in annotation file.
Version 4:Sample training_set_metastatic_roi_088 missed one color annotation for a nuclei_apoptosis in the geojson file rendering it qupath uncompatible. This is fixed in the new version.&nbsp;
Version 5:Addition of correct sample of training_set_metastatic_roi_103" after deadline of panoptic segmentation of nuclei and tissue in advanced melanoma challenge test phase.&nbsp;

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/15050523](https://zenodo.org/records/15050523)

[https://doi.org/10.5281/zenodo.15050523](https://doi.org/10.5281/zenodo.15050523)


---

## NeurIPS 2022 Cell Segmentation Competition Dataset

Jun Ma, Ronald Xie, Shamini Ayyadhury, Cheng Ge, Anubha Gupta, Ritu Gupta, Song Gu, Yao Zhang, Gihun Lee, Joonkee Kim, Wei Lou, Haofeng Li, Eric Upschulte, Timo Dickscheid, de Almeida, José Guilherme, Yixin Wang, Lin Han, Xin Yang, Marco Labagnara, Vojislav Gligorovski, Maxime Scheder, Rahi, Sahand Jamal, Carly Kempster, Alice Pollitt, Leon Espinosa, Tam Mignot, Middeke, Jan Moritz, Jan-Niklas Eckardt, Wangkai Li, Zhaoyang Li, Xiaochen Cai, Bizhe Bai, Greenwald, Noah F., Van Valen, David, Erin Weisbart, Cimini, Beth A, Trevor Cheung, Oscar Brück, Bader, Gary D., Bo Wang

Published 2024-02-27

Licensed CC-BY-NC-ND-4.0



The official data set for the NeurIPS 2022 competition: cell segmentation in multi-modality microscopy images.
https://neurips22-cellseg.grand-challenge.org/
Please cite the following paper if this dataset is used in your research.&nbsp;
&nbsp;
@article{NeurIPS-CellSeg,
      title = {The Multi-modality Cell Segmentation Challenge: Towards Universal Solutions},
      author = {Jun Ma and Ronald Xie and Shamini Ayyadhury and Cheng Ge and Anubha Gupta and Ritu Gupta and Song Gu and Yao Zhang and Gihun Lee and Joonkee Kim and Wei Lou and Haofeng Li and Eric Upschulte and Timo Dickscheid and Jos&eacute; Guilherme de Almeida and Yixin Wang and Lin Han and Xin Yang and Marco Labagnara and Vojislav Gligorovski and Maxime Scheder and Sahand Jamal Rahi and Carly Kempster and Alice Pollitt and Leon Espinosa and T&acirc;m Mignot and Jan Moritz Middeke and Jan-Niklas Eckardt and Wangkai Li and Zhaoyang Li and Xiaochen Cai and Bizhe Bai and Noah F. Greenwald and David Van Valen and Erin Weisbart and Beth A. Cimini and Trevor Cheung and Oscar Br&uuml;ck and Gary D. Bader and Bo Wang},
      journal = {Nature Methods}, &nbsp; &nbsp; &nbsp;volume={21},      pages={1103&ndash;1113},      year = {2024},
      doi = {https://doi.org/10.1038/s41592-024-02233-6}
  }
&nbsp;
This is an instance segmentation task where each cell has an individual label under the same category (cells). The training set contains both labeled images and unlabeled images. You can only use the labeled images to develop your model but we encourage participants to try to explore the unlabeled images through weakly supervised learning, semi-supervised learning, and self-supervised learning.
&nbsp;
The images are provided with original formats, including tiff, tif, png, jpg, bmp... The original formats contain the most amount of information for competitors and you have free choice over different normalization methods. For the ground truth, we standardize them as tiff formats.
&nbsp;
We aim to maintain this challenge as a sustainable benchmark platform. If you find the top algorithms (https://neurips22-cellseg.grand-challenge.org/awards/) don't perform well on your images, welcome to send us the dataset (neurips.cellseg@gmail.com)! We will include them in the new testing set and credit your contributions on the challenge website!
&nbsp;
Dataset License: CC-BY-NC-ND

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/10719375](https://zenodo.org/records/10719375)

[https://doi.org/10.5281/zenodo.10719375](https://doi.org/10.5281/zenodo.10719375)


---

## OCELOT: Overlapped Cell on Tissue Dataset for Histopathology

Jeongun Ryu, Aaron Valero Puche, JaeWoong Shin, Seonwook Park, Biagio Brattoli, Mohammad Mostafavi, Jinhee Lee, Sérgio Pereira, Wonkyung Jung, Soo Ick Cho, Chan-Young Ock, Kyunghyun Paeng, Donggeun Yoo

Published 2023-03-23



The OCELOT dataset is a histopathology dataset designed to facilitate the development of methods that utilize cell and tissue relationships. The dataset comprises both small and large field-of-view (FoV) patches extracted from digitally scanned whole slide images (WSIs), with overlapping regions. The small and large FoV patches are accompanied by annotations of cells and tissues, respectively. The WSIs are sourced from the publicly available TCGA database and were stained using the H&amp;E method before being scanned with an Aperio scanner.

For more details, please check&nbsp;https://lunit-io.github.io/research/ocelot_dataset/.

&nbsp;

Before downloading the dataset, please make sure to carefully read and agree to the Terms and Conditions at (https://lunit-io.github.io/research/ocelot_tc/).

Also, please provide 1. name, 2. e-mail address, 3. organization/company name.

&nbsp;

-----------------------------------------------------------------------------------

Release note.

In version 1.0.1, we exclude four test cases (586, 589, 609, 615) due to under-annotated issue.
In version 1.0.0, we include&nbsp;images and annotations of validation and test splits.
In version 0.1.2, we modified the coordinates of cell labels to range from 0 to 1023 (-1 from the previous coordinates).
In version 0.1.1, we removed non-H&amp;E stained patches from the dataset.

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/8417503](https://zenodo.org/records/8417503)

[https://doi.org/10.5281/zenodo.8417503](https://doi.org/10.5281/zenodo.8417503)


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

Tags: Ai-Ready

Content type: Data

[https://zenodo.org/records/8188948](https://zenodo.org/records/8188948)

[https://doi.org/10.5281/zenodo.8188948](https://doi.org/10.5281/zenodo.8188948)


---

