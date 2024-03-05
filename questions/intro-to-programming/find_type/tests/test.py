from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback as feedback
import numpy as np
import builtins

def finish(points,message):
    feedback.add_feedback(message)
    feedback.set_score(points)
    return

feedback.finish = finish

old_type = builtins.type
old_isinstance = builtins.isinstance

def new_type(*args, **kwargs):
    new_type.count += 1
    return old_type(*args, **kwargs)

def new_isinstance(*args, **kwargs):
    new_isinstance.count += 1
    return old_isinstance(*args, **kwargs)


class Test(PLTestCase):

    @points(1)
    @name('find_type test')
    def test_0(self):
    
        # initialize the count for calling type and isinstance 
        new_type.count = 0
        new_isinstance.count = 0

        st_ans = self.st.find_type
        ref_ans = self.ref.find_type
        
        target_list = [1] * 6 + ["Kangyu"] * 4
        np.random.shuffle(target_list)

        wrong_count = 0
        for i in target_list:
            
            builtins.type = new_type
            builtins.isinstance = new_isinstance
            
            st = feedback.call_user(st_ans, i)
            
            builtins.type = old_type
            builtins.isinstance = old_isinstance
            
            if not isinstance(st, str):
                feedback.add_feedback("Your find_type does not return a string. Please check the notes for the return.")
                feedback.set_score(0)
                return
            
            if new_type.count or new_isinstance.count:
                feedback.add_feedback("You are attempting to use type() or isinstance(). The use of these functions is not allowed.")
                feedback.set_score(0)
                return

            if st != ref_ans(i):
                wrong_count += 1
                
        if wrong_count == 4: # wrong count is 4
            feedback.add_feedback("Your find_type is incorrect! Did you correctly handle str case?")
            feedback.set_score(0.5)
        elif wrong_count == 6:
            feedback.add_feedback("Your find_type is incorrect! Did you correctly handle int case?")
            feedback.set_score(0.5)
        elif wrong_count == 0:
            feedback.add_feedback("Your find_type is correct")
            feedback.set_score(1)
        else:
            feedback.add_feedback("Your find_type is incorrect.")
            feedback.set_score(0)

