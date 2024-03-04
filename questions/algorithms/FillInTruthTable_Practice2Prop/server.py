import random

def generate(data):

    choices = [{"logical_expression": "$(P \\vee Q) \\wedge (P \\rightarrow (\\neg Q))$",
               "TT":"F", 
               "TF":"T",
               "FT":"T",
               "FF":"F",},
               
               {"logical_expression": "$(P \\vee Q \\vee (\\neg Q))$",
               "TT":"T", 
               "TF":"T",
               "FT":"T",
               "FF":"T",},

               {"logical_expression": "$\\neg (P \\leftrightarrow Q)$",
               "TT":"F", 
               "TF":"T",
               "FT":"T",
               "FF":"F",},

               {"logical_expression": "$((\\neg P) \\wedge Q) \\vee (P \\wedge (\\neg Q))$",
               "TT":"F", 
               "TF":"T",
               "FT":"T",
               "FF":"F",},

               {"logical_expression": "$\\neg (P \\rightarrow Q)$",
               "TT":"F", 
               "TF":"T",
               "FT":"F",
               "FF":"F",},

               {"logical_expression": "$(\\neg P) \\rightarrow (\\neg Q)$",
               "TT":"T", 
               "TF":"T",
               "FT":"F",
               "FF":"T",},
               
               {"logical_expression": "$(P \\rightarrow Q) \\wedge ((\\neg P) \\vee (\\neg Q))$",
               "TT":"F", 
               "TF":"F",
               "FT":"T",
               "FF":"T",},]
               
    choice = random.choice(choices)
    
    
    data['params']['expression'] = choice["logical_expression"]
    #print(data)
    for pair in ["TT", "TF", "FT", "FF"]:
        if(choice[pair] == "T"):
            right, wrong = ("T", "F")
        else:
            right, wrong = ("F", "T")
        data['params'][pair + "right"] = right
        data['params'][pair + "wrong"] = wrong
    
