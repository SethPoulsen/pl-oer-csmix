import json


### original grader material
       
original = 'I0. S -> .aEf { a: s1 }\n' + \
    '| .xF { f: s2 }\n'

solution = 'I0. S -> .aEf { a: s1 }\n' + \
    '| .xF { x: s2 }\n' + \
    'I1. S -> a.Ef { E: g3 }\n' + \
    'E -> .Ey { E: g3 }\n' + \
    '| .z { z: s4 }\n' + \
    'I2. S -> x.F { F: g5 }\n' + \
    'F -> .aE { a: s6 }\n' + \
    '| .aF { a: s6 }\n' + \
    'I3. S -> aE.f { f: s7 }\n' + \
    'E -> E.y { y: s8 }\n' + \
    'I4. E -> z. { $,f,y: r3 }\n' + \
    'I5. S -> xF. { $: r1 }\n' + \
    'I6. F -> a.E { E: g9 }\n' + \
    '| a.F { F: g10 }\n' + \
    'E -> .Ey { E: g9 }\n' + \
    '| .z { z: s4 }\n' + \
    'F -> .aE { a: s6 }\n' + \
    '| .aF { a: s6 }\n' + \
    'I7. S -> aEf. { $: r0 }\n' + \
    'I8. E -> Ey. { $,f,y: r2 }\n' + \
    'I9. F -> aE. { $: r4 }\n' + \
    'E -> E.y { y: s8 }\n' + \
    'I10. F -> aF. { $: r5 }\n'

### HOW TO GENERATE json SOLUTION w/out installing Nearley
# 1. open sol.js, enter in correct solution as JS string
# 2. in question.html, change parser.feed(editor.getValue()) to parser.feed(sol_x)
# 3. in test.py, uncomment
#       result['message'] = result['message'] + json.dumps(treeData, indent=2) + "\n"
# 4. comment out code under `# complex feedback`
# 5. run the question, the question output should now dump the JSON

solJS = '[{"iName":"I0.","groupList":[{"nonterm":"S","prodList":[{"production":[".","a","E","f"],"action":{"symList":["a"],"action":"s","id":"1"}},{"production":[".","x","F"],"action":{"symList":["x"],"action":"s","id":"2"}}]}]},{"iName":"I1.","groupList":[{"nonterm":"S","prodList":[{"production":["a",".","E","f"],"action":{"symList":["E"],"action":"g","id":"3"}}]},{"nonterm":"E","prodList":[{"production":[".","E","y"],"action":{"symList":["E"],"action":"g","id":"3"}},' +\
    '{"production":[".","z"],"action":{"symList":["z"],"action":"s","id":"4"}}]}]},{"iName":"I2.","groupList":[{"nonterm":"S","prodList":[{"production":["x",".","F"],"action":{"symList":["F"],"action":"g","id":"5"}}]},{"nonterm":"F","prodList":[{"production":[".","a","E"],"action":{"symList":["a"],"action":"s","id":"6"}},{"production":[".","a","F"],"action":{"symList":["a"],"action":"s","id":"6"}}]}]},{"iName":"I3.","groupList":[{"nonterm":"S","prodList":[{"production":' +\
    '["a","E",".","f"],"action":{"symList":["f"],"action":"s","id":"7"}}]},{"nonterm":"E","prodList":[{"production":["E",".","y"],"action":{"symList":["y"],"action":"s","id":"8"}}]}]},{"iName":"I4.","groupList":[{"nonterm":"E","prodList":[{"production":["z","."],"action":{"symList":["$","f","y"],"action":"r","id":"3"}}]}]},{"iName":"I5.","groupList":[{"nonterm":"S","prodList":[{"production":["x","F","."],"action":{"symList":["$"],"action":"r","id":"1"}}]}]},{"iName":"I6.",' +\
    '"groupList":[{"nonterm":"F","prodList":[{"production":["a",".","E"],"action":{"symList":["E"],"action":"g","id":"9"}}]},{"nonterm":"F","prodList":[{"production":["a",".","F"],"action":{"symList":["F"],"action":"g","id":"10"}}]},{"nonterm":"E","prodList":[{"production":[".","E","y"],"action":{"symList":["E"],"action":"g","id":"9"}},{"production":[".","z"],"action":{"symList":["z"],"action":"s","id":"4"}}]},{"nonterm":"F","prodList":[{"production":[".","a","E"],"action":' +\
    '{"symList":["a"],"action":"s","id":"6"}},{"production":[".","a","F"],"action":{"symList":["a"],"action":"s","id":"6"}}]}]},{"iName":"I7.","groupList":[{"nonterm":"S","prodList":[{"production":["a","E","f","."],"action":{"symList":["$"],"action":"r","id":"0"}}]}]},{"iName":"I8.","groupList":[{"nonterm":"E","prodList":[{"production":["E","y","."],"action":{"symList":["$","f","y"],"action":"r","id":"2"}}]}]},{"iName":"I9.","groupList":[{"nonterm":"F","prodList":[{"production"' +\
    ':["a","E","."],"action":{"symList":["$"],"action":"r","id":"4"}}]},{"nonterm":"E","prodList":[{"production":["E",".","y"],"action":{"symList":["y"],"action":"s","id":"8"}}]}]},{"iName":"I10.","groupList":[{"nonterm":"F","prodList":[{"production":["a","F","."],"action":{"symList":["$"],"action":"r","id":"5"}}]}]}]'

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

