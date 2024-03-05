from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback as feedback
from functools import wraps


def finish(points,message):
    feedback.add_feedback(message)
    feedback.set_score(points)
    return

feedback.finish = finish

class Test(PLTestCase):

    @points(1)
    @name('products_number Test')
    def test_0(self):
        score = 0
        # try:
            # Check the values.
        st_ans = self.st.products_number
        ref_ans = self.ref.products_number
        if feedback.check_list("products_number", ref_ans, st_ans):
            # just make sure they are same order
            st_ans.sort()
            ref_ans.sort()
            for i in range(len(ref_ans)):
                if ref_ans[i] != st_ans[i]:
                    feedback.add_feedback("there exists a invaild product number!")
                    feedback.set_score(score)
                    pass
            score += 1
            feedback.add_feedback("\'products_number\' looks good!")
        feedback.set_score(score)
    @points(1)
    @name('products_number Test')
    def test_1(self):
        score = 0
        st_ans = self.st.product_info
        ref_ans = self.ref.product_info
        
        
        try: 
            if st_ans["name"] == ref_ans["name"]:
                score += 0.5
                feedback.add_feedback("\'Name\' is correct!")
            else:
                feedback.add_feedback("\'Name\' is incorrect.")
            if feedback.check_scalar("product price", ref_ans["price"], st_ans["price"]):
                score += 0.5
        except:
            feedback.add_feedback("\'product_info\' is incorrect. Is it a dictionary?")
        feedback.set_score(score)
    @points(1)
    @name('product_name Test')
    def test_2(self):
        score = 0
        # try:
            # Check the values.
        st_ans = self.st.product_name
        ref_ans = self.ref.product_name
        if isinstance(st_ans, str):
            if st_ans == ref_ans:
                score += 1
                feedback.add_feedback("\'product_name\' looks good" )
            else:
                feedback.add_feedback("\'product_name\' is incorrect" )
        else:
            feedback.add_feedback("\'product_name\' is not a string")
        feedback.set_score(score)