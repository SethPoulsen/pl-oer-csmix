import random
from collections import namedtuple
from typing import List, NamedTuple
import os

# Student = namedtuple("Student", "NetId FirstName Lastname Department")
# Enrollment = namedtuple("Enrollment", "Netid CRN Credits Score")
# Course = namedtuple("Course", "CRN Title Department Instructor")
class Student(NamedTuple):
    NetId: str
    FirstName: str
    LastName: str
    Department: str


class Enrollment(NamedTuple):
    NetId: str
    CRN: int
    Credits: int
    Score: float


class Course(NamedTuple):
    CRN: int
    Title: str
    Department: str
    Instructor: str


student_list = []
enrollment_list = []
course_list = []

# got 1000 popular first name from internet
popular_first_names = ['Abbott', 'Acevedo', 'Acosta', 'Adams', 'Adkins', 'Aguilar', 'Aguirre', 'Ahmed', 'Alexander',
                       'Alfaro', 'Ali', 'Allen', 'Allison', 'Alvarado', 'Alvarez', 'Andersen', 'Anderson', 'Andrade',
                       'Andrews', 'Anthony', 'Archer', 'Arellano', 'Arias', 'Armstrong', 'Arnold', 'Arroyo', 'Ashley',
                       'Atkins', 'Atkinson', 'Austin', 'Avalos', 'Avery', 'Avila', 'Ayala', 'Ayers', 'Bailey', 'Baker',
                       'Baldwin', 'Ball', 'Ballard', 'Banks', 'Barajas', 'Barber', 'Barker', 'Barnes', 'Barnett',
                       'Barr', 'Barrera', 'Barrett', 'Barron', 'Barry', 'Bartlett', 'Barton', 'Bass', 'Bates', 'Bauer',
                       'Bautista', 'Baxter', 'Bean', 'Beard', 'Beasley', 'Beck', 'Becker', 'Beil', 'Bell', 'Beltran',
                       'Bender', 'Benitez', 'Benjamin', 'Bennett', 'Benson', 'Bentley', 'Benton', 'Berg', 'Berger',
                       'Bernal', 'Bernard', 'Berry', 'Best', 'Bishop', 'Black', 'Blackburn', 'Blackwell', 'Blair',
                       'Blake', 'Blanchard', 'Blankenship', 'Blevins', 'Bond', 'Bonilla', 'Booker', 'Boone', 'Booth',
                       'Bowen', 'Bowers', 'Bowman', 'Boyd', 'Boyer', 'Boyle', 'Bradford', 'Bradley', 'Bradshaw',
                       'Brady', 'Branch', 'Brandt', 'Bravo', 'Brennan', 'Brewer', 'Bridges', 'Briggs', 'Brock',
                       'Brooks', 'Brown', 'Browning', 'Bruce', 'Bryan', 'Bryant', 'Buchanan', 'Buck', 'Buckley',
                       'Bullock', 'Burch', 'Burgess', 'Burke', 'Burnett', 'Burns', 'Burton', 'Bush', 'Butler', 'Byrd',
                       'Cabrera', 'Cain', 'Calderon', 'Caldwell', 'Calhoun', 'Callahan', 'Camacho', 'Cameron',
                       'Campbell', 'Campos', 'Cannon', 'Cano', 'Cantrell', 'Cantu', 'Cardenas', 'Carey', 'Carlson',
                       'Carpenter', 'Carr', 'Carrillo', 'Carroll', 'Carson', 'Carter', 'Case', 'Casey', 'Castaneda',
                       'Castillo', 'Castro', 'Cervantes', 'Chambers', 'Chan', 'Chandler', 'Chang', 'Chapman', 'Charles',
                       'Chase', 'Chavez', 'Chen', 'Cherry', 'Choi', 'Christensen', 'Christian', 'Chung', 'Church',
                       'Cisneros', 'Clark', 'Clarke', 'Clay', 'Clayton', 'Clements', 'Cline', 'Cobb', 'Cochran',
                       'Coffey', 'Cohen', 'Cole', 'Coleman', 'Collier', 'Collins', 'Colon', 'Combs', 'Compton',
                       'Conley', 'Conner', 'Conrad', 'Contreras', 'Conway', 'Cook', 'Cooper', 'Copeland', 'Cordova',
                       'Corona', 'Correa', 'Cortes', 'Cortez', 'Costa', 'Cox', 'Craig', 'Crane', 'Crawford', 'Crosby',
                       'Cross', 'Cruz', 'Cuevas', 'Cummings', 'Cunningham', 'Curry', 'Curtis', 'Dalton', 'Daniel',
                       'Daniels', 'Daugherty', 'Davenport', 'David', 'Davidson', 'Davila', 'Davis', 'Dawson', 'Day',
                       'Dean', 'Decker', 'Dejesus', 'Delacruz', 'Delarosa', 'Deleon', 'Delgado', 'Dennis', 'Diaz',
                       'Dickerson', 'Dickson', 'Dillon', 'Dixon', 'Dodson', 'Dominguez', 'Donaldson', 'Donovan',
                       'Dorsey', 'Dougherty', 'Douglas', 'Doyle', 'Drake', 'Duarte', 'Dudley', 'Duffy', 'Duke',
                       'Duncan', 'Dunlap', 'Dunn', 'Duran', 'Durham', 'Dyer', 'Eaton', 'Edwards', 'Elliott', 'Ellis',
                       'Ellison', 'English', 'Enriquez', 'Erickson', 'Escobar', 'Esparza', 'Espinosa', 'Espinoza',
                       'Esquivel', 'Estes', 'Estrada', 'Evans', 'Everett', 'Farley', 'Farmer', 'Farrell', 'Faulkner',
                       'Felix', 'Ferguson', 'Fernandez', 'Fields', 'Figueroa', 'Finley', 'Fischer', 'Fisher',
                       'Fitzgerald', 'Fitzpatrick', 'Fleming', 'Fletcher', 'Flores', 'Flowers', 'Floyd', 'Flynn',
                       'Foley', 'Ford', 'Foster', 'Fowler', 'Fox', 'Francis', 'Franco', 'Frank', 'Franklin', 'Frazier',
                       'Frederick', 'Freeman', 'French', 'Friedman', 'Frost', 'Fry', 'Frye', 'Fuentes', 'Fuller',
                       'Gaines', 'Galindo', 'Gallagher', 'Gallegos', 'Galvan', 'Garcia', 'Gardner', 'Garner', 'Garrett',
                       'Garrison', 'Garza', 'Gates', 'Gentry', 'George', 'Gibbs', 'Gibson', 'Gilbert', 'Giles', 'Gill',
                       'Gillespie', 'Gilmore', 'Glass', 'Glenn', 'Glover', 'Golden', 'Gomez', 'Gonzales', 'Gonzalez',
                       'Good', 'Goodman', 'Goodwin', 'Gordon', 'Gould', 'Graham', 'Grant', 'Graves', 'Gray', 'Green',
                       'Greene', 'Greer', 'Gregory', 'Griffin', 'Griffith', 'Grimes', 'Gross', 'Guerra', 'Guerrero',
                       'Guevara', 'Gutierrez', 'Guzman', 'Hahn', 'Hail', 'Hale', 'Haley', 'Hall', 'Hamilton', 'Hammond',
                       'Hampton', 'Hancock', 'Hanna', 'Hansen', 'Hanson', 'Hardin', 'Harding', 'Hardy', 'Harmon',
                       'Harper', 'Harrell', 'Harrington', 'Harris', 'Harrison', 'Hart', 'Hartman', 'Harvey', 'Hawkins',
                       'Hayden', 'Hayes', 'Haynes', 'Heath', 'Hebert', 'Henderson', 'Hendricks', 'Hendrix', 'Henry',
                       'Hensley', 'Henson', 'Herman', 'Hernandez', 'Herrera', 'Herring', 'Hess', 'Hester', 'Hickman',
                       'Hicks', 'Higgins', 'Hill', 'Hines', 'Hinton', 'Ho', 'Hobbs', 'Hodge', 'Hodges', 'Hoffman',
                       'Hogan', 'Holland', 'Holloway', 'Holmes', 'Holt', 'Hood', 'Hoover', 'Hopkins', 'Horn', 'Horne',
                       'Horton', 'House', 'Houston', 'Howard', 'Howe', 'Howell', 'Huang', 'Hubbard', 'Huber', 'Hudson',
                       'Huerta', 'Huff', 'Huffman', 'Hughes', 'Hull', 'Humphrey', 'Hunt', 'Hunter', 'Hurley', 'Hurst',
                       'Hutchinson', 'Huynh', 'Ibarra', 'Ingram', 'Jackson', 'Jacobs', 'Jacobson', 'James', 'Jaramillo',
                       'Jarvis', 'Jefferson', 'Jenkins', 'Jennings', 'Jensen', 'Jimenez', 'Johns', 'Johnson',
                       'Johnston', 'Jones', 'Jordan', 'Joseph', 'Juarez', 'Kane', 'Kaur', 'Keith', 'Keller', 'Kelley',
                       'Kelly', 'Kemp', 'Kennedy', 'Kent', 'Kerr', 'Khan', 'Kim', 'King', 'Kirby', 'Kirk', 'Klein',
                       'Kline', 'Knapp', 'Knight', 'Knox', 'Koch', 'Kramer', 'Krueger', 'Lam', 'Lamb', 'Lambert',
                       'Landry', 'Lane', 'Lang', 'Lara', 'Larsen', 'Larson', 'Lawrence', 'Lawson', 'Le', 'Leach',
                       'Leal', 'Leblanc', 'Lee', 'Leon', 'Leonard', 'Lester', 'Levy', 'Lewis', 'Li', 'Lim', 'Lin',
                       'Lindsey', 'Little', 'Liu', 'Livingston', 'Lloyd', 'Logan', 'Long', 'Lopez', 'Love', 'Lowe',
                       'Lowery', 'Lozano', 'Lu', 'Lucas', 'Lucero', 'Lugo', 'Luna', 'Lynch', 'Lynn', 'Lyons',
                       'Macdonald', 'Macias', 'Mack', 'Madden', 'Maddox', 'Magana', 'Mahoney', 'Maldonado', 'Malone',
                       'Mann', 'Manning', 'Marin', 'Marks', 'Marquez', 'Marsh', 'Marshall', 'Martin', 'Martinez',
                       'Mason', 'Massey', 'Mata', 'Mathews', 'Mathis', 'Matthews', 'Maxwell', 'May', 'Mayer', 'Maynard',
                       'Mayo', 'Mays', 'Mcbride', 'Mccall', 'Mccann', 'Mccarthy', 'Mccarty', 'Mcclain', 'Mcclure',
                       'Mcconnell', 'Mccormick', 'Mccoy', 'Mccullough', 'Mcdaniel', 'Mcdonald', 'Mcdowell', 'Mcfarland',
                       'Mcgee', 'Mcguire', 'Mcintosh', 'Mcintyre', 'Mckay', 'Mckee', 'Mckenzie', 'Mckinney',
                       'Mclaughlin', 'Mclean', 'Mcmahon', 'Mcmillan', 'Mcpherson', 'Meadows', 'Medina', 'Medrano',
                       'Mejia', 'Melendez', 'Melton', 'Mendez', 'Mendoza', 'Mercado', 'Merritt', 'Meyer', 'Meyers',
                       'Meza', 'Michael', 'Middleton', 'Miles', 'Miller', 'Mills', 'Miranda', 'Mitchell', 'Molina',
                       'Monroe', 'Montes', 'Montgomery', 'Montoya', 'Moody', 'Moon', 'Moore', 'Mora', 'Morales',
                       'Moran', 'Moreno', 'Morgan', 'Morris', 'Morrison', 'Morrow', 'Morse', 'Morton', 'Moses',
                       'Mosley', 'Moss', 'Moyer', 'Mueller', 'Mullen', 'Mullins', 'Munoz', 'Murillo', 'Murphy',
                       'Murray', 'Myers', 'Nash', 'Nava', 'Navarro', 'Neal', 'Nelson', 'Newman', 'Newton', 'Nguyen',
                       'Nichols', 'Nicholson', 'Nielsen', 'Nixon', 'Noble', 'Nolan', 'Norman', 'Norris', 'Norton',
                       'Novak', 'Nunez', 'Obrien', 'Ochoa', 'Oconnell', 'Oconnor', 'Odom', 'Odonnell', 'Oliver',
                       'Olsen', 'Olson', 'Oneal', 'Oneill', 'Orozco', 'Orr', 'Ortega', 'Ortiz', 'Osborne', 'Owen',
                       'Owens', 'Pace', 'Pacheco', 'Padilla', 'Page', 'Palacios', 'Palmer', 'Park', 'Parker', 'Parks',
                       'Parra', 'Parrish', 'Parsons', 'Patel', 'Patrick', 'Patterson', 'Patton', 'Paul', 'Payne',
                       'Pearson', 'Peck', 'Pena', 'Pennington', 'Peralta', 'Perez', 'Perkins', 'Perry', 'Person',
                       'Peters', 'Petersen', 'Peterson', 'Pham', 'Phan', 'Phelps', 'Phillips', 'Pierce', 'Pineda',
                       'Pittman', 'Pitts', 'Pollard', 'Ponce', 'Poole', 'Pope', 'Porter', 'Portillo', 'Potter', 'Potts',
                       'Powell', 'Powers', 'Pratt', 'Preston', 'Price', 'Prince', 'Proctor', 'Pruitt', 'Pugh', 'Quinn',
                       'Quintana', 'Quintero', 'Ramirez', 'Ramos', 'Ramsey', 'Randall', 'Randolph', 'Rangel',
                       'Rasmussen', 'Ray', 'Raymond', 'Reed', 'Reese', 'Reeves', 'Reid', 'Reilly', 'Reyes', 'Reyna',
                       'Reynolds', 'Rhodes', 'Rice', 'Rich', 'Richard', 'Richards', 'Richardson', 'Richmond', 'Riley',
                       'Rios', 'Rivas', 'Rivera', 'Rivers', 'Roach', 'Robbins', 'Roberson', 'Roberts', 'Robertson',
                       'Robinson', 'Robles', 'Rocha', 'Rodgers', 'Rodriguez', 'Rogers', 'Rojas', 'Rollins', 'Roman',
                       'Romero', 'Rosales', 'Rosario', 'Rosas', 'Rose', 'Ross', 'Roth', 'Rowe', 'Rowland', 'Roy',
                       'Rubio', 'Ruiz', 'Rush', 'Russell', 'Russo', 'Ryan', 'Salas', 'Salazar', 'Salgado', 'Salinas',
                       'Sampson', 'Sanchez', 'Sanders', 'Sandoval', 'Sanford', 'Santana', 'Santiago', 'Santos',
                       'Saunders', 'Savage', 'Sawyer', 'Schaefer', 'Schmidt', 'Schmitt', 'Schneider', 'Schroeder',
                       'Schultz', 'Schwartz', 'Scott', 'Sellers', 'Serrano', 'Sexton', 'Shaffer', 'Shah', 'Shannon',
                       'Sharp', 'Shaw', 'Shelton', 'Shepard', 'Shepherd', 'Sheppard', 'Sherman', 'Shields', 'Short',
                       'Sierra', 'Silva', 'Simmons', 'Simon', 'Simpson', 'Sims', 'Singh', 'Singleton', 'Skinner',
                       'Sloan', 'Small', 'Smith', 'Snow', 'Snyder', 'Solis', 'Solomon', 'Sosa', 'Soto', 'Sparks',
                       'Spears', 'Spence', 'Spencer', 'Stafford', 'Stanley', 'Stanton', 'Stark', 'Steele', 'Stein',
                       'Stephens', 'Stephenson', 'Stevens', 'Stevenson', 'Stewart', 'Stokes', 'Stone', 'Stout',
                       'Strickland', 'Strong', 'Stuart', 'Suarez', 'Sullivan', 'Summers', 'Sutton', 'Swanson',
                       'Sweeney', 'Tang', 'Tanner', 'Tapia', 'Tate', 'Taylor', 'Terrell', 'Terry', 'Thomas', 'Thompson',
                       'Thornton', 'Todd', 'Torres', 'Townsend', 'Tran', 'Travis', 'Trejo', 'Trevino', 'Trujillo',
                       'Truong', 'Tucker', 'Turner', 'Tyler', 'Underwood', 'Valdez', 'Valencia', 'Valentine',
                       'Valenzuela', 'Vance', 'Vang', 'Vargas', 'Vasquez', 'Vaughan', 'Vaughn', 'Vazquez', 'Vega',
                       'Velasquez', 'Velazquez', 'Velez', 'Ventura', 'Villa', 'Villalobos', 'Villanueva', 'Villarreal',
                       'Villegas', 'Vincent', 'Vo', 'Vu', 'Wade', 'Wagner', 'Walker', 'Wall', 'Wallace', 'Waller',
                       'Walls', 'Walsh', 'Walter', 'Walters', 'Walton', 'Wang', 'Ward', 'Ware', 'Warner', 'Warren',
                       'Washington', 'Waters', 'Watkins', 'Watson', 'Watts', 'Weaver', 'Webb', 'Weber', 'Webster',
                       'Weeks', 'Weiss', 'Welch', 'Wells', 'West', 'Wheeler', 'Whitaker', 'White', 'Whitehead',
                       'Whitney', 'Wiggins', 'Wilcox', 'Wiley', 'Wilkerson', 'Wilkins', 'Wilkinson', 'Williams',
                       'Williamson', 'Willis', 'Wilson', 'Winters', 'Wise', 'Wolf', 'Wolfe', 'Wong', 'Wood', 'Woodard',
                       'Woods', 'Woodward', 'Wright', 'Wu', 'Wyatt', 'Xiong', 'Yang', 'Yates', 'Yoder', 'York', 'Young',
                       'Yu', 'Zamora', 'Zavala', 'Zhang', 'Zimmerman', 'Zuniga']

