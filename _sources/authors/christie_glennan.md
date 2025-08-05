# Christie glennan (2)
## Gut Analysis Toolbox

Luke Sorensen, Ayame Saito, Sabrina Poon, Noe Han, Myat, Ryan Hamnett, Peter Neckel, Adam Humenick, Keith Mutunduwe, Christie Glennan, Narges Mahdavian, JH Brookes, Simon, M McQuade, Rachel, PP Foong, Jaime, Estibaliz Gómez-de-Mariscal, Muñoz Barrutia, Arrate, Kaltschmidt, Julia A., King, Sebastian K., Robert Haase, Simona Carbone, A. Veldhuis, Nicholas, P. Poole, Daniel, Pradeep Rajasekhar

Published 2025-07-24

Licensed BSD-3-CLAUSE




Reverted to StarDist for neuron segmentation. Used this bugfix for stardist plugin issue. protobuf-java-3.23.4.jar is being shipped as part of GAT update site.
Added StarDist models back and removed deepimageJ models for neuron segmentation
Updated documentation website to use a stable Fiji download: https://gut-analysis-toolbox.gitbook.io/docs#installation-and-configuration

Full Changelog: https://github.com/pr4deepr/GutAnalysisToolbox/compare/v1.0...v1.1

[https://zenodo.org/records/16396219](https://zenodo.org/records/16396219)

[https://doi.org/10.5281/zenodo.16396219](https://doi.org/10.5281/zenodo.16396219)


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

[https://zenodo.org/records/15314214](https://zenodo.org/records/15314214)

[https://doi.org/10.5281/zenodo.15314214](https://doi.org/10.5281/zenodo.15314214)


---

