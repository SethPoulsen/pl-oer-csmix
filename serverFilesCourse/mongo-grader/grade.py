import json
from random import randint
from pymongo import MongoClient
import sys
import ast
import os
import pymongo
import re


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


if __name__ == "__main__":
 #client = MongoClient(port=27017)
 client = MongoClient('mongodb://127.0.0.1:27017/')
 db=client.test

 grading_result = {}
  # If `dump.sql` is present, that means we'll need to just execute
  # the solution and student queries without inspecting their output,
  # and then run the dump to compare the table state after.
 is_modification = os.path.isfile('/grade/tests/dump.sql')
 if is_modification:
     with open('/grade/tests/dump.sql') as dump_file:
         dump_query  = dump_file.read()

  # Generate solution rows based on the solution query
 solution_docs = []
 try:
     with open('/grade/tests/sol_qry_res.json') as solution_file:
         solution_cursor = solution_file.read()

 except Exception as e:
    record_failure_and_exit("Error in solution query: " + str(e))
  # Run student query in a brand-new, duplicate database

 student_docs = []
 try:
     exists = os.path.isfile('/grade/student/std_qry_res.json')
     sort_exists = os.path.isfile('/grade/student/std_qry_sort_res.json')
     if exists:
         with open('/grade/student/std_qry_res.json') as student_file:
             student_cursor = student_file.read()
     else:
         with open('/grade/student/std_qry_sort_res.json') as student_file:
             student_cursor = student_file.read()

 except Exception as e:
     record_failure_and_exit(str(e))

 # Diff solution and student query results
 # Diff solution and student query results
 # solution_cursor = eval('db.Stars.find({"actor_id": "0"})')
 # student_cursor = solution_cursor
 # print(solution_cursor)
 solution_dict_list = []
 student_dict_list = []

 try:
     illegal_format = False
     for line in student_cursor.splitlines():
         if line != "" and line[0] == "{" or line.isdigit() == True:
             if "ObjectId" in line:
                 line = re.sub(r'ObjectId\s*\(\s*\"(\S+)\"\s*\)',r'{"$oid": "\1"}',line)
             student_dict_list.append(eval(line))
         else:
             student_dict_list.append(line)
         # print(line[0])
         # if illegal_format == False and (line[0] != "{" or line.isdigit() == False) :
         #     #Empty results or syntax problem from students' queries.
         #     #WE might need other key words from more corner cases.
         #     student_dict_list.append(line)
         #     illegal_format = True
         # elif "ObjectId" in line and illegal_format != True:
         #     #Student_cursor might contain default _id, of which the value is like ObjectId("123445")
         #     #We need to get rid of "ObjectId()"
         #     line = re.sub(r'ObjectId\s*\(\s*\"(\S+)\"\s*\)',r'{"$oid": "\1"}',line)
         #     student_dict_list.append(eval(line))
         # elif illegal_format != True:
         #     if "null" in line:
         #         #When using false aggregate attribute
         #         line = line.replace("null","0")
         #     student_dict_list.append(eval(line))
         # else:
         #     student_dict_list.append(line)
 except Exception as e:
     record_failure_and_exit(str(e))



 for line in solution_cursor.splitlines():
     if 'ObjectId' in line:
         line = re.sub(r'ObjectId\s*\(\s*\"(\S+)\"\s*\)',r'{"$oid": "\1"}',line)
     solution_dict_list.append(eval(line))

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



 sol = ''
 for elem in solution_dict_list:
     sol += json.dumps(elem)
     sol += "\n"

 std_sol = ''
 for elem in student_dict_list:
     std_sol += json.dumps(elem)
     std_sol += "\n"


 output = ""
 output += "Expected results\n"
 output += "================\n"
 output += sol
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
