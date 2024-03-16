import prairielearn as pl
import numpy as np
import random

def generate_transaction_sequence(elements, n, num_transactions):
    transcations = []
    for _ in range(num_transactions):
        elem = random.choice(elements)
        transcations.append(f"{random.choice(['R', 'W'])}_{random.choice(n)[2]}({elem});")
    return transcations

def getAnswer(transactions, n):
    graph = np.zeros((n, n))
    
    for i in range(len(transactions)):
        curr = transactions[i]
        o1 = curr[0]
        n1 = curr[2]
        e1 = curr[4]
        for j in range(i+1, len(transactions)):
            comp = transactions[j]
            o2 = comp[0]
            n2 = comp[2]
            e2 = comp[4]

            if n1 != n2 and (o1 != 'R' or o2 != 'R') and e1 == e2: #WR, RW, WW
                graph[int(n1) - 1, int(n2) - 1] = 1
                
    return graph.tolist()

def has_cycle(adjacency_matrix):
    num_nodes = len(adjacency_matrix)

    def dfs(node, stack):
        if stack[node]:
            return True
        
        stack[node] = True
        for v in range(num_nodes):
            if adjacency_matrix[node][v]:
                if dfs(v, stack):
                    return True
        
        stack[node] = False
        return False
    
    stack = [False] * num_nodes
    for i in range(num_nodes):
        if dfs(i, stack):
            return True
    return False
        
def generate(data):
    #auto-generated transactions sequence setting
      #elements: elements that transcations can read or write
      #type: types of transaction
      #seq_num: total number of transaction in a sequence
      #cycle: is the generated transaction acyclic
    elements = ['A', 'B']
    type = ['T_1', 'T_2', 'T_3']
    seq_num = 8
    cycle = True
    transactions = generate_transaction_sequence(elements, type, seq_num)
    mat = getAnswer(transactions, len(type))
    has_cycle_flag = has_cycle(mat)
    while has_cycle_flag != cycle:
        transactions = generate_transaction_sequence(elements, type, seq_num)
        mat = getAnswer(transactions, len(type))
        has_cycle_flag = has_cycle(mat)
    
    data['params']['seq_transactions'] = "".join(transactions)
    data['params']['transactions'] = ", ".join(type)
    data['params']['elements'] = ", ".join(elements)

    mat = getAnswer(transactions, len(type))
    data["correct_answers"]["matrixA"] = pl.to_json(mat)
    
    has_cycle_flag = has_cycle(mat)
    data["params"]["q1"] = [
      {"tag": str(not has_cycle_flag), "ans": "is"},
      {"tag": str(has_cycle_flag), "ans": "is not"},
    ]
    data["params"]["q2"] = [
      {"tag": str(has_cycle_flag), "ans": "is not"},
      {"tag": str(not has_cycle_flag), "ans": "is"},
    ]

def parse(data):
    if "matrixA" not in data["format_errors"]:
        matrix = data["submitted_answers"]["matrixA"]['_value']
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != 0 and matrix[i][j] != 1:
                    data["format_errors"]["matrixA"] = "Please check your input. Only 0 and 1 are allowed to input in matrix"
                    break

   