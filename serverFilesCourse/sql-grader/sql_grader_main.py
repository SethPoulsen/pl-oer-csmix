import sys
import sql_dataset_generator
from base_grader import BaseGrader
from sql_grader import SqlGrader, AUTOMATE_STUDENT_SUBMISSION_COUNT


def student_grading_function(base_grader_obj):
    data_generator = sql_dataset_generator.SqlDataGenerator()
    data_generator.generate_data()

    sql_grader = SqlGrader(base_grader_obj)
    sql_grader.grade()


def student_grading_function_ddl(base_grader_obj):
    data_generator = sql_dataset_generator.SqlDataGenerator()
    data_generator.generate_data()

    sql_grader = SqlGrader(base_grader_obj)
    sql_grader.grade_ddl()


def student_grading_function_sp(base_grader_obj):
    data_generator = sql_dataset_generator.SqlDataGenerator()
    data_generator.generate_data()

    sql_grader = SqlGrader(base_grader_obj)
    sql_grader.grade_sp()


if __name__ == "__main__":
    # This is used to determine which script has been run (The normal ones or the Stored Procedure ones) and
    # run the corresponding auto-grading functionality.
    if len(sys.argv) == 1:
        grader = BaseGrader(student_grading_function, AUTOMATE_STUDENT_SUBMISSION_COUNT)
        grader.run()
    elif sys.argv[1] == 'ddl':
        grader = BaseGrader(student_grading_function_ddl, 1)
        grader.run()
    elif sys.argv[1] == "grade_sp":
        grader = BaseGrader(student_grading_function_sp, AUTOMATE_STUDENT_SUBMISSION_COUNT)
        grader.run()
    else:
        print('error unknown argument:', sys.argv)