popular_last_names = ["Anderson", "Bing", "Cho", "Da-Cruz", "Espenson",
                      "Frost", "Glow", "Hipster", "Indiana", "Joe"]

department_list = ["CS", "ECE", "Physics", "Economics", "Statistics", "Finance", "Accounting", "Psychology", "Sports",
                   "Music"]

num_of_student = 100
num_of_course = 100
for first_name in random.sample(popular_first_names, num_of_student):
    lottery_num = random.randint(0, 9)
    last_name = popular_first_names[lottery_num % 10]
    netid = first_name.lower()[:7] + str(lottery_num)
    department = department_list[lottery_num % 10]
    student_list.append(Student(netid, first_name, last_name, department))

random_CRNS = random.sample(range(100, 999), num_of_course)
if 127 not in random_CRNS:
    random_CRNS.append(127)
if 301 not in random_CRNS:
    random_CRNS.append(301)

for CRN in random_CRNS:
    credit = random.randint(0, 4)
    lottery_num = random.randint(0, len(popular_first_names) - 1)
    department = department_list[lottery_num % 10]
    instructor_first_name = popular_first_names[lottery_num]
    instructor_last_name = popular_last_names[lottery_num % 10]
    instructor_name = instructor_first_name + " " + instructor_last_name
    title = department + str(random.randint(100, 599))
    course_list.append(Course(CRN, title, department, instructor_name))

