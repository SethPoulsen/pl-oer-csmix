from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback as feedback
from functools import wraps


class Test(PLTestCaseWithPlot):

    @points(2)
    @name("xmat")
    def test_0(self):
        score = 0

        if feedback.check_numpy_array_allclose('xmat', self.ref.xmat, self.st.xmat, accuracy_critical=False, atol=1e-8):
            score += 1.0

        elif feedback.check_numpy_array_allclose('xmat',self.ref.xwrong, self.st.xmat,
                report_failure = False, report_success=False):
            feedback.add_feedback('Make sure you are reshaping your arrays row-wise, not column-wise')

        elif feedback.check_numpy_array_allclose('xmat',self.ref.xwrong2, self.st.xmat,
                report_failure = False, report_success=False):
            feedback.add_feedback('Make sure you are reshaping your arrays row-wise, not column-wise')

        elif feedback.check_numpy_array_allclose('xmat',self.ref.xwrong3, self.st.xmat,
                report_failure = False, report_success=False):
            feedback.add_feedback('Make sure you are reshaping your arrays row-wise, not column-wise')

        feedback.set_score(score)

