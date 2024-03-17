import json
import neo4j
import random
import sys
import time  # For timing neo4j transactions
import os.path
import py2neo
from py2neo import Graph, Node, Relationship, NodeMatcher
from base_grader import BaseGrader
from os.path import exists


AUTOMATE_STUDENT_SUBMISSION_COUNT = 5
NEO4J_HOST_ADDR = 'http://127.0.0.1:7474'
NEO4J_BOLT_URI = 'bolt://127.0.0.1:7687'
FILE_OPEN_MODE = 'w+'
DUMP_SQL_PATH = '/grade/tests/dump.sql'
STUDENT_QUERY_PATH = '/grade/student/query.cypher'
STUENT_SORT_QUERY_PATH = '/grade/student/sort_query.cypher'
SOLUTION_QUERY_PATH = '/grade/tests/solution.cypher'
SETTINGS_PATH = '/grade/settings.json'

# Database data generation/delete(cleanup) commands in Cypher
DETACH_DELETE_ALL_NODES = "MATCH (n) DETACH DELETE n"
CREATE_PERSON_NODES_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///person-nodes-cypher.csv'
AS line
MERGE (person:Person {person_id: toInteger(line.person_id),
                    person_name: line.person_name,
                    birth_year: toInteger(line.birth_year)});
"""

CREATE_PERSON1_NODES_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///person-nodes-cypher.csv'
AS line
MERGE (person:Person1 {person_id: toInteger(line.person_id),
                    person_name: line.person_name,
                    birth_year: toInteger(line.birth_year)});
"""

CREATE_RESTAURANT_NODES_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///restaurant-nodes-cypher.csv'
AS line
MERGE (restaurant:Restaurant {restaurant_id: toInteger(line.restaurant_id),
                    restaurant_name: line.restaurant_name,
                    established_year: toInteger(line.established_year),
                    ratings: toInteger(line.ratings)});
"""
CREATE_RESTAURANT1_NODES_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///restaurant-nodes-cypher.csv'
AS line
MERGE (restaurant:Restaurant1 {restaurant_id: toInteger(line.restaurant_id),
                    restaurant_name: line.restaurant_name,
                    established_year: toInteger(line.established_year),
                    ratings: toInteger(line.ratings)});
"""
CREATE_PERSON_LIKED_RESTAURANT_RELATIONSHIP_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///personToRestaurant-cypher.csv'
AS line
MERGE (person:Person {person_id: toInteger(line.person_id)})
MERGE (restaurant:Restaurant {restaurant_id: toInteger(line.restaurant_id)})
MERGE (person)-[r:LIKED]->(restaurant);
"""

CREATE_PERSON1_LIKED_RESTAURANT1_RELATIONSHIP_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///personToRestaurant-cypher.csv'
AS line
MERGE (person:Person1 {person_id: toInteger(line.person_id)})
MERGE (restaurant:Restaurant1 {restaurant_id: toInteger(line.restaurant_id)})
MERGE (person)-[r:LIKED]->(restaurant);
"""

CREATE_PERSON_FRIENDSWITH_PERSON_RELATIONSHIP_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///personToPerson-cypher.csv'
AS line
MATCH (person1:Person {person_id: toInteger(line.person1_id)}), (person2:Person {person_id: toInteger(line.person2_id)})
MERGE (person1)-[:FRIENDS_WITH]-(person2);
"""

CREATE_CUISINE_NODES_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///cuisine-nodes-cypher.csv'
AS line
MERGE (cuisine:Cuisine {cuisine_id: toInteger(line.cuisine_id),
                    cuisine_name: line.cuisine_name});
"""

CREATE_RESTAURANT_SERVES_CUISINE_RELATIONSHIP_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///restaurantToCuisine-cypher.csv'
AS line
MERGE (restaurant:Restaurant {restaurant_id: toInteger(line.restaurant_id)})
MERGE (cuisine:Cuisine {cuisine_id: toInteger(line.cuisine_id)})
MERGE (restaurant)-[r:SERVES]->(cuisine);
"""

CREATE_CITY_NODES_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///city-nodes-cypher.csv'
AS line
MERGE (city:City {city_id: toInteger(line.city_id),
                    city_name: line.city_name});
"""

