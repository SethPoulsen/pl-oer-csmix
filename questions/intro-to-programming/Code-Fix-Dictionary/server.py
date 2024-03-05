import random

def generate(data):
    student_names = ['Alice', 'Bob', 'Eve', 'Mallory', 'Trent']
    assessment_names = [str(kind) + str(i) for kind in ['hw', 'quiz'] for i in range(1, 7)]

    student_to_fix = random.choice(student_names)
    assessment_to_fix = random.choice(assessment_names[1: ])
    score_to_add = random.randint(3, 7)

    data['params']['student_to_fix'] = student_to_fix
    data['params']['assessment_to_fix'] = assessment_to_fix
    data['params']['score_to_add'] = score_to_add

    names_for_user = [
        {"name": 'gradebook', "description": "the gradebook dictionary you want to modify", 
        "type": "dictionary"}
    ]
    names_from_user = [
        {"name": 'gradebook', "description": "the gradebook dictionary you want to modify", 
        "type": "dictionary"}
    ]
    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user

    typo_index = random.randint(0, len(student_to_fix) - 1)
    typo_content = chr(random.randint(0, 25) + ord('a'))
    typo_name = student_to_fix[0: typo_index] + typo_content + student_to_fix[typo_index + 1:]

    bugged_code = f'''
gradebook[\'{typo_name}\', \'{assessment_to_fix}\'] += {score_to_add}
for student in gradebook:
    student['hw1'] += 1
'''
    data['params']['bugged_code'] = bugged_code

    return data