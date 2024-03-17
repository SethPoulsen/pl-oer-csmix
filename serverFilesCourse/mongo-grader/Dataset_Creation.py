import random

popular_first_names = ["Alise", "Bobby", "Charles", "Dalg", "Emmy",
                    "Fresica", "Gloria", "Hieh", "Idnia", "Jackman",
                    "Kevin", "Scarlett", "Cassy", "Olivia", "Patrick"]

popular_last_names = ["Amber", "Bert", "Chaw", "Dale", "Emert",
                   "Folk", "Gusk", "Hink", "Indi", "Joey",
                   "Rice", "Tan", "Woo", "Lim", "Pratt"]

countries = ["USA", "UK", "Australia", "Mexico", "Brazil", "China"]

movie_names = ["Angels & Demons", "Harry Potter", "Joker", "Watchmen", "Charlie's Angels",
               "Shark", "Alien", "Born To Be A Winner", "Detachment", "Ironman",
               "Sideways", "I Know What You Did Last CS411", "Lost In Translation"]

movie_genre = ['Horror', 'Comedy', 'Romantic', 'Action']

company_info = [['Disney', 1990, random.choice(countries)],
                  ['Paramount', 1995, random.choice(countries)],
                  ['Fox', 2000, random.choice(countries)],
                  ['Universal Studio', 2005, random.choice(countries)],
                  ['Pixel', 2010, random.choice(countries)],
                  ['Warner Brothers', 2015, random.choice(countries)]]

actors = []

f1=open('/grade/tests/setup-data.js', 'w+')

for actor_id in range(100, 200):
    star_name = random.choice(popular_first_names)+' '+ random.choice(popular_last_names)
    birth_country = random.choice(countries)
    birth_year = str(random.randint(1960, 2000))
    actors.append([actor_id, star_name, birth_country])
    f1.write('db.Actors.insert(')
    f1.write('{actor_id: NumberInt('+str(actor_id)+'), actor_name: "'+star_name+'", birth_country: "'+birth_country+'"}')
    f1.write(');\n')

f1.write('\n')

for movie_id in range(100, 200):
    director_name = random.choice(popular_first_names)+' '+random.choice(popular_last_names)
    release_year = str(random.randint(1990, 2019))
    ratings = str(random.randint(1, 10))
    movie_name = random.choice(movie_names)+' '+str(movie_id*2-3)
    movie_country = random.choice(countries)
    genre = random.choice(movie_genre)
    company = random.choice(company_info)
    star_count = random.randint(3, 13)
    star_list = []
    star_string = '['
    for i in range(0, star_count):
        star = random.choice(actors)[0]
        if star not in star_list:
            star_list.append(star)
            star_string += 'NumberInt('+str(star)+'), '
    star_string = star_string[:-2]+']'
    f1.write('db.Movies.insert(') 
    f1.write('{movie_id: NumberInt('+str(movie_id)+'), director: "'+director_name+'", release_year: NumberInt('+ release_year+'), ratings: NumberInt('+ratings+
   '), movie_name: "'+movie_name+'", country: "'+movie_country+'",     genre: "'+genre+'", actors: '+star_string+ ',company:{name:"'+company[0]+
   '", start_year:NumberInt('+str(company[1])+'), country:"'+company[2]+'"}}')
    f1.write(');\n')
    
f1.close()
