# Extract lidar ontology concepts
This repository is part of the article...

## Project Description

### Introduction:

An ontology defines a common vocabulary within a specific domain of knowledge, providing a means to share information in the domain, and includes machine-interpretable definitions of fundamental concepts and the relations among them. To tackle the problems related to data digitalization, recently some global initiatives focused on developing standardization tools. A global initiative project, [e-WindLidar](https://zenodo.org/record/2478051), focused on the development of wind lidar community based tools and data standards, and published a lidar data form to make them FAIR, i.e., Findable, Accessible, Interoperable, and Reusable. [IEA Wind Task 52](https://iea-wind.org/task52/) (former IEA Wind Task 32) brings together researchers and industry stakeholders to collaborate on the standardization, research and development, and knowledge exchange of wind lidar. 

Within the IEA Wind Task 52, an open-source ontology has been developed with the aim of establishing an industry-wide consensus on wind lidar concepts and terminology. This repository provides an demo for accessing the developed ontology along with the source code. 

:link: The IEA Wind Task 52 Wind Lidar Ontology is available [here](https://data.windenergy.dtu.dk/ontologies/view/ontolidar/en/).


### Objectives
This repository provides access to an open-source lidar ontology which has been developed with the aim of establishing an industry-wide consensus on wind lidar concepts and terminology. The repository contains guidance and a working example on how to use the ontology and extract information from it. 

### Goals
1. Agree upon common terminology and definitions for different wind energy applications, namely Ontology. This helps in avoiding ambiguity while promoting consistency and standardisation of lidar-related knowledge, models and methodologies.
2. Describe and define different modules and their interaction related to lidar technology.
3. Develop tools to transfer knowledge, data and metadata between different users. This fosters collaborations and information exchange. 
4. Simplify data inter-operability and accessibility.
5. Simplifying the process of creating input files for lidar simulations, the integration of new numerical models, etc.
6. Provide a demo application case related to wind energy

### Scope
The Ontology includes the lidar module design according to the OpenLidar Architecture, atmospheric parameters, data configuration, measurement principles, etc. The scope is limited to wind energy applications and to lidar technology. 

### For whom
The Ontology is meant as:
- A dictionary for new entrants to wind energy. A new entrant can get detailed information about different lidar components and how they relate to each other.
- A variable-definition reference for datasets for the OEMs delivering data to clients.
- An input for lidar and wind modelling simulations.
 
## Related projects and concepts:

- [FAIR Data](https://www.go-fair.org/fair-principles/)
- [Open Science Handbook](https://github.com/MSCA-LIKE/OpenScienceTrainingCourse/blob/master/00_handbook/readme.md)
- [eWind Lidar](https://github.com/e-WindLidar)
- Ontology: "Formal machine-readable specification of a conceptual model in which concepts, properties, relationships, functions, constraints and axioms are all explicitly defined" [1]

## Methodology:
The methodology followed is based on the tools developed by [Fair Data Collective](https://www.linkedin.com/company/fair-data-collective/about/). More information about the tools used to create, mantain and deploy the lidar ontology can be found in [[2]](#important-links-and-references)[[3]](#important-links-and-references)[[4]](#important-links-and-references)

- [GoogleSheets](https://docs.google.com/spreadsheets/d/1rC2bugsJzRpuINqbVKR7GO1xNHPvzUvrKEz-75MNdXY/edit#gid=1744776504): An excel sheet is used as input for the ontology. This format allows easy implementation and maintenance of the ontology.
- [sheet2rdf](https://github.com/fair-data-collective/sheet2rdf): The data contained in the Google Sheet is transformed into a Resource Description Framework (RDF) format by using sheet2rdf. RDF allows to digitise and handle knowledge organisation systems in a machine-readable format.
- [ontostack](https://github.com/fair-data-collective/sheet2rdf): a DTU Wind and Energy Systems instance of ontostack is used to serve the lidar ontology. 

## Demo:
- Input
    - Standard input file: [yaml file](https://github.com/PacoCosta/Extract-lidar-ontology-concepts/blob/main/Ontology_yml.yml)
- Main Script:
    - [Extract data from Ontology](https://github.com/PacoCosta/Extract-lidar-ontology-concepts/blob/main/Extract_Data_From_Ontology.ipynb)
- Background
    - functions [`getLabel`](https://github.com/PacoCosta/Extract-lidar-ontology-concepts/blob/main/fun/getLabel.py) / [`getConcept`](https://github.com/PacoCosta/Extract-lidar-ontology-concepts/blob/main/fun/getConcept.py) and [`edit_ymal_from_ontology`](https://github.com/PacoCosta/Extract-lidar-ontology-concepts/blob/main/fun/edit_yaml_from_ontology.py)
- Output:
    - Current Parameters
    - Custom options
    - Future Parameters
    - Updated lidar simulator input file

## Outlook

- Link to existing wind-related ontologies or [digital data standards](https://github.com/IEA-Task-43/digital_wra_data_standard)
- Updating and maintenance will be carried out at least once per year. In addition, the authors will address possible external contributions and add/edit the ontology accordingly if necessary.

## Important Links and references

[1] Patricia Harpring – Introduction to Controlled Vocabularies - ISBN-978-1-60606-026-1<br>
[2] https://github.com/DTUWindEnergy/NEAT-taxonomy<br>
[3] https://github.com/nikokaoja/sheet2rdf<br>
[4] https://github.com/IEA-Wind-Task-32/wind-lidar-ontology<br>

## Contributions
The Lidar Ontology will continue to incorporate new ideas/concepts and keep them up to date to be a practical tool for lidar community. Any suggestion or comment, particularly from lidar researchers, developers, manufacturer, users, etc. are very welcome!
If you wish to:

- [Add a new a concept to the IEA Wind Task 52 Wind Lidar Ontology](https://github.com/PacoCosta/Extract-lidar-ontology-concepts/issues/new?assignees=&labels=documentation&template=add-a-concept-to-the-iea-wind-task52-wind-lidar-ontology.md&title=)
- [Suggest an update in an existing concept of the IEA Wind Task52 Wind Lidar Ontology](https://github.com/PacoCosta/Extract-lidar-ontology-concepts/issues/new?assignees=&labels=documentation&template=suggest-an-update-in-an-existing-concept-of-the-iea-wind-task52-wind-lidar-ontology.md&title=)
- [Create a pull request](pull_request_template.md)
- Seek for support: please contact the authors
- Participate in IEA Wind Task52 

## License
This work is licensed under **[Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/legalcode)**

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

## Citing and Contact
<div itemscope itemtype="https://schema.org/Person"><a itemprop="sameAs" content="https://orcid.org/0000-0003-1318-9677" href="https://orcid.org/0000-0003-1318-9677" target="orcid.widget" rel="me noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">Francisco Costa García</a></div>

<div itemscope itemtype="https://schema.org/Person"><a itemprop="sameAs" content="https://orcid.org/0000-0002-8397-7348" href="https://orcid.org/0000-0002-8397-7348" target="orcid.widget" rel="me noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">Ashim Giyanani</a></div>
