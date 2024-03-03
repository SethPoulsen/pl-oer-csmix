from digital_logic.digitalLogic import *
from digital_logic.constants import youtube_videos

def file(data):
    if data['filename'] == 'figure.png':
        return gen_circuit(data['correct_answers']['expression'], 3)

def generate(data):
    expression = gen_expression(3,1)
    data['correct_answers']['expression'] = expression

    data['params']['video_hash'] = youtube_videos['c2e']

def grade(data):
    try:
        student_answer = get_truth_table(data['submitted_answers']['expression'],3)
    except:
        data['score'] = 0
        data['feedback']['msg'] = 'Your submitted answer contained unacceptable characters'

        return data
    
    correct_answer = get_truth_table(data['correct_answers']['expression'],3)

    data['score'] = 1 if student_answer == correct_answer else 0
    # override the score badge on the pl-string-input
    data['partial_scores']['expression']['score'] = data['score']
    data['feedback']['msg'] = ''

    return data