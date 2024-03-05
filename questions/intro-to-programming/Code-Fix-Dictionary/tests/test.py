from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback as feedback

class Test(PLTestCaseWithPlot):

    # helper: return the score for a given student and assessment
    # check for key existance and inner layer type
    def get_score_helper(self, dict, key1, key2):
        if not key1 in dict:
            feedback.add_feedback(f'{key1} is not in the dictionary anymore')
            feedback.set_score(0)
            return
        
        if type(dict[key1]) != type({}):
            print(type(dict[key1]))
            feedback.add_feedback(f'grades for {key1} is not a dictionary anymore')
            feedback.set_score(0)
            return
        
        if not key2 in dict[key1]:
            feedback.add_feedback(f'{key2} is not in the dictionary anymore')
            feedback.set_score(0)
            return
        
        return dict[key1][key2]

    @points(1)
    @name("Sanity check of the gradebook")
    def test_0(self):

        gradebook_st = self.st.gradebook
        gradebook_ref = self.ref.gradebook

        if (gradebook_st is None):
            feedback.add_feedback('Your gradebook is None or not defined')
            feedback.set_score(0)
            feedback.finish('')

        if (type(gradebook_ref) != type(gradebook_st)):
            feedback.add_feedback('Your gradebook is not a dictionary')
            feedback.set_score(0)
            feedback.finish('')

        feedback.set_score(1)
        
    @points(1)
    @name("Check if the one assignment score is changed correctly")
    def test_1(self):

        gradebook_st = self.st.gradebook
        gradebook_ref = self.ref.gradebook

        student_to_fix = self.data['params']['student_to_fix']
        assessment_to_fix = self.data['params']['assessment_to_fix']

        st_score = self.get_score_helper(gradebook_st, student_to_fix, assessment_to_fix)
        if st_score is None:
            return
        ref_score = gradebook_ref[student_to_fix][assessment_to_fix]
        
        if st_score == ref_score:
            feedback.add_feedback(f'{assessment_to_fix} score for {student_to_fix} is changed correctly')
            feedback.set_score(1)
        else:
            feedback.add_feedback(f'{assessment_to_fix} score for {student_to_fix} is not changed correctly')
            feedback.set_score(0)

    @points(1)
    @name("Check if hw1 scores are updated correctly")
    def test_2(self):

        gradebook_st = self.st.gradebook
        gradebook_ref = self.ref.gradebook

        student_to_fix = self.data['params']['student_to_fix']
        assessment_to_fix = 'hw1'

        for student_to_fix in gradebook_ref:

            st_score = self.get_score_helper(gradebook_st, student_to_fix, assessment_to_fix)
            if st_score is None:
                return
            ref_score = gradebook_ref[student_to_fix][assessment_to_fix]
            
            if st_score != ref_score:
                feedback.add_feedback(f'{assessment_to_fix} score for {student_to_fix} is not changed correctly')
                feedback.set_score(0)
                return

        feedback.add_feedback(f'{assessment_to_fix} scores are changed correctly')
        feedback.set_score(1)

    @points(1)
    @name("Check if the whole gradebook is correct")
    def test_3(self):

        gradebook_st = self.st.gradebook
        gradebook_ref = self.ref.gradebook

        if (gradebook_ref != gradebook_st):
            feedback.add_feedback('Your gradebook is inaccurate. Are you changing values that do not need to be changed?')
            feedback.set_score(0)
        else:
            feedback.set_score(1)