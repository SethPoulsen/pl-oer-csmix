import random
import os

import time

from data_constraints_generator import DataConstraintGenerator


popular_first_names = ["Alice", "Amelia", "Bob", "Charlie", "Doug", "Emily",
					"Freya", "G-eazy", "Hisham", "Isabella", "Jack"]				

popular_last_names = ["Anderson", "Bing", "Cho", "Da-Cruz", "Espenson",
					"Frost", "Glow", "Hipster", "Indiana", "Joe", "Watson"]

cities = ["New York", "Washington D.C", "San Francisco", "Chicago", "Los Angeles", "Austin", 
		  "Seattle", "Denver", "Houston", "Boston", "Cahokia", "Cairo", "Canton", "Carbondale", 
          "Carlinville", "Carthage", "Centralia", "Champaign", "Charleston", "Chester", 
          "Cicero", "Collinsville", "Urbana"]

cuisines = ["Chinese", "Mexican", "Italian", "Indian", "American", "Japanese", "Thai", 
			"Greek", "French", "Lebanese"]

countries = ["USA", "UK", "Australia", "Mexico", "Canada"]

restaurant_names = ["The Lady & Sons", "Chez Panisse Cafe", "Spago", "Chipotle Mexican Grill", 
					"Burgrill", "The Gourmet Kitchen", "Banana Leaf", "Yum Yum Tree", "McDonald's", 
                    "Pizza Hut", "Piano Piano", "Pane e Vino", "Pho With Us", "Pita Pan",
                    "Planet of the Crepes", "Patati Patata", "Pork on a Fork", "Peg Leg Porker", 
                    "Phlavz", "Plan B Burger", "Promiscuous Fork"]


persons = []
restaurants = []
product_list=[]
brand_list = []
product_names=["Phone","iPad","Camera","Notebook","Laptop","Dress","TV","Refrigerator","Car","Bike",
 					"Cosmetics","Hard disk","Bag","Travel bag", "Shoes"]
brand_names=['Apple','Nike','Samsung','Sephora','Sony']

brand_product_dict={'Apple':['Watch','iPhone','iPad','TV','iPod','AirTag'],'Samsung':['TV','Galaxy Note','Camera','TV','Refrigerator','Galaxy'],'Nike':['Bag','Gloves','Shoes'],'Sephora':['Makeup','Skincare','Haircare'],'Sony':['Camera','TV','Phone','Headphones']}

# Neo4j import files' location for using LOAD CSV WITH clause
NEO4J_IMPORT_DIR = "/var/lib/neo4j/import/"

ITEM_COUNT = 50


