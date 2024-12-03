# Recently added (10)
## Axioscan 7 fluorescent channels not displaying in QuPath

j

Published 2024-06-25



Hi&nbsp;@ome team,Please find the .czi file attached. When loaded into QuPath using BioFormats, the fluorescence channels populate the brightness/contrast panel but do not show up in the viewer. Re-exporting as OME.Tiff from Zen and loading into QuPath does not help either - the channels do not populate the brightness/contrast panel in this case, and it shows as a RGB image.Please let me know if any further info is needed from me to troubleshoot!
Best,J

[https://zenodo.org/records/12533989](https://zenodo.org/records/12533989)

[https://doi.org/10.5281/zenodo.12533989](https://doi.org/10.5281/zenodo.12533989)


---

## Engineering a Software Environment for Research Data Management of Microscopy Image Data in a Core Facility

Kunis

Published 2022-05-30



This thesis deals with concepts and solutions in the field of data management in everyday scientific life for image data from microscopy. The focus of the formulated requirements has so far been on published data, which represent only a small subset of the data generated in the scientific process. More and more, everyday research data are moving into the focus of the principles for the management of research data that were formulated early on (FAIR-principles). The adequate management of this mostly multimodal data is a real challenge in terms of its heterogeneity and scope. There is a lack of standardised and established workflows and also the software solutions available so far do not adequately reflect the special requirements of this area. However, the success of any data management process depends heavily on the degree of integration into the daily work routine. Data management must, as far as possible, fit seamlessly into this process. Microscopy data in the scientific process is embedded in pre-processing, which consists of preparatory laboratory work and the analytical evaluation of the microscopy data. In terms of volume, the image data often form the largest part of data generated within this entire research process. In this paper, we focus on concepts and techniques related to the handling and description of this image data and address the necessary basics. The aim is to improve the embedding of the existing data management solution for image data (OMERO) into the everyday scientific work. For this purpose, two independent software extensions for OMERO were implemented within the framework of this thesis: OpenLink and MDEmic. OpenLink simplifies the access to the data stored in the integrated repository in order to feed them into established workflows for further evaluations and enables not only the internal but also the external exchange of data without weakening the advantages of the data repository. The focus of the second implemented software solution, MDEmic, is on the capturing of relevant metadata for microscopy. Through the extended metadata collection, a corresponding linking of the multimodal data by means of a unique description and the corresponding semantic background is aimed at. The configurability of MDEmic is designed to address the currently very dynamic development of underlying concepts and formats. The main goal of MDEmic is to minimise the workload and to automate processes. This provides the scientist with a tool to handle this complex and extensive task of metadata acquisition for microscopic data in a simple way. With the help of the software, semantic and syntactic standardisation can take place without the scientist having to deal with the technical concepts. The generated metadata descriptions are automatically integrated into the image repository and, at the same time, can be transferred by the scientists into formats that are needed when publishing the data.

[https://zenodo.org/records/6905931](https://zenodo.org/records/6905931)

[https://doi.org/10.5281/zenodo.6905931](https://doi.org/10.5281/zenodo.6905931)


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

## LZ4-compressed Imaris ims example datasets.

Marco Stucchi

Published 2024-11-21

Licensed CC-BY-4.0



The files contained in this repository are cropped versions of Imaris demo images compressed with LZ4.

[https://zenodo.org/records/14197622](https://zenodo.org/records/14197622)

[https://doi.org/10.5281/zenodo.14197622](https://doi.org/10.5281/zenodo.14197622)


---

## OME2024 NGFF Challenge Results

Josh Moore

Published 2024-11-01

Licensed CC-BY-4.0



Presented at the 2024 FoundingGIDE event in Okazaki, Japan: https://founding-gide.eurobioimaging.eu/event/foundinggide-community-event-2024/
Note: much of the presentation was a demonstration of the OME2024-NGFF-Challenge -- https://ome.github.io/ome2024-ngff-challenge/ especially of querying an extraction of the metadata (https://github.com/ome/ome2024-ngff-challenge-metadata)
&nbsp;

[https://zenodo.org/records/14234608](https://zenodo.org/records/14234608)

[https://doi.org/10.5281/zenodo.14234608](https://doi.org/10.5281/zenodo.14234608)


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


[https://zenodo.org/records/7018750](https://zenodo.org/records/7018750)

[https://doi.org/10.5281/zenodo.7018750](https://doi.org/10.5281/zenodo.7018750)


---

