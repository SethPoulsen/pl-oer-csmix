import json
import sys
import time
from custom_errors import StudentWrongAnswerError, StudentIncorrectAnswerError


class BaseGrader:
    PL_RESULT_JSON_FILENAME = "results.json"
    PL_FINAL_RESULT_PATH = "/grade/results/results.json"  # The directory where PL looks to display results on its website
    INCORRECT_COUNT_MESSAGE =  "Number of incorrect answers: {}\n100% is only given when all tests correctly passed."
    CORRECT_COUNT_MESSAGE = "Great Job!" #"You received the highest score awarded by the autograder.\n The remaining 10% will be awarded after manual grading."  
    TEST_CORRECT_MESSAGE = "Correct result!"
    TEST_INCORRECT_MESSAGE = "Wrong result!"
    REMINDER_TO_CLICK_ON_TABS_FOR_INFO_TO_STUDENTS_WHO_CANNOT_FIGURE_THINGS_OUT_ON_THEIR_OWN_GEEZE = "*HINT: You can click on tabs below to look at more detailed info of each test results!*\n\n"

    def __init__(self, grading_function, submission_num):
        self.grading_function = grading_function
        self.submission_num = submission_num

        self.submission_count = 0
        self.grading_result = dict()
        self.tests_list = []

    # A self created decorator to help time methods for optimization
    @staticmethod
    def function_timer(message):
        def time_function(func):
            def wrapped_func(*args, **kwargs):
                start_time = time.time()
                func(*args, **kwargs)
                time_ran = time.time() - start_time
                print(message % time_ran)

            return wrapped_func

        return time_function

    def total_score_percentage(self):
        correct_count = 0
        for test_res in self.tests_list:
            if test_res["points"] != 0:  # Passed
                correct_count += 1
        return correct_count / len(self.tests_list)

    def count_total_incorrect(self):
        incorrect_count = 0
        for test_res in self.tests_list:
            if test_res["points"] == 0:  # Incorrect result/test
                incorrect_count += 1
        return incorrect_count

    def dump_pl_grading_result(self):
        """
        Final grades dumped to students into the results.json file.
        If total incorrect count is not 0 for any runs, student's will not get 100% grade.
        """
        print("Total Grading finished! Dumping json results!!!!")
        incorrect_count = self.count_total_incorrect()
        if incorrect_count != 0:
            self.grading_result['score'] = 0
            self.grading_result['message'] = self.REMINDER_TO_CLICK_ON_TABS_FOR_INFO_TO_STUDENTS_WHO_CANNOT_FIGURE_THINGS_OUT_ON_THEIR_OWN_GEEZE + \
                                             self.INCORRECT_COUNT_MESSAGE.format(incorrect_count)
        else:
            self.grading_result['score'] = 1 # UPDATE THIS TO 0.9 FOR EXAMS
            self.grading_result['message'] = self.REMINDER_TO_CLICK_ON_TABS_FOR_INFO_TO_STUDENTS_WHO_CANNOT_FIGURE_THINGS_OUT_ON_THEIR_OWN_GEEZE +\
                                             self.CORRECT_COUNT_MESSAGE
            if self.grading_result['score'] == 0.9:
                self.grading_result['message'] += "\n\n*NOTE: The remaining 10% will be awarded after manual grading.*"
        self.grading_result["tests"] = self.tests_list
        '''
        this is an override for grading Data Definition Language (DDL) questions
        Saturday 22:05 Feb 3rd 2024
        '''
        key = 'question_type'
        for test_result in self.tests_list:
            if test_result.get(key, '') == 'DDL':
                self.grading_result['message'] = self.REMINDER_TO_CLICK_ON_TABS_FOR_INFO_TO_STUDENTS_WHO_CANNOT_FIGURE_THINGS_OUT_ON_THEIR_OWN_GEEZE
                self.grading_result['score'] = test_result['points']
        self.pl_json_dump()  # Dump the result to the "/grade/results/results.json" file

    def pl_json_dump(self):
        # Dump the result to the "/grade/results/results.json" file
        with open(BaseGrader.PL_FINAL_RESULT_PATH, mode='w') as out:
            json.dump(self.grading_result, out)

    # def pl_output_dict(self, solution_output_string, student_output_string, student_success):
    #     """Old messaging code for printing out total table results of solution and student queries (In case if one
    #       needs to roll back.)
    #     """
    #     test_run_dict = dict()
    #     test_run_dict["name"] = "Test Number: {}".format(self.submission_count + 1)
    #
    #     if student_success:
    #         test_run_dict["message"] = BaseGrader.TEST_CORRECT_MESSAGE
    #         test_run_dict["points"] = 1
    #         test_run_dict["max_points"] = 1
    #     else:
    #         # If there are any mistakes (not 100%) students get 0
    #         test_run_dict["message"] = BaseGrader.TEST_INCORRECT_MESSAGE
    #         test_run_dict["points"] = 0
    #         test_run_dict["max_points"] = 1
    #
    #     output = ""
    #     output += "Expected results\n"
    #     output += "================\n"
    #     output += solution_output_string
    #     output += "\n\n"
    #     output += "Actual results\n"
    #     output += "==============\n"
    #     output += student_output_string
    #
    #     test_run_dict["output"] = output
    #     self.tests_list.append(test_run_dict)

    def construct_final_diffs_message(self, solution_list, student_list, student_success, string_conversion_func, header=False):
        """
        Method used to construct diff information on the results within the pl_output_dict method.
        """
        header_message = ""
        sorting_message = ""
        diff_message = ""
        error_message = ""
        table_message = ""
        hint_message = ""

        message_body = """
        *** DIFFS ***
        {}
        
        {}
        
    ============TABLE REPRESENTATION OF SOLUTION & YOUR OUTPUT============
        {}
        """
        if header:
            try:
                student_header = student_list[0]
            except IndexError as e:
                error_message += "Your result is empty! (Empty as in not even Headers of Table Exists! Check the slides!\n"

            try:
                solution_header = solution_list[0]
                header_result = student_header == solution_header
                if not header_result:
                    error_message += "Your Table column header didn't match that of the solution!\n"

            except Exception as e:
                error_message += "Error with solution code or database data. Contact course staff about this problem!\n"

        solution_set = set(solution_list)
        student_set = set(student_list)

        solution_diff_set = solution_set.difference(student_set)
        student_diff_set = student_set.difference(solution_set)

        diff_message += self.construct_diff_message('+', solution_list, solution_diff_set, string_conversion_func)
        diff_message += "\n"
        diff_message += self.construct_diff_message('-', student_list, student_diff_set, string_conversion_func)
        if len(diff_message.strip()) == 0:
            diff_message = "*** NO DIFFS IN DATA ***"
            if not student_success:
                sorting_message = "No discrepancy in data. Check if it could be related to \"SORTING\"."

        table_message += "\n\nEXPECTED RESULTS\n==============="
        table_message += self.construct_diff_message('+', solution_list, solution_diff_set, string_conversion_func,
                                                        print_table=True)

        table_message += "\n\n\nACTUAL RESULTS\n==============="
        table_message += self.construct_diff_message('-', student_list, student_diff_set, string_conversion_func,
                                                        print_table=True)

        if sorting_message or error_message:
            hint_message += "* HINT *\n" + sorting_message + "\n" + error_message

        if student_success:
            header_message = BaseGrader.TEST_CORRECT_MESSAGE
        else:
            header_message = """
DIFFS Explanation:
'+': Means the correct data entry in the solution your result missed!
'-': Means the incorrect data entry in your result that is not part of the solution!
"""

        return header_message, message_body.format(diff_message, hint_message, table_message)

    def construct_diff_message(self, type_char, type_list, type_diff_set, string_conversion_func, print_table=False):
        result_string = ""
        for data in type_list:
            if data in type_diff_set:
                result_string += "\n{}  {}".format(type_char, string_conversion_func(data))
            elif print_table:
                result_string += "\n{}".format(string_conversion_func(data))
        return result_string

    @staticmethod
    def tuple_to_string(tuple_data):
        # Used for SQL hw message formatting implementation of the pl_output_dict method
        return ' '.join([str(data) for data in tuple_data])

    @staticmethod
    def data_message_string_function(tuple_data):
        # Provided for neo4j & MongoDB HW
        # to work around the message formatting implementation (A function must be provided
        # for the pl_output_dict method signature
        return str(tuple_data)

    @staticmethod
    def data_return_function(tuple_data):
        # Provided for Stored Procedure SQL Instances. Could also delete this and use the data_message_string_function
        # to work around the message formatting implementation (A function must be provided
        # for the pl_output_dict method signature
        return tuple_data

    def pl_output_dict(self, solution_list, student_list, student_success, string_conversion_func):
        test_run_dict = dict()
        test_run_dict["name"] = "Test Number: {}".format(self.submission_count + 1)

        header_message, message_body = self.construct_final_diffs_message(solution_list, student_list, student_success,
                                                                          string_conversion_func)

        test_run_dict["message"] = header_message
        if student_success:
            test_run_dict["points"] = 1
            test_run_dict["max_points"] = 1
        else:
            # If there are any mistakes (not 100%) students get 0
            test_run_dict["points"] = 0
            test_run_dict["max_points"] = 1

        test_run_dict["output"] = message_body
        self.tests_list.append(test_run_dict)

    @staticmethod
    def record_failure_and_exit(msg, record_file=PL_FINAL_RESULT_PATH):
        grading_result = {
            'score': 0.0,
            'succeeded': False,
            'message': msg,
        }
        with open(record_file, mode='w') as out:
            json.dump(grading_result, out)
        sys.exit(0)

    @staticmethod
    def list_of_tuples_to_string(elems):
        out = ""
        for elem in elems:
            first = True
            for val in elem:
                if not first:
                    out += " "
                else:
                    first = False
                out += str(val)
            out += "\n"
        return out

    @staticmethod
    def list_of_dict_to_string(dict_list):
        result_output = ''
        for elem in dict_list:
            result_output += json.dumps(elem)
            result_output += "\n"

        return result_output

    def run(self):
        while self.submission_count < self.submission_num:
            print("[Base Grader] Number of current test run: {}...".format(self.submission_count + 1))
            self.grading_function(self)  # Inject self instance into grading function
            self.submission_count += 1
        print("Finished Loop. Calling dump_pl_grading_result to dump json result file to PL.")
        self.dump_pl_grading_result()


if __name__ == "__main__":
    print(StudentWrongAnswerError)