CREATE_RESTAURANT_LOCATEDIN_CITY_RELATIONSHIP_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///restaurantToCity-cypher.csv'
AS line
MERGE (restaurant:Restaurant {restaurant_id: toInteger(line.restaurant_id)})
MERGE (city:City {city_id: toInteger(line.city_id)})
MERGE (restaurant)-[r:LOCATED_IN]->(city);
"""

CREATE_PERSON_LIVESIN_CITY_RELATIONSHIP_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///personToCity-cypher.csv'
AS line
MERGE (person:Person {person_id: toInteger(line.person_id)})
MERGE (city:City {city_id: toInteger(line.city_id)})
MERGE (person)-[r:LIVES_IN]->(city);
"""
#online shopping database
CREATE_PRODUCTS_NODES_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///products-nodes-cypher.csv'
AS line
MERGE (product:Product {product_id: toInteger(line.product_id),
                    product_name: line.product_name,
                    price: toFloat(line.price),
                    quantity: toInteger(line.quantity),
                    rate: toInteger(line.rate)});
"""
CREATE_PRODUCT1_NODES_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///products-nodes-cypher.csv'
AS line
MERGE (product1:Product1 {product_id: toInteger(line.product_id),
                    product_name: line.product_name,
                    price: toFloat(line.price),
                    quantity: toInteger(line.quantity),
                    rate: toInteger(line.rate)});
"""

CREATE_BRANDS_NODES_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///brands-nodes-cypher.csv'
AS line
MERGE (product:Brand {brand_id: toInteger(line.brand_id),
                    brand_name: line.brand_name,
                    year_established: toInteger(line.year_established)});
"""
CREATE_PRODUCT_BELONGSTO_BRAND_RELATIONSHIP_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///ProductsToBrands-cypher.csv'
AS line
MERGE (product:Product {product_id: toInteger(line.product_id)})
MERGE (brand:Brand {brand_id: toInteger(line.brand_id)})
MERGE (product)-[r:BELONGS_TO]->(brand);
"""
CREATE_PRODUCT1_BELONGSTO_BRAND_RELATIONSHIP_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///ProductsToBrands-cypher.csv'
AS line
MERGE (product1:Product1 {product_id: toInteger(line.product_id)})
MERGE (brand:Brand {brand_id: toInteger(line.brand_id)})
MERGE (product1)-[r:BELONGS_TO1]->(brand);
"""

CREATE_PERSON_BOUGHT_PRODUCT_RELATIONSHIP_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///PersonBuyProducts-cypher.csv'
AS line
MERGE (person:Person {person_id: toInteger(line.person_id)})
MERGE (product:Product {product_id: toInteger(line.product_id)})
MERGE (person)-[r:BOUGHT]->(product);
"""

