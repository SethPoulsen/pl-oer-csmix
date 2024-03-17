"""
This is the Faster/performance tuned entry point for Neo4j at the moment (2020/04/17).
The combination is with the other two performance tuned python files:
neo4j_csv_dataset_generator.py & neo4j_native_cypher_grader.py
Point to this file as the main entry from the shell script!
"""


import neo4j_csv_dataset_generator
from base_grader import BaseGrader
from neo4j_native_cypher_grader import Neo4jGrader, AUTOMATE_STUDENT_SUBMISSION_COUNT

import time

class GradeMaster: # Stores data on previous grades

	def __init__(self):
		self.prev_data = False

	def student_grading_function(self, base_grader_obj):
		start_time = time.time()
		data_generator = neo4j_csv_dataset_generator.Neo4jDataGenerator()
		data_generator.generate_data()
		print("[n_g_c_m] All data generated: %s seconds" % (time.time() - start_time))
		sql_grader = Neo4jGrader(base_grader_obj)
		self.prev_data = sql_grader.grade(self.prev_data) # Solution list, student list, success
		print("[n_g_c_m] Grading completed: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
	gradeMaster = GradeMaster()
	grader = BaseGrader(gradeMaster.student_grading_function, AUTOMATE_STUDENT_SUBMISSION_COUNT)
	grader.run()