### json to string conversion

def actionToString(act):
    return "{ " + (",".join(act["symList"])) + ": " + act["action"] + act["id"] + " }"

def prodToString(prod):
    actStr = "" if not ("action" in prod) else " " + actionToString(prod["action"])
    return "| " + "".join(prod["production"]) + actStr + "\n"

def groupToString(group):
    prodList = group["prodList"]
    prod1 = prodList[0]
    prodTail = prodList[1:]
    act1Str = "" if not ("action" in prod1) else " " + actionToString(prod1["action"])
    otherStr = "".join(map(prodToString, prodTail))
    return group["nonterm"] + " -> " + "".join(prod1["production"]) + act1Str + "\n" + otherStr

def isetToString(iset):
    return iset["iName"] + " " + "".join(map(groupToString, iset["groupList"]))

def dataToString(data):
    return "".join(map(isetToString, data))

### 

def compareTotal(treeData, solTreeData):
    realLen = len(treeData)
    solLen = len(solTreeData)
    if solLen == realLen:
        return "Correct number of item sets generated? [YES]"
    else:
        return "Correct number of item sets generated? [NO] " + str(realLen) + "/" + str(solLen)

def getInitProdSet(itemSet):
    initProdSet = set()
    groupList = itemSet["groupList"]
    for group in groupList:
        nonTerm = group["nonterm"]
        prodList = group["prodList"]
        for prod in prodList:
            prodDetail = prod["production"]
            if len(prodDetail) == 0 or prodDetail[0] != ".":
                initProdSet.add((nonTerm, tuple(prodDetail)))
    return initProdSet

    # isetMap :: index 0 --> [sol] I0. 
def checkInitProd(treeData, solTreeData):
    isetMap = []
    badIset = []
    solInitProdAll = list(map(getInitProdSet, solTreeData))
    for i, itemSet in enumerate(treeData):
        iName = itemSet["iName"]
        initProdSet = getInitProdSet(itemSet)
        solId = -1
        for j, solInitProdSet in enumerate(solInitProdAll):
            if initProdSet == solInitProdSet:
                solId = j
        isetMap.append(solId)
        if solId == -1:
            badIset.append(iName)
    if len(badIset) == 0:
        return ("Item sets have correct productions before taking transitive closure? [YES]", isetMap)
    else:
        msg = "Item sets have correct productions before taking transitive closure? [NO]\n" + \
            "    Item sets: [" + (", ".join(badIset)) + "] productions before taking transitive closure do not match any solution item sets."
        return (msg, isetMap)

