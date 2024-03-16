import random
import math
import json

def getVariant5():
    # Randomize. Get a list of unique 1-2 digit integers.
    x = random.sample(range(1,100), 19)
    x.sort()
    #
    operation = "Insert "+str(x[15])+", then insert "+str(x[18])+"."
    #
    initial_tree = [
                [[x[9]]],
                [[x[2],x[5]],[x[11],x[14]]],
                [[x[0],x[1]],[x[2],x[3],x[4]],[x[5],x[6],x[7],x[8]],[x[9],x[10]],[x[11],x[12],x[13]],[x[14],x[16],x[17]]]
    ]
    final_tree = [
                [[x[9]]],
                [[x[2],x[5]],[x[11],x[14],x[16]]],
                [[x[0],x[1]],[x[2],x[3],x[4]],[x[5],x[6],x[7],x[8]],[x[9],x[10]],[x[11],x[12],x[13]],[x[14],x[15]],[x[16],x[17],x[18]]]
    ]
    return initial_tree, [final_tree], operation
    
# def getVariant4():
#     # Randomize. Get a list of unique 1-2 digit integers.
#     x = random.sample(range(1,100), 17)
#     x.sort()
#     #
#     operation = "Delete "+str(x[1])+", then delete "+str(x[2])+"."
#     #
#     initial_tree = [
#                 [[x[9]]],
#                 [[x[2],x[5]],[x[11],x[14]]],
#                 [[x[0],x[1]],[x[2],x[3],x[4]],[x[5],x[6],x[7],x[8]],[x[9],x[10]],[x[11],x[12],x[13]],[x[14],x[15],x[16]]]
#     ]
#     final_tree = [
#                 [[x[5],x[9],x[11],x[14]]],
#                 [[x[0],x[3],x[4]],[x[5],x[6],x[7],x[8]],[x[9],x[10]],[x[11],x[12],x[13]],[x[14],x[15],x[16]]]
#     ]
#     return initial_tree, [final_tree], operation
    
# def getVariant3():
#     # Randomize. Get a list of unique 1-2 digit integers.
#     x = random.sample(range(1,100), 18)
#     x.sort()
#     #
#     operation = "Insert "+str(x[9])+", then delete "+str(x[4])+"."
#     #
#     initial_tree = [
#                 [[x[10]]],
#                 [[x[2],x[5]],[x[12],x[15]]],
#                 [[x[0],x[1]],[x[2],x[3],x[4]],[x[5],x[6],x[7],x[8]],[x[10],x[11]],[x[12],x[13],x[14]],[x[15],x[16],x[17]]]
#     ]
#     final_tree = [
#                 [[x[10]]],
#                 [[x[2],x[5],x[7]],[x[12],x[15]]],
#                 [[x[0],x[1]],[x[2],x[3]],[x[5],x[6]],[x[7],x[8],x[9]],[x[10],x[11]],[x[12],x[13],x[14]],[x[15],x[16],x[17]]]
#     ]
#     return initial_tree, [final_tree], operation

# def getVariant2():
#     # Randomize. Get a list of unique 1-2 digit integers.
#     x = random.sample(range(1,100), 17)
#     x.sort()
#     #
#     operation = "Delete "+str(x[2])+", then delete "+str(x[3])+"."
#     #
#     initial_tree = [
#                 [[x[9]]],
#                 [[x[2],x[4],x[6]],[x[12],x[15]]],
#                 [[x[0],x[1]],[x[2],x[3]],[x[4],x[5]],[x[6],x[7],x[8]],[x[9],x[10],x[11]],[x[12],x[13],x[14]],[x[15],x[16]]]
#     ]
#     final_tree = [
#                 [[x[9]]],
#                 [[x[2],x[6]],[x[12],x[15]]],
#                 [[x[0],x[1]],[x[4],x[5]],[x[6],x[7],x[8]],[x[9],x[10],x[11]],[x[12],x[13],x[14]],[x[15],x[16]]]
#     ]
#     final_tree_2 = [
#                 [[x[9]]],
#                 [[x[4],x[6]],[x[12],x[15]]],
#                 [[x[0],x[1]],[x[4],x[5]],[x[6],x[7],x[8]],[x[9],x[10],x[11]],[x[12],x[13],x[14]],[x[15],x[16]]]
#     ]
#     return initial_tree, [final_tree, final_tree_2], operation
    
# def getVariant1():
#     # Randomize. Get a list of unique 1-2 digit integers.
#     x = random.sample(range(1,100), 17)
#     x.sort()
#     #
#     operation = "Delete "+str(x[5])+", then delete "+str(x[6])+"."
#     #
#     initial_tree = [
#                 [[x[9]]],
#                 [[x[2],x[4],x[6]],[x[12],x[15]]],
#                 [[x[0],x[1]],[x[2],x[3]],[x[4],x[5]],[x[6],x[7],x[8]],[x[9],x[10],x[11]],[x[12],x[13],x[14]],[x[15],x[16]]]
#     ]
#     final_tree = [
#                 [[x[9]]],
#                 [[x[2],x[4]],[x[12],x[15]]],
#                 [[x[0],x[1]],[x[2],x[3]],[x[4],x[7],x[8]],[x[9],x[10],x[11]],[x[12],x[13],x[14]],[x[15],x[16]]]
#     ]
#     return initial_tree, [final_tree], operation





def generate(data):
    # Generate input data
    rTuples = math.ceil(random.random()*16) * 1000
    sTuples = math.ceil(random.random()*16) * 1000
    tpb = random.choice([5,10,20,25,50])
    mem = math.ceil(random.random()*16)+8
    #
    # variants = [getVariant1,getVariant2,getVariant3,getVariant4,getVariant5]
    initial_tree, final_tree, operation = getVariant5()
    #
    data['params']['description'] = json.dumps({'initial_tree': initial_tree})
    data['params']['initial_tree'] = str(initial_tree)
    data['params']['operation'] = operation
    data['correct_answers']['question'] = json.dumps({'c': final_tree})
    
def grade(data):
    s = ''.join(data["submitted_answers"]["question"].split())
    correct = 0
    final_trees = json.loads(data["correct_answers"]["question"])['c']
    for tree in final_trees:
        c = ''.join(str(tree).split())
        if (s==c):
            correct=1
    data["partial_scores"]["question"]["score"] = data["score"] = correct