for s in student_list:
    num_course_taken = random.randint(0, 6)
    courses_taken = random.sample(random_CRNS, num_course_taken)
    # a = len(set(courses_taken))
    # if a != len(courses_taken):
    #     print(set(courses_taken),num_course_taken)
    for crn in courses_taken:
        credit = random.randint(0, 4)
        score = random.uniform(0, 100)
        enrollment_list.append(Enrollment(s.NetId, crn, credit, score))

schemas = """
CREATE TABLE IF NOT EXISTS Students(
  NetId VARCHAR(10),
  FirstName VARCHAR(255),
  LastName VARCHAR(255),
  Department VARCHAR(100),
  PRIMARY KEY (NetId)
);

CREATE TABLE IF NOT EXISTS Enrollments(
  NetId VARCHAR(10),
  CRN INT,
  Credits INT,
  Score REAL,
  PRIMARY KEY (NetId, CRN)
);

CREATE TABLE IF NOT EXISTS Courses(
  CRN INT,
  Title VARCHAR(255),
  Department VARCHAR(100),
  Instructor VARCHAR(255),
  PRIMARY KEY (CRN)
);\n
"""

static_data = """
INSERT IGNORE INTO Students VALUES
  ("tswift2", "Taylor", "Swift", "CS"),
  ("esheeran5", "Ed", "Sheeran", "ECE"),
  ("ssmith6", "Sam", "Smith", "ECE"),
  ("tjones9", "Tom", "Jones", "ECE"),
  ("bmars4", "Bruno", "Mars", "Physics");

INSERT IGNORE INTO Enrollments VALUES
  ("tswift2", 124, 4, 90),
  ("tswift2", 125, 3, 96),
  ("tswift2", 126, 3, 88),
  ("tswift2", 127, 4, 92),
  ("esheeran5", 124, 4, 70),
  ("esheeran5", 125, 3, 78),
  ("tjones9", 125, 3, 60),
  ("tjones9", 127, 4, 77),
  ("ssmith6", 124, 4, 87),
  ("bmars4", 124, 4, 99);

INSERT IGNORE INTO Courses VALUES
(124, "Deep Learning", "CS", "Andrew Ng"),
(125, "Data Base", "CS", "Abdu Alawini"),
(126, "Fieds and Waves", "ECE", "Erhan Kudeki"),
(127, "Computer System", "ECE", "Michael Bailey");
"""
with open('/grade/tests/setup.sql', 'w+') as f1:
    f1.write(schemas)
    f1.write(static_data)
    for s in student_list:
        f1.write(
            f"""INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("{s.NetId}","{s.FirstName}","{s.LastName}","{s.Department}");\n""")
    for e in enrollment_list:
        f1.write(
            f"""INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("{e.NetId}",{e.CRN},{e.Credits},{e.Score});\n""")
    for c in course_list:
        f1.write(
            f"""INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES ({c.CRN},"{c.Title}","{c.Department}","{c.Instructor}");\n""")

