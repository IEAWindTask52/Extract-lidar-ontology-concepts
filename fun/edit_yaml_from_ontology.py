def edit_yaml_from_ontology(file_name,Lidar_Dictionary,nestedfields,fields2change):
    import ruamel.yaml
    str_nestedfields = 'config'
    for inf0 in range (len(nestedfields)):   
        str_nestedfields+='{}'.format(nestedfields[inf0])


    # Use the package ruamel to edit the yaml file    
    config, ind, bsi = ruamel.yaml.util.load_yaml_guess_indent(open(file_name))
    # Dictionary level where fields we want to change are located
    instances        = eval(str_nestedfields)    
    for inf1 in range (len(fields2change)):   
        str_fields2change='{}'.format(fields2change[inf1])    
        
    
        #Fields we want to change to the new values extracted from the ontology  
        instances[str_fields2change]      = Lidar_Dictionary[str_fields2change]
        #pdb.set_trace()
        #instances['Preferred Label']   = Lidar_Dictionary['Preferred Label']
        #instances['Alternative Label'] = Lidar_Dictionary['Alternative Label']

        yaml = ruamel.yaml.YAML()
        yaml.indent(mapping=ind, sequence=ind, offset=bsi) 

        with open(file_name, 'w') as fp:
            yaml.dump(config, fp)