CREATE_PERSON_WISHLIST_PRODUCT_RELATIONSHIP_FROM_CSV = """
LOAD CSV WITH HEADERS
FROM 'file:///PersonWishProducts-cypher.csv'
AS line
MERGE (person:Person {person_id: toInteger(line.person_id)})
MERGE (product:Product {product_id: toInteger(line.product_id)})
MERGE (person)-[r:WISHLIST]->(product);
"""
class Neo4jGrader:

    def __init__(self, base_grader_obj):
        # print(py2neo.__version__)  # 4.2.0
        self.base_grader_obj = base_grader_obj
        self.g = Graph(NEO4J_BOLT_URI)  # Use for Bolt protocol
        # self.g = Graph(NEO4J_HOST_ADDR)  # Use for HTTP protocol
        self.tx = self.g.begin()
        self.star_id_node_map = {}
        self.restaurant_id_node_map = {}
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

    # @BaseGrader.function_timer("[Neo4jGrader - DELETION TIMER] --- %s seconds ---")
    def cleanup_database(self):
        print("[Neo4jGrader] Cleaning up Neo4j Database (Detaching and Deleting nodes...)")
        deleted_results = self.g.run(DETACH_DELETE_ALL_NODES)
        print("[Neo4jGrader - Deletor] DELETED RESULTS: ", deleted_results)

    # @BaseGrader.function_timer("[Neo4jGrader - PERSON NODES CREATION TIMER] --- %s seconds ---")
    def create_person_nodes(self):
        self.g.run(CREATE_PERSON_NODES_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - PERSON NODES CREATION TIMER] --- %s seconds ---")
    def create_person1_nodes(self):
        self.g.run(CREATE_PERSON1_NODES_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RESTAURANT NODES CREATION TIMER] --- %s seconds ---")
    def create_restaurant_nodes(self):
        self.g.run(CREATE_RESTAURANT_NODES_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RESTAURANT NODES CREATION TIMER] --- %s seconds ---")
    def create_restaurant1_nodes(self):
        self.g.run(CREATE_RESTAURANT1_NODES_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (ActedIn) CREATION TIMER] --- %s seconds ---")
    def create_relationship(self):
        self.g.run(CREATE_PERSON_LIKED_RESTAURANT_RELATIONSHIP_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (ActedIn) CREATION TIMER] --- %s seconds ---")
    def create_relationship1(self):
        self.g.run(CREATE_PERSON1_LIKED_RESTAURANT1_RELATIONSHIP_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (FriendWith) CREATION TIMER] --- %s seconds ---")
    def create_friend_relationship(self):
        self.g.run(CREATE_PERSON_FRIENDSWITH_PERSON_RELATIONSHIP_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - CUISINE NODES CREATION TIMER] --- %s seconds ---")
    def create_cuisine_nodes(self):
        self.g.run(CREATE_CUISINE_NODES_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (Serves) CREATION TIMER] --- %s seconds ---")
    def create_serves_relationship(self):
        self.g.run(CREATE_RESTAURANT_SERVES_CUISINE_RELATIONSHIP_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - CITY NODES CREATION TIMER] --- %s seconds ---")
    def create_city_nodes(self):
        self.g.run(CREATE_CITY_NODES_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (LocatedIn) CREATION TIMER] --- %s seconds ---")
    def create_located_in_relationship(self):
        self.g.run(CREATE_RESTAURANT_LOCATEDIN_CITY_RELATIONSHIP_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (LivesIn) CREATION TIMER] --- %s seconds ---")
    def create_lives_in_relationship(self):
        self.g.run(CREATE_PERSON_LIVESIN_CITY_RELATIONSHIP_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - PRODUCTS NODES CREATION TIMER] --- %s seconds ---")
    def create_products_nodes(self):
        self.g.run(CREATE_PRODUCTS_NODES_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - BRANDS NODES CREATION TIMER] --- %s seconds ---")
    def create_brands_nodes(self):
        self.g.run(CREATE_BRANDS_NODES_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (BelongTo) CREATION TIMER] --- %s seconds ---")
    def create_belongs_to_relationship(self):
        self.g.run(CREATE_PRODUCT_BELONGSTO_BRAND_RELATIONSHIP_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (Buys) CREATION TIMER] --- %s seconds ---")
    def create_buys_relationship(self):
        self.g.run(CREATE_PERSON_BOUGHT_PRODUCT_RELATIONSHIP_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (Wishlist) CREATION TIMER] --- %s seconds ---")
    def create_wishlist_relationship(self):
        self.g.run(CREATE_PERSON_WISHLIST_PRODUCT_RELATIONSHIP_FROM_CSV)

    def create_product1_nodes(self):
        self.g.run(CREATE_PRODUCT1_NODES_FROM_CSV)

    # @BaseGrader.function_timer("[Neo4jGrader - RELATIONSHIP (Wishlist) CREATION TIMER] --- %s seconds ---")
    def create_belongs_to1_relationship(self):
        self.g.run(CREATE_PRODUCT1_BELONGSTO_BRAND_RELATIONSHIP_FROM_CSV)

    def print_friends_of(self, tx, name):
        for record in tx.run("MATCH (a:Person)-[:KNOWS]->(f) "
                             "WHERE a.name = {name} "
                             "RETURN f.name", name=name):
            print(record["f.name"])

    @BaseGrader.function_timer("[Neo4jGrader - TOTAL DATASET CREATION TIMER] --- %s seconds ---")
    def create_dataset_in_DB(self, specified_dataset = None):
        self.cleanup_database()
        print("Injecting data into database")

        # generate everything
        if specified_dataset is None or "all" in specified_dataset:
            self.create_person_nodes()
            self.create_person1_nodes()
            self.create_restaurant_nodes()
            self.create_restaurant1_nodes()
            self.create_relationship()
            self.create_relationship1()
            self.create_friend_relationship()
            self.create_cuisine_nodes()
            self.create_serves_relationship()
            self.create_city_nodes()
            self.create_located_in_relationship()
            self.create_lives_in_relationship()
            self.create_products_nodes()
            self.create_product1_nodes()
            self.create_brands_nodes() 
            self.create_belongs_to_relationship()
            self.create_buys_relationship()
            self.create_wishlist_relationship()
            self.create_belongs_to1_relationship()
        else:       
            if "restaurants" in specified_dataset:
                self.create_person_nodes()
                self.create_person1_nodes()
                self.create_restaurant_nodes()
                self.create_restaurant1_nodes()
                self.create_relationship()
                self.create_relationship1()
                self.create_friend_relationship()
                self.create_cuisine_nodes()
                self.create_serves_relationship()
                self.create_city_nodes()
                self.create_located_in_relationship()
                self.create_lives_in_relationship()

            if "purchases" in specified_dataset:
                self.create_products_nodes()
                self.create_product1_nodes()
                self.create_brands_nodes() 
                self.create_belongs_to_relationship()
                self.create_buys_relationship()
                self.create_wishlist_relationship()
                self.create_belongs_to1_relationship()
        
        try:
            if not self.tx.finished:
                self.tx.commit()
        except Exception as e:
            print(f"Error while committing the transaction: {str(e)}")
            if not self.tx.finished:
                self.tx.rollback()
            raise


    def get_solution_query_tuple(self) -> (list, str, list):
        # Generate solution rows based on the solution query
        sol = ''
        solution_docs = []
        solution_data_list = []
        try:
            with open(SOLUTION_QUERY_PATH) as solution_file:
                solution_query = solution_file.read()

            if True:
                solution_cursor = self.g.run(solution_query)
                for rel in solution_cursor:
                    newTuple = []
                    for ele in rel:
                        newTuple.append(ele)
                        solution_docs.append(json.dumps(ele))

                    newTuple = rearrange_list_inside_documents_new(newTuple)
                    solution_data_list.append(json.dumps(newTuple))
                    # solution_data_list.append(json.dumps(rel))
                    sol += json.dumps(rel)
                    sol += "\n"

        except Exception as e:
            BaseGrader.record_failure_and_exit("Error in solution query: " + str(e))

        return solution_docs, sol, solution_data_list

    def get_student_query_tuple(self) -> (list, str, list):
        std_sol = ''
        student_docs = []
        student_data_list = []
        try:
            if self.student_query_exists:
                with open(STUDENT_QUERY_PATH) as student_file:
                    student_query = student_file.read()
            else:
                with open(STUENT_SORT_QUERY_PATH) as student_file:
                    student_query = student_file.read()

            student_cursor = self.g.run(student_query)
            for rel in student_cursor:
                newTuple = []
                for ele in rel:
                    newTuple.append(ele)
                    student_docs.append(json.dumps(ele))

                newTuple = rearrange_list_inside_documents_new(newTuple)
                student_data_list.append(json.dumps(newTuple))
                # student_data_list.append(json.dumps(rel))

                std_sol += json.dumps(rel)
                std_sol += "\n"

        except Exception as e:
            BaseGrader.record_failure_and_exit(str(e))

        return student_docs, std_sol, student_data_list

    def grade(self, prev_data):

        # We use this to reduce unnecessary operations
        resetDB = False
        dataset = None

        if exists('settings.json'):
            with open('settings.json') as f:
                data = json.load(f)
                resetDB = data.get('resetDB', resetDB)
                dataset = data.get('dataset', dataset)

        start_time = time.time()
        print("[GRADER] Running grading. prev_data = " + str(prev_data))
        if (prev_data):
            if (prev_data[2] == False):
                print("[GRADER] Early stop activated.")
                self.base_grader_obj.pl_output_dict(['Test failed - early stop set.'], ['Test failed - early stop set.'], prev_data[2], BaseGrader.data_message_string_function)
                return prev_data
        self.create_dataset_in_DB(specified_dataset = dataset) # This creates the dataset in the DB
        print("[GRADER] Created dataset in DB: %s seconds" % (time.time() - start_time))
        student_docs, actual_output, student_list = self.get_student_query_tuple()
        print("[GRADER] Student query tuple: %s seconds" % (time.time() - start_time))

        # This is a special toggle for questions where students alter the db
        if resetDB:
            self.create_dataset_in_DB(specified_dataset = dataset) # This creates the dataset in the DB

        solution_docs, expected_output, solution_list = self.get_solution_query_tuple()
        print("[GRADER] Solution query tuple: %s seconds" % (time.time() - start_time))
        # Go through the docs and verify that everything matches.
        success = False
        if self.student_query_exists:
            all_docs = True

            solution_docs = rearrange_list_inside_documents(solution_docs)
            student_docs = rearrange_list_inside_documents(student_docs)

            for i in solution_list:
                if i not in student_list:
                    all_docs = False
                    break
            no_extra_docs = True
            for i in student_list:
                if i not in solution_list:
                    no_extra_docs = False
                    break

            if all_docs and no_extra_docs:
                success = True
            else:
                success = False

        elif self.student_sort_query_exists:
            flag = True
            if len(solution_docs) != len(student_docs):
                flag = False
            if flag:
                for i in range(len(solution_docs)):
                    if not the_same(solution_docs[i], student_docs[i]):
                        flag = False
                        break
            if flag:
                success = True
            else:
                success = False
        print("[GRADER] Assorted boilerplate: %s seconds" % (time.time() - start_time))
        # # Original Table output representation only
        # self.base_grader_obj.pl_output_dict(expected_output, actual_output, success)

        # Updated code for messaging diffs between student and solution answer
        self.base_grader_obj.pl_output_dict(solution_list, student_list, success, BaseGrader.data_message_string_function)
        print("[GRADER] Difference checking: %s seconds" % (time.time() - start_time))
        return (solution_list, student_list, success)

