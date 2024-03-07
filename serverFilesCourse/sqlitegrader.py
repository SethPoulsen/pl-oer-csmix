import sqlite3
import pprint
import operator
import re
import math
from tabulate import tabulate


def set_all_or_nothing_score_data(data) -> None:
    """Gives points to main question score if all partial scores are correct."""

    data["score"] = 1.0 if all_partial_scores_correct(data) else 0.0


def all_partial_scores_correct(data) -> bool:
    """Return true if all questions are correct in partial scores and it's nonempty."""
    partial_scores = data["partial_scores"]

    if len(partial_scores) == 0:
        return False

    return all(
        part["score"] is not None and math.isclose(part["score"], 1.0)
        for part in partial_scores.values()
    )


def compare_cursors(sol, sub):

    sol_columns = list(map(operator.itemgetter(0), sol.description))
    sub_columns = list(map(operator.itemgetter(0), sub.description))

    sol_list = sol.fetchall()
    sub_list = sub.fetchall()

    sub_output = tabulate(sub_list, headers=sub_columns, floatfmt=".10g")

    if (sol_columns != sub_columns):
        if len(sub_columns) != len(sol_columns):
            msg = f'Column count mismatch: submission has {len(sub_columns)} columns and solution has {len(sol_columns)} columns'
            #return (False, f'Column count mismatch: submission has {len(sub_columns)} columns and solution has {len(sol_columns)} columns')
        else:
            msg = f'Column name or order mismatch: submission does not match solution'
            # return (False, f'Column name or order mismatch: submission does not match solution')

        return (False, msg, sub_output)

    if sol_list == sub_list:
        return(True, "Tests passed!", sub_output)

    return (False, "Row mismatch: Solution and submission differ in row values or count", sub_output)


# Partial credit thoughts
# Check order of columns
# Check order of rows, if not specified, sort both and recompare?
# Randomly generate new database and compare outputs

# sqlparse check
# output check
# state of the database check

def setup_question(data):

    dbfile = data["params"]["element-pl-sqlite"]["dbfile"]
    if dbfile:
        dbfile = f"/grade/serverFilesCourse/{dbfile}"
    else:
        dbfile = ":memory:"

    con = sqlite3.connect(dbfile)

    sub = con.cursor()
    sol = con.cursor()
    cursors = [sub, sol]

    for query in data["params"]["element-pl-sqlite"]["queries"]:
        if 'sql' in query:
            # Handle multiple SQL blocks, ignore blank and SELECTs
            for q in query["sql"].split(';'):
                q = q.strip()
                if not q or bool(re.match('select', q, re.IGNORECASE)):
                    continue
                q += ';'
                print(q)
                sol.execute(q)

        if 'answers_name' in query:
            answers_name = query["answers_name"]
            print(answers_name)
            try:
                sub.execute(data["submitted_answers"][answers_name])
                if answers_name in data["correct_answers"]:
                    sol.execute(data["correct_answers"][answers_name])
                    (result, msg, output) = compare_cursors(sol, sub)

            except Exception as e:
                (result, msg, output) = (False, 'ERROR: ' + str(e), None)
                # Make errors invalid submissions and not count against submission?

            if 'result' in locals():
                print(result, msg)
                data["partial_scores"][answers_name] = {
                    "score": 1 if result else 0,
                    "feedback": msg,
                    "output": output
                }



# https://sqlparse.readthedocs.io/en/latest/