def getClosure(itemSet):
    closure = []
    groupList = itemSet["groupList"]
    for group in groupList:
        nonTerm = group["nonterm"]
        prodList = group["prodList"]
        for prod in prodList:
            prodDetail = prod["production"]
            if len(prodDetail) > 0 and prodDetail[0] == ".":
                closure.append((nonTerm, tuple(prodDetail)))
    return closure

def checkClosure(treeData, solTreeData, isetMap):
    badIset = []
    for i, itemSet in enumerate(treeData):
        if isetMap[i] == -1:
            continue
        iName = itemSet["iName"]
        solItemSet = solTreeData[isetMap[i]]
        if set(getClosure(itemSet)) != set(getClosure(solItemSet)):
            badIset.append(iName)
    if len(badIset) == 0:
        return "Valid item sets have correct transitive closures? [YES]"
    else:
        msg = "Valid item sets have correct transitive closures? [NO]\n" + \
            "    Item sets: [" + (",".join(badIset)) + "] have incorrect transitive closures."
        return msg

    # ordermap :: index 0 --> [stu] I0.
def checkOrder(treeData):
    bad = False
    orderMap = []
    for i, itemSet in enumerate(treeData):
        iName = itemSet["iName"]
        if iName != "I" + str(i) + ".":
            bad = True
        j = "".join(filter(lambda c: c.isdigit(), iName))
        orderMap.append(int(j))
    if bad:
        return ("Item sets presented in order? [NO]", orderMap)
    else:
        return ("Item sets presented in order? [YES]", orderMap)

def getProdActionList(itemSet):
    prodActionList = []
    groupList = itemSet["groupList"]
    for group in groupList:
        nonTerm = group["nonterm"]
        prodList = group["prodList"]
        for prod in prodList:
            prodDetail = prod["production"]
            action = prod["action"]
            symList = action["symList"]
            ax = action["action"]
            ix = action["id"]
            prodActionList.append(((nonTerm, prodDetail), (symList, ax, ix)))
    return prodActionList

    # lookupIset :: [stu] I0. --> [index 1 ==> [stu] I0.] --> 1
def lookupIset(ix, orderMap):
    for i, j in enumerate(orderMap):
        if j == ix:
            return i
    return -1

def compareAction(action, solAction, orderMap, isetMap):
    (symList, ax, ix) = action
    stuIx = lookupIset(int(ix), orderMap)
    if stuIx == -1:
        return ["Transition to non-existent state"]
    realIx = isetMap[stuIx]
    (solSymList, solAx, solIx) = solAction
    msg = []
    if symList != solSymList:
        msg.append("Transition on incorrect symbols")
    if ax != solAx:
        msg.append("Incorrect action [s, g, r]")
    if realIx != int(solIx):
        msg.append("Transition to incorrect/invalid state")
    return msg

def checkActions(treeData, solTreeData, orderMap, isetMap):
    badProdActionList = []
    for i, itemSet in enumerate(treeData):
        if isetMap[i] == -1:
            continue
        iName = itemSet["iName"]
        prodActionList = getProdActionList(itemSet)
        solItemSet = solTreeData[isetMap[i]]
        solProdActionList = getProdActionList(solItemSet)
        for prod, action in prodActionList:
            for solProd, solAction in solProdActionList:
                if prod == solProd:
                    mList = compareAction(action, solAction, orderMap, isetMap)
                    if len(mList) != 0:
                        badProdActionList.append((iName, prod, mList))
    if len(badProdActionList) == 0:
        return "Valid item set productions have correct actions? [YES]"
    else:
        msg = "Valid item set productions have correct actions? [NO]"
        for iName, prod, mList in badProdActionList:
            (nonTerm, prodDetail) = prod
            pStr = nonTerm + " -> " + ("".join(prodDetail))
            msg = msg + "\n    " + iName + " " + pStr + " :: " + (", ".join(mList))
        return msg