schemas = """CREATE TABLE IF NOT EXISTS Customers(
  CustomerId INT,
  FirstName VARCHAR(255),
  LastName VARCHAR(255),
  PhoneNumber REAL,
  PRIMARY KEY (CustomerId)
);

CREATE TABLE IF NOT EXISTS Purchases(
  PurchaseId INT,
  CustomerId INT,
  ProductId INT,
  Price INT,
  PRIMARY KEY (PurchaseId)
);

CREATE TABLE IF NOT EXISTS Products(
  ProductId INT,
  ProductName VARCHAR(255),
  BrandName VARCHAR(255),
  YearReleased INT,
  PRIMARY KEY (ProductId)
);

CREATE TABLE IF NOT EXISTS Brands(
  BrandName VARCHAR(255),
  YearEstablished INT,
  CEO VARCHAR(255),
  PRIMARY KEY (BrandName)
);\n
"""

num_of_customers = 100
num_of_products = 100


class Customer(NamedTuple):
    Customer_Id: int
    FirstName: str
    LastName: str
    PhoneNumber: int


class Purchase(NamedTuple):
    PurchaseId: int
    Customer_Id: int
    ProductId: int
    Price: int


class Product(NamedTuple):
    ProductId: int
    ProductName: str
    BrandName: str
    YearReleased: int


