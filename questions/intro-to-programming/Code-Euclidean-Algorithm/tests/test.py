from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback as feedback
import random

class Test(PLTestCaseWithPlot):

    @points(1)
    @name("Case 1: one input is a multiple of the other")
    def test_0(self):

        # generate a and b where b is multiple of a
        a = random.randint(3, 10)
        b = random.randint(3, 10) * a

        # swap a and b randomly
        if random.random() > .5:
            a, b = b, a

        gcd_st = feedback.call_user(self.st.gcd, a, b)
        gcd_ref = self.ref.gcd(a, b)

        print(f'a = {a}, b = {b}, gcd_ref = {gcd_ref}, gcd_st = {gcd_st}')

        if feedback.check_scalar('gcd', gcd_ref, gcd_st):
            feedback.set_score(1)
        else:
            feedback.set_score(0)

    @points(1)
    @name("Case 2: general non-coprime")
    def test_1(self):

        gcd = random.randint(3, 10)

        # generate a and b with gcd
        a = random.randint(3, 10) * gcd
        b = random.randint(3, 10) * gcd

        gcd_st = feedback.call_user(self.st.gcd, a, b)
        gcd_ref = self.ref.gcd(a, b)

        print(f'a = {a}, b = {b}, gcd_ref = {gcd_ref}, gcd_st = {gcd_st}')

        if feedback.check_scalar('gcd', gcd_ref, gcd_st):
            feedback.set_score(1)
        else:
            feedback.set_score(0)

    @points(1)
    @name("Case 3: coprime")
    def test_2(self):

        # generate a and b randomly
        a = random.randint(10, 100)
        b = random.randint(10, 100)
        gcd_ref = self.ref.gcd(a, b)
        
        # remove gcd to ensure coprime
        a = int(a / gcd_ref)
        b = int(b / gcd_ref)

        gcd_st = feedback.call_user(self.st.gcd, a, b)
        gcd_ref = self.ref.gcd(a, b)

        print(f'a = {a}, b = {b}, gcd_ref = {gcd_ref}, gcd_st = {gcd_st}')

        if feedback.check_scalar('gcd', gcd_ref, gcd_st):
            feedback.set_score(1)
        else:
            feedback.set_score(0)

    @points(1)
    @name("Case 4: one of the inputs is 1")
    def test_3(self):

        # generate a and b randomly
        a = 1
        b = random.randint(10, 100)
        
        # swap a and b randomly
        if random.random() > .5:
            a, b = b, a

        gcd_st = feedback.call_user(self.st.gcd, a, b)
        gcd_ref = self.ref.gcd(a, b)

        print(f'a = {a}, b = {b}, gcd_ref = {gcd_ref}, gcd_st = {gcd_st}')

        if feedback.check_scalar('gcd', gcd_ref, gcd_st):
            feedback.set_score(1)
        else:
            feedback.set_score(0)