def checkIsetOrder(treeData, orderMap, isetMap):
    badIset = []
    for i, itemSet in enumerate(treeData):
        stuId = orderMap[i]
        solId = isetMap[i]
        if solId != -1 and stuId != solId:
            badIset.append(itemSet["iName"])
    if len(badIset) == 0:
        return "Item sets generated in canonical order? [YES]"
    else:
        msg = "Item sets generated in canonical order? [NO]\n" + \
            "    Item sets: [" + (", ".join(badIset)) + "] are enumerated incorrectly."
        return msg

def checkProdOrder(treeData, solTreeData, isetMap):
    badIset = set()
    for i, itemSet in enumerate(treeData):
        if isetMap[i] == -1:
            continue
        iName = itemSet["iName"]
        prodActionList = getProdActionList(itemSet)
        solItemSet = solTreeData[isetMap[i]]
        solProdActionList = getProdActionList(solItemSet)
        for i, (prod, action) in enumerate(prodActionList):
            if i < len(solProdActionList):
                (solProd, solAction) = solProdActionList[i]
                if prod != solProd:
                    badIset.add(iName)
    badIset = list(badIset)
    if len(badIset) == 0:
        return "Item set productions generated in canonical order? [YES]"
    else:
        msg = "Item set productions generated in canonical order? [NO]\n" + \
            "    Item sets: [" + (", ".join(badIset)) + "] have productions out of order."
        return msg

def feedback(treeData, solTreeData):
    # checks whether the student has the correct number of item sets
    message = "-- ITEM SET CORRECTNESS --"
    message = message + "\n" + compareTotal(treeData, solTreeData)
    # checks whether the student's item sets have the correct productions before taking the transitive closure
    #   (also obtains a mapping from student's item set to solution's item set)
    (eMsg1, isetMap) = checkInitProd(treeData, solTreeData)
    message = message + "\n" + eMsg1
    # checks whether the student takes the correct transitive closures
    message = message + "\n" + checkClosure(treeData, solTreeData, isetMap)
    # checks whether item sets are given in order
    #   (also obtains a mapping from integers to student's item sets)
    (eMsg2, orderMap) = checkOrder(treeData)
    # checks whether the actions associated with each state are correct
    message = message + "\n" + checkActions(treeData, solTreeData, orderMap, isetMap)

    # appends the ordering error message
    message = message + "\n\n -- ORDERING CORRECTNESS --"
    message = message + "\n" + eMsg2
    # checks whether the item sets are produced in canonical order
    message = message + "\n" + checkIsetOrder(treeData, orderMap, isetMap)
    # checks whether the productions are in canonical order
    message = message + "\n" + checkProdOrder(treeData, solTreeData, isetMap)
    message = message + "\n(If all checks pass and you are still losing points, check your use of `|` vs `->`)."
    return message

### test runner

def runTests():

    # read the results
    treeData = {}
    strData = ""
    result = { "gradable": True, "message": ""}
    
    with open('/grade/data/data.json') as o:
        j = json.loads(o.read())
        rawTreeData = json.loads(j['submitted_answers']['treeBox']);
        treeData = json.loads(json.dumps(rawTreeData, separators=(',', ':')))
        strData = dataToString(treeData)
        #result['message'] = result['message'] + json.dumps(treeData, indent=2) + "\n"

    # complex feedback
    solTreeData = json.loads(solJS)
    result['message'] = result['message'] + feedback(treeData, solTreeData) + "\n\n"

    # original grader
    dist = levenshteinDistance(strData,solution)
    scale = levenshteinDistance(original,solution)
    distpc = max(0.0, (scale - dist) / scale)

    score = 0
    result['message'] = result['message'] + "Your answer is {:.2f}% correct so far.".format(distpc * 100)

    if distpc >= 0.95:
        score = distpc
    else:
        result['message'] = result['message'] + " Threshold for credit is 95%"

    result['score'] = score

    return result
