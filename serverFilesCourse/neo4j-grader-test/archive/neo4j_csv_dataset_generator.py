import random
import os

from data_constraints_generator import DataConstraintGenerator


popular_first_names = ["Alice", "Bob", "Charlie", "Doug", "Emily",
                    "Freya", "G-eazy", "Hisham", "Isabella", "Jack"]

popular_last_names = ["Anderson", "Bing", "Cho", "Da-Cruz", "Espenson",
                   "Frost", "Glow", "Hipster", "Indiana", "Joe"]

countries = ["USA", "UK", "Australia", "Mexico", "Canada"]

movie_names = ["Avengers", "Spider Man", "Batman", "Superman", "Mission Impossible",
               "Fast & Furious", "Indiana Jones", "Bourne", "Shark Movie", "Horror Movie"]

actors = []

# Neo4j import files' location for using LOAD CSV WITH clause
NEO4J_IMPORT_DIR = "/var/lib/neo4j/import/"


class Neo4jDataGenerator:
    """
    Sets up CSV files of nodes and relation data in the NEO4J_IMPORT_DIR for later dataset generation within the
    neo4j_grader_main.py with native Cypher on the Neo4j Database. (This is how we make the data injection into
    the Graph database faster!)
    """

    def __init__(self):
        # Data Constraint generator
        self.data_constraint_generator = DataConstraintGenerator()  # used to generate constraint data
        self.TA_defined_actor_name_to_id_map = {}  # Used for keeping track of TA's provided actors with their generated IDs

        # Used to create headers for all .*-cypher.csv files for Cypher import
        self.f2 = open(NEO4J_IMPORT_DIR + 'actor-nodes-cypher.csv', 'w+')
        self.f3 = open(NEO4J_IMPORT_DIR + 'movie-nodes-cypher.csv', 'w+')
        self.f4 = open(NEO4J_IMPORT_DIR + 'relationships-cypher.csv', 'w+')
        self.f5 = open(NEO4J_IMPORT_DIR + 'friendRelationships-cypher.csv', 'w+')
        # Write in Headers for Cypher to create data through "LOAD CSV WITH HEADERS" clause
        self.f2.write("actor_id,actor_name,birth_year,birth_country\n")
        self.f3.write("movie_id,movie_name,release_year,ratings,genre\n")
        self.f4.write("actor_id,movie_id\n")
        self.f5.write("person1_id,person2_id\n")

    def create_actor_relationship_data(self):
        ACTOR_ENTITY_NAME = "Actor"
        ACTOR_NAME = "actor_name"
        ACTOR_BIRTH_COUNTRY = "birth_country"
        ACTOR_BIRTH_YEAR = "birth_year"

        # In order to create relation of friends between two actor nodes, we need this virtual entity to be
        # provided by the TA in order to create friend relationships within the database.
        # A mapping data structure also needs to be implemented to keep track of friendship IDs if this is provided by the TA.
        FRIEND_WITH_RELATIONSHIP_ENTITY_NAME = "FriendsWith"
        ACTOR_FRIEND_NAME = "actor_friend_name"  # What this should be provided is using the IN operator in the csv file
        # RIGHT NOW THE LOGIC IS THAT IF TAS PROVIDE ANY ACTOR NAME IN THE CSV FILE FOR THE VIRTUAL ENTITY - FriendsWith
        # ALL PROVIDED ACTOR NAMES WOULD BE FRIENDS OF EACH OTHER
        friend_with_constraint_dict_list = self.data_constraint_generator.generate_data_instances(
            FRIEND_WITH_RELATIONSHIP_ENTITY_NAME)
        friend_names_list = [data_dict[ACTOR_FRIEND_NAME] for data_dict in friend_with_constraint_dict_list if
                             ACTOR_FRIEND_NAME in data_dict]
        data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(ACTOR_ENTITY_NAME)

        constraint_index = 0

        for actor_id in range(0, 100):
            if constraint_index < len(data_constraint_dict_list):
                data_constraint_dict = data_constraint_dict_list[constraint_index]

                if ACTOR_NAME in data_constraint_dict:
                    actor_name = data_constraint_dict[ACTOR_NAME]

                    # Keep track of self defined name and given id
                    # Used to see if friends are defined by the TA or should be randomized
                    self.TA_defined_actor_name_to_id_map[actor_name] = actor_id
                else:
                    actor_name = popular_first_names[actor_id // 10] + ' ' + popular_last_names[actor_id % 10]

                birth_country = data_constraint_dict[ACTOR_BIRTH_COUNTRY] \
                    if ACTOR_BIRTH_COUNTRY in data_constraint_dict else random.choice(countries)

                birth_year = data_constraint_dict[ACTOR_BIRTH_YEAR] \
                    if ACTOR_BIRTH_YEAR in data_constraint_dict else str(random.randint(1960, 2000))

                actors.append([actor_id, actor_name, birth_country])
                lst = [str(actor_id), actor_name, str(birth_year), str(birth_country)]
                self.f2.write(','.join(lst) + "\n")

                # If self.TA_defined_actor_name_to_id_map exists with entries, as well as virtual entity (FriendsWith) contains
                # data it means TAs have defined friendship and should not be randomized
                if self.TA_defined_actor_name_to_id_map and friend_with_constraint_dict_list:
                    # Create a mapping of TA's constraint data input on friend relationship for current actor
                    for friend_name in friend_names_list:
                        # In case TA's made human error
                        if friend_name in self.TA_defined_actor_name_to_id_map and friend_name != actor_name:  # Excluding oneself
                            friend_id = self.TA_defined_actor_name_to_id_map[friend_name]
                            self.f5.write(str(actor_id) + "," + str(friend_id) + "\n")
                else:
                    friend_count = random.randint(3, 13)
                    friend_list = []
                    while len(friend_list) < friend_count:
                        friend_id = random.randint(0, 99)
                        if friend_id != actor_id:
                            friend_list.append(friend_id)
                    for friend_id in friend_list:
                        self.f5.write(str(actor_id) + "," + str(friend_id) + "\n")

                constraint_index += 1

            else:
                actor_name = popular_first_names[actor_id//10]+' '+popular_last_names[actor_id%10]
                birth_country = random.choice(countries)
                birth_year = str(random.randint(1960, 2000))
                actors.append([actor_id, actor_name, birth_country])
                lst = [str(actor_id), actor_name, str(birth_year), str(birth_country)]
                self.f2.write(','.join(lst)+"\n")
                friend_count = random.randint(3, 13)
                friend_list = []
                while len(friend_list) < friend_count:
                    friend_id = random.randint(0, 99)
                    if friend_id != actor_id:
                        friend_list.append(friend_id)
                for friend_id in friend_list:
                    self.f5.write(str(actor_id)+","+str(friend_id)+"\n")

    def create_movie_relationship_data(self):
        MOVIE_ENTITY_NAME = "Movie"
        MOVIE_RELEASE_YEAR = "release_year"
        MOVIE_RATINGS = "ratings"
        MOVIE_NAME = "movie_name"
        MOVIE_GENRE = "genre"

        data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(MOVIE_ENTITY_NAME)

        constraint_index = 0

        for movie_id in range(1, 100):
            if constraint_index < len(data_constraint_dict_list):
                data_constraint_dict = data_constraint_dict_list[constraint_index]

                release_year = data_constraint_dict[MOVIE_RELEASE_YEAR] \
                    if MOVIE_RELEASE_YEAR in data_constraint_dict else str(random.randint(1990, 2019))

                ratings = data_constraint_dict[MOVIE_RATINGS] \
                    if MOVIE_RATINGS in data_constraint_dict else str(random.randint(1, 10))

                movie_name = data_constraint_dict[MOVIE_NAME] \
                    if MOVIE_NAME in data_constraint_dict \
                    else random.choice(movie_names) + ' ' + str(movie_id * 2 - 1)

                genre = data_constraint_dict[MOVIE_GENRE] \
                    if MOVIE_GENRE in data_constraint_dict \
                    else random.choice(['Horror', 'Comedy', 'Romantic', 'Action'])

                # If users (TAs) have defined their own movie as well as their own actors. Then all TA-defined actors
                # WILL ALL act in TA-defined Movies!
                if self.TA_defined_actor_name_to_id_map:
                    # print(self.TA_defined_actor_name_to_id_map)
                    for _, self_defined_actor_id in self.TA_defined_actor_name_to_id_map.items():
                        self.f4.write(str(self_defined_actor_id) + "," + str(movie_id) + "\n")

                    lst = [str(movie_id), movie_name, str(release_year), str(ratings), genre]
                    self.f3.write(','.join(lst) + "\n")

                else:
                    star_count = random.randint(3, 13)
                    star_list = []
                    star_string = '['
                    for i in range(0, star_count):
                        star = random.choice(actors)[0]
                        if star not in star_list:
                            star_list.append(star)
                            star_string += '"' + str(star) + '", '

                    star_string = star_string[:-2] + ']'
                    lst = [str(movie_id), movie_name, str(release_year), str(ratings), genre]
                    self.f3.write(','.join(lst) + "\n")
                    for star in star_list:
                        self.f4.write(str(star) + "," + str(movie_id) + "\n")

                constraint_index += 1

            else:
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
                self.f3.write(','.join(lst)+"\n")
                for star in star_list:
                    self.f4.write(str(star)+","+str(movie_id)+"\n")

    def close_files(self):
        self.f2.close()
        self.f3.close()
        self.f4.close()
        self.f5.close()
        print("[NEO4J CSV CREATOR] FINISHED creating CSV FILES TO /var/lib/neo4j/import/")
        os.system("ls /var/lib/neo4j/import/")

    def generate_data(self):
        self.create_actor_relationship_data()
        self.create_movie_relationship_data()
        self.close_files()


# if __name__ == "__main__":
#     # Provided only for testing this module separately (by changing within the run.sh to "python3 -m [module_name]")
#     data_generator = Neo4jDataGenerator()
#     print("Generating Data...")
#     data_generator.generate_data()