class Brand(NamedTuple):
    BrandName: str
    YearEstablished: int
    CEO: str


customer_list = []
purchase_list = []
product_list = [
    Product(0, "iPhone 7", "Apple", 2016),
    Product(1, "iPhone 8", "Apple", 2017),
    Product(2, "iPhone X", "Apple", 2017),
    Product(3, "iPhone XS", "Apple", 2018),
    Product(4, "iPhone XR", "Apple", 2018),
    Product(5, "Samsung Galaxy S10", "Samsung", 2019),
    Product(6, "Samsung Galaxy Note 9", "Samsung", 2018),
    Product(7, "OnePlus 7 Pro", "OnePlus", 2019),
    Product(8, "Google Pixel 3 XL", "Google", 2018),
    Product(9, "Honor View 20", "Honor", 2019),
    Product(10, "HUAWEI P30 Pro", "HUAWEI", 2019),
    Product(11, "HUAWEI Mate 20 X", "HUAWEI", 2019),
    Product(12, "HUAWEI Nova 5T", "HUAWEI", 2019),
    Product(13, "HUAWEI P20", "HUAWEI", 2018),
    Product(14, "Redmi 7A", "MI", 2019),
    Product(15, "Redmi Note7", "MI", 2019),
    Product(16, "Mi 9T Pro", "MI", 2019),
    Product(17, "Mi A3", "MI", 2019),
    Product(18, "Mi 9 SE", "MI", 2019),
    Product(19, "Reno2 F", "OPPO", 2019),
    Product(20, "K3", "OPPO", 2019)]

