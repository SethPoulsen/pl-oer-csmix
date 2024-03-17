"""
This module was originally designed for detection of student's errors and could be caught individually.
Keeping it here if any future changes would like to use such/more custom errors for new features in the future.
"""


class StudentWrongAnswerError(Exception):
    """Raised when student's answer fail any generated data set"""
    def __init__(self, grading_result_dict):
        self.grading_result = grading_result_dict


class StudentIncorrectAnswerError(Exception):
    """Raised when student's answer fail any generated data set"""
    def __init__(self, solution_dict_list, student_dict_list):
        self.solution_dict_list = solution_dict_list
        self.student_dict_list = student_dict_list
        self.success = False
