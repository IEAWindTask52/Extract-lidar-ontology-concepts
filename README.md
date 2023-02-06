# Extract lidar ontology concepts

## Project Description
### Introduction:

An ontology defines a common vocabulary within a domain, providing a means to share information in the domain, and includes machine-interpretable definitions of fundamental concepts and the relations among them. To tackle the problems related to data digitalization, recently some global initiatives focussed on developing standardization tools. A global initiative project e-WindLidar focused on development of wind lidar community based tools and data standards, and publish a lidar data form to make them FAIR, i.e. Findable, Accessible, Interoperable and Reusable \cite{ref-Vasiljevi}. IEA Task 52 (former Task 32) bringing together researchers and industry stakeholders to collaborate on the standardization, research and development, and knowledge exchange of wind lidar. 

Within the IEA Task 52, an open-source ontology has been developed with the aim of establishing an industry-wide consensus on wind lidar concepts and terminology. This repository provides an demo for accessing the developed ontology along with the source code. 

:link: The lidar ontology is available [here](https://data.windenergy.dtu.dk/ontologies/view/ontolidar/en/).


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
A dictionary for new entrants to wind energy. A new entrant can get detailed information about different lidar components and how they relate to each other.
A variable-definition reference for datasets for the OEMs delivering data to clients.
An input for lidar and wind modelling simulations.
 
## Related projects and concepts:

- [FAIR Data](https://www.go-fair.org/fair-principles/)
- [Open Science Handbook](https://github.com/MSCA-LIKE/OpenScienceTrainingCourse/blob/master/00_handbook/readme.md)
- [eWind Lidar](https://github.com/e-WindLidar)
- Ontology: "Formal machine-readable specification of a conceptual model in which concepts, properties, relationships, functions, constraints and axioms are all explicitly defined" [1]

## Methodology:
- [Google Sheets](https://docs.google.com/spreadsheets/d/1rC2bugsJzRpuINqbVKR7GO1xNHPvzUvrKEz-75MNdXY/edit#gid=1744776504): an excel sheet is used as input for the ontology. This format allows easy implementation and maintenance of the ontology
- [sheet2rdf](https://github.com/fair-data-collective/sheet2rdf): The data contained in the Google Sheet is transformed into a Resource Description Framework (RDF) format by using shee2rdf. RDF allows to digitise and handle knowledge organisation systems in a machine-readable format. 
- ontostack: a DTU Wind and Energy Systems instance of ontostack is used to serve the lidar ontology.

sheet2rdf and ontostack have been developed by [Fair Data Collective](https://www.linkedin.com/company/fair-data-collective/about/).

## Demo:
- Input
    - Standard input file: [yaml file](https://github.com/PacoCosta/Extract-lidar-ontology-concepts/blob/main/Ontology_yml.yml)
- Main Script:
    - Extract data from Ontology
- Background
    - functions getLabel / getConcept
- Output:
    - Current Parameters
    - Custom options
    - Future Parameters

## Outlook

- Link to existing wind-related ontologies or [digital data standards](https://github.com/IEA-Task-43/digital_wra_data_standard)
- Update and maintenance

## Important Links and references
[1] Patricia Harpring – Introduction to Controlled Vocabularies - ISBN-978-1-60606-026-1

## Contributions
Contributions are very welcome!
If you wish to:
- Colaborate: please contact the authors
- Report issues or enhance the code: post an [issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/quickstart)(ARE WE INCLUDING A TEMPLATE FOR ISSUES??) or make a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- Seek for support: please contact the authors

## License
This work is licensed under **[XXX](XXX)**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

## Citing and Contact
<div itemscope itemtype="https://schema.org/Person"><a itemprop="sameAs" content="https://orcid.org/0000-0003-1318-9677" href="https://orcid.org/0000-0003-1318-9677" target="orcid.widget" rel="me noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">Francisco Costa García</a></div>

<div itemscope itemtype="https://schema.org/Person"><a itemprop="sameAs" content="https://orcid.org/0000-0002-8397-7348" href="https://orcid.org/0000-0002-8397-7348" target="orcid.widget" rel="me noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">Ashim Giyanani</a></div>


# To Dos: 
1) Show images in jupyter notebook [##### 100%]
2) Write Readme.md as instruction [# 20% ]
3) update license
4) Find a host options github + binder / github + JupyterHub / github + ...
