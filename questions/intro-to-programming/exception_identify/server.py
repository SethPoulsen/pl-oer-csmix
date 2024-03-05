def generate(data):
    
    import numpy as np
    num = np.random.randint(0,3)
    if num == 0:
        scope = "5"
        ans = "ZeroDivisionError"
        wrong1 = "No Exception"
        wrong2 = "IndexError"
    elif num == 1:
        scope = "6,1,-1"
        ans = "IndexError"
        wrong1 = "ZeroDivisionError"
        wrong2 = "No Exception"
    else:
        scope = "4,0,-1"
        ans = "No Exception"
        wrong1 = "ZeroDivisionError"
        wrong2 = "IndexError"
    data["params"]["scope"] = scope
    data["params"]["ans"] = ans
    data["params"]["wrong1"] = wrong1
    data["params"]["wrong2"] =wrong2
    
    return data