brand_list = [
    Brand("Apple", 1976, "Tim Cook"),
    Brand("Samsung", 1938, "Ki Nam Kim, Hyun Suk Kim, Dong Jin Koh"),
    Brand("OnePlus", 2013, "Pete Lau"),
    Brand("Google", 1998, "Sundar Pichai"),
    Brand("Honor", 2013, "George Zhao"),
    Brand("HUAWEI", 1987, "Zhengfei Ren"),
    Brand("OPPO", 2004, "Tony Chen"),
    Brand("MEIZU", 2003, "Zhang Huang"),
    Brand("MI", 2010, "Jun Lei"),
    Brand("vivo", 2009, "Wei Shen, YongPing Duan")]

for Customer_Id, first_name in enumerate(random.sample(popular_first_names, num_of_customers)):
    lottery_num = random.randint(0, 9)
    last_name = popular_first_names[lottery_num % 10]
    phone = random.randint(1000000000, 9999999999)
    customer_list.append(Customer(Customer_Id, first_name, last_name, phone))
purchase_count = 0
for c in customer_list:
    buy_n = random.randint(0, 2)
    bought = random.sample(range(len(product_list)), buy_n)
    for product_id in bought:
        purchase_list.append(Purchase(purchase_count, c.Customer_Id, product_id, random.randint(3000, 6000)))
        purchase_count += 1

