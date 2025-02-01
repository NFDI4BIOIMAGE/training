# Silke tulok (6)
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

[https://zenodo.org/records/13807114](https://zenodo.org/records/13807114)

[https://doi.org/10.5281/zenodo.13807114](https://doi.org/10.5281/zenodo.13807114)


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

Tags: Nfdi4Bioimage, Research Data Management

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

Tags: Nfdi4Bioimage, Research Data Management

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

[https://zenodo.org/records/12547566](https://zenodo.org/records/12547566)

[https://doi.org/10.5281/zenodo.12547566](https://doi.org/10.5281/zenodo.12547566)


---

## Report on a pilot study:  Implementation of OMERO for  microscopy data management

Silke Tulok, Gunar Fabig, Andy Vogelsang, Thomas Kugel, Thomas Müller-Reichert

Published 2023-11-10

Licensed CC-BY-4.0



The Core Facility Cellular Imaging (CFCI) at the Faculty of Medicine Carl Gustav Carus (TU Dresden) is currently running a pilot project for testing the use and handling of the OMERO software. This is done together with interested users of the imaging facility and a research group. Currently, we are pushing forward this pilot study on a small scale without any data steward. Our experiences argue so far for giving data management issues into the hands of dedicated personnel not fully involved in research projects. As funding agencies will ask for higher and higher standards for implementing FAIRdata principles in the future, this will be a releva

[https://zenodo.org/records/10103316](https://zenodo.org/records/10103316)

[https://doi.org/10.5281/zenodo.10103316](https://doi.org/10.5281/zenodo.10103316)


---

