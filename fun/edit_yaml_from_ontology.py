

def find(obj,tag):    
    if tag in obj:
        yield obj[tag]
    for k,v in obj.items():       
        if isinstance(v,dict):
            for i in find(v,tag):
                yield i                

def edit(local_yaml,tag,fields2change,Lidar_Dictionary):
    import ruamel.yaml
    yaml = ruamel.yaml.YAML()
    with open (local_yaml,"r") as file:
        data = yaml.load_all(file)
        for obj in data:
            for val in find(obj,tag):
                for i in fields2change:
                    val[i]=Lidar_Dictionary[i]
    
    # Edit the desired fields of the local file
    with open(local_yaml, "w") as file:
        yaml.dump(obj, file)
    
    