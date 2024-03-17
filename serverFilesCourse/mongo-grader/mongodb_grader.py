import json
import os
import re
from base_grader import BaseGrader


AUTOMATE_STUDENT_SUBMISSION_COUNT = 5
MONGODB_ADDRESS = 'mongodb://127.0.0.1:27017/'
# SOLUTION_QUERY_JSON_PATH = '/grade/tests/sol_qry_res.json'
# STUDENT_QUERY_JSON_PATH = '/grade/student/std_qry_res.json'
# STUDENT_QUERY_SORT_JSON_PATH = '/grade/student/std_qry_sort_res.json'

SOLUTION_QUERY_JSON_PATH = 'sol_qry_res.json'
STUDENT_QUERY_JSON_PATH = 'std_qry_res.json'
STUDENT_QUERY_SORT_JSON_PATH = 'std_qry_sort_res.json'


class MongodbGrader:
    REGEX_SUBSTITUTION_RAW_STRING = r'ObjectId\s*\(\s*\"(\S+)\"\s*\)'
    REGEX_REPL = r'{"$oid": "\1"}'

    def __init__(self, base_grader_obj, sol_qry_json_path, student_qry_json_path, student_qry_sort_json_path):
        self.base_grader_obj = base_grader_obj
        self.mongo_address = MONGODB_ADDRESS
        self.sol_qry_json_path = sol_qry_json_path
        self.student_qry_json_path = student_qry_json_path
        self.student_qry_sort_json_path = student_qry_sort_json_path

    def grade(self):
        try:
            with open(self.sol_qry_json_path) as solution_file:
                solution_cursor = solution_file.read()

        except Exception as e:
            BaseGrader.record_failure_and_exit("Error in solution query: " + str(e))

        try:
            exists = os.path.isfile(self.student_qry_json_path)
            sort_exists = os.path.isfile(self.student_qry_sort_json_path)
            if exists:
                with open(self.student_qry_json_path) as student_file:
                    student_cursor = student_file.read()
            else:
                with open(self.student_qry_sort_json_path) as student_file:
                    student_cursor = student_file.read()

        except Exception as e:
            BaseGrader.record_failure_and_exit(str(e))

        solution_dict_list = []
        student_dict_list = []

        try:
            # parse student answer
            illegal_format = False
            for line in student_cursor.splitlines():
                if line != "" and line[0] == "{" or line.isdigit():
                    if "ObjectId" in line:
                        line = re.sub(MongodbGrader.REGEX_SUBSTITUTION_RAW_STRING, MongodbGrader.REGEX_REPL, line)
                        # line = re.sub(r'ObjectId\s*\(\s*\"(\S+)\"\s*\)', r'{"$oid": "\1"}', line)
                    student_dict_list.append(eval(line))
        except Exception as e:
            BaseGrader.record_failure_and_exit(str(e))

        # Parse the solutions' answer
        for line in solution_cursor.splitlines():
            if line != "" and line[0] == "{" or line.isdigit():
                if 'ObjectId' in line:
                    line = re.sub(MongodbGrader.REGEX_SUBSTITUTION_RAW_STRING, MongodbGrader.REGEX_REPL, line)
                solution_dict_list.append(eval(line))


        success = False
        if exists:
            flag_1 = True
            for i in solution_dict_list:
                if i not in student_dict_list:
                    flag_1 = False
                    break
            flag_2 = True
            for i in student_dict_list:
                if i not in solution_dict_list:
                    flag_2 = False
                    break

            if flag_1 and flag_2:
                success = True
            else:
                success = False

        elif sort_exists:
            flag = True
            if len(solution_dict_list) != len(student_dict_list):
                flag = False
            if flag:
                for i in range(len(solution_dict_list)):
                    if solution_dict_list[i] != student_dict_list[i]:
                        flag = False
                        break
            if flag:
                success = True
            else:
                success = False

        solution_dict_string_list = [json.dumps(dict_data) for dict_data in solution_dict_list]
        student_dict_string_list = [json.dumps(dict_data) for dict_data in student_dict_list]

        # # Previous message code for only outputing table of both solution and student query results
        # expected_output_string = BaseGrader.list_of_dict_to_string(solution_dict_list)
        # actual_output_string = BaseGrader.list_of_dict_to_string(student_dict_list)
        # self.base_grader_obj.pl_output_dict(expected_output_string, actual_output_string, success)

        # Updated code for messaging diffs between student and solution answer
        self.base_grader_obj.pl_output_dict(solution_dict_string_list, student_dict_string_list, success,
                                            BaseGrader.data_message_string_function)


if __name__ == "__main__":
    # Provided only for testing this module separately (by changing within the run.sh to "python3 -m [module_name]")
    def student_grading_function(base_grader_obj):
        # run grader
        mongo_grader = MongodbGrader(base_grader_obj, SOLUTION_QUERY_JSON_PATH, STUDENT_QUERY_JSON_PATH,
                                     STUDENT_QUERY_SORT_JSON_PATH)
        mongo_grader.grade()


    grader = BaseGrader(student_grading_function, AUTOMATE_STUDENT_SUBMISSION_COUNT)
    grader.run()