def the_same(solution, student):
    """Compares two dictionary without taking the sequence of lists into consideration"""
    # evaluate the input value so it is a list not a string
    solution = eval(solution)
    student = eval(student)
    same = True

    #if it is a list, step in
    if isinstance(solution, list):

        # make sure it is not a list of list
        if isinstance(solution[0], list):
            for idx, s in enumerate(solution):
                same = the_same(s, student[idx])
        
        #compare the list in sorted mannar
        elif sorted(solution) != sorted(student):
            same = False
    
    # if it is not a list, compare the value
    elif solution != student:
        same = False

    return same

def rearrange_list_inside_documents(list_of_documents):
    for idx, doc in enumerate(list_of_documents):
        
        if doc == "null": doc = doc # this breaks eval if neo4j returns null
        try: doc = eval(doc)
        except: doc = doc
        
        if isinstance(doc, list):
            # this will not take care of lists with types of different elements
            try: doc = sorted(doc)
            except: doc = doc
            list_of_documents[idx] = doc

    return list_of_documents

def rearrange_list_inside_documents_new(list_of_documents):
    for idx, doc in enumerate(list_of_documents):
        # doc = eval(doc)
        if isinstance(doc, list):
            # this will not take care of lists with types of different elements
            try: doc = sorted(doc)
            except: doc = doc
            list_of_documents[idx] = doc

    return list_of_documents

if __name__ == "__main__":
    # Provided only for testing this module separately (by changing within the run.sh to "python3 -m [module_name]")
    def student_grading_function(base_grader_obj):
        # run grader
        neo_grader = Neo4jGrader(base_grader_obj)
        neo_grader.grade()


    grader = BaseGrader(student_grading_function, 3)
    grader.run()
