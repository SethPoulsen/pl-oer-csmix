def generate(data):

    names_for_user = [ 
        {"name": "file_path", "type": "string", "description": "the path of file"},
        {"name": "name", "type": "string", "description": "the name you should add to the file"},
    ]
    names_from_user = [ 

    ]
    
    import numpy as np
    code = np.random.randint(0,2)  
    if code == 0:
        mode = "write"
    else:
        mode = "append"
    data["params"]['method'] = mode
    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user
    
    return data