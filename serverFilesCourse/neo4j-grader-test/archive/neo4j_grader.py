import json
import neo4j
import random
import sys
import time  # For timing neo4j transactions
import os.path
import py2neo
from py2neo import Graph, Node, Relationship, NodeMatcher
from base_grader import BaseGrader


AUTOMATE_STUDENT_SUBMISSION_COUNT = 5
NEO4J_HOST_ADDR = 'http://127.0.0.1:7474'
NEO4J_BOLT_URI = 'bolt://127.0.0.1:7687'
ACTOR_NODES_TXT = 'actor-nodes.txt'
MOVIE_NODES_TXT = 'movie-nodes.txt'
RELATIONSHIP_TXT = 'relationships.txt'
FRIEND_RELATIONSHIP_TXT = 'friendRelationships.txt'
FILE_OPEN_MODE = 'w+'
DUMP_SQL_PATH = '/grade/tests/dump.sql'
STUDENT_QUERY_PATH = '/grade/student/query.cypher'
STUENT_SORT_QUERY_PATH = '/grade/student/sort_query.cypher'
SOLUTION_QUERY_PATH = '/grade/tests/solution.cypher'

# Cypher Query strings
DETACH_DELETE_ALL_NODES = "MATCH (n) DETACH DELETE n"


class Neo4jGrader:

    def __init__(self, base_grader_obj):
        # print(py2neo.__version__)  # 4.2.0
        self.base_grader_obj = base_grader_obj
        self.g = Graph(NEO4J_HOST_ADDR)
        self.tx = self.g.begin()
        self.star_id_node_map = {}
        self.movie_id_node_map = {}
        # If `dump.sql` is present, that means we'll need to just execute
        # the solution and student queries without inspecting their output,
        # and then run the dump to compare the table state after.
        self.is_modification = os.path.isfile(DUMP_SQL_PATH)
        if self.is_modification:
            try:
                with open(DUMP_SQL_PATH) as dump_file:
                    self.dump_query = dump_file.read()
            except Exception as e:
                BaseGrader.record_failure_and_exit("Error in path {}".format(DUMP_SQL_PATH) + str(e))

        self.student_query_exists = os.path.isfile(STUDENT_QUERY_PATH)
        self.student_sort_query_exists = os.path.isfile(STUENT_SORT_QUERY_PATH)

    @BaseGrader.function_timer("[Neo4jGrader - DELETION TIMER] --- %s seconds ---")
    def cleanup_database(self):
        print("[Neo4jGrader] Cleaning up Neo4j Database (Detaching and Deleting nodes...)")
        deleted_results = self.g.run(DETACH_DELETE_ALL_NODES)
        print("[Neo4jGrader - Deletor] DELETED RESULTS: ", deleted_results)

    @BaseGrader.function_timer("[Neo4jGrader - ACTOR NODES CREATION TIMER] --- %s seconds ---")
    def create_actor_nodes(self):
        with open(ACTOR_NODES_TXT) as f:
            for l in f.read().splitlines():
                lst = l.split("\t")
                s = Node("Actor", actor_name=lst[1], birth_year=int(lst[2]), birth_country=lst[3])
                self.star_id_node_map[lst[0]] = s
                self.tx.create(s)

    @BaseGrader.function_timer("[Neo4jGrader - MOVIE NODES CREATION TIMER] --- %s seconds ---")
    def create_movie_nodes(self):
        with open(MOVIE_NODES_TXT) as f:
            for l in f.read().splitlines():
                lst = l.split("\t")
                m = Node("Movie", movie_name=lst[1], release_year=int(lst[2]), ratings=int(lst[3]), genre=lst[4])
                self.movie_id_node_map[lst[0]] = m
                self.tx.create(m)

    @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (ActedIn) CREATION TIMER] --- %s seconds ---")
    def create_relationship(self):
        with open(RELATIONSHIP_TXT) as f:
            for l in f.read().splitlines():
                s_id, m_id = l.split("\t")
                s_node = self.star_id_node_map[s_id]
                m_node = self.movie_id_node_map[m_id]
                self.tx.create(Relationship(s_node, "ActedIn", m_node))

    @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (FriendWith) CREATION TIMER] --- %s seconds ---")
    def create_friend_relationship(self):
        with open(FRIEND_RELATIONSHIP_TXT) as f:
            for l in f.read().splitlines():
                s_id, f_id = l.split("\t")
                s_node = self.star_id_node_map[s_id]
                f_node = self.star_id_node_map[f_id]
                self.tx.create(Relationship(s_node, "FriendWith", f_node))

    def print_friends_of(self, tx, name):
        for record in tx.run("MATCH (a:Person)-[:KNOWS]->(f) "
                             "WHERE a.name = {name} "
                             "RETURN f.name", name=name):
            print(record["f.name"])

    @BaseGrader.function_timer("[Neo4jGrader - TOTAL DATASET CREATION TIMER] --- %s seconds ---")
    def create_dataset_in_DB(self):
        self.cleanup_database()
        print("Injecting data into database")
        self.create_actor_nodes()
        self.create_movie_nodes()
        self.create_relationship()
        self.create_friend_relationship()
        self.tx.commit()

    def get_solution_query_tuple(self) -> (list, str):
        # Generate solution rows based on the solution query
        sol = ''
        solution_docs = []
        try:
            with open(SOLUTION_QUERY_PATH) as solution_file:
                solution_query = solution_file.read()

            if True:
                solution_cursor = self.g.run(solution_query)
                for rel in solution_cursor:
                    sol += json.dumps(rel)
                    sol += "\n"
                    for ele in rel:
                        solution_docs.append(json.dumps(ele))

        except Exception as e:
            BaseGrader.record_failure_and_exit("Error in solution query: " + str(e))
        return solution_docs, sol

    def get_student_query_tuple(self) -> (list, str):
        std_sol = ''
        student_docs = []
        try:
            if self.student_query_exists:
                with open(STUDENT_QUERY_PATH) as student_file:
                    student_query = student_file.read()
            else:
                with open(STUENT_SORT_QUERY_PATH) as student_file:
                    student_query = student_file.read()

            student_cursor = self.g.run(student_query)
            for rel in student_cursor:
                std_sol += json.dumps(rel)
                std_sol += "\n"
                for ele in rel:
                    student_docs.append(json.dumps(ele))

        except Exception as e:
            BaseGrader.record_failure_and_exit(str(e))

        return student_docs, std_sol

    def grade(self):
        self.create_dataset_in_DB()
        print("[GRADER] Running grading...")
        solution_docs, expected_output = self.get_solution_query_tuple()
        student_docs, actual_output = self.get_student_query_tuple()
        success = False
        if self.student_query_exists:
            flag_1 = True
            for i in solution_docs:
                if i not in student_docs:
                    flag_1 = False
                    break
            flag_2 = True
            for i in student_docs:
                if i not in solution_docs:
                    flag_2 = False
                    break

            if flag_1 and flag_2:
                success = True
            else:
                success = False

        elif self.student_sort_query_exists:
            flag = True
            if len(solution_docs) != len(student_docs):
                flag = False
            if flag:
                for i in range(len(solution_docs)):
                    if solution_docs[i] != student_docs[i]:
                        flag = False
                        break
            if flag:
                success = True
            else:
                success = False

        self.base_grader_obj.pl_output_dict(expected_output, actual_output, success)


if __name__ == "__main__":
    # Provided only for testing this module separately (by changing within the run.sh to "python3 -m [module_name]")
    def student_grading_function(base_grader_obj):
        # run grader
        neo_grader = Neo4jGrader(base_grader_obj)
        neo_grader.grade()


    grader = BaseGrader(student_grading_function, 3)
    grader.run()

