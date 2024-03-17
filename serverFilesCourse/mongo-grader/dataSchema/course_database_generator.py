from dataSchema.random_generator import get_random_firstNames, get_random_lastNames
import random
from os import system

DATA_COURSE_LIST_FILE = "course_list.txt"

class MDBCoursesGenerator():
    mdb_js_path = '/grade/tests/setup-data-cbtf.js'
    
    def __init__(self):
        self.popular_first_names = get_random_firstNames(20)
        self.popular_last_names = get_random_lastNames(20)
        self.popular_student_first_names = get_random_firstNames(20)
        self.popular_student_last_names = get_random_lastNames(20)

    def set_up_course_data(self):
        file = open(self.mdb_js_path, 'w')
        file.write('db.Courses.remove({});\n')
        file.write('db.Reviews.remove({});\n')
        file.write('db.Instructors.remove({});\n')
        file.write('db.Locations.remove({});\n')
        courseFile = open(DATA_COURSE_LIST_FILE, 'r')
        courseStrings = courseFile.readlines()

        
        instructor_list = []
        student_list = []
        location_list = []
        for instructor_id in range(90):
            instructorName = random.choice(self.popular_first_names) + ' ' + random.choice(self.popular_last_names)
            instructor = {
                "instructor_id": instructor_id,
                "name": instructorName,
                "office": random.choice(range(1000, 9999)),
                "salary": random.choice(range(95000, 115000))
            }
            instructor_list.append(instructor)
            studentName = random.choice(self.popular_student_first_names) + ' ' + random.choice(self.popular_student_last_names)
            student_list.append(studentName)
        
        for location_id in range(50):
            location = {
                "location_id": location_id,
                "capacity": random.choice(range(10, 400)),
                "num_of_window": random.choice(range(0, 20)),
                "num_of_doors": random.choice(range(1, 4))
            }
            location_list.append(location)

        # courseStrings = random.sample(courseStrings, 300)
        review_id = 0
        for course_id in range(len(courseStrings)):
            # course info
            course = str(courseStrings[course_id]).strip()
            courseInfo = course.split(",")
            department = courseInfo[2]
            course_number = courseInfo[0]
            course_name = courseInfo[1]
            year_offered = random.choice(range(2013, 2022))            

            ## student info
            # decide number of students
            studentList = random.sample(range(80), random.choice(range(3, 8)))
            studentList.sort()

            locationList = random.sample(range(50), random.choice(range(2, 5)))
            locationList.sort()

            reviewList = []

            for student_id in studentList:
                channel = random.choice(["Online", "Online", "InPerson", "InPerson", "InPerson", "InPerson", "Hybrid", "Coursera", "Edx", "PrairieLearn"])
                file.write('db.Reviews.insert(')
                file.write('{'+
                    'review_id: NumberInt(' + str(review_id) + '), ' +
                    'student_id: NumberInt(' + str(student_id) + '), ' +
                    'student_name: "' + student_list[student_id] + '", ' + 
                    'course_id: NumberInt(' + str(course_id) + '), ' +
                    'rating: NumberInt(' + str(random.choice(range(0, 10))) + '), ' +
                    'channel: "' + channel + '"}')
                file.write(');\n')
                reviewList.append(review_id)
                review_id += 1
            

            reviewString = '['
            for review in reviewList:
                reviewString += 'NumberInt(' + str(review) + '), '
            reviewString = reviewString[:-2] + ']'
            

            studentString = '['
            for student in studentList:
                studentString += 'NumberInt(' + str(student) + '), '
            studentString = studentString[:-2] + ']'

            locationString = '['
            for location in locationList:
                locationString += 'NumberInt(' + str(location) + '), '
            locationString = locationString[:-2] + ']'

            ## instructors
            instructorList = random.sample(range(80), random.choice([1,1,1,1,2,2,2,3]))
            instructorList.sort()

            instructorString = '['
            for instructor in instructorList:
                instructorString += 'NumberInt(' + str(instructor) + '), '
            instructorString = instructorString[:-2] + ']'


            file.write('db.Courses.insert(')
            file.write('{'+
                'course_id: NumberInt(' + str(course_id) + '), ' +
                'department: "' + department + '",' +
                'course_number: NumberInt(' + str(course_number) + '),' +
                'course_name: "' + course_name + '", ' +
                'year_offered: NumberInt(' + str(year_offered) + '),' +
                'instructors: ' + instructorString + ', ' +
                'reviews: ' + reviewString + ', ' +
                'locations: ' + locationString + ', ' +
                'students: ' + studentString + "}")
            file.write(');\n')
        
        for instructor in instructor_list:
            file.write('db.Instructors.insert(')
            file.write('{'+
                'instructor_id: NumberInt(' + str(instructor["instructor_id"]) + '), ' +
                'instructor_name: "' + instructor["name"] + '",' +
                'office: NumberInt(' + str(instructor["office"]) + '),' +
                'salary: NumberInt(' + str(instructor["salary"]) + ')}')
            file.write(');\n')
        
        for location in location_list:
            file.write('db.Locations.insert(')
            file.write('{'+
                'location_id: NumberInt(' + str(location["location_id"]) + '), ' +
                'capacity: NumberInt(' + str(location["capacity"]) + '),' +
                'num_of_window: NumberInt(' + str(location["num_of_window"]) + '),' +
                'num_of_doors: NumberInt(' + str(location["num_of_doors"]) + ')}')
            file.write(');\n')

        courseFile.close()
        file.close()

    def inject_mongodb_data(self):
        """injects generated mdb js into db"""
        system("mongo --quiet " + self.mdb_js_path)
        system('echo "Injected Data into MongoDB Database"')