import random

popular_first_names = ["Alice", "Bob", "Charlie", "Doug", "Emily",
                    "Freya", "G-eazy", "Hisham", "Isabella", "Jack"]

popular_last_names = ["Anderson", "Bing", "Cho", "Da-Cruz", "Espenson",
                   "Frost", "Glow", "Hipster", "Indiana", "Joe"]

countries = ["USA", "UK", "Australia", "Mexico", "Canada"]

movie_names = ["Avengers", "Spider Man", "Batman", "Superman", "Mission Impossible",
               "Fast & Furious", "Indiana Jones", "Bourne", "Shark Movie", "Horror Movie"]

actors = []


class Neo4jDataGenerator:

    def __init__(self):
        self.f2 = open('actor-nodes.txt', 'w+')
        self.f3 = open('movie-nodes.txt', 'w+')
        self.f4 = open('relationships.txt', 'w+')
        self.f5 = open('friendRelationships.txt', 'w+')

    def create_actor_relationship_data(self):
        for actor_id in range(0, 100):
            actor_name = popular_first_names[actor_id//10]+' '+popular_last_names[actor_id%10]
            birth_country = random.choice(countries)
            birth_year = str(random.randint(1960, 2000))
            actors.append([actor_id, actor_name, birth_country])
            lst = [str(actor_id), actor_name, str(birth_year), str(birth_country)]
            self.f2.write('\t'.join(lst)+"\n")
            friend_count = random.randint(3, 13)
            friend_list = []
            while len(friend_list) < friend_count:
                friend_id = random.randint(0, 99)
                if (friend_id != actor_id):
                    friend_list.append(friend_id)
            for friend_id in friend_list:
                self.f5.write(str(actor_id)+"\t"+str(friend_id)+"\n")

    def create_movie_relationship_data(self):
        for movie_id in range(1, 100):

            release_year = str(random.randint(1990, 2019))
            ratings = str(random.randint(1, 10))
            movie_name = random.choice(movie_names)+' '+str(movie_id*2-1)

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
            lst = [str(movie_id), movie_name, str(release_year), str(ratings), genre]
            self.f3.write('\t'.join(lst)+"\n")
            for star in star_list:
                self.f4.write(str(star)+"\t"+str(movie_id)+"\n")

    def close_files(self):
        self.f2.close()
        self.f3.close()
        self.f4.close()
        self.f5.close()

    def generate_data(self):
        self.create_actor_relationship_data()
        self.create_movie_relationship_data()
        self.close_files()


if __name__ == "__main__":
    # Provided only for testing this module separately (by changing within the run.sh to "python3 -m [module_name]")
    data_generator = Neo4jDataGenerator()
    print("Generating Data...")
    data_generator.generate_data()
