def find(obj,tag):  
""".   
Function digging into the local YAML file to find 
the fetched concept and the field(s) to be updated:      
    
Inputs
------- 
* obj:
    Each element contained in the local YAML file
* tag:
    Fields of the ontology concept to be updated  
Returns
-------
String    
"""
    if tag in obj:
        yield obj[tag]
    for k,v in obj.items():       
        if isinstance(v,dict):
            for i in find(v,tag):
                yield i                

def edit(local_yaml,tag,fields2change,Lidar_Dictionary):
""".   
Opens, updates, saves, and closes the local YAML file.    
    
Inputs
-------    
* local_yaml:
    Local YAML file to be updated
* tag:
    Concept to be updated   
* fields2change:
    Fields to be updated 
* Lidar_Dictionary:
    dict-like output object from the Github tool
Returns
-------
YAML file    
"""
    import ruamel.yaml
    yaml = ruamel.yaml.YAML()
    
    # Read and assign the desired fields of the downloaded concept     
    with open (local_yaml,"r") as file:
        data = yaml.load_all(file)
        for obj in data:
            for val in find(obj,tag):
                for i in fields2change:
                    if not val[i]:
                        val[i]=Lidar_Dictionary[i]
    
    # Edit the desired fields of the local file
    with open(local_yaml, "w") as file:
        yaml.dump(obj, file)
    
    
