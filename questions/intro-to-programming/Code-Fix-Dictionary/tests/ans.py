student_to_fix = data['params']['student_to_fix']
assessment_to_fix = data['params']['assessment_to_fix']
score_to_add = data['params']['score_to_add']

gradebook[student_to_fix][assessment_to_fix] += score_to_add
for student in gradebook.values():
    student['hw1'] += 1
    