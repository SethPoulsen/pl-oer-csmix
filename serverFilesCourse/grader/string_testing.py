from collections import OrderedDict


solution_list = [("NetID", "TotalCourses"), ("jk2", "3"),("ad2", "5"),("aasf4", "1"),("asx3", "1"),("k2", "13")]
student_list = [("NetID", "TotalCourses"), ("jk2", "3"),("ad2", "5"),("aasf4", "1"),("asx3", "1"),("k2", "13")]
student_order_list = [("NetID", "TotalCourses"), ("ad2", "5"),("aasf4", "1"),("asx3", "1"),("k2", "13"), ("jk2", "3")]
student_wrong_header_list = [("NetID", "TotalCoursesss"), ("ad2", "5"),("aasf4", "1"),("asx3", "1"),("k2", "13"), ("jk2", "3")]
student_wrong_info_list = [("NetID", "TotalCourses"), ("ad2", "5"),("a412as4f4", "13"),("asx3", "1"),("k222", "13"), ("jk2", "333")]




# Check headers - For SQL  (Signature for header checking boolean)
# Use sets to check for differences - Save in 2 sets (Solution diff set, Student diff set)
# Go through both sets, create a list in order of results in the sets for both
# Show diffs of both sets. Solution set would have + at the front, student set would have - at the front
# Check for both in order for grade correctness

def grade_diffs(solution_list, student_list, header=False, ordered=False):
    grade_result = True
    if header:
        student_header = student_list[0]
        solution_header = solution_list[0]
        grade_result = student_header == solution_header
        if not grade_result:
            return #TODO: Return somthing... and some extra operations...

    solution_set = set(solution_list)
    student_set = set(student_list)

    solution_diff_set = solution_set.difference(student_set)
    student_diff_set = student_set.difference(solution_set)

    DIFF_MESSAGE_HEADER = "DIFFS \n('+': Means the correct data entry in the solution your result missed!\n'-': Means the incorrect" \
                          " data entry in your result which is not a part of the solution!):\n"

    returned_message = ""

    returned_message += construct_diff_message('+', solution_list, solution_diff_set, tuple_to_string)
    returned_message += "\n"
    returned_message += construct_diff_message('-', student_list, student_diff_set, tuple_to_string)
    returned_message += "\n\n==========TABLE REPRESENTATION=========="
    returned_message += "\n\nExpected Results\n==============\n"
    returned_message += construct_diff_message('+', solution_list, solution_diff_set, tuple_to_string, True)
    returned_message += "\n\n\nActual Results\n=============="
    returned_message += construct_diff_message('-', student_list, student_diff_set, tuple_to_string, True)

    return DIFF_MESSAGE_HEADER + returned_message


def construct_diff_message(type_char, type_list, type_diff_set, string_conversion_func, print_table=False):
    result_string = ""
    for data in type_list:
        if data in type_diff_set:
            result_string += "\n{}  {}".format(type_char, string_conversion_func(data))
        elif print_table:
            result_string += "\n{}".format(string_conversion_func(data))
    return result_string


def tuple_to_string(tuple_data):
    return ' '.join(tuple_data)


if __name__ == "__main__":
    print(grade_diffs(solution_list, student_wrong_info_list, True))