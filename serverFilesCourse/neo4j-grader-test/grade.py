import json
import neo4j
import random

import sys
import os.path
from py2neo import Graph, Node, Relationship, NodeMatcher



def record_failure_and_exit(msg):
 grading_result = {
  'score': 0.0,
  'succeeded': False,
  'message': msg,
 }
 with open('results.json', mode='w') as out:
  json.dump(grading_result, out)
 sys.exit(0)



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

def print_friends_of(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(f) "
                         "WHERE a.name = {name} "
                         "RETURN f.name", name=name):
        print(record["f.name"])


if __name__ == "__main__":

 g = Graph('http://127.0.0.1:7474')

 #Create the dataset
 tx = g.begin()
 star_id_node_map  = {}
 movie_id_node_map  = {}
 star1_id_node_map  = {} #for update problem
 movie1_id_node_map  = {} #for update problem
 with open('actor-nodes.txt') as f:
     for l in f.read().splitlines():
         lst = l.split("\t")
         s = Node("Actor", actor_name=lst[1], birth_year = int(lst[2]),  birth_country= lst[3])
         star_id_node_map[lst[0]] = s
         tx.create(s)
 with open('actor-nodes.txt') as f:
    for l in f.read().splitlines():
        lst = l.split("\t")
        s1 = Node("Actor1", actor_name=lst[1], birth_year = int(lst[2]),  birth_country= lst[3])
        star1_id_node_map[lst[0]] = s1
        tx.create(s1)

 with open('movie-nodes.txt') as f:
     for l in f.read().splitlines():
         lst = l.split("\t")
         m = Node("Movie", movie_name=lst[1], release_year = int(lst[2]),  ratings = int(lst[3]), genre = lst[4])
         movie_id_node_map[lst[0]] = m
         tx.create(m)

 with open('movie-nodes.txt') as f:
    for l in f.read().splitlines():
        lst = l.split("\t")
        m1 = Node("Movie1", movie_name=lst[1], release_year = int(lst[2]),  ratings = int(lst[3]), genre = lst[4])
        movie1_id_node_map[lst[0]] = m1 #for update problem
        tx.create(m1)    #for update problem

 with open('relationships.txt') as f:
     for l in f.read().splitlines():
         s_id, m_id = l.split("\t")
         s_node = star_id_node_map[s_id]
         m_node = movie_id_node_map[m_id]
         tx.create(Relationship(s_node,"ActedIn", m_node))

 with open('relationships.txt') as f:
    for l in f.read().splitlines():
        s1_id, m1_id = l.split("\t")
        s1_node = star1_id_node_map[s1_id]
        m1_node = movie1_id_node_map[m1_id]
        tx.create(Relationship(s1_node,"ActedIn_1", m1_node))

 with open('friendRelationships.txt') as f:
     for l in f.read().splitlines():
         s_id, f_id = l.split("\t")
         s_node = star_id_node_map[s_id]
         f_node = star_id_node_map[f_id]
         tx.create(Relationship(s_node,"FriendWith", f_node))

 tx.commit()


 solution_result = ""



 grading_result = {}

  # If `dump.sql` is present, that means we'll need to just execute
  # the solution and student queries without inspecting their output,
  # and then run the dump to compare the table state after.
 is_modification = os.path.isfile('/grade/tests/dump.sql')
 if is_modification:
     with open('/grade/tests/dump.sql') as dump_file:
         dump_query  = dump_file.read()

  # Generate solution rows based on the solution query
 sol = ''
 solution_docs = []
 try:
     with open('/grade/tests/solution.cypher') as solution_file:
         solution_query = solution_file.read()

     if True:
     #original 'if is_modification'
        solution_cursor = g.run(solution_query)
        #print(solution_cursor)
        for rel in solution_cursor:
            sol += json.dumps(rel)
            sol += "\n"
            for ele in rel:
                solution_docs.append(json.dumps(ele))

 except Exception as e:
    record_failure_and_exit("Error in solution query: " + str(e))
 
 std_sol = ''
 student_docs = []
 try:
     exists = os.path.isfile('/grade/student/query.cypher')
     sort_exists = os.path.isfile('/grade/student/sort_query.cypher')
     if exists:
         with open('/grade/student/query.cypher') as student_file:
             student_query = student_file.read()
     else:
         with open('/grade/student/sort_query.cypher') as student_file:
             student_query = student_file.read()

     if True:
        student_cursor = g.run(student_query)
        for rel in student_cursor:
            std_sol += json.dumps(rel)
            std_sol += "\n"
            for ele in rel:
                student_docs.append(json.dumps(ele))

 except Exception as e:
     record_failure_and_exit(str(e))
 
 if exists:
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

 elif sort_exists:
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



  # Build student-readable output
 output = ""
 output += "Expected results\n"
 output += "================\n"
 output += sol
# output += x1
# output += sol
 output += "\n\n"
 output += "Actual results\n"
 output += "==============\n"
 output += std_sol

 grading_result = {}
 grading_result['score'] = (0.9 if success else 0.0)
 grading_result['succeeded'] = success
 grading_result['message']= ("You received the highest score awarded by the autograder. The remaining 10% will be awarded after manual grading." if success else "")
 grading_result['output'] = output

 with open('results.json', mode='w') as out:
   json.dump(grading_result, out)
