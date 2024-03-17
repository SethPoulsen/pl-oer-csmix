import random

from typing import NamedTuple

from data_constraints_generator import DataConstraintGenerator

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


student_courses_schemas = """
CREATE TABLE IF NOT EXISTS Students(
  NetId VARCHAR(10),
  FirstName VARCHAR(255),
  LastName VARCHAR(255),
  Department VARCHAR(100),
  PRIMARY KEY (NetId)
);

CREATE TABLE IF NOT EXISTS Courses(
  CRN INT,
  Title VARCHAR(255),
  Department VARCHAR(100),
  Instructor VARCHAR(255),
  PRIMARY KEY (CRN)
);

CREATE TABLE IF NOT EXISTS Enrollments(
  NetId VARCHAR(10),
  CRN INT,
  Credits INT,
  Score REAL,
  PRIMARY KEY (NetId, CRN)
  -- FOREIGN KEY (NetId) REFERENCES Students(NetId),
  -- FOREIGN KEY (CRN) REFERENCES Courses(CRN)
);
\n
"""

student_courses_static_data = """
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


num_of_student = 100
num_of_course = 100

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

# Data for Customers and Products
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


customer_product_schemas = """CREATE TABLE IF NOT EXISTS Customers(
  CustomerId INT,
  FirstName VARCHAR(255),
  LastName VARCHAR(255),
  PhoneNumber REAL,
  PRIMARY KEY (CustomerId)

);

CREATE TABLE IF NOT EXISTS Brands(
  BrandName VARCHAR(255),
  YearEstablished INT,
  CEO VARCHAR(255),
  PRIMARY KEY (BrandName)
);

CREATE TABLE IF NOT EXISTS Products(
  ProductId INT,
  ProductName VARCHAR(255),
  BrandName VARCHAR(255),
  YearReleased INT,
  PRIMARY KEY (ProductId)
  -- FOREIGN KEY (BrandName) REFERENCES Brands(BrandName)
);

CREATE TABLE IF NOT EXISTS Purchases(
  PurchaseId INT,
  CustomerId INT,
  ProductId INT,
  Price INT,
  PRIMARY KEY (PurchaseId),
  FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
  FOREIGN KEY (ProductId) REFERENCES Products(ProductId)

);

\n
"""

customer_product_static_data = """
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

