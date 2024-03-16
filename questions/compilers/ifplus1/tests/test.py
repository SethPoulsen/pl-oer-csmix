import json

solution = """0. \\langle \\mathtt{if}\\ x\\gt y\\ \\mathtt{then}\\ m:=x*x\\ \\mathtt{else}\\ m:=y*y\\ \\mathtt{fi},\\{x:=10,y:=20\\}\\rangle \\Downarrow \\{m:=400,x:=10,y:=20\\} (If2)
1. \\langle x\\gt y,\\{x:=10,y:=20\\}\\rangle \\Downarrow_b \\mathtt{false} (Comp)
2. \\langle x,\\{x:=10,y:=20\\}\\rangle \\Downarrow_e 10 (Var)
2. \\langle y,\\{x:=10,y:=20\\}\\rangle \\Downarrow_e 20 (Var)
1. \\langle m:=y*y,\\{x:=10,y:=20\\}\\rangle \\Downarrow \\{m:=400,x:=10,y:=20\\} (Assign)
2. \\langle y*y,\\{x:=10,y:=20\\}\\rangle \\Downarrow_e 400 (Arith)
3. \\langle y,\\{x:=10,y:=20\\}\\rangle \\Downarrow_e 20 (Var)
3. \\langle y,\\{x:=10,y:=20\\}\\rangle \\Downarrow_e 20 (Var)
"""

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def canonicalize_sigmas(data):
    for g in data['sigmas']:
        tlist = '\\{' + ','.join(g['list']) + '\\}'
        sigma = "\\sigma"
        if g['sigma']=="":
            sigma = sigma + "_{}"
        else:
            sigma = sigma + "_{" + str(g['sigma']) + "}"
        for p in data['tree']:
            p['conclusion'] = p['conclusion'].replace(sigma,tlist)
    out = ""
    for p in data['tree']:
        out = out + str(p['level']) + '. ' + p['conclusion'] + ' (' + p['rule'] + ')\n'
    return out

def runTests():
    data = {}
    with open('/grade/data/data.json') as o:
        j = json.loads(o.read())
        data = json.loads(j['submitted_answers']['treeBox'])

    submitted = canonicalize_sigmas(data)
    print(submitted)
    print(solution)
    dist = levenshteinDistance(submitted,solution)

    result = { "succeeded": True, "score": max(0.0, 1.0 - dist * 2.0 / len(solution)), "message": submitted }

    return result
