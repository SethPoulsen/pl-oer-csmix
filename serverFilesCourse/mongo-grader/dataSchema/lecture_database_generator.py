from dataSchema.random_generator import get_random_firstNames, get_random_lastNames
import random
from os import system

DATA_COURSE_LIST_FILE = "course_list.txt"

class MDBLectureDBGenerator():

    mdb_js_path = '/grade/tests/setup-practice-data-cbtf.js'

    def __init__(self):
        self.popular_first_names = get_random_firstNames(20)
        self.popular_last_names = get_random_lastNames(20)

    def set_up_lecture_data(self):
        file = open(self.mdb_js_path, 'w')
        file.write('db.Lectures.remove({});\n')
        lectureFile = open(DATA_COURSE_LIST_FILE, 'r')
        lectureStrings = lectureFile.readlines()
        lectureStrings = random.sample(lectureStrings, 200)
        lectureData = []
        for idx in range(len(lectureStrings)):
            lecture = str(lectureStrings[idx]).strip()
            lectureInfo = lecture.split(",")
            department = lectureInfo[2]
            number = lectureInfo[0]
            name = lectureInfo[1]
            instrcutorName = random.choice(self.popular_first_names) + ' ' + random.choice(self.popular_last_names)
            rating = random.randint(1, 10)
            lectureData.append([idx, department, number, name])
            studentNum = random.randint(5, 20)
            studentList = random.sample(range(100), studentNum)
            studentString = '['
            for student in studentList:
                studentString += 'NumberInt(' + str(student) + '), '
                # print 'CREATE(s'+str(star)+': Stars)-[:ActedIn]-(m'+str(movie_id)+':Movie)'
            studentString = studentString[:-2] + ']'

            file.write('db.Lectures.insert(')
            file.write('{lecture_id: NumberInt(' + str(idx) + '), ' +
                     'instructor: "' + instrcutorName + '", ' +
                     'lecture_number: NumberInt(' + str(number) + '),' +
                     'rating: NumberInt(' + str(rating) + '), ' +
                     'lecture_name: "' + name + '", ' +
                     'department: "' + department + '",' +
                     'students: ' + studentString + "}")
            # f1.write('{lecture,lectureInfo, department, nnumber, name,instructor, rating, lectureData, studentNum, studentList}')
            file.write(');\n')
        lectureFile.close()
        file.close()

    def inject_mongodb_data(self):
        """injects generated mdb js into db"""
        system("mongo --quiet " + self.mdb_js_path)
        system('echo "Injected Data into MongoDB Database"')