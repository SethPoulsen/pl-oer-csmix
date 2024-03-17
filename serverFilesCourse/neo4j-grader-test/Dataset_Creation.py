import random

popular_first_names = ["Alice", "Bob", "Charlie", "Doug", "Emily",
                    "Freya", "G-eazy", "Hisham", "Isabella", "Jack"]

popular_last_names = ["Anderson", "Bing", "Cho", "Da-Cruz", "Espenson",
                   "Frost", "Glow", "Hipster", "Indiana", "Joe"]

countries = ["USA", "UK", "Australia", "Mexico", "Canada"]

movie_names = ["Avengers", "Spider Man", "Batman", "Superman", "Mission Impossible",
               "Fast & Furious", "Indiana Jones", "Bourne", "Shark Movie", "Horror Movie"]

actors = []

f1 = open('data.json', 'w+')
f2 =open('star-nodes.txt', 'w+')
f3 =open('movie-nodes.txt', 'w+')

f4 =open('relationships.txt', 'w+')
f5 =open('friendRelationships.txt', 'w+')

for actor_id in range(0, 100):
    actor_name = popular_first_names[actor_id//10]+' '+popular_last_names[actor_id%10]
    birth_country = random.choice(countries)
    birth_year = str(random.randint(1960, 2000))
    actors.append([actor_id, actor_name, birth_country])
    #f1.write('{"actor_id": "'+str(actor_id)+'", "actor_name": "'+actor_name+'", "birth_country": "'+birth_country+'"},\n')
    #f2.write('s'+str(actor_id)+'= Node("Star", name = "'+actor_name+'", birth_year = '+birth_year+', birth_country = "'+birth_country+'")\n')
    lst = [str(actor_id), actor_name, str(birth_year), str(birth_country)]
    f2.write('\t'.join(lst)+"\n")
    #f2.write('s'+str(actor_id)+'= Node("Star", actor_name = "'+actor_name+'", birth_year = '+birth_year+', birth_country = "'+birth_country+'")\n')
    #f2.write('tx.CREATE('+'s'+str(actor_id)+')\n')
    friend_count = random.randint(3, 13)
    friend_list = []
    while len(friend_list) < friend_count:
        friend_id = random.randint(0, 99)
        if (friend_id != actor_id):
            friend_list.append(friend_id)
    for friend_id in friend_list:
        f5.write(str(actor_id)+"\t"+str(friend_id)+"\n")


#print actors

for movie_id in range(1, 100):
    director_name = random.choice(popular_first_names)+' '+random.choice(popular_last_names)
    release_year = str(random.randint(1990, 2019))
    ratings = str(random.randint(1, 10))
    movie_name = random.choice(movie_names)+' '+str(movie_id*2-1)
    movie_country = random.choice(countries)
    genre = random.choice(['Horror', 'Comedy', 'Romantic', 'Action'])
    star_count = random.randint(3, 13)
    star_list = []
    star_string = '['
    for i in range(0, star_count):
        star = random.choice(actors)[0]
        if star not in star_list:
            star_list.append(star)
            star_string += '"'+str(star)+'", '

    star_string = star_string[:-2]+']'
    #f2.write('m'+str(movie_id)+'= Node("Movie", name = "'+movie_name+'", id = "'+str(movie_id)+'", release_year = '+release_year+', ratings = '+ratings+', genre = "'+genre+'")\n')
    #f2.write('tx.CREATE('+'m'+str(movie_id)+')\n')
    lst = [str(movie_id), movie_name, str(release_year), str(ratings), genre]
    f3.write('\t'.join(lst)+"\n")
    for star in star_list:
        #f2.write('s'+str(star)+'_'+'m'+str(movie_id)+'= Relationship('+'s'+str(star)+', "ActedIn", '+'m'+str(movie_id)+')\n')
        #f2.write('tx.CREATE('+'s'+str(star)+'_'+'m'+str(movie_id)+')\n')
        f4.write(str(star)+"\t"+str(movie_id)+"\n")

    #f1.write('{"movie_id": "'+str(movie_id)+'", "director": "'+director_name+'", "release_year": '+ release_year+', "ratings": '+ratings+
             #', "movie_name": "'+movie_name+'", "country": "'+movie_country+'", "genre": "'+genre+'", "stars": '+star_string+'},\n')

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
