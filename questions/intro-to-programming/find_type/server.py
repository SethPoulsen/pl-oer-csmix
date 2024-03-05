def generate(data):

    names_for_user = [ 
    ]
    names_from_user = [ 
    {"name": "find_type", "type": "function", "description": "function that will return the type of the input"}
    ]

    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user
    
    return data
