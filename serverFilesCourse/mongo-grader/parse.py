import json
import sys
import os


def record_failure_and_exit(msg):
    grading_result = {
        'score': 0.0,
        'succeeded': False,
        'message': msg,
    }
    with open('parse.json', mode='w') as out:
        json.dump(grading_result, out)
    sys.exit(0)


# //grade/student/std_qry_res.json
if __name__ == "__main__":

 try:
     exists = os.path.isfile('/grade/student/query.js')
     sort_exists = os.path.isfile('/grade/student/query_sort.js')
     if exists:
         with open('/grade/student/query.js') as student_file:
             student_cursor = student_file.read()
         for line in student_cursor.splitlines():
             if 'print' in line or 'cat(' in line or 'ls(' in line or 'printjson' in line or 'ls( )' in line or 'listFiles' in line or 'cd(' in line or 'load(' in line or 'trim(' in line or 'eval(' in line or 'eval' in line or '.json' in line or '.js' in line:
                 record_failure_and_exit("It seems that your query may contain non-mongoDB commands.\nYou can only write mongoDB queries.\nPlease contact teaching staff if you think your query is correct.")
     elif sort_exists:
         with open('/grade/student/query_sort.js') as student_file:
             student_cursor = student_file.read()
         for line in student_cursor.splitlines():
             if 'print' in line or 'cat(' in line or 'ls(' in line or 'printjson' in line or 'ls( )' in line or 'listFiles' in line or 'cd(' in line or 'load(' in line or 'trim(' in line or 'eval(' in line or 'eval' in line or '.json' in line or '.js' in line:
                 record_failure_and_exit("It seems that your query may contain non-mongoDB commands.\nYou can only write mongoDB queries.\nPlease contact teaching staff if you think your query is correct.")
 except Exception as e:
     record_failure_and_exit(str(e))
