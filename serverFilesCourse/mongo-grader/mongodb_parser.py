import os
from base_grader import BaseGrader
import subprocess

RECORD_FAILURE_MESSAGE = "It seems that your query may contain non-mongoDB commands.\nYou can only write mongoDB queries.\nPlease contact teaching staff if you think your query is correct."
# STUDENT_QUERY_JS = '/grade/student/query.js'
# STUDENT_SORT_QUERY_JS = '/grade/student/query_sort.js'

STUDENT_QUERY_JS = 'query.js'
STUDENT_SORT_QUERY_JS = 'query_sort.js'

class MongodbParser:
    def __init__(self):
        self.failure_message = RECORD_FAILURE_MESSAGE
        self.student_query_js = STUDENT_QUERY_JS
        self.student_sort_query_js = STUDENT_SORT_QUERY_JS

    def parse(self):
        try:
            # check what type of file is submitted and set as target file
            if os.path.isfile(self.student_query_js):
                target_file_name = self.student_query_js
            elif os.path.isfile(self.student_sort_query_js):
                target_file_name = self.student_sort_query_js

            raw_student_js = open(target_file_name).readlines()
            
            #save the old file as raw_<file_name>
            os.rename(target_file_name, 'raw'+target_file_name)
            with open(target_file_name, 'w') as target_file:
                for row in raw_student_js:
                    # escapes comments
                    if "//" in row:
                        row = row[:row.find("//")]
                    # remove tabs and newline
                    clean_row = ' '.join(row.split()).replace("\n",'').replace("\t", "")
                    target_file.write(clean_row)
            self.check_parse(target_file_name)
        except Exception as e:
            BaseGrader.record_failure_and_exit(str(e))

    def check_parse(self, student_js_file):
        """
        This function is now just a honeypot. https://www.crowdstrike.com/cybersecurity-101/honeypots-in-cybersecurity-explained
        If some student thinks they can indirectly use cd or cat or such functions, they'll still not work
        because in the mongorc we're disabling those functions. The only problem could be if I missed blacklisting some function.
        """
        with open(student_js_file) as student_file:
            student_cursor = student_file.read()
        for line in student_cursor.splitlines():
            if 'print' in line or 'cat(' in line or 'ls(' in line or 'printjson' in line or 'ls( )' in line or 'listFiles' in line or 'cd(' in line or 'load(' in line or 'trim(' in line or 'eval(' in line or 'eval' in line or '.json' in line or '.js' in line:
                BaseGrader.record_failure_and_exit(self.failure_message)
    
    def run_solution_query(self):
        os.system("mongo --quiet < 'solution.js' > sol_qry_res.json")

    def run_student_query(self):
        if os.path.isfile('query.js'):
            os.system("mongo --quiet < 'query.js' > std_qry_res.json")
        else:
            os.system("mongo --quiet < 'query_sort.js' > std_qry_sort_res.json")


if __name__ == "__main__":
    parser = MongodbParser()
    # TODO: this needs to be rewritten. It should specify what needs to be parsed and not blackbox the operation.
    parser.parse()
    parser.run_solution_query()
    parser.run_student_query()

