import random

student_names = ['Alice', 'Bob', 'Eve', 'Mallory', 'Trent']
assessment_names = [str(kind) + str(i) for kind in ['hw', 'quiz'] for i in range(1, 7)]

gradebook = {}
for student in student_names:
    assessments = {}
    for assessment in assessment_names:
        assessments[assessment] = random.randint(70, 90)
    gradebook[student] = assessments