def edit_yaml_from_ontology(file_name):
    import ruamel
    # Use the package ruamel to edit the yaml file
    pdb.set_trace()
    config, ind, bsi = ruamel.yaml.util.load_yaml_guess_indent(open(file_name))
    pdb.set_trace()
    instances        = config['Components']['Scanner module']['Azimuth angle']    
    pdb.set_trace()
    instances['Definition']        = Lidar_Dictionary['Definition']
    pdb.set_trace()
    instances['Preferred Label']   = Lidar_Dictionary['Preferred Label']
    instances['Alternative Label'] = Lidar_Dictionary['Alternative Label']
    pdb.set_trace()
    yaml = ruamel.yaml.YAML()
    yaml.indent(mapping=ind, sequence=ind, offset=bsi) 
    pdb.set_trace()
    with open(file_name, 'w') as fp:
        yaml.dump(config, fp)
    
