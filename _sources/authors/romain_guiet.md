# Romain guiet (10)
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

## Highlights from the 2016-2020 NEUBIAS training schools for Bioimage Analysts: a success story and key asset for analysts and life scientists

Gabriel G. Martins, Fabrice P. Cordelières, Julien Colombelli, Rocco D’Antuono, Ofra Golani, Romain Guiet, Robert Haase, Anna H. Klemm, Marion Louveaux, Perrine Paul-Gilloteaux, Jean-Yves Tinevez, Kota Miura

Published 2021

Licensed CC-BY-4.0



Tags: Bioimage Analysis, Neubias

Content type: Publication

[https://f1000research.com/articles/10-334/v1](https://f1000research.com/articles/10-334/v1)


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

## Measuring reporter activity domain in EPI aggregates and Gastruloids.ijm

Romain Guiet, Olivier Burri, Mehmet Girgin, Matthias Lutolf

Published 2022-12-07

Licensed CC-BY-4.0



This imagej macro analyses the reporter intensity activity and expression domain in EPI aggregates and Gastruloids.

[https://zenodo.org/records/7409423](https://zenodo.org/records/7409423)

[https://doi.org/10.5281/zenodo.7409423](https://doi.org/10.5281/zenodo.7409423)


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

## Upcoming Image Analysis Events

Curtis Rueden, Albane de la Villegeorges, Simon F. Nørrelykke, Romain Guiet, Olivier Burri, et al.

Licensed UNKNOWN



Tags: Bioimage Analysis, Microscopy Image Analysis

Content type: Collection, Event, Forum Post, Workshop

[https://forum.image.sc/t/upcoming-image-analysis-events/60018/67](https://forum.image.sc/t/upcoming-image-analysis-events/60018/67)


---
