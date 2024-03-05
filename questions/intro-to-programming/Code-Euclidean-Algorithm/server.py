import prairielearn as pl

def generate(data):
    names_for_user = [
    ]
    names_from_user = [
        {"name": "gcd", "description": "function that calculates the gcd for two integers using the Euclidean Algorithm", 
        "type": "python function"}
    ]

    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user
    return data
