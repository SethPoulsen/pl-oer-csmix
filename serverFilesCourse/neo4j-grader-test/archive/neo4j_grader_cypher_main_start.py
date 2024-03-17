"""
This is the Faster/performance tuned entry point for Neo4j at the moment (2020/04/17).
The combination is with the other two performance tuned python files:
neo4j_csv_dataset_generator.py & neo4j_native_cypher_grader.py
Point to this file as the main entry from the shell script!
"""


import neo4j_csv_dataset_generator
from base_grader import BaseGrader
from neo4j_native_cypher_grader import Neo4jGrader, AUTOMATE_STUDENT_SUBMISSION_COUNT


def student_grading_function(base_grader_obj):
    data_generator = neo4j_csv_dataset_generator.Neo4jDataGenerator()
    data_generator.generate_data()

    sql_grader = Neo4jGrader(base_grader_obj)
    sql_grader.grade()


if __name__ == "__main__":
    grader = BaseGrader(student_grading_function, AUTOMATE_STUDENT_SUBMISSION_COUNT)
    grader.run()