product_list.append(Product(70, "XBOX", "MICROSOFT", 2013))
brand_list.append(Brand("MICROSOFT", 1975, "Bill Gates"))

static_data2 = """
INSERT IGNORE INTO Customers VALUES
  (0,"Eleanora","Lacey",3224481987),
  (1,"Wesley","Herman",3818704297),
  (2,"Elfreda","Patrick",6152434505),
  (3,"James","Grenville",4604696876),
  (4,"Jayme","Castle",9888068257),
  (5,"Christopher","Ryley",6269151400),
  (6,"Barry","Easom",9946933996),
  (7,"Aretha","Tyson",1043606869),
  (8,"Josh","Derrickson",4901831434),
  (9,"Rebecca","Harlan",3022508325),
  (10,"Lowell","Best",8355960400),
  (11,"Jannah","Gladyn",3097916838),
  (12,"Ellie","Ball",5528466008),
  (13,"Jenna","Watts",9970238914),
  (14,"Stacey","Anthonyson",2877513601),
  (15,"Jez","Hopper",4272233457),
  (16,"Janet","Ogden",6758513134),
  (17,"Shonda","Winchester",2491137414),
  (18,"Kelly","Jerome",5994784854),
  (19,"Bethany","Barnet",1809417852),
  (20,"Deven","Miles",8293617850),
  (21,"Haylie","Roy",1792049905),
  (22,"Adriana","Mendez",6341264996),
  (23,"Luisa","Alamilla",5975485340),
  (24,"Luis","Alamilla",5983411596);

INSERT IGNORE INTO Purchases VALUES
  (0, 11, 4, 426),
  (1, 12, 3, 129),
  (2, 11, 5, 675),
  (3, 8, 3, 872),
  (4, 16, 9, 500),
  (5, 0, 0, 123),
  (6, 19, 1, 100),
  (7, 20, 5, 780),
  (8, 22, 2, 716),
  (9, 11, 5, 951),
  (10, 22, 1, 165),
  (11, 0, 7, 569),
  (12, 8, 8, 556),
  (13, 19, 2, 813),
  (14, 17, 8, 175),
  (15, 3, 2, 51),
  (16, 2, 2, 750),
  (17, 5, 1, 957),
  (18, 14, 2, 373),
  (19, 13, 1, 439),
  (20, 11, 7, 215),
  (21, 0, 6, 395),
  (22, 7, 4, 476),
  (23, 21, 0, 928),
  (24, 19, 1, 706),
  (25, 20, 0, 466),
  (26, 21, 5, 553),
  (27, 5, 2, 232),
  (28, 5, 2, 851),
  (29, 6, 2, 401),
  (30, 1, 4, 739),
  (31, 0, 6, 889),
  (32, 16, 4, 472),
  (33, 9, 2, 876),
  (34, 2, 9, 104),
  (35, 4, 8, 410),
  (36, 13, 8, 571),
  (37, 22, 8, 598),
  (38, 24, 7, 236),
  (39, 4, 3, 449),
  (40, 12, 3, 727),
  (41, 8, 4, 734),
  (42, 15, 9, 444),
  (43, 22, 8, 319),
  (44, 11, 1, 958),
  (45, 17, 0, 721),
  (46, 10, 3, 304),
  (47, 18, 9, 664),
  (48, 23, 7, 645),
  (49, 1, 5, 657),
  (50, 11, 4, 500);

INSERT IGNORE INTO Products VALUES
  (0, "iPhone 7", "Apple", 2016),
  (1, "iPhone 8", "Apple", 2017),
  (2, "iPhone X", "Apple", 2017),
  (3, "iPhone XS", "Apple", 2018),
  (4, "iPhone XR", "Apple", 2018),
  (5, "Samsung Galaxy S10", "Samsung", 2019),
  (6, "Samsung Galaxy Note 9", "Samsung", 2018),
  (7, "OnePlus 7 Pro", "OnePlus", 2019),
  (8, "Google Pixel 3 XL", "Google", 2018),
  (9, "Honor View 20", "Honor", 2019);

INSERT IGNORE INTO Brands VALUES
  ("Apple",1976,"Tim Cook"),
  ("Samsung",1938,"Ki Nam Kim, Hyun Suk Kim, Dong Jin Koh"),
  ("OnePlus",2013,"Pete Lau"),
  ("Google",1998,"Sundar Pichai"),
  ("Honor",2013,"George Zhao");
"""
with open("/grade/tests/setup.sql", "a") as f:
    f.write(schemas)
    f.write(static_data2)
    for c in customer_list:
        f.write(
            f"""INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES ({c.Customer_Id},"{c.FirstName}","{c.LastName}",{c.PhoneNumber});\n""")
    for p in purchase_list:
        f.write(
            f"""INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES ({p.PurchaseId},{p.Customer_Id},{p.ProductId},{p.Price});\n""")
    for p in product_list:
        f.write(
            f"""INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES ({p.ProductId},"{p.ProductName}","{p.BrandName}",{p.YearReleased});\n""")
    for b in brand_list:
        f.write(
            f"""INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("{b.BrandName}",{b.YearEstablished},"{b.CEO}");\n""")