class Neo4jDataGenerator:
	"""
	Sets up CSV files of nodes and relation data in the NEO4J_IMPORT_DIR for later dataset generation within the
	neo4j_grader_main.py with native Cypher on the Neo4j Database. (This is how we make the data injection into
	the Graph database faster!)
	"""

	def __init__(self):
		# Data Constraint generator
		self.data_constraint_generator = DataConstraintGenerator()  # used to generate constraint data
		self.TA_defined_person_name_to_id_map = {}  # Used for keeping track of TA's provided persons with their generated IDs
		self.TA_defined_restaurant_name_to_id_map = {}

		# Used to create headers for all .*-cypher.csv files for Cypher import
		self.f2 = open(NEO4J_IMPORT_DIR + 'person-nodes-cypher.csv', 'w+')
		self.f3 = open(NEO4J_IMPORT_DIR + 'restaurant-nodes-cypher.csv', 'w+')
		self.f4 = open(NEO4J_IMPORT_DIR + 'personToRestaurant-cypher.csv', 'w+')
		self.f5 = open(NEO4J_IMPORT_DIR + 'personToPerson-cypher.csv', 'w+')
		self.f6 = open(NEO4J_IMPORT_DIR + 'cuisine-nodes-cypher.csv', 'w+')
		self.f7 = open(NEO4J_IMPORT_DIR + 'restaurantToCuisine-cypher.csv', 'w+')
		self.f8 = open(NEO4J_IMPORT_DIR + 'city-nodes-cypher.csv', 'w+')
		self.f9 = open(NEO4J_IMPORT_DIR + 'restaurantToCity-cypher.csv', 'w+')
		self.f10 = open(NEO4J_IMPORT_DIR + 'personToCity-cypher.csv', 'w+')
		#Online store database
		self.f11 = open(NEO4J_IMPORT_DIR + 'products-nodes-cypher.csv', 'w+')
		self.f12 = open(NEO4J_IMPORT_DIR + 'brands-nodes-cypher.csv', 'w+')
		self.f13 = open(NEO4J_IMPORT_DIR + 'ProductsToBrands-cypher.csv', 'w+')
		self.f14 = open(NEO4J_IMPORT_DIR + 'PersonBuyProducts-cypher.csv', 'w+')
		self.f15 = open(NEO4J_IMPORT_DIR + 'PersonWishProducts-cypher.csv', 'w+')

		# Write in Headers for Cypher to create data through "LOAD CSV WITH HEADERS" clause
		self.f2.write("person_id,person_name,birth_year\n")
		self.f3.write("restaurant_id,restaurant_name,established_year,ratings\n")
		self.f4.write("person_id,restaurant_id\n")
		self.f5.write("person1_id,person2_id\n")
		self.f6.write("cuisine_id,cuisine_name\n")
		self.f7.write("restaurant_id,cuisine_id\n")
		self.f8.write("city_id,city_name\n")
		self.f9.write("restaurant_id,city_id\n")
		self.f10.write("person_id,city_id\n")
		self.f11.write("product_id,product_name,price,quantity,rate\n")
		self.f12.write("brand_id,brand_name,year_established\n")
		self.f13.write("product_id,brand_id\n")
		self.f14.write("person_id,product_id\n")
		self.f15.write("person_id,product_id\n")

	def create_person_relationship_data(self):
		PERSON_ENTITY_NAME = "Person"
		PERSON_NAME = "person_name"
		PERSON_BIRTH_YEAR = "birth_year"

		# In order to create relation of friends between two person nodes, we need this virtual entity to be
		# provided by the TA in order to create friend relationships within the database.
		# A mapping data structure also needs to be implemented to keep track of friendship IDs if this is provided by the TA.
		FRIEND_WITH_RELATIONSHIP_ENTITY_NAME = "FriendsWith"
		PERSON_FRIEND_NAME = "person_friend_name"  # What this should be provided is using the IN operator in the csv file
		# RIGHT NOW THE LOGIC IS THAT IF TAS PROVIDE ANY person NAME IN THE CSV FILE FOR THE VIRTUAL ENTITY - FriendsWith
		# ALL PROVIDED person NAMES WOULD BE FRIENDS OF EACH OTHER
		friend_with_constraint_dict_list = self.data_constraint_generator.generate_data_instances(
			FRIEND_WITH_RELATIONSHIP_ENTITY_NAME)
		friend_names_list = [data_dict[PERSON_FRIEND_NAME] for data_dict in friend_with_constraint_dict_list if
							 PERSON_FRIEND_NAME in data_dict]
		data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(PERSON_ENTITY_NAME)

		constraint_index = 0
		for person_id in range(0, ITEM_COUNT):
			if constraint_index < len(data_constraint_dict_list):
				data_constraint_dict = data_constraint_dict_list[constraint_index]

				if PERSON_NAME in data_constraint_dict:
					person_name = data_constraint_dict[PERSON_NAME]

					# Keep track of self defined name and given id
					# Used to see if friends are defined by the TA or should be randomized
					self.TA_defined_person_name_to_id_map[person_name] = person_id
				else:
					person_name = popular_first_names[person_id // 11] + ' ' + popular_last_names[person_id % 11]


				birth_year = data_constraint_dict[PERSON_BIRTH_YEAR] \
					if PERSON_BIRTH_YEAR in data_constraint_dict else str(random.randint(1970, 2010))

				persons.append([person_id, person_name, birth_year])
				lst = [str(person_id), person_name, str(birth_year)]
				self.f2.write(','.join(lst) + "\n")

				# If self.TA_defined_person_name_to_id_map exists with entries, as well as virtual entity (FriendsWith) contains
				# data it means TAs have defined friendship and should not be randomized
				if self.TA_defined_person_name_to_id_map and friend_with_constraint_dict_list:
					# Create a mapping of TA's constraint data input on friend relationship for current person
					# print(friend_names_list)
					for friend_name in friend_names_list:
						# In case TA's made human error
						if friend_name in self.TA_defined_person_name_to_id_map and friend_name != person_name:  # Excluding oneself
							friend_id = self.TA_defined_person_name_to_id_map[friend_name]
							self.f5.write(str(person_id) + "," + str(friend_id) + "\n")
				else:
					friend_count = random.randint(3, 13)
					friend_list = []
					while len(friend_list) < friend_count:
						friend_id = random.randint(0, 99)
						if friend_id != person_id:
							friend_list.append(friend_id)
					for friend_id in friend_list:
						self.f5.write(str(person_id) + "," + str(friend_id) + "\n")

				constraint_index += 1

			else:
				person_name = popular_first_names[person_id//10]+' '+popular_last_names[person_id%10]
				birth_year = str(random.randint(1960, 2000))
				persons.append([person_id, person_name, birth_year])
				lst = [str(person_id), person_name, str(birth_year)]
				self.f2.write(','.join(lst)+"\n")
				friend_count = random.randint(3, 13)
				friend_list = []
				while len(friend_list) < friend_count:
					friend_id = random.randint(0, 99)
					if friend_id != person_id:
						friend_list.append(friend_id)
				for friend_id in friend_list:
					self.f5.write(str(person_id)+","+str(friend_id)+"\n")

		# print(persons)

	def create_restaurant_relationship_data(self):
		RESTAURANT_ENTITY_NAME = "Restaurant"
		RESTAURANT_ESTABLISHED_YEAR = "established_year"
		RESTAURANT_RATINGS = "ratings"
		RESTAURANT_NAME = "restaurant_name"

		data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(RESTAURANT_ENTITY_NAME)

		constraint_index = 0

		for restaurant_id in range(1, ITEM_COUNT):
			if constraint_index < len(data_constraint_dict_list):
				data_constraint_dict = data_constraint_dict_list[constraint_index]

				established_year = data_constraint_dict[RESTAURANT_ESTABLISHED_YEAR] \
					if RESTAURANT_ESTABLISHED_YEAR in data_constraint_dict else str(random.randint(1990, 2020))

				ratings = data_constraint_dict[RESTAURANT_RATINGS] \
					if RESTAURANT_RATINGS in data_constraint_dict else str(random.randint(1, 10))

				if RESTAURANT_NAME in data_constraint_dict:
					restaurant_name = data_constraint_dict[RESTAURANT_NAME]
					# Keep track of self defined name and given id
					self.TA_defined_restaurant_name_to_id_map[restaurant_name] = restaurant_id
				else:
					restaurant_name = random.choice(restaurant_names) + ' ' + str(restaurant_id * 2 - 1)

				restaurants.append([restaurant_id, restaurant_name, established_year, ratings])
				# If users (TAs) have defined their own restaurant as well as their own persons. Then all TA-defined persons
				# WILL ALL like TA-defined Restaurants!
				if self.TA_defined_person_name_to_id_map:
					# print(self.TA_defined_person_name_to_id_map)
					for _, self_defined_person_id in self.TA_defined_person_name_to_id_map.items():
						self.f4.write(str(self_defined_person_id) + "," + str(restaurant_id) + "\n")

					lst = [str(restaurant_id), restaurant_name, str(established_year), str(ratings)]
					self.f3.write(','.join(lst) + "\n")

				else:
					star_count = random.randint(3, 13)
					star_list = []
					star_string = '['
					for i in range(0, star_count):
						star = random.choice(persons)[0]
						if star not in star_list:
							star_list.append(star)
							star_string += '"' + str(star) + '", '

					star_string = star_string[:-2] + ']'
					lst = [str(restaurant_id), restaurant_name, str(established_year), str(ratings)]
					self.f3.write(','.join(lst) + "\n")
					for star in star_list:
						self.f4.write(str(star) + "," + str(restaurant_id) + "\n")

				constraint_index += 1

			else:
				established_year = str(random.randint(1980, 2019))
				ratings = str(random.randint(1, 10))
				restaurant_name = random.choice(restaurant_names)+' '+str(restaurant_id*2-1)
				restaurants.append([restaurant_id, restaurant_name, established_year, ratings])
				star_count = random.randint(3, 13)
				star_list = []
				star_string = '['
				for i in range(0, star_count):
					star = random.choice(persons)[0]
					if star not in star_list:
						star_list.append(star)
						star_string += '"'+str(star)+'", '

				star_string = star_string[:-2]+']'
				lst = [str(restaurant_id), restaurant_name, str(established_year), str(ratings)]
				self.f3.write(','.join(lst)+"\n")
				for star in star_list:
					self.f4.write(str(star)+","+str(restaurant_id)+"\n")

		# print(restaurants)

	def create_cuisine_relationship_data(self):
		CUISINE_ENTITY_NAME = "Cuisine"
		CUISINE_NAME = "cuisine_name"

		data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(CUISINE_ENTITY_NAME)

		constraint_index = 0

		for cuisine_id in range(1, ITEM_COUNT):
			if constraint_index < len(data_constraint_dict_list):
				data_constraint_dict = data_constraint_dict_list[constraint_index]

				cuisine_name = data_constraint_dict[CUISINE_NAME] \
					if CUISINE_NAME in data_constraint_dict \
					else random.choice(cuisines) + ' ' + str(cuisine_id * 2 - 1)

				# If users (TAs) have defined their own cuisine as well as their own restaurant. Then all TA-defined restaurants
				# WILL ALL serve TA-defined Cuisines!
				if self.TA_defined_restaurant_name_to_id_map:
					# print(self.TA_defined_person_name_to_id_map)
					for _, self_defined_restaurant_id in self.TA_defined_restaurant_name_to_id_map.items():
						self.f7.write(str(self_defined_restaurant_id) + "," + str(cuisine_id) + "\n")

					lst = [str(cuisine_id), cuisine_name]
					self.f6.write(','.join(lst) + "\n")

				else:
					restaurant_count = random.randint(3, 13)
					restaurant_list = []
					for i in range(0, restaurant_count):
						restaurant = random.choice(restaurants)[0]
						if restaurant not in restaurant_list:
							restaurant_list.append(restaurant)

					lst = [str(cuisine_id), cuisine_name]
					self.f6.write(','.join(lst) + "\n")
					for restaurant in restaurant_list:
						self.f7.write(str(restaurant) + "," + str(cuisine_id) + "\n")

				constraint_index += 1

			else:
				cuisine_name = random.choice(cuisines) + ' ' + str(cuisine_id * 2 - 1)
				restaurant_count = random.randint(3, 13)
				restaurant_list = []
				for i in range(0, restaurant_count):
					restaurant = random.choice(restaurants)[0]
					if restaurant not in restaurant_list:
						restaurant_list.append(restaurant)

				lst = [str(cuisine_id), cuisine_name]
				self.f6.write(','.join(lst) + "\n")
				for restaurant in restaurant_list:
					self.f7.write(str(restaurant) + "," + str(cuisine_id) + "\n")

	def create_city_relationship_data(self):
		CITY_ENTITY_NAME = "City"
		CITY_NAME = "city_name"

		data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(CITY_ENTITY_NAME)

		constraint_index = 0
		if constraint_index < len(data_constraint_dict_list):
			data_constraint_dict = data_constraint_dict_list[constraint_index]
			if CITY_NAME in data_constraint_dict:
				if data_constraint_dict[CITY_NAME] not in cities:
					cities.append(data_constraint_dict[CITY_NAME])
			constraint_index += 1

		for city_id in range(len(cities)):
			restaurant_count = random.randint(3, 13)
			restaurant_list = []
			for i in range(0, restaurant_count):
				restaurant = random.choice(restaurants)[0]
				if restaurant not in restaurant_list:
					restaurant_list.append(restaurant)

			person_count = random.randint(3, 13)
			person_list = []
			for i in range(0, person_count):
				person = random.choice(persons)[0]
				if person not in person_list:
					person_list.append(person)

			lst = [str(city_id), cities[city_id]]
			self.f8.write(','.join(lst) + "\n")
			for restaurant in restaurant_list:
				self.f9.write(str(restaurant) + "," + str(city_id) + "\n")
			for person in person_list:
				self.f10.write(str(person) + "," + str(city_id) + "\n")

	def create_product_brand_relation_data(self):
		PRODUCT_ENTITY_NAME = "Product"
		PRODUCT_NAME = "product_name"
		BRAND_ENTITY_NAME="Brand"
		BRAND_NAME="brand_name"
		brand_list = []
		data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(PRODUCT_ENTITY_NAME)
		brand_data_constraint_dict_list=self.data_constraint_generator.generate_data_instances(BRAND_ENTITY_NAME)

		p_constraint_index = 0
		if p_constraint_index < len(data_constraint_dict_list):
			data_constraint_dict = data_constraint_dict_list[p_constraint_index]
			if PRODUCT_NAME in data_constraint_dict:
				if data_constraint_dict[PRODUCT_NAME] not in product_names:
					product_names.append(data_constraint_dict[PRODUCT_NAME])
			p_constraint_index += 1

		b_constraint_index = 0
		if b_constraint_index < len(brand_data_constraint_dict_list):
			data_constraint_dict = brand_data_constraint_dict_list[b_constraint_index]
			if BRAND_NAME in data_constraint_dict:
				if data_constraint_dict[BRAND_NAME] not in brand_names:
					brand_names.append(data_constraint_dict[BRAND_NAME])
			b_constraint_index += 1

		# brand_id=1
		product_id=1
		#quick fix for update question
		for brand_id,bd_name in enumerate(brand_names):
			year=random.randint(1980, 2010)
			self.f12.write(str(brand_id)+","+bd_name+","+str(year)+ "\n")
			brand_list.append([str(brand_id),bd_name,str(year)])


			for _ in range(10):
				if bd_name in brand_product_dict:
					pd_name = random.choice(brand_product_dict[bd_name]) + ' ' + str(product_id*2-1)
				else:
					pd_name=random.choice(product_names) + ' ' + str(product_id*2-1)
				price=round(random.uniform(50.00,500.00),2)
				qt=random.randint(0,20)
				p_ratings=random.randint(1,5)
				product_list.append([product_id,pd_name,price,qt,p_ratings])

				self.f11.write(str(product_id)+","+str(pd_name)+","+str(price)+","+str(qt)+","+str(p_ratings)+ "\n")
				self.f13.write(str(product_id)+","+str(brand_id)+ "\n")
				product_id+=1
			# brand_id+=1
		


	def create_bought_wishlist_relation_data(self):
			for _ in range(15):
				person=random.choice(persons)[0]
				for _ in range(random.randint(1,10)):
					product=random.choice(product_list)[0]
					self.f14.write(str(person)+","+str(product)+ "\n")

			for _ in range(10):
				person=random.choice(persons)[0]
				for _ in range(random.randint(1,5)):
					product=random.choice(product_list)[0]
					self.f15.write(str(person)+","+str(product)+ "\n")


	def close_files(self):
		self.f2.close()
		self.f3.close()
		self.f4.close()
		self.f5.close()
		self.f6.close()
		self.f7.close()
		self.f8.close()
		self.f9.close()
		self.f10.close()
		self.f11.close()
		self.f12.close()
		self.f13.close()
		self.f14.close()
		self.f15.close()

		print("[NEO4J CSV CREATOR] FINISHED creating CSV FILES TO /var/lib/neo4j/import/")
		os.system("ls /var/lib/neo4j/import/")

	def generate_data(self):
		start_time = time.time()
		self.create_person_relationship_data()
		print("[csv_d_g] person data generated: %s seconds" % (time.time() - start_time))
		self.create_restaurant_relationship_data()
		print("[csv_d_g] Restaurant data generated: %s seconds" % (time.time() - start_time))
		self.create_cuisine_relationship_data()
		print("[csv_d_g] Cuisine data generated: %s seconds" % (time.time() - start_time))
		self.create_city_relationship_data()
		print("[csv_d_g] City data generated: %s seconds" % (time.time() - start_time))
		self.create_product_brand_relation_data()
		print("[csv_d_g] Product and Brand data generated: %s seconds" % (time.time() - start_time))
		self.create_bought_wishlist_relation_data()
		print("[csv_d_g] Bought and Wishlist data generated: %s seconds" % (time.time() - start_time))
		self.close_files()


# if __name__ == "__main__":
#     # Provided only for testing this module separately (by changing within the run.sh to "python3 -m [module_name]")
#     data_generator = Neo4jDataGenerator()
#     print("Generating Data...")
#     data_generator.generate_data()