INSERT IGNORE INTO Brands VALUES
  ("Apple",1976,"Tim Cook"),
  ("Samsung",1938,"Ki Nam Kim, Hyun Suk Kim, Dong Jin Koh"),
  ("OnePlus",2013,"Pete Lau"),
  ("Google",1998,"Sundar Pichai"),
  ("Honor",2013,"George Zhao");

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
"""


class SqlDataGenerator:

    def __init__(self):
        # Data Constraint generator
        self.data_constraint_generator = DataConstraintGenerator()  # used to generate constraint data
        self.company_name_list = []  # Used for product generation if TA's provided product information

        # Student Courses data info
        self.student_list = []
        self.enrollment_list = []
        self.course_list = []
        self.random_CRNS = random.sample(range(100, 999), num_of_course)
        if 127 not in self.random_CRNS:
            self.random_CRNS.append(127)
        if 301 not in self.random_CRNS:
            self.random_CRNS.append(301)

        # Customer purchase data info
        self.customer_list = []
        self.purchase_list = []
        self.product_list = [
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

        self.brand_list = [
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

    def populate_student_list(self):
        STUDENTS_ENTITY_NAME = "Students"
        STUDENTS_FIRST_NAME = "FirstName"
        STUDENTS_LAST_NAME = "LastName"
        STUDENTS_NETID = "NetId"
        STUDENTS_DEPARTMENT = "Department"
        seen_set = set()  # For data deduplication

        student_data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(STUDENTS_ENTITY_NAME)
        constraint_index = 0

        for first_name in random.sample(popular_first_names, num_of_student):

            lottery_num = random.randint(0, 9)
            # If there are constraint data specified by the TA's. Run it first before the default random generation
            if constraint_index < len(student_data_constraint_dict_list):
                data_constraint_dict = student_data_constraint_dict_list[constraint_index]

                if STUDENTS_FIRST_NAME in data_constraint_dict:
                    first_name = data_constraint_dict[STUDENTS_FIRST_NAME]

                last_name = data_constraint_dict[STUDENTS_LAST_NAME] \
                    if STUDENTS_LAST_NAME in data_constraint_dict else popular_first_names[lottery_num % 10]

                netid = data_constraint_dict[STUDENTS_NETID] \
                    if STUDENTS_NETID in data_constraint_dict else first_name.lower()[:7] + str(lottery_num)

                department = data_constraint_dict[STUDENTS_DEPARTMENT] \
                    if STUDENTS_DEPARTMENT in data_constraint_dict else department_list[lottery_num % 10]

                # Deduplicate same data info generated by the data constraint generator
                if (first_name, last_name, department) not in seen_set:
                    self.student_list.append(Student(netid, first_name, last_name, department))
                    seen_set.add((first_name, last_name, department))

                constraint_index += 1
            else:
                last_name = popular_first_names[lottery_num % 10]
                netid = first_name.lower()[:7] + str(lottery_num)
                department = department_list[lottery_num % 10]

                self.student_list.append(Student(netid, first_name, last_name, department))

    def populate_course_list(self):
        COURSES_ENTITY_NAME = "Courses"
        COURSES_CRN = "CRN"
        COURSES_DEPARTMENT = "Department"
        COURSES_INSTRUCTOR_FIRST_NAME = "instructor_first_name"
        COURSES_INSTRUCTOR_LAST_NAME = "instructor_last_name"
        COURSES_TITLE = "Title"
        seen_set = set()  # For data deduplication

        course_data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(COURSES_ENTITY_NAME)
        constraint_index = 0

        # Since things are based on CRNS and CRNS itself already is based on randomness. Need to add TA specified
        # CRNS into the list for randomization
        for constraint_dict in course_data_constraint_dict_list:
            if COURSES_CRN in constraint_dict:
                self.random_CRNS.append(constraint_dict[COURSES_CRN])

        for CRN in self.random_CRNS:
            lottery_num = random.randint(0, len(popular_first_names) - 1)
            # If there are constraint data specified by the TA's. Run it first before the default random generation
            if constraint_index < len(course_data_constraint_dict_list):
                data_constraint_dict = course_data_constraint_dict_list[constraint_index]

                department = data_constraint_dict[COURSES_DEPARTMENT] \
                    if COURSES_DEPARTMENT in data_constraint_dict else department_list[lottery_num % 10]
                instructor_first_name = data_constraint_dict[COURSES_INSTRUCTOR_FIRST_NAME] \
                    if COURSES_INSTRUCTOR_FIRST_NAME in data_constraint_dict else popular_first_names[lottery_num]
                instructor_last_name = data_constraint_dict[COURSES_INSTRUCTOR_LAST_NAME] \
                    if COURSES_INSTRUCTOR_LAST_NAME in data_constraint_dict else popular_last_names[lottery_num % 10]
                title = data_constraint_dict[COURSES_TITLE] \
                    if COURSES_TITLE in data_constraint_dict else department + str(random.randint(100, 599))
                instructor_name = instructor_first_name + " " + instructor_last_name

                # Deduplicate same data info generated by the data constraint generator
                if (CRN, title, department, instructor_name) not in seen_set:
                    self.course_list.append(Course(CRN, title, department, instructor_name))
                    seen_set.add((CRN, title, department, instructor_name))

                constraint_index += 1

            else:
                department = department_list[lottery_num % 10]
                instructor_first_name = popular_first_names[lottery_num]
                instructor_last_name = popular_last_names[lottery_num % 10]

                title = department + str(random.randint(100, 599))

                instructor_name = instructor_first_name + " " + instructor_last_name
                self.course_list.append(Course(CRN, title, department, instructor_name))

    def populate_enrollment_list(self):
        ENROLLMENT_ENTITY_NAME = "Enrollments"
        ENROLLMENT_COURSE_NUM = "course_taken_number"
        ENROLLMENT_COURSES_DEPARTMENT = "department"
        ENROLLMENT_COURSE_CREDIT = "Credits"
        ENROLLMENT_COURSE_SCORE = "Score"
        COURSES_TITLE = "Title"
        seen_set = set()  # For data deduplication

        data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(ENROLLMENT_ENTITY_NAME)
        constraint_index = 0

        # all special case flags should be here
        special_case1 = False
        try:
            # this handles backward compatibility, flags in the constraint sets are translated into local variables
            for cnts in data_constraint_dict_list:
                done = [] # removes the flags
                for dic in cnts:
                    if cnts[dic] == "case1":
                        special_case1 = True
                        done.append(dic)
                if len(done) > 0:
                    for x in done:
                        cnts.pop(x, None) #pops out the flags
            if len(data_constraint_dict_list) > 0:
                # clean up the constraint list
                data_constraint_dict_list = [x for x in filter(None, data_constraint_dict_list)]
        except:
            pass
        

        # Reloop through constraint dict data all over to find certain keys for nested generation
        inner_constraint_index = 0

        for s in self.student_list:
            if constraint_index < len(data_constraint_dict_list):
                data_constraint_dict = data_constraint_dict_list[constraint_index]

                num_course_taken = data_constraint_dict[ENROLLMENT_COURSE_NUM] \
                    if ENROLLMENT_COURSES_DEPARTMENT in data_constraint_dict else random.randint(0, 6)
                num_course_taken = min(len(self.random_CRNS) - 1, num_course_taken)
                courses_taken = random.sample(self.random_CRNS, num_course_taken)

                for crn in courses_taken:
                    if inner_constraint_index < len(data_constraint_dict_list):
                        constraint_dict = data_constraint_dict_list[inner_constraint_index]

                        credit = constraint_dict[ENROLLMENT_COURSE_CREDIT] \
                            if ENROLLMENT_COURSE_CREDIT in constraint_dict else random.randint(0, 6)
                        score = constraint_dict[ENROLLMENT_COURSE_SCORE] \
                            if ENROLLMENT_COURSE_SCORE in constraint_dict else round(random.uniform(0, 100), 3)

                        # Increment inner constraint index
                        inner_constraint_index = inner_constraint_index + 1 \
                            if inner_constraint_index < len(data_constraint_dict_list) else 0

                        # Deduplicate same data info generated by the data constraint generator
                        if (crn, credit, score) not in seen_set:
                            self.enrollment_list.append(Enrollment(s.NetId, crn, credit, score))
                            seen_set.add((crn, credit, score))

                    constraint_index += 1

            else:
                num_course_taken = random.randint(0, 6)
                courses_taken = random.sample(self.random_CRNS, num_course_taken)
                for crn in courses_taken:
                    if special_case1 == True:
                        credit = random.randint(1, 5)
                    else:
                        credit = random.randint(0, 4)
                    score = round(random.uniform(0, 100), 3)
                    self.enrollment_list.append(Enrollment(s.NetId, crn, credit, score))



    def create_student_course_data(self):
        self.populate_student_list()
        self.populate_course_list()
        self.populate_enrollment_list()
        self.write_setup_sql(student_courses_schemas, student_courses_static_data, "courses")

    def populate_customer_list(self):
        CUSTOMER_ENTITY_NAME = "Customers"
        CUSTOMER_FIRST_NAME = "FirstName"
        CUSTOMER_LAST_NAME = "LastName"
        CUSTOMER_PHONE_NUMBER = "PhoneNumber"
        seen_customer_set = set()

        data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(CUSTOMER_ENTITY_NAME)
        constraint_index = 0

        for Customer_Id, first_name in enumerate(random.sample(popular_first_names, num_of_customers)):
            lottery_num = random.randint(0, 9)
            if constraint_index < len(data_constraint_dict_list) and Customer_Id > 24:
                data_constraint_dict = data_constraint_dict_list[constraint_index]

                if CUSTOMER_FIRST_NAME in data_constraint_dict:
                    first_name = data_constraint_dict[CUSTOMER_FIRST_NAME]

                last_name = data_constraint_dict[CUSTOMER_LAST_NAME] \
                    if CUSTOMER_LAST_NAME in data_constraint_dict else popular_first_names[lottery_num % 10]

                phone = data_constraint_dict[CUSTOMER_PHONE_NUMBER] \
                    if CUSTOMER_PHONE_NUMBER in data_constraint_dict else random.randint(1000000000, 9999999999)

                # Deduplicate same customer info generated by the data constraint generator
                if (first_name, last_name, phone) not in seen_customer_set:
                    self.customer_list.append(Customer(Customer_Id, first_name, last_name, phone))
                    seen_customer_set.add((first_name, last_name, phone))

                constraint_index += 1
            else:
                last_name = popular_first_names[lottery_num % 10]
                phone = random.randint(1000000000, 9999999999)

                self.customer_list.append(Customer(Customer_Id, first_name, last_name, phone))

    def populate_purchase_list(self):
        purchase_count = 0
        for c in self.customer_list:
            buy_n = random.randint(1, 6)
            bought = random.sample(range(len(self.product_list)), buy_n)
            for product_id in bought:
                self.purchase_list.append(Purchase(purchase_count, c.Customer_Id, product_id, random.randint(3000, 6000)))
                purchase_count += 1
        for i in range(6):
            self.purchase_list.append(Purchase(purchase_count, random.randint(98, 99), random.randint(15, 20), random.randint(100, 9000)))
            purchase_count += 1

    def populate_product_list(self):
        # Product(14, "Redmi 7A", "MI", 2019),
        PRODUCT_ENTITY_NAME = "Products"
        PRODUCT_NAME = "ProductName"
        PRODUCT_COMPANY = "BrandName"
        PRODUCT_RELEASED_YEAR = "YearReleased"
        seen_set = set()  # For data deduplication

        product_id = 21
        # If TA's don't specify some certain fields, the system will generate them...
        seen_product_name_set = set()
        seen_product_company_set = set()

        data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(PRODUCT_ENTITY_NAME)
        # print("PRODUCT DATA MAP LIST: ", data_constraint_dict_list)
        # Need to look into all constraint data to see if any are specified for specific product.
        for data_constraint_dict in data_constraint_dict_list:
            if PRODUCT_NAME in data_constraint_dict and data_constraint_dict[PRODUCT_NAME] not in seen_product_name_set:
                product_name = data_constraint_dict[PRODUCT_NAME]
            else:
                product_name = "Product #{}".format(random.randint(30, 500))
            seen_product_name_set.add(product_name)

            if PRODUCT_COMPANY in data_constraint_dict and data_constraint_dict[PRODUCT_COMPANY] not in seen_product_company_set:
                product_company = data_constraint_dict[PRODUCT_COMPANY]
            else:
                product_company = "COMPANY #{}".format(random.randint(30, 500))
            seen_product_company_set.add(product_company)
            self.company_name_list.append(product_company)

            release_year = data_constraint_dict[PRODUCT_RELEASED_YEAR] \
                if PRODUCT_RELEASED_YEAR in data_constraint_dict else random.randint(1950, 2020)

            # Deduplicate same data info generated by the data constraint generator
            if (str(product_name), str(product_company), int(release_year)) not in seen_set:
                self.product_list.append(
                    Product(product_id, str(product_name), str(product_company), int(release_year)))
                product_id += 1
                seen_set.add((str(product_name), str(product_company), int(release_year)))

        self.product_list.append(Product(70, "XBOX", "MICROSOFT", 2013))  # This was already here from Abdu's initial code!
        self.product_list.append(Product(71, "XBOX ONE", "MICROSOFT", 2015))
        self.product_list.append(Product(72, "XBOX TWO", "MICROSOFT", 2019))
        self.product_list.append(Product(73, "XBOX THREE", "MICROSOFT", 2020))
        self.product_list.append(Product(74, "XBOX IV", "MICROSOFT", 2024))

        # We shuffle these to be more random
        random.shuffle(self.product_list)

    def populate_brand_list(self):
        BRAND_ENTITY_NAME = "Brands"
        BRAND_NAME = ""  # This will not be used in the system as brand names are tied to company names in Product entity. Used Product entity to add the corresponding data constraints
        BRAND_FOUND_YEAR = "YearEstablished"
        BRAND_FOUNDER = "CEO"
        seen_set = set()  # For data deduplication

        data_constraint_dict_list = self.data_constraint_generator.generate_data_instances(BRAND_ENTITY_NAME)
        # Need to look into all constraint data to see if any are specified for specific product.
        used_brand_name_index = 0
        for data_dict in data_constraint_dict_list:
            if used_brand_name_index < len(self.company_name_list):
                brand_name = self.company_name_list[used_brand_name_index]
                used_brand_name_index += 1
                brand_found_year = data_dict[BRAND_FOUND_YEAR] if BRAND_FOUND_YEAR in data_dict else random.randint(1780, 2020)
                brand_founder = data_dict[BRAND_FOUNDER] if BRAND_FOUNDER in data_dict else random.choice(['Roger First', 'Ping-che Last', 'Teemo Must DI', "Captain You"])

                # Deduplicate same data info generated by the data constraint generator
                if (brand_name, int(brand_found_year), str(brand_founder)) not in seen_set:
                    self.brand_list.append(Brand(brand_name, int(brand_found_year), str(brand_founder)))
                    seen_set.add((brand_name, int(brand_found_year), str(brand_founder)))
            else:
                break

        self.brand_list.append(Brand("MICROSOFT", 1975, "Bill Gates"))  # This was already here from Abdu's initial code!

        # We shuffle these to be more random
        random.shuffle(self.brand_list)

    def create_customer_products_data(self):
        self.populate_customer_list()
        self.populate_product_list()
        self.populate_brand_list()
        self.populate_purchase_list()  # Changed order to incorporate TA inputs
        self.write_setup_sql(customer_product_schemas, customer_product_static_data, "products")

    def write_setup_sql(self, schemas_sql, static_data_sql, data_info_str):
        if data_info_str == "courses":
            with open("/grade/tests/setup.sql", "w+") as f:
                f.write(schemas_sql)
                f.write(static_data_sql)
                self.insert_student_courses_data(f)
        elif data_info_str == "products":
            with open("/grade/tests/setup.sql", "a") as f:
                f.write(schemas_sql)
                f.write(static_data_sql)
                self.insert_customer_products_data(f)

    def insert_student_courses_data(self, file_pointer):
        for s in self.student_list:
            file_pointer.write(
                f"""INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("{s.NetId}","{s.FirstName}","{s.LastName}","{s.Department}");\n""")
        for e in self.enrollment_list:
            file_pointer.write(
                f"""INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("{e.NetId}",{e.CRN},{e.Credits},{e.Score});\n""")
        for c in self.course_list:
            file_pointer.write(
                f"""INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES ({c.CRN},"{c.Title}","{c.Department}","{c.Instructor}");\n""")

    def insert_customer_products_data(self, file_pointer):
        for c in self.customer_list:
            file_pointer.write(
                f"""INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES ({c.Customer_Id},"{c.FirstName}","{c.LastName}",{c.PhoneNumber});\n""")
        for b in self.brand_list:
            file_pointer.write(
                f"""INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("{b.BrandName}",{b.YearEstablished},"{b.CEO}");\n""")
        for p in self.product_list:
            file_pointer.write(
                f"""INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES ({p.ProductId},"{p.ProductName}","{p.BrandName}",{p.YearReleased});\n""")
        for p in self.purchase_list:
            file_pointer.write(
                f"""INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES ({p.PurchaseId},{p.Customer_Id},{p.ProductId},{p.Price});\n""")
        
    def generate_data(self):
        self.create_student_course_data()
        self.create_customer_products_data()


if __name__ == "__main__":
    # Provided only for testing this module separately (by changing within the run.sh to "python3 -m [module_name]")
    sql_generator = SqlDataGenerator()
    sql_generator.generate_data()

