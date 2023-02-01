# Extract lidar ontology concepts

## Project Description
### Introduction:

An ontology defines a common vocabulary within a domain, providing a means to share information in the domain, and includes machine-interpretable definitions of fundamental concepts and the relations among them. To tackle the problems related to data digitalization, recently some global initiatives focussed on developing standardization tools. A global initiative project e-WindLidar focused on development of wind lidar community based tools and data standards, and publish a lidar data form to make them FAIR, i.e. Findable, Accessible, Interoperable and Reusable \cite{ref-Vasiljevi}. IEA Task 52 (former Task 32) bringing together researchers and industry stakeholders to collaborate on the standardization, research and development, and knowledge exchange of wind lidar. 

Within the IEA Task 52, an open-source ontology has been developed with the aim of establishing an industry-wide consensus on wind lidar concepts and terminology. This repository provides an demo for accessing the developed ontology along with the source code.

### Objectives
This repository provides access to an open-source ontology which has been developed with the aim of establishing an industry-wide consensus on wind lidar concepts and terminology.

### Goals
Agree upon common terminology and definitions for different wind energy applications, namely Ontology.
Describe and define different modules and their interaction related to lidar technology.
Develop tools to transfer knowledge, data and metadata between different users.
Simplify data inter-operability and accessibility.
Simplifying the process of creating input files for lidar simulations, etc.
Provide a demo application case related to wind energy

### Scope
The Ontology includes the lidar module design according to the OpenLidar Architecture, atmospheric parameters, data configuration, measurement principles, etc. The scope is limited to wind energy applications and to lidar technology. 

### For whom
The Ontology is meant as:
A dictionary for new entrants to wind energy.
A variable-definition reference for datasets for the OEMs delivering data to clients.
An input for lidar and wind modelling simulations.

    outlook
Related projects
Concepts:
    FAIR Data
    eWind Lidar
    Ontology
Methodology:
    Google sheet
    sheet2rdf
    ontostack
Demo:
    Input
        Standard input file yaml file
    Main Script:
        Extract data from Ontology
    Background
        functions getLabel / getConcept
    Output:
        Current Parameters
        Custom options
        Future Parameters
Important Links:
License:
Contributions:
Issue:
# To Dos: 
1) Show images in jupyter notebook [##### 100%]
2) Write Readme.md as instruction [# 20% ]
3) update license
4) Find a host options github + binder / github + JupyterHub / github + ...
