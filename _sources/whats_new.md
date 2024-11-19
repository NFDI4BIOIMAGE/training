# Recently added (10)
## Axioscan 7 fluorescent channels not displaying in QuPath

j

Published 2024-06-25



Hi&nbsp;@ome team,Please find the .czi file attached. When loaded into QuPath using BioFormats, the fluorescence channels populate the brightness/contrast panel but do not show up in the viewer. Re-exporting as OME.Tiff from Zen and loading into QuPath does not help either - the channels do not populate the brightness/contrast panel in this case, and it shows as a RGB image.Please let me know if any further info is needed from me to troubleshoot!
Best,J

[https://zenodo.org/records/12533989](https://zenodo.org/records/12533989)

[https://doi.org/10.5281/zenodo.12533989](https://doi.org/10.5281/zenodo.12533989)


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

## High throughput & automated data analysis and data management workflow with Cellprofiler and OMERO

Sarah Weischer, Jens Wendt, Thomas Zobel

Published 2023-07-12

Licensed CC-BY-4.0



In this workshop a fully integrated data analysis solutions employing OMERO and commonly applied image analysis tools (e.g., CellProfiler, Fiji) using existing python interfaces (OMERO Python language bindings, ezOmero, Cellprofiler Python API) is presented.

[https://zenodo.org/records/8139354](https://zenodo.org/records/8139354)

[https://doi.org/10.5281/zenodo.8139354](https://doi.org/10.5281/zenodo.8139354)


---

## Human DAB staining Axioscan BF 20x

Mario Garcia

Published 2024-05-21

Licensed CC-BY-4.0



Human brain tissue with DAB immunostaining. Image acquired by BF microscopy in&nbsp; Zeiss Axioscan at 20x.&nbsp;

[https://zenodo.org/records/11234863](https://zenodo.org/records/11234863)

[https://doi.org/10.5281/zenodo.11234863](https://doi.org/10.5281/zenodo.11234863)


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

## Ink in a dish

Cavanagh

Published 2024-09-03

Licensed CC-ZERO



A test data set for troublshooting. no scientific meaning.

[https://zenodo.org/records/13642395](https://zenodo.org/records/13642395)

[https://doi.org/10.5281/zenodo.13642395](https://doi.org/10.5281/zenodo.13642395)


---

## LauLauThom/MaskFromRois-Fiji: Masks from ROIs plugins for Fiji - initial release

Laurent Thomas, Pierre Trehin

Published 2021-07-22

Licensed MIT



Fiji plugins for the creation of binary and semantic masks from ROIs in the RoiManager. Works with stacks too.

Installation in Fiji: activate the Rois from masks update site in Fiji.

See GitHub readme for the documentation.

Latest tested with Fiji 2.1.0/ImageJ 1.53j

[https://zenodo.org/records/5121890](https://zenodo.org/records/5121890)

[https://doi.org/10.5281/zenodo.5121890](https://doi.org/10.5281/zenodo.5121890)


---

