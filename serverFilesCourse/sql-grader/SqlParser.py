from moz_sql_parser import parse
import json
import re
import itertools

join_keywords = ["join", "full join", "cross join", "inner join", "left join", "right join", \
                 "full outer join", "right outer join", "left outer join"]


def getTerms(key, value, res):
    if (key == "eq" or key == "gt" or key == "lt") and \
            not isinstance(value[1], list) and \
            not isinstance(value[1], dict):
        res.append(value)
        return

    if key == "from":
        res += extractTableNames(value)
        return

    if not (isinstance(value, dict) or isinstance(value, list)):
        return

    if isinstance(value, dict):
        for k, v in value.items():
            getTerms(k, v, res)

    if isinstance(value, list):
        for item in value:
            getTerms(None, item, res)


def getValueConstraints(query: str):
    res = parse(query)
    constraints = list()
    for key, value in res.items():
        getTerms(key, value, constraints)

    return constraints


def extractTableNames(value):
    tableNames = list()
    if isinstance(value, dict):
        tableNames.append(value["value"])
    elif not isinstance(value, list):
        tableNames.append(value)
    else:
        for item in value:
            if not isinstance(item, dict):
                tableNames.append(item)
            else:
                if "value" in item:
                    tableNames.append(item["value"])
                    continue
                for keyword in join_keywords:
                    if keyword in item:
                        if not isinstance(item[keyword], dict):
                            tableNames.append(item[keyword])
                        else:
                            tableNames.append(item[keyword]["value"])

    return tableNames


def getConstraints(query: str):
    valueContraints = getValueConstraints(query)
    constraints = [item for item in valueContraints if isinstance(item, list)]
    tableNamesSet = {item for item in valueContraints if not isinstance(item, list)}
    queryTokens = query.split()

    constraintPointer = 0
    queryTokenPointer = 0
    prevMatchIndex = 0
    res = list()

    while (constraintPointer < len(constraints) and queryTokenPointer < len(queryTokens)):
        if queryTokens[queryTokenPointer].find(constraints[constraintPointer][0]) != -1:
            if queryTokens[queryTokenPointer].find(str(constraints[constraintPointer][1])) != -1 or \
                    queryTokens[queryTokenPointer + 1].find(str(constraints[constraintPointer][1])) != -1 or \
                    queryTokens[queryTokenPointer + 2].find(str(constraints[constraintPointer][1])) != -1:

                i = queryTokenPointer - 1
                grpTables = list()
                while i >= 0:
                    if queryTokens[i].lower() == "from":
                        break
                    tokens = queryTokens[i].split(",")
                    for token in tokens:
                        if token in tableNamesSet:
                            grpTables.append(token)
                    i -= 1

                for element in itertools.product(grpTables, [constraints[constraintPointer]]):
                    res.append(element)
                prevMatchIndex = queryTokenPointer
                constraintPointer += 1
        queryTokenPointer += 1

    return res
