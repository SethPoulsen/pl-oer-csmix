import random

popular_first_names = ["Alice", "Bob", "Charlie", "Doug", "Emily",
                    "Freya", "G-eazy", "Hisham", "Isabella", "Jack","Emma",
                    "Olivia","Ava","Isabella","Sophia","Charlotte","Mia","Amelia",
                    "Harper","Evelyn","Abigail","Emily"]

popular_last_names = ["Anderson", "Bing", "Cho", "Da-Cruz", "Espenson",
                   "Frost", "Glow", "Hipster", "Indiana", "Joe", "White","Harris","Martin","Garcia","Martinez","Robinson","Clark",
                   "Rodriguez","Lewis","Walker","Lee", "Robinson","Clark"]

# countries = ["USA", "UK", "Australia", "Mexico", "Brazil"]

# movie_names = ["Avengers", "Spider Man", "Batman", "Superman", "Mission Impossible",
#                "Fast & Furious", "Indiana Jones", "Bourne", "Shark Movie", "Horror Movie"]

actors = []

# student group by school, [match, group, sort and limit]
# student group by name, unwind list of learning courses, list of[ match, unwind, group]
# course group by instructor, []
#course group by course name, unwind list of attending student
# teacher group b

f1=open('setup-data-cbtf.js', 'w+')

courseFile =open('couse_list.txt', 'rb')
courseStrings = courseFile.readlines()
courseData = []
for courseID in range(len(courseStrings)):
	course = courseStrings[courseID]
	courseInfo = course.split()
	print(courseInfo)
	department = courseInfo[0]
	number = courseInfo[1]
	name = ' '.join(courseInfo[2:])
	instrcutorName = random.choice(popular_first_names)+' '+random.choice(popular_last_names)
	rating = random.randint(1, 10)
	courseData.append([courseID, department, number, name])
	studentNum = random.randint(5, 20)
	studentList = random.sample(range(100), studentNum)
	studentString = '['
	for student in studentList:
	        studentString += 'NumberInt('+str(student)+'), '
	        #print 'CREATE(s'+str(star)+': Stars)-[:ActedIn]-(m'+str(movie_id)+':Movie)'
	studentString = studentString[:-2]+']'

	f1.write('db.Courses.insert(') 
	f1.write('{course_id: NumberInt('+str(courseID)+'), '+
			   'instructor: "'+instrcutorName+'", '+
			   'course_number: NumberInt('+ str(number)+'),'+
			   'rating: NumberInt('+str(rating)+'), '+
			   'course_name: "'+name+'", '+
			   'department: "'+department +'",' +
			    'students: '+studentString+ "}")
	#f1.write('{course,courseInfo, department, nnumber, name,instructor, rating, courseData, studentNum, studentList}')
	f1.write(');\n')


# for actor_id in range(0, 100):
#     star_name = popular_first_names[actor_id/10]+' '+popular_last_names[actor_id%10]
#     birth_country = random.choice(countries)
#     birth_year = str(random.randint(1960, 2000))
#     actors.append([actor_id, star_name, birth_country])
#     f1.write('{"actor_id": "'+str(actor_id)+'", "star_name": "'+star_name+'", "birth_country": "'+birth_country+'"},\n')
#     #print 'CREATE(s'+str(actor_id)+': Stars{actor_id: "'+str(actor_id)+'", star_name: "'+star_name+'", born_year: "'+birth_year+'", birth_country: "'+birth_country+'")'


# #print actors

# for movie_id in range(1, 100):
#     director_name = random.choice(popular_first_names)+' '+random.choice(popular_last_names)
#     release_year = str(random.randint(1990, 2019))
#     ratings = str(random.randint(1, 10))
#     movie_name = random.choice(movie_names)+' '+str(random.randint(1, 100))
#     movie_country = random.choice(countries)
#     genre = random.choice(['Horror', 'Comedy', 'Romantic', 'Action'])
#     star_count = random.randint(3, 13)

#     star_string = star_string[:-2]+']'
    
            
#     f1.write('{"movie_id": "'+str(movie_id)+'", "director": "'+director_name+'", "release_year": "'+ release_year+'", "ratings": "'+ratings+
#              '", "movie_name": "'+movie_name+'", "country": "'+movie_country+'", "genre": "'+genre+'", "stars": "'+star_string+'},\n')
    
f1.close()
