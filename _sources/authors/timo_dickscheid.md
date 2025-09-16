# Timo dickscheid (4)
## A Perspective on FAIR and Scalable Access to Large Image Data

Julia Thönnißen, Sarah Oliveira, Alexander Oberstrass, Jan-Oliver Kropp, Xiao Gui, Christian Schiffer, Timo Dickscheid

Published 2025-08-04

Licensed CC-BY-4.0



The rapid development of new imaging technologies across scientific domains–especially high-throughput technologies–results in a growing volume of image datasets in the Tera- to Petabyte scale. Efficient visualization and analysis of such massive image resources is critical but remains challenging due to the sheer size of the data, its continuous growth, and the limitations of conventional software tools to address these problems. Tools for visualization, annotation and analysis of large image data are confronted with the fundamental dilemma of balancing computational efficiency and memory requirements. Many tools are unable to process large datasets due to memory constraints, requiring workarounds like downsampling. On the other hand, solutions that can handle large data efficiently often rely on specialized or even proprietary file formats, limiting interoperability with other software. This reflects diverging requirements: storage favours compression for efficiency, analysis demands fast data access, and visualization requires tiled, multi-resolution representations. Lacking a unified approach for these conflicting needs, the operation of large and dynamically evolving image repositories in practice often requires undesirable data conversions and costly data duplication. In addressing these challenges, the bioimaging community increasingly adheres to the FAIR principles [1] through national and international initiatives [2], [3], [4]. For example, the Open Microscopy Environment (OME) fosters standards such as OME-TIFF [5] and its cloud-native successor OME-NGFF [6]; BioFormats [7] and OMERO [8] facilitate metadata-rich data handling across diverse platforms; and BrAinPI [9] provides web-based visualization of images via Neuroglancer [10]. These tools represent important developments towards more efficient and standardized use of bioimaging data. However, for very large and dynamically growing repositories, it is still not feasible to settle on a single standard for a subset of these tools, in particular in the light of very diverging needs for massively parallel processing on HPC systems. Therefore, converting data to a single target format is often not a practical solution. We propose a concept for a modular image delivery service which acts as a middleware between large image data resources and applications, serving image data from a cloud resource in multiple requested representations on demand. The service allows reading data stored in different input file formats, applying coordinate transformations and filtering operations on-the-fly, and serving the results in a range of different output formats and layouts. Building upon a common framework for reading and transforming data, an extensible set of access points connects the service to client applications: Lightweight REST APIs allow web-based mutli-resolution access (e.g., in common formats such as used in Neuroglancer and OpenSeadragon base viewers); mountable filesystem interfaces enable linking the repository to file-oriented solutions (e.g., OMERO, ImageJ); and programmatic access from customizable software tools (e.g., Napari). To provide compatibility with upcoming image data standards like BIDS [11] and minimize conversion efforts, the service is able to dynamically expose standard-conform views into arbitrarily organized datasets. The proposed approach for reading and transforming data on-the-fly eliminates the need for redundant storage and application-specific conversions of datasets, improving workflow efficiency and sustainability. In summary, we advocate for the development of a flexible and extensible image data service that supports large-scale analysis, dynamic transformations, multi-tool interoperability, and compatibility with community standards for large image datasets. This way it supports the FAIR principles, reduces integration barriers, meets the performance demands of modern imaging research, and still fosters the use of existing community developments.

[https://zenodo.org/records/16736220](https://zenodo.org/records/16736220)

[https://doi.org/10.5281/zenodo.16736220](https://doi.org/10.5281/zenodo.16736220)


---

## Combining the BIDS and ARC Directory Structures for Multimodal Research Data Organization

Torsten Stöter, Tobias Gottschall, Andrea Schrager, Peter Zentis, Monica Valencia-Schneider, Niraj Kandpal, Werner Zuschratter, Astrid Schauss, Timo Dickscheid, Timo Mühlhaus, Dirk von Suchodoletz

Published 2023-09-12

Licensed CC-BY-4.0



Interdisciplinary collaboration and integration of large and diverse datasets are becoming increasingly important. Answering complex research questions requires combining and analysing multimodal datasets. Research data management follows the FAIR principles making data findable, accessible, interoperable, and reusable. However, there are challenges in capturing the entire research cycle and contextualizing data according, not only for the DataPLANT and NFDI4BIOIMAGE communities. To address these challenges, DataPLANT developed a data structure called Annotated Research Context (ARC). The Brain Imaging Data Structure (BIDS) originated from the neuroimaging community extended for microscopic image data. Both concepts provide standardised and file system based data storage structures for organising and sharing research data accompanied with metadata. We exemplarily compare the ARC and BIDS designs and propose structural and metadata mapping.

Tags: Research Data Management

Content type: Poster

[https://zenodo.org/records/8349563](https://zenodo.org/records/8349563)


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

## The role of Helmholtz Centers in NFDI4BIOIMAGE - A national consortium enhancing FAIR data management for microscopy and bioimage analysis

Riccardo Massei, Christian Schmidt, Michele Bortolomeazzi, Julia Thoennissen, Jan Bumberger, Timo Dickscheid, Jan-Philipp Mallm, Elisa Ferrando-May

Published 2024-06-06

Licensed CC-BY-4.0



Germany&rsquo;s National Research Data Infrastructure (NFDI) aims to establish a sustained, cross-disciplinary research data management (RDM) infrastructure that enables researchers to handle FAIR (findable, accessible, interoperable, reusable) data. While&nbsp;FAIR principles have been&nbsp;adopted by funders, policymakers, and publishers, their practical implementation remains an ongoing effort. In the field of bio-imaging, harmonization of&nbsp;data formats, metadata ontologies, and open data repositories is necessary&nbsp;to achieve FAIR data.&nbsp;The NFDI4BIOIMAGE was established&nbsp;to address these issues and&nbsp;develop tools and best practices to facilitate FAIR microscopy and image analysis data in alignment with international community activities. The&nbsp;consortium operates through its Data Stewards team to provide expertise and direct support to help overcome RDM challenges. The three Helmholtz Centers in NFDI4BIOIMAGE aim to collaborate closely with other centers and initiatives, such as HMC, Helmholtz AI, and HIP. Here we present NFDI4BIOIMAGE&rsquo;s work and its significance for research in Helmholtz and beyond

Tags: Nfdi4Bioimage, Research Data Management

[https://zenodo.org/records/11501662](https://zenodo.org/records/11501662)

[https://doi.org/10.5281/zenodo.11501662](https://doi.org/10.5281/zenodo.11501662)


---

