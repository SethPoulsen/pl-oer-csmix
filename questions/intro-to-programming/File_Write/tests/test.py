from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback as feedback


def finish(points,message):
    feedback.add_feedback(message)
    feedback.set_score(points)
    return

feedback.finish = finish

class Test(PLTestCase):

    @points(1)
    @name('File Test')
    def test_0(self):
        score = 0
        # try:
        with open("text.txt") as f1:
            student_file = f1.read()
        with open("test_text.txt") as f2:
            stardard_file = f2.read()
        with open("wrong_test_text.txt") as f3:
            wrong_mode_file = f3.read()
        if student_file == stardard_file:
            score += 1
            feedback.add_feedback("You correctly modified the file")
        elif student_file == wrong_mode_file:
            feedback.add_feedback("You incorrectly modified the file. Did you use the right open mode?")
        else:
            feedback.add_feedback("You incorrectly modified the file")
            feedback.add_feedback("This is the expected resulting file:")
            feedback.add_feedback(stardard_file)
            feedback.add_feedback("This is your resulting file:")
            feedback.add_feedback(student_file)

        feedback.set_score(score)
