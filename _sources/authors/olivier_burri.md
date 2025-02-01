# Olivier burri (6)
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

## Neubias Academy 2020: Introduction to Nuclei Segmentation with StarDist

Martin Weigert, Olivier Burri, Siân Culley, Uwe Schmidt

Licensed UNKNOWN



Tags: Python, Neubias, Artificial Intelligence, Bioimage Analysis

Content type: Slides, Notebook

[https://github.com/maweigert/neubias_academy_stardist](https://github.com/maweigert/neubias_academy_stardist)


---

## Upcoming Image Analysis Events

Curtis Rueden, Albane de la Villegeorges, Simon F. Nørrelykke, Romain Guiet, Olivier Burri, et al.

Licensed UNKNOWN



Tags: Bioimage Analysis

Content type: Collection, Event, Forum Post, Workshop

[https://forum.image.sc/t/upcoming-image-analysis-events/60018/67](https://forum.image.sc/t/upcoming-image-analysis-events/60018/67)


---

