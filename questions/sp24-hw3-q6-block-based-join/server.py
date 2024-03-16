import random
import math
import re

def generate(data):
    # Generate input data
    # Tuples
    pTuples = random.randint(1, 5) * 800
    data["params"]["pTuples"] = str(pTuples)
    cTuples = random.randint(6, 10) * 1000
    data["params"]["cTuples"] = str(cTuples)
    mTuples = math.ceil(random.random()*6) * 100
    data["params"]["mTuples"] = str(mTuples)
    tpb = random.choice([5,10,20,25,50,30,15,40])
    
    # block
    bp = random.choice([20, 25])
    bc = random.choice([300, 310, 320, 330, 340])
    bm = random.choice([45, 50, 55, 60])
    
    data["params"]["bp"] = str(bp)
    data["params"]["bc"] = str(bc)
    data["params"]["bm"] = str(bm)
    
    mem = random.randint(20, 30) +8
    data["params"]["mem"] = str(mem)
    
    # The first question was designed for No, calculate the cost using block-based nested loop join.
    # Calculate the optimal cost to perform the join in "Join A". Please answer the following questions: (8 points)
    # Is one-pass join feasible for this question? Justify your answer.
    # If YES, calculate the cost using one-pass join. 
    # If NO, calculate the cost using block-based nested loop join.

    # I: block-based nested loop join.
    # B(R) + B(S)B(R)/(M-2) 
    # B(M) + B(C)B(M)/(M-2)
    q1 = bm + bc * bm / (mem - 2)
    
    
    joinATuples = random.choice([6800, 7200, 7600])
    data["params"]["joinATuples"] = str(joinATuples)
    bjoinA = random.choice([50, 80])
    data["params"]["bjoinA"] = str(bjoinA)
    
    # What is the total number of blocks for the result after "Join A"?
    # B(Join A) = joinATuples / B(joinA)
    q2 = joinATuples / bjoinA
    
    # The third question was designed for Yes, calculate the cost using one pass join.
    # Is one-pass join feasible for “Join B”? Justify your answer.
    # If YES, calculate the cost using one-pass join.
    # If NO, calculate the cost using block-based nested loop join.
    # B(P) + B(joinA)
    q3 = bp + q2
    
    # Questions
    temp = 100
    data['correct_answers']['questionI'] = str(int(math.ceil(q1)))
    data['correct_answers']['questionII'] = str(int(math.ceil(q2)))
    data['correct_answers']['questionIII'] = str(int(math.ceil(q3)))
    
def grade(data):   
    # q2_submit = data["submitted_answers"]['questionII']
    # # Note: Only for Fall 2021 (? not sure what this comment is about ?)
    # rTuples = int(data["params"]["pTuples"])
    # sTuples = int(re.findall(r"Sauces has (\d+)", data['params']['description'])[0])
    # tpb = int(re.findall(r"block can hold (\d+)", data['params']['description'])[0])
    # mem = int(re.findall(r"The memory size is (\d+)", data['params']['description'])[0])
    
    # q2_almost = str(math.ceil(rTuples / tpb + sTuples / tpb * math.ceil(rTuples / tpb / (mem-2))))
    # if q2_submit == q2_almost:
    #     data["submitted_answers"]['questionII'] = data["correct_answers"]['questionII']
    #
    total = 0.0
    for s in ['questionI','questionII','questionIII']:
        v = 1 if data["submitted_answers"][s]==data["correct_answers"][s] else 0
        data["partial_scores"][s]["score"] = v
        total += v
    data["score"] = total/3.0