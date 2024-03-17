import random

popular_first_names = ["Alice", "Bob", "Charlie", "Doug", "Emily",
                    "Freya", "G-eazy", "Hisham", "Isabella", "Jack"]

popular_last_names = ["Anderson", "Bing", "Cho", "Da-Cruz", "Espenson",
                   "Frost", "Glow", "Hipster", "Indiana", "Joe"]

countries = ["USA", "UK", "Australia", "Mexico", "Brazil"]

movie_names = ["Avengers", "Spider Man", "Batman", "Superman", "Mission Impossible",
               "Fast & Furious", "Indiana Jones", "Bourne", "Shark Movie", "Horror Movie"]

actors = []

f1=open('data.json', 'w+')

for actor_id in range(0, 100):
    star_name = popular_first_names[actor_id/10]+' '+popular_last_names[actor_id%10]
    birth_country = random.choice(countries)
    birth_year = str(random.randint(1960, 2000))
    actors.append([actor_id, star_name, birth_country])
    f1.write('{"actor_id": "'+str(actor_id)+'", "star_name": "'+star_name+'", "birth_country": "'+birth_country+'"},\n')
    #print 'CREATE(s'+str(actor_id)+': Stars{actor_id: "'+str(actor_id)+'", star_name: "'+star_name+'", born_year: "'+birth_year+'", birth_country: "'+birth_country+'")'


#print actors

for movie_id in range(1, 100):
    director_name = random.choice(popular_first_names)+' '+random.choice(popular_last_names)
    release_year = str(random.randint(1990, 2019))
    ratings = str(random.randint(1, 10))
    movie_name = random.choice(movie_names)+' '+str(random.randint(1, 100))
    movie_country = random.choice(countries)
    genre = random.choice(['Horror', 'Comedy', 'Romantic', 'Action'])
    star_count = random.randint(3, 13)
    star_list = []
    star_string = '"['
    for i in range(0, star_count):
        star = random.choice(actors)[0]
        if star not in star_list:
            star_list.append(star)
            star_string += '"'+str(star)+'", '
            #print 'CREATE(s'+str(star)+': Stars)-[:ActedIn]-(m'+str(movie_id)+':Movie)'
    star_string = star_string[:-2]+']'
    
            
    f1.write('{"movie_id": "'+str(movie_id)+'", "director": "'+director_name+'", "release_year": "'+ release_year+'", "ratings": "'+ratings+
             '", "movie_name": "'+movie_name+'", "country": "'+movie_country+'", "genre": "'+genre+'", "stars": "'+star_string+'},\n')
    
f1.close()
