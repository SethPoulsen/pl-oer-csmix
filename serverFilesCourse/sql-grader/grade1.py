import json
import sys
import mysql.connector
import sqlparse
import os.path

# Creates a new database with the given name, populates it with data from the
# "setup.sql" file, and sets that database as the current database. Returns a
# cursor for use
def create_and_use_database(cnx, name):
  cursor = cnx.cursor()

  cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(name))
  cursor.execute("USE {}".format(name))

  # populate with data
  with open('/grade/tests/setup.sql') as setup_queries_file:
    setup_queries_raw = setup_queries_file.read()
  setup_queries = sqlparse.split(setup_queries_raw)
  for query in setup_queries:
    cursor.execute(query)

  return cursor

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
  cnx = mysql.connector.connect(user='root', password="password")

  grading_result = {}

  # If `dump.sql` is present, that means we'll need to just execute
  # the solution and student queries without inspecting their output,
  # and then run the dump to compare the table state after.
  is_modification = os.path.isfile('/grade/tests/dump.sql')
  if is_modification:
    with open('/grade/tests/dump.sql') as dump_file:
      dump_query  = dump_file.read()

  # Generate solution rows based on the solution query
  # solution_rows = []
  # try:
  #   with open('/grade/tests/solution.sql') as solution_file:
  #     solution_query = solution_file.read()
  #   solution_cursor = create_and_use_database(cnx, "solution")
  #   #solution_cursor.execute(solution_query)
  #   setup_sol_queries = sqlparse.split(solution_query)
  #   for query in setup_sol_queries:
  #     solution_cursor.execute(query)
  #   # Even if this is a query that will be checked by a dump,
  #   # we still need to clear the cursor
  #   for solution_row in solution_cursor:
  #     solution_rows.append(solution_row)
  #   if is_modification:
  #     solution_rows.clear()
  #     solution_cursor.execute(dump_query)
  #     for solution_row in solution_cursor:
  #       solution_rows.append(solution_row)
  #
  # except Exception as e:
  #   record_failure_and_exit("Error in solution query: " + str(e))

  # Run student query in a brand-new, duplicate database
  student_rows = []
  try:
    with open('/grade/student/query.sql') as student_file:
      student_query = student_file.read()
    student_cursor = create_and_use_database(cnx, "student")
    #student_cursor.execute(student_query)
    setup_std_queries = sqlparse.split(student_query)
    for query in setup_std_queries:
      student_cursor.execute(query)
  #   for student_row in student_cursor:
  #     student_rows.append(student_row)
  #   if is_modification:
  #     student_rows.clear()
  #     student_cursor.execute(dump_query)
  #     for student_row in student_cursor:
  #       student_rows.append(student_row)
  except Exception as e:
    record_failure_and_exit(str(e))

  # Diff solution and student query results
  success = True
  # if len(solution_rows) != len(student_rows):
  #   success = False
  # else:
  #   for row_pair in zip(solution_rows, student_rows):
  #     if len(row_pair[0]) != len(row_pair[1]):
  #       success = False
  #     for val_pair in zip(row_pair[0], row_pair[1]):
  #       if val_pair[0] != val_pair[1]:
  #         success = False
  #         break

  # Build student-readable output
  output = ""
  # output += "Expected results\n"
  # output += "================\n"
  # output += list_of_tuples_to_string(solution_rows)
  # output += "\n\n"
  output += "query results\n"
  output += "==============\n"
  output += list_of_tuples_to_string(student_cursor)

  grading_result = {}
  grading_result['score'] = (1.0 if success else 0.0)
  grading_result['succeeded'] = success
  grading_result['output'] = output

  with open('results.json', mode='w') as out:
    json.dump(grading_result, out)
