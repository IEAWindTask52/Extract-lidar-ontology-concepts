def find(obj,tag,field):    
    pdb.set_trace()
    if tag in obj:
        yield obj[tag]
    for k,v in obj.items():       
        if isinstance(v,dict):
            for i in find(v,tag,field):
                yield i                
    
    # with open (Lidar_inputs,"r") as file:
    #     data = yaml.load_all(file)
    #     for obj in data:
    #         for val in find(obj,tag,field):
    #             for i in field:
    #                 val[i]=Lidar_Dictionary[i]
    
    # with open(Lidar_inputs, "w") as file:
    #     #pdb.set_trace()
    #     yaml.dump(obj, file)