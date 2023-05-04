# def edit_yaml_from_ontology(file_name,Lidar_Dictionary,nestedfields,fields2change):
import yaml
import pdb
def find(doc, tag,docs):
    if tag in doc:
        yield doc[tag]
        # yaml.dump(doc[tag]['Definition'],docs)
        # yaml.dump('jamon jamon',doc)
        pdb.set_trace()
    for k, v in doc.items():
        if isinstance(v, dict):
            for i in find(v, tag,docs):
                pdb.set_trace()
                yield i
        
def edit_yaml_from_ontology(file_name,tag,fields2change):
    # import ruamel.yaml
    import yaml
    import pdb
    with open (file_name) as file: # WHere the yaml file is in order to get the input data
        Qlunc_yaml_inputs={}
        docs = yaml.load_all(file, Loader=yaml.FullLoader)
        pdb.set_trace()
        for doc in docs: 
            # pdb.set_trace()
        #     for k, v in doc.items():           
        #         Qlunc_yaml_inputs.setdefault(k,v)  # save a dictionary with the data coming from yaml file 
            # pdb.set_trace()
        # with open(file_name,'w') as file:
            tag='Azimuth angle'
            # pdb.set_trace()
            did=[]
            pdb.set_trace()
            for val in find(doc, tag,docs):
                did.append(val)
                yaml.dump('daf',file, default_flow_style=False)
    pdb.set_trace()
    return did
    
    # for ind_f2c in range(len(fields2change)):
    #     # pdb.set_trace()
    #     if fields2change[ind_f2c] in did[0].keys():
            
    #         list(did[0].values())[ind_f2c]='Ajuarez'
      
    
    
    
sd=edit_yaml_from_ontology(r'C:/SWE_LOCAL/Task32/Lidar_ontology/Example_coding_efficiency/LidarOntologyConceptsRepo/Extract-lidar-ontology-concepts/Ontology_yml.yml','Azimuth ',['Definition'])    

 
# import sys
# import ruamel.yaml

# yaml = ruamel.yaml.YAML()
# # yaml.preserve_quotes = True
# with open(r'C:/SWE_LOCAL/Task32/Lidar_ontology/Example_coding_efficiency/LidarOntologyConceptsRepo/Extract-lidar-ontology-concepts/Ontology_yml.yml') as fp:
#     data = yaml.load(fp)
# for elem in data:
#     pdb.set_trace()
#     if isinstance(elem, dict):
         
        
#         elem['Definition'] = 1234
#         break  # no need to iterate further
# yaml.dump(data, sys.stdout)
    
data = dict(
    A = 'a',
    B = dict(
        C = 'c',
        D = 'd',
        E = 'e',
    )
)

with open('C:/SWE_LOCAL/Task32/Lidar_ontology/Example_coding_efficiency/LidarOntologyConceptsRepo/Extract-lidar-ontology-concepts/Ontology_Concepts/data.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)

    
    
    

    # str_nestedfields = 'config'
    # for inf0 in range (len(nestedfields)):   
    #     str_nestedfields+='{}'.format(nestedfields[inf0])


    # # Use the package ruamel to edit the yaml file    
    # config, ind, bsi = ruamel.yaml.util.load_yaml_guess_indent(open(file_name))
    # # Dictionary level where fields we want to change are located
    # instances        = eval(str_nestedfields)    
    # for inf1 in range (len(fields2change)):   
    #     str_fields2change='{}'.format(fields2change[inf1])  # str_fields2change is the field   
        
    
    #     #Fields we want to change to the new values extracted from the ontology  
    #     instances[str_fields2change]      = Lidar_Dictionary[str_fields2change]


    # yaml = ruamel.yaml.YAML()
    # yaml.indent(mapping=ind, sequence=ind, offset=bsi) 

    # with open(file_name, 'w') as fp:
    #     yaml.dump(config, fp)