import imp
from base_grader import BaseGrader
from dataSchema.lecture_database_generator import MDBLectureDBGenerator
from dataSchema.course_database_generator import MDBCoursesGenerator
from dataSchema.movie_database_generator import MDBMoviesGenerator
from dataSchema.hospital_database_generator import MDBHospitalGenerator
from mongodb_parser import MongodbParser
from mongodb_grader import (MongodbGrader, AUTOMATE_STUDENT_SUBMISSION_COUNT, MONGODB_ADDRESS,
                            SOLUTION_QUERY_JSON_PATH, STUDENT_QUERY_JSON_PATH,
                            STUDENT_QUERY_SORT_JSON_PATH)
from mongodb_grader import MongodbGrader
import json
from os.path import exists

def get_dataset():
    if exists("settings.json"):
        try:
            return(json.load(open("settings.json",'r'))['dataset'])
        except:
            return ["courses", "lecture", "movie", "hospital"]
    else:
        return "all"

def student_grading_function(base_grader_obj):
    
    dataset = get_dataset()
    # this is for backward compatibility
    if dataset == "all":
        dataset = ["courses", "lecture", "movie", "hospital"]
    
    if "movie" in dataset:
        print("Adding movie to db...")
        data_generator = MDBMoviesGenerator()
        data_generator.set_up_movie_dataset()
        data_generator.inject_mongodb_data()
    if "courses" in dataset:
        print("Adding courses to db...")
        cbtf_data_generator = MDBCoursesGenerator()
        cbtf_data_generator.set_up_course_data()
        cbtf_data_generator.inject_mongodb_data()
    if "lecture" in dataset:
        print("Adding lecture to db...")
        practice_cbtf_data_generator = MDBLectureDBGenerator()
        practice_cbtf_data_generator.set_up_lecture_data()
        practice_cbtf_data_generator.inject_mongodb_data()
    if "hospital" in dataset:
        print("Adding hospital to db...")
        practice_cbtf_data_generator = MDBHospitalGenerator()
        practice_cbtf_data_generator.set_up_database()
        practice_cbtf_data_generator.inject_mongodb_data()

    # Parse student code (again, just in case)
    parser = MongodbParser()
    parser.parse()
    # Run student and correct solution on MongoDB after student submitted solutions safely passed parser
    parser.run_solution_query()
    parser.run_student_query()

    # run grader
    mongo_grader = MongodbGrader(base_grader_obj, SOLUTION_QUERY_JSON_PATH, STUDENT_QUERY_JSON_PATH,
                                 STUDENT_QUERY_SORT_JSON_PATH)
    mongo_grader.grade()


if __name__ == "__main__":
    # Finally run grader ( Only for testing purpose!)
    grader = BaseGrader(student_grading_function, AUTOMATE_STUDENT_SUBMISSION_COUNT)
    grader.run()