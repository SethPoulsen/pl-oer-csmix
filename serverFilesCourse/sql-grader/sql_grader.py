import json
import mysql.connector
import sqlparse
import os.path
import re
from base_grader import BaseGrader
import grade_ddl


AUTOMATE_STUDENT_SUBMISSION_COUNT = 5  # For tuning of how many runs done automatically for students
DB_USER = "root"
DB_PASSWORD = "password"


class SqlGrader:
    DATABASE_CREATION_STRING = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'"
    USE_DATABASE_STRING = "USE {}"
    DATABASE_DELETION_STRING = "DROP DATABASE IF EXISTS {}"
    SETUP_SQL_PATH = "/grade/tests/setup.sql"
    DUMP_SQL_PATH = '/grade/tests/dump.sql'

    SOLUTION_SQL_QRY_PATH = '/grade/tests/solution.sql'
    STUDENT_SQL_QRY_PATH = '/grade/run/bin/query.sql'

    def __init__(self, base_grader_obj):
        self.base_grader_obj = base_grader_obj
        self.cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD)
        self.is_modification = os.path.isfile(SqlGrader.DUMP_SQL_PATH)
        if self.is_modification:
            with open(SqlGrader.DUMP_SQL_PATH) as dump_file:
                self.dump_query = dump_file.read()

    def create_and_use_database(self, cnx, name):
        """
        Creates a new database with the given name, populates it with data from the
        "setup.sql" file, and sets that database as the current database. Returns a
        cursor for use

        :param cnx: Database connection object of mysql.connector.connect()
        :param name: Name of the database to use
        :return: cnx.cursor()
        """
        cursor = cnx.cursor()
        # Before creating database. Make sure to empty it and clean it out fully first before each loop
        self.clean_up_database(name)
        # Now create database to make it ready for this grading run
        cursor.execute(SqlGrader.DATABASE_CREATION_STRING.format(name))
        cursor.execute(SqlGrader.USE_DATABASE_STRING.format(name))

        # Populate database
        with open(SqlGrader.SETUP_SQL_PATH) as setup_queries_file:
            setup_queries_raw = setup_queries_file.read()
            setup_queries = sqlparse.split(setup_queries_raw)
            for query in setup_queries:
                cursor.execute(query)
        return cursor

    def setup_role_query_execution(self, role):
        # Helper function to help setup and using database cursor for either students or solution
        sql_query_path = ""
        if role == "solution":
            sql_query_path = SqlGrader.SOLUTION_SQL_QRY_PATH
        elif role == "student":
            sql_query_path = SqlGrader.STUDENT_SQL_QRY_PATH

        try:
            with open(sql_query_path) as role_file:
                role_query = role_file.read()               
            role_cursor = self.create_and_use_database(self.cnx, role)
        except Exception as query_error:
            raise query_error

        return role_cursor, role_query

    def get_SP_query_list_tuple(self, role):
        # Generate solution rows based on the solution query
        try:
            role_cursor, role_query = self.setup_role_query_execution(role)
            
            # This prevents passing comments into the cursor.execute() function that causes errors
            # see https://stackoverflow.com/questions/11583083/python-mysql-commands-out-of-sync-you-cant-run-this-command-now
            role_query = re.sub(r'(--.*)|(((/\*)+?[\w\W]+?(\*/)+))', '', role_query)
            
            role_cursor.execute(role_query)
        except Exception as e:
            BaseGrader.record_failure_and_exit("Error in {} query[1]: ".format(role) + str(e))

        try:
            if role == "solution":
                role_cursor.callproc('Result2')
            else:
                role_cursor.callproc('Result')

            # Lists for saving query results based on roles provided
            role_rows = []

            for role_row in role_cursor.stored_results():
                role_rows.append(role_row.fetchall())
            if self.is_modification:
                role_rows.clear()
                role_cursor.execute(self.dump_query)
                for role_row in role_cursor:
                    role_rows.append(role_row)
        except Exception as e2:
            BaseGrader.record_failure_and_exit("Error in {} query[2]: ".format(role) + str(e2))

        return role_rows, role_rows

    def get_query_list_tuple(self, role):
        # Generate solution rows based on the solution query
        try:
            role_cursor, role_query = self.setup_role_query_execution(role)
            # role_cursor.execute(role_query)
            setup_role_queries = sqlparse.split(role_query)
            for query in setup_role_queries:
                role_cursor.execute(query)

            # Lists for saving query results based on roles provided
            role_rows = []
            role_rows_returned = []

            # Even if this is a query that will be checked by a dump,
            # we still need to clear the cursor
            if role_cursor.description is not None:
                role_rows_returned.append(tuple([x[0] for x in role_cursor.description]))
                role_rows_returned.append("- - - -" for x in role_cursor.description)

            for role_row in role_cursor:
                role_rows.append(role_row)
                role_rows_returned.append(role_row)
            if self.is_modification:
                role_rows.clear()
                role_cursor.execute(self.dump_query)

                if role_cursor.description is not None:
                    role_rows_returned.append(tuple([x[0] for x in role_cursor.description]))

                for role_row in role_cursor:
                    role_rows.append(role_row)
                    role_rows_returned.append(role_row)

        except Exception as e:
            print(str(e))
            if role == "solution":
                BaseGrader.record_failure_and_exit("Error in solution query: " + str(e))
            elif role == "student":
                BaseGrader.record_failure_and_exit(str(e))

        return role_rows, role_rows_returned

    def clean_up_database(self, role_name):
        # Used to cleanup the database before each automated run and grading action
        cursor = self.cnx.cursor()
        cursor.execute(SqlGrader.DATABASE_DELETION_STRING.format(role_name))
        print("Cleaning up Database...")

    def grade(self):
        solution_rows, solution_rows_returned = self.get_query_list_tuple("solution")
        student_rows, student_rows_returned = self.get_query_list_tuple("student")

        success = True
        if len(solution_rows) != len(student_rows):
            success = False
        else:
            for row_pair in zip(solution_rows, student_rows):
                if len(row_pair[0]) != len(row_pair[1]):
                    success = False
                for val_pair in zip(row_pair[0], row_pair[1]):
                    if val_pair[0] != val_pair[1]:
                        success = False
                        break

        # # Original Table output representation only
        # expected_output = BaseGrader.list_of_tuples_to_string(solution_rows_returned)
        # actual_output = BaseGrader.list_of_tuples_to_string(student_rows_returned)
        # self.base_grader_obj.pl_output_dict(expected_output, actual_output, success)

        # Updated output with diffs in Table format and other prompts
        self.base_grader_obj.pl_output_dict(solution_rows, student_rows, success, BaseGrader.tuple_to_string)

    def grade_ddl(self):
        # 13:00 Tuesday Nov 14 2023
        print('start grade_ddl()')
        def _execute_file(cursor, path):
            with open(path) as r:
                for query in sqlparse.split(r.read()):
                    # remove comments
                    query = re.sub(r'(--.*)|(((/\*)+?[\w\W]+?(\*/)+))', '', query)
                    cursor.execute(query)
        def _query_result(file_name):
            # initialize an empty database
            role = file_name.split('.')[0]
            cursor = self.cnx.cursor()
            self.clean_up_database(role)
            cursor.execute(SqlGrader.DATABASE_CREATION_STRING.format(role))
            cursor.execute(SqlGrader.USE_DATABASE_STRING.format(role))
            # setup if ddl_setup.sql exits
            if os.path.isfile(grade_ddl.SETUP_PATH):
                '''
                in the same folder of solution.sql
                if setup.sql exits, then it sets up the database for each test case
                '''
                _execute_file(cursor, grade_ddl.SETUP_PATH)
            # read solution and student sql file
            if file_name == grade_ddl.STUDENT_FILE:
                path = grade_ddl.STUDENT_DIR + file_name
            else:
                path = grade_ddl.SOLUTION_DIR + file_name
            try:
                _execute_file(cursor, path)
            except Exception as e:
                print(str(e))
                if file_name == grade_ddl.STUDENT_FILE:
                    BaseGrader.record_failure_and_exit(str(e))
                else:
                    err = 'Error in `%s`: %s' % (file_name, e)
                    BaseGrader.record_failure_and_exit(err)
            # collect result from SHOW CREATE TABLE
            cursor.execute('SHOW TABLES;')
            table_1d = list()
            for row in cursor:
                table_1d.append(row[0])
            result = dict()
            for table in table_1d:
                cursor.execute('SHOW CREATE TABLE %s;' % (str(table)))
                for row in cursor:
                    result[table] = grade_ddl.parse_schema(row[1])
            return result
        # read solution
        with open(grade_ddl.CONFIG_PATH, 'r', encoding='utf-8') as r:
            config = json.load(r)
        solutions = list()
        for name in config.get('#solutions', list()):
            solutions.append(_query_result(name))
        # read student
        student = _query_result(grade_ddl.STUDENT_FILE)
        # grade
        best_score, message, grade_output = grade_ddl.grade(solutions, student)
        # override self.base_grader_obj.pl_output_dict method
        # base grader treats greater than 0 as correct, max points is 1.
        test_run_dict = {
            'max_points': 1,
            'message': ('Score %.2f/1.\n' % (best_score)) + message,
            'name': 'Test Number: 1',
            'output': grade_output,
            'points': best_score,
            'question_type': 'DDL',
        }
        self.base_grader_obj.tests_list.append(test_run_dict)

    def grade_sp(self):
        solution_rows, solution_rows_returned = self.get_SP_query_list_tuple("solution")
        student_rows, student_rows_returned = self.get_SP_query_list_tuple("student")

        success = True
        if len(solution_rows) != len(student_rows):
            success = False
        else:
            for row_pair in zip(solution_rows, student_rows):
                if len(row_pair[0]) != len(row_pair[1]):
                    success = False
                for val_pair in zip(row_pair[0], row_pair[1]):
                    if val_pair[0] != val_pair[1]:
                        success = False
                        break

        # # Original Table output representation only
        # expected_output = BaseGrader.list_of_tuples_to_string(solution_rows_returned)
        # actual_output = BaseGrader.list_of_tuples_to_string(student_rows_returned)
        # self.base_grader_obj.pl_output_dict(expected_output, actual_output, success)

        # Updated output with diffs in Table format and other prompts
        def output_list(list_of_list_of_tuples):
            """
            Because Stored Procedure contains a list of list of tuples of data entry (Tongue twister, I know lol),
            in order to use it on the new message functionality, we need to change it to list of string representation
            of tuples then use the data_return_function to just return the data later on within the pl_output_dict
            final function ==> Because lists are unhashable within sets -> which is used for the DIFF formatting.
            """
            ans_list = list_of_list_of_tuples[0]
            return ['(' + ', '.join([str(d) for d in data]) + ')' for data in ans_list]

        solution_str_list = output_list(solution_rows)
        student_str_list = output_list(student_rows)

        self.base_grader_obj.pl_output_dict(solution_str_list, student_str_list, success, BaseGrader.data_return_function)


if __name__ == "__main__":
    # Provided only for testing this module separately (by changing within the run.sh to "python3 -m [module_name]")
    def student_grading_function(base_grader_obj):
        # run grader
        sql_grader = SqlGrader(base_grader_obj)
        sql_grader.grade()


    grader = BaseGrader(student_grading_function, 3)
    grader.run()
