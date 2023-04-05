def edit_yaml_from_ontology(file_name,Lidar_Dictionary,fields_edit_yaml):
    # Use the package ruamel to edit the yaml file    
    config, ind, bsi = ruamel.yaml.util.load_yaml_guess_indent(open(file_name))
    # Dictionary level where fields we want to change are located
    instances        = eval(fields_edit_yaml)    
    
    #Fields we want to change to the new values extracted from the ontology  
    instances['Definition']        = Lidar_Dictionary['Definition']   
    instances['Preferred Label']   = Lidar_Dictionary['Preferred Label']
    instances['Alternative Label'] = Lidar_Dictionary['Alternative Label']
    
    yaml = ruamel.yaml.YAML()
    yaml.indent(mapping=ind, sequence=ind, offset=bsi) 
    
    with open(file_name, 'w') as fp:
        yaml.dump(config, fp)
    
