import random

def generate(data):
    
    problem_size = 8
    coins = []
    for i in range(problem_size):
        coins.append(random.randint(1,10))
    
    best_value_up_to_coin_i = []
    best_value_up_to_coin_i.append(coins[0])
    best_value_up_to_coin_i.append(max(coins[0], coins[1]))
    for i in range(2, len(coins)):
        best_value_up_to_coin_i.append(max(coins[i] + best_value_up_to_coin_i[i-2], best_value_up_to_coin_i[i-1]))
    answer = best_value_up_to_coin_i[-1]
    
    
    
    data['params']['coins'] = coins
    
    for i in range(problem_size):
        data['correct_answers']['subproblem' + str(i)] = best_value_up_to_coin_i[i]
    data['correct_answers']['answer'] = answer

