Create database if not exists solution;
Use solution;


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
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("hester8","Hester","Alexander","Sports");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("long9","Long","Alfaro","Music");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("mathews4","Mathews","Adkins","Statistics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("phillip6","Phillips","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("mcmahon1","Mcmahon","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("dean1","Dean","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("gibson6","Gibson","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("cobb9","Cobb","Alfaro","Music");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("dennis2","Dennis","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("strong9","Strong","Alfaro","Music");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("bishop6","Bishop","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("rhodes7","Rhodes","Ahmed","Psychology");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("barton1","Barton","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("guzman5","Guzman","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("lester5","Lester","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("arnold7","Arnold","Ahmed","Psychology");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("raymond6","Raymond","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("graves2","Graves","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("yates2","Yates","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("christi2","Christian","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("marin1","Marin","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("contrer3","Contreras","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("moon6","Moon","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("pratt3","Pratt","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("tyler6","Tyler","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("warren1","Warren","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("barrett5","Barrett","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("jenning0","Jennings","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("roberso1","Roberson","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("mckee7","Mckee","Ahmed","Psychology");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("farrell7","Farrell","Ahmed","Psychology");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("stewart3","Stewart","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("briggs5","Briggs","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("lin6","Lin","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("smith3","Smith","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("copelan2","Copeland","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("tang2","Tang","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("oneill1","Oneill","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("rogers8","Rogers","Alexander","Sports");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("norton2","Norton","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("mejia0","Mejia","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("herrera4","Herrera","Adkins","Statistics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("abbott0","Abbott","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("lara5","Lara","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("elliott2","Elliott","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("medina5","Medina","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("hebert3","Hebert","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("good8","Good","Alexander","Sports");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("diaz5","Diaz","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("farmer4","Farmer","Adkins","Statistics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("hodge9","Hodge","Alfaro","Music");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("oneal3","Oneal","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("branch0","Branch","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("manning1","Manning","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("weaver3","Weaver","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("melende0","Melendez","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("webster1","Webster","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("stevens8","Stevens","Alexander","Sports");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("noble0","Noble","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("pollard8","Pollard","Alexander","Sports");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("caldero9","Calderon","Alfaro","Music");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("huang9","Huang","Alfaro","Music");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("vega2","Vega","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("reilly0","Reilly","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("preston0","Preston","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("haynes8","Haynes","Alexander","Sports");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("horn3","Horn","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("oconnor3","Oconnor","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("drake0","Drake","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("waller5","Waller","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("correa3","Correa","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("adkins3","Adkins","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("wise1","Wise","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("hendrix5","Hendrix","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("ramirez9","Ramirez","Alfaro","Music");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("jacobs9","Jacobs","Alfaro","Music");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("costa7","Costa","Ahmed","Psychology");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("mccann9","Mccann","Alfaro","Music");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("york5","York","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("francis2","Francis","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("gomez0","Gomez","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("mosley5","Mosley","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("erickso5","Erickson","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("hill1","Hill","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("clay9","Clay","Alfaro","Music");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("leblanc0","Leblanc","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("carson0","Carson","Abbott","CS");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("gonzale7","Gonzalez","Ahmed","Psychology");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("salinas4","Salinas","Adkins","Statistics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("beltran6","Beltran","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("pham6","Pham","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("coffey2","Coffey","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("mayer4","Mayer","Adkins","Statistics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("liu1","Liu","Acevedo","ECE");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("hurley3","Hurley","Adams","Economics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("bauer6","Bauer","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("jones6","Jones","Aguirre","Accounting");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("brewer5","Brewer","Aguilar","Finance");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("frazier2","Frazier","Acosta","Physics");
INSERT IGNORE INTO Students(NetId, FirstName, LastName, Department) VALUES ("payne3","Payne","Adams","Economics");
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hester8",467,2,90.6994400824784);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hester8",880,2,78.98774130746943);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hester8",810,1,40.808410501864856);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hester8",319,3,80.38573003249347);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hester8",965,4,90.12701549978624);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hester8",468,0,64.63718173633329);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("long9",736,3,90.24374152131767);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("long9",796,1,44.92546459319262);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mathews4",158,2,10.893814674540891);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mathews4",641,0,49.200721090275145);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mathews4",866,0,46.405746869217346);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mathews4",363,3,36.95138419017984);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mathews4",583,1,61.49909646521431);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mathews4",527,3,97.68212525088042);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mcmahon1",926,3,40.71263387195352);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mcmahon1",244,3,26.186281862095516);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mcmahon1",670,2,7.8140595607966485);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mcmahon1",882,0,61.597402492469946);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gibson6",877,1,25.21700457535737);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gibson6",301,2,5.280047174257085);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gibson6",148,1,75.13811444676499);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gibson6",363,0,56.275597301981136);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("cobb9",320,4,63.710569784886026);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("cobb9",803,3,93.18360422441813);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("cobb9",215,3,88.37664784578378);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("cobb9",301,1,10.420651869935915);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("cobb9",158,1,98.81967828940266);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("cobb9",322,4,48.099006414096614);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("dennis2",926,0,13.716698860591169);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("strong9",631,4,22.89747062436176);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("strong9",191,0,19.583982368747822);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("strong9",137,0,19.22855993720417);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("strong9",859,0,90.69457669140458);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("strong9",929,2,88.97654794045262);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("strong9",567,0,3.1898070211280105);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("bishop6",905,0,80.31271593516652);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("bishop6",924,3,4.194117444580325);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("bishop6",400,4,30.343986820974735);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("bishop6",279,0,0.2290549989977575);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("bishop6",866,0,17.425819685065346);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barton1",392,4,7.9884695726554655);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barton1",430,4,39.61941590240309);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barton1",785,1,67.2226624470422);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barton1",670,3,97.37425019885002);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barton1",242,3,66.02975149596743);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("guzman5",338,3,67.76580029952558);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("guzman5",288,3,22.329749647197637);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("guzman5",249,4,54.0259074838645);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("guzman5",148,3,9.527097531436436);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("guzman5",503,3,53.56454591404539);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("guzman5",406,1,93.21938656504602);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("lester5",244,4,2.3174297604014793);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("lester5",926,4,43.79957013356912);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("lester5",119,1,8.764613653923092);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("lester5",503,2,16.278852755375837);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("lester5",199,4,95.45692722245421);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("lester5",301,3,19.645067852756306);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("arnold7",641,0,96.46442763650506);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("arnold7",215,1,68.05174621422233);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("graves2",495,4,38.21398738261238);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("graves2",567,3,52.525034861192196);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("graves2",734,0,27.6227095804217);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("yates2",249,4,94.11778749208207);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("christi2",468,1,8.559098969178603);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("marin1",320,1,27.42876511872756);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("marin1",406,4,32.64510837739161);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("marin1",158,0,64.73809544352692);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("marin1",285,3,99.84712112902349);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("marin1",468,2,17.78473586386721);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("moon6",430,2,97.66624519691223);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("moon6",486,4,86.1308254113058);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("moon6",157,1,36.588841738224176);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("moon6",202,4,82.28349388661982);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pratt3",905,3,39.707800586717966);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pratt3",271,3,26.235428572328345);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("tyler6",583,2,57.21986583016737);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("tyler6",612,3,58.68560477821756);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("tyler6",709,2,87.21134865050863);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("tyler6",880,1,34.461019055187045);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("tyler6",157,3,66.51786155101833);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("warren1",877,4,9.680629615526426);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("warren1",540,0,77.01714355390439);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("warren1",918,2,11.925673083433864);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("warren1",467,3,84.80550881340025);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("warren1",432,1,52.8460976637003);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barrett5",215,4,21.322013018091546);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barrett5",278,4,28.607864034566898);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barrett5",392,3,63.43871266282428);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barrett5",301,2,62.857467803654465);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barrett5",486,0,27.63376390367477);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("barrett5",127,4,86.11181434378204);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jenning0",949,1,75.85241142495978);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jenning0",199,0,72.6915363551515);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jenning0",859,3,22.02128428998976);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jenning0",550,0,91.71955167363184);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jenning0",215,0,64.44412387484037);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jenning0",803,3,73.51099060566693);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("roberso1",271,4,66.73249065940173);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("farrell7",803,4,34.07412496284813);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("farrell7",731,4,86.80824454379267);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("farrell7",703,1,47.04261691010927);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("stewart3",709,4,36.90372299565718);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("stewart3",486,4,80.69977902532854);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("stewart3",443,1,11.040934034701111);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("stewart3",670,0,66.88999308447741);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("briggs5",495,3,56.49625872931365);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("briggs5",540,3,51.19509509993192);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("smith3",926,2,95.014850155596);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("smith3",882,1,30.33096098073663);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("smith3",244,4,48.06366699442115);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("smith3",443,1,94.10189374059041);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("copelan2",400,0,23.650555058375634);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("tang2",866,2,85.73466581516091);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("tang2",614,4,54.846370229915934);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("tang2",184,0,4.5375576289439445);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("tang2",882,0,8.082650142377734);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("oneill1",242,1,81.44292159072735);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("oneill1",924,2,44.74859623485672);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("norton2",158,0,21.21824211698152);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("norton2",929,0,50.777178721337734);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("norton2",168,4,32.409267203008426);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("norton2",687,4,6.7645579342812905);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("norton2",288,4,91.43079275940732);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mejia0",202,2,94.27782800893529);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mejia0",168,2,73.30071087915799);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mejia0",613,4,29.366199073265207);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mejia0",924,4,54.036019656912394);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mejia0",158,0,85.24431914640319);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mejia0",709,1,58.15345263929351);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("herrera4",400,2,9.615436928545007);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("herrera4",493,4,66.94990397548449);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("abbott0",148,2,76.75891007360322);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("abbott0",583,2,43.95405882165946);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("abbott0",443,4,50.05982174262225);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("abbott0",194,1,27.253611015527458);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("abbott0",271,1,1.8401428005926146);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("abbott0",704,2,69.92635931121374);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("lara5",583,1,3.686495983742566);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("lara5",670,2,62.328274334949995);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("elliott2",119,1,93.98999510987022);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("elliott2",279,4,66.40497841902217);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("medina5",319,4,42.741178946334124);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("medina5",279,4,71.96265320818938);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("medina5",392,3,72.13724225371544);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("medina5",493,4,51.02631323367456);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("medina5",918,3,34.84790025845756);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("good8",687,4,65.44822147230512);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("good8",866,0,84.53985881772857);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("good8",123,0,49.2975224695442);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("diaz5",641,4,37.5953535079505);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("diaz5",363,2,55.600809035276);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("diaz5",527,0,35.76755296643886);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("diaz5",495,0,48.487078772664184);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("diaz5",322,2,44.787241654345145);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("diaz5",168,2,34.85399611487312);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("farmer4",430,0,33.77112936582293);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("farmer4",278,2,4.930479615462435);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("farmer4",540,0,17.22010569418516);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hodge9",687,1,61.895236816962004);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hodge9",301,4,12.86306811948542);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hodge9",168,4,60.04231085445062);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hodge9",271,1,83.29950348077811);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("oneal3",614,4,28.382350544817303);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("oneal3",320,2,96.06847017081819);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("oneal3",880,3,46.41716194380932);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("oneal3",567,2,12.334796939883773);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("branch0",949,4,6.991784973073956);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("branch0",123,0,99.68044392010542);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("branch0",202,1,3.612790163355295);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("branch0",157,3,54.560357537773626);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("manning1",965,1,41.57732637219891);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("manning1",146,2,89.8169258864595);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("manning1",363,4,74.90192075986212);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("weaver3",534,1,19.570131104393873);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("weaver3",528,3,71.16958222165299);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("weaver3",882,0,46.097466618015005);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("weaver3",119,4,1.93754678863729);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("weaver3",400,1,75.58382236682444);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("melende0",503,3,67.72793341657352);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("melende0",137,1,33.62451668598203);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("melende0",631,0,85.44948571222422);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("melende0",802,3,18.877957515005917);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("stevens8",319,4,29.1873291154254);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("stevens8",244,3,88.95781677410682);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pollard8",320,2,72.18385198250188);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pollard8",665,2,44.3625551877438);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pollard8",215,1,87.84323653439988);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("caldero9",929,4,94.17740115577703);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("caldero9",392,4,27.07326921558679);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("caldero9",493,0,33.74121862896119);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("caldero9",285,0,30.499262346609303);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("caldero9",307,4,70.87313894772038);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("caldero9",299,2,71.91147163940583);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("vega2",877,3,12.82611866467005);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("vega2",301,0,40.68529749427536);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("preston0",944,1,15.163136430904444);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("preston0",613,3,84.33501003107848);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("preston0",731,2,75.73597834728093);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("preston0",392,4,9.347260374068867);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("preston0",101,0,35.01144576021478);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("haynes8",467,1,32.08748725103108);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("haynes8",803,2,42.5824946457581);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("haynes8",796,0,23.75876829702569);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("horn3",495,4,51.18623332247498);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("horn3",962,2,86.20008505537352);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("horn3",338,1,16.89017855062387);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("horn3",242,3,57.30417503705494);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("horn3",515,2,0.3609896636910137);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("horn3",973,3,16.589257564476277);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("oconnor3",803,4,17.24199916402558);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("oconnor3",503,0,88.27606290356074);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("waller5",194,3,14.731479459446795);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("waller5",417,0,10.055629455137538);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("waller5",242,2,67.66213650509462);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("waller5",612,2,17.187317420950563);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("correa3",731,2,80.42372159116347);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("correa3",285,3,44.22758021014257);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("correa3",528,1,62.94728366963118);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("correa3",550,3,91.63282657456513);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("correa3",279,1,43.76636383282341);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("correa3",301,2,4.98398253070651);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("adkins3",202,0,82.14965940780432);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("adkins3",767,3,27.400592633730348);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("adkins3",467,0,11.175618832307732);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("wise1",320,4,52.1323693289078);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("wise1",285,2,76.43600776043505);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("wise1",882,3,99.59984390380524);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("wise1",288,2,71.6096209117572);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("wise1",965,3,29.06977387186084);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("wise1",889,0,33.351902638761054);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("hendrix5",503,1,18.160802507705686);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("ramirez9",148,2,81.81640140870728);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("ramirez9",123,4,11.88545651333095);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jacobs9",157,3,54.227623107400646);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("costa7",299,2,26.261311640133446);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("costa7",322,3,69.16965676897124);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("costa7",432,2,96.5791194151746);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("mccann9",734,3,37.177211172157456);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("york5",803,3,70.58968434958966);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("york5",123,2,0.8681595130013209);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("york5",767,0,56.170463174911426);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("francis2",320,4,15.520900579810116);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("francis2",202,0,48.50999907541045);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("francis2",796,0,95.27807683240057);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("francis2",550,3,27.44456791038553);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("francis2",285,0,3.01910395584416);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gomez0",929,3,27.466458455128507);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gomez0",119,2,33.55786852747493);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gomez0",567,3,42.33146930887164);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gomez0",417,0,67.01993522239995);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gomez0",973,3,15.519005247340178);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gomez0",242,2,61.6317264413284);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("erickso5",785,0,64.2146123833084);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("erickso5",271,3,90.03029274429399);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("clay9",967,4,61.58027030006985);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("clay9",944,1,71.82870820903179);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("clay9",734,3,6.532670712780442);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("clay9",322,1,90.01500766606199);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("clay9",880,4,78.77103777848346);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("clay9",810,2,63.4847956498049);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("leblanc0",967,2,30.92075033645074);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("leblanc0",846,0,26.77283364587617);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("leblanc0",880,4,71.62927611395224);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("leblanc0",905,2,78.19132690810439);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("leblanc0",461,2,46.39512043875482);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("carson0",944,1,19.208965065748274);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("carson0",880,3,95.28306448456945);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("carson0",445,0,33.62635721411395);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("carson0",191,0,67.68773107539509);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("carson0",918,1,48.08837226990591);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("gonzale7",665,0,7.732589167262804);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("salinas4",495,2,3.0701601837549553);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("salinas4",432,0,97.70848758417505);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("beltran6",467,4,93.97857934951735);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("beltran6",215,2,29.10230726576565);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("beltran6",148,2,46.6139206855673);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("beltran6",579,4,98.06269738522825);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("beltran6",119,4,81.05195411320457);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pham6",127,2,78.37109397964028);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pham6",734,0,67.95779356569321);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pham6",704,4,44.83357489766223);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pham6",802,2,17.52403420759436);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pham6",355,3,70.44312328631086);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("pham6",614,4,89.07607465265787);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("coffey2",665,4,98.75346622303715);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("coffey2",973,1,53.971431876468856);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("coffey2",271,3,8.638676043772552);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("liu1",962,1,47.15051240023933);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("liu1",468,2,19.361075690905704);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("liu1",392,1,2.4521852792281584);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("liu1",271,4,98.23272554770483);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("liu1",202,3,37.586840173644234);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jones6",803,1,92.28877419295873);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jones6",461,0,9.056967352558809);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jones6",503,4,24.919564079053124);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("jones6",882,0,16.89909521664856);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("frazier2",417,0,33.214811182188996);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("frazier2",123,1,74.39606960191395);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("frazier2",191,1,55.743398231204075);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("frazier2",654,2,8.885653548493833);
INSERT IGNORE INTO Enrollments(NetId, CRN, Credits, Score) VALUES ("payne3",215,1,70.66163905962469);
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (137,"Sports215","Sports","Zimmerman Indiana");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (148,"Accounting354","Accounting","Chavez Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (285,"Statistics156","Statistics","Hull Espenson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (540,"Economics115","Economics","Branch Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (277,"CS159","CS","Lang Anderson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (467,"CS589","CS","Hogan Anderson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (734,"Finance420","Finance","Ellison Frost");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (495,"Economics338","Economics","Murillo Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (278,"CS204","CS","Santana Anderson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (432,"Finance512","Finance","Davila Frost");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (962,"Accounting597","Accounting","English Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (929,"Accounting591","Accounting","Mcpherson Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (736,"Accounting187","Accounting","Townsend Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (656,"Music173","Music","Lindsey Joe");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (307,"Finance243","Finance","Costa Frost");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (563,"Economics104","Economics","Miller Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (583,"Statistics527","Statistics","Blake Espenson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (866,"Economics519","Economics","Cortes Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (731,"Accounting149","Accounting","Conway Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (802,"ECE287","ECE","Mullins Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (417,"Psychology581","Psychology","Molina Hipster");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (460,"Accounting300","Accounting","Dennis Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (194,"CS212","CS","Decker Anderson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (613,"ECE400","ECE","Walton Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (973,"Music509","Music","Kennedy Joe");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (579,"Physics574","Physics","Pratt Cho");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (877,"Psychology584","Psychology","Dawson Hipster");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (338,"CS342","CS","Morris Anderson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (199,"Finance492","Finance","Murray Frost");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (926,"Psychology392","Psychology","Robles Hipster");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (400,"Accounting545","Accounting","Hunt Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (550,"Economics124","Economics","Fletcher Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (924,"Sports458","Sports","Gordon Indiana");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (905,"Physics447","Physics","Huffman Cho");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (119,"Statistics320","Statistics","Krueger Espenson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (859,"Economics496","Economics","Kaur Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (392,"Music430","Music","Wolfe Joe");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (803,"Sports559","Sports","Cherry Indiana");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (641,"Statistics136","Statistics","Cummings Espenson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (443,"Music112","Music","Yang Joe");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (101,"Statistics349","Statistics","Price Espenson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (665,"Accounting339","Accounting","Curry Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (567,"Accounting132","Accounting","Garrison Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (158,"Sports473","Sports","Glass Indiana");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (949,"Statistics209","Statistics","Conrad Espenson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (503,"Economics531","Economics","Kim Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (846,"Finance182","Finance","Garrett Frost");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (461,"Accounting447","Accounting","Mcconnell Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (631,"Economics341","Economics","Peck Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (687,"Economics327","Economics","Mendez Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (810,"Statistics219","Statistics","Duke Espenson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (288,"Finance109","Finance","Estrada Frost");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (528,"Physics199","Physics","Ibarra Cho");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (796,"ECE261","ECE","Mathis Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (249,"Sports535","Sports","Landry Indiana");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (944,"Psychology454","Psychology","Weiss Hipster");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (534,"ECE224","ECE","Grant Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (355,"ECE131","ECE","Acevedo Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (493,"ECE117","ECE","Roach Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (535,"Accounting275","Accounting","Tapia Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (445,"ECE535","ECE","Blackburn Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (202,"Accounting157","Accounting","Hunt Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (168,"Statistics185","Statistics","Blake Espenson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (242,"Physics337","Physics","Morrow Cho");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (191,"Economics112","Economics","Stanton Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (146,"Finance484","Finance","Rubio Frost");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (299,"ECE319","ECE","Allen Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (123,"Accounting197","Accounting","Brennan Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (527,"Psychology435","Psychology","Mccormick Hipster");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (279,"Economics109","Economics","Rollins Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (965,"Economics164","Economics","Browning Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (654,"ECE502","ECE","Hall Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (889,"Finance133","Finance","Wilson Frost");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (468,"CS106","CS","Farrell Anderson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (430,"Physics185","Physics","Ramirez Cho");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (486,"Physics498","Physics","Fleming Cho");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (775,"Economics503","Economics","Howard Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (670,"Psychology170","Psychology","Robles Hipster");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (709,"Sports140","Sports","Buck Indiana");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (320,"CS146","CS","Person Anderson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (406,"Accounting242","Accounting","Morales Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (614,"ECE405","ECE","Boone Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (882,"CS185","CS","Fitzgerald Anderson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (244,"Finance428","Finance","Pacheco Frost");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (184,"CS324","CS","Drake Anderson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (271,"ECE223","ECE","Higgins Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (319,"Economics262","Economics","Rollins Da-Cruz");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (612,"Accounting513","Accounting","Oneill Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (785,"Statistics389","Statistics","Nguyen Espenson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (363,"Statistics384","Statistics","Sims Espenson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (918,"Music289","Music","Byrd Joe");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (515,"Sports308","Sports","Huber Indiana");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (703,"Finance393","Finance","Callahan Frost");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (157,"Accounting168","Accounting","Vaughn Glow");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (704,"CS551","CS","Benson Anderson");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (767,"ECE333","ECE","Simmons Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (215,"Physics306","Physics","Wang Cho");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (880,"ECE431","ECE","Beck Bing");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (967,"Music515","Music","Mccullough Joe");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (322,"Sports103","Sports","Jones Indiana");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (127,"Sports262","Sports","Wiley Indiana");
INSERT IGNORE INTO Courses(CRN, Title, Department, Instructor) VALUES (301,"Statistics180","Statistics","Adkins Espenson");
CREATE TABLE IF NOT EXISTS Customers(
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
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (0,"Sullivan","Alfaro",5489887674);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (1,"Shaw","Acosta",9389312645);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (2,"Walker","Alexander",4361933283);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (3,"Kirby","Adkins",1530888837);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (4,"Sheppard","Acevedo",7877323271);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (5,"Andrade","Aguirre",6690721647);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (6,"Lane","Abbott",9344948005);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (7,"Peck","Acevedo",4281160420);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (8,"Miles","Acevedo",2733490015);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (9,"Gregory","Alfaro",5923747208);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (10,"Osborne","Alexander",9816915844);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (11,"Dixon","Acevedo",4837814737);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (12,"Fitzpatrick","Acosta",8830636267);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (13,"Randall","Aguirre",4822543010);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (14,"Mueller","Alexander",5157352711);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (15,"Robertson","Acosta",8596756192);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (16,"Barrett","Adkins",6654958240);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (17,"Moore","Ahmed",5646743777);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (18,"Wheeler","Abbott",2999441463);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (19,"Gibbs","Alexander",3504854467);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (20,"Pham","Alfaro",3051144052);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (21,"Alvarado","Alexander",3294824885);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (22,"Blair","Acosta",7352317229);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (23,"Gordon","Aguirre",5186078406);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (24,"Park","Abbott",4987242791);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (25,"Stein","Adkins",8468973721);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (26,"Pierce","Adkins",1979670869);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (27,"Roach","Acosta",3972869567);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (28,"Collier","Alexander",5579952746);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (29,"Vazquez","Aguirre",4829339623);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (30,"Bell","Adams",4860240394);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (31,"Acosta","Acosta",4242083943);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (32,"Kelly","Aguilar",4201528669);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (33,"Payne","Acevedo",1916111825);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (34,"Ware","Acevedo",5224628882);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (35,"Winters","Adkins",3523003068);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (36,"Bernard","Alfaro",7877094570);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (37,"Hendricks","Aguirre",7976577254);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (38,"Ellis","Aguirre",9043711172);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (39,"Esquivel","Acosta",6292255140);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (40,"Vargas","Alfaro",9128255013);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (41,"Peralta","Acevedo",4823177437);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (42,"Parra","Acevedo",8792179391);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (43,"Cuevas","Adams",6472415833);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (44,"Adams","Alexander",4003817514);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (45,"Bentley","Alexander",3201948255);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (46,"Lu","Adams",8890545967);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (47,"Wagner","Adkins",6917569555);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (48,"Charles","Ahmed",1387460573);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (49,"Walls","Alexander",5196218899);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (50,"Patterson","Aguirre",5347238908);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (51,"Bond","Adkins",1572835187);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (52,"Spence","Acosta",7715836594);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (53,"Clayton","Acevedo",6184408405);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (54,"Mullins","Adkins",8577021947);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (55,"Johnson","Alfaro",2965741059);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (56,"Benson","Abbott",1875839983);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (57,"Cano","Ahmed",4106266928);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (58,"Love","Aguilar",6578242901);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (59,"Petersen","Alfaro",6542090357);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (60,"Wright","Aguilar",8538899421);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (61,"Cantrell","Alexander",1787524506);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (62,"Castillo","Ahmed",9870664747);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (63,"Boyle","Alexander",6794089522);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (64,"Berger","Alfaro",8916469211);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (65,"Howe","Alfaro",2233581016);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (66,"Marsh","Aguilar",6985344628);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (67,"Perez","Alfaro",1119955756);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (68,"Avalos","Alfaro",7193941383);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (69,"Giles","Abbott",7409537888);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (70,"Salazar","Acosta",4763485178);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (71,"Byrd","Adams",7500584126);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (72,"Choi","Ahmed",5357986229);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (73,"Joseph","Acosta",3927830593);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (74,"Atkinson","Acevedo",1938693311);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (75,"Wall","Aguirre",6984276929);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (76,"Rush","Adkins",5714724890);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (77,"Galindo","Alfaro",8320726958);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (78,"Schwartz","Adams",1495243320);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (79,"Edwards","Aguilar",8418571404);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (80,"Pineda","Ahmed",5027784566);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (81,"Combs","Ahmed",8938735796);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (82,"Schmitt","Aguirre",5838951001);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (83,"Ayers","Aguirre",7706687332);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (84,"Mosley","Aguilar",7401555882);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (85,"Blake","Abbott",7517520772);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (86,"Williams","Adkins",1641334219);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (87,"Burns","Acevedo",2017442041);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (88,"Guzman","Abbott",9461301068);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (89,"Conway","Abbott",4096185863);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (90,"Sellers","Alfaro",8012504675);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (91,"Frank","Alexander",8908981072);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (92,"Todd","Abbott",7322231145);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (93,"Nicholson","Acosta",6238895396);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (94,"Neal","Aguilar",9140994506);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (95,"Hammond","Aguirre",3675303156);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (96,"Koch","Ahmed",3987876493);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (97,"Proctor","Alfaro",7605086879);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (98,"Orozco","Alfaro",7276600115);
INSERT IGNORE INTO Customers(CustomerId, FirstName, LastName, PhoneNumber) VALUES (99,"Noble","Adkins",1388869463);
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("MEIZU",2003,"Zhang Huang");
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("OnePlus",2013,"Pete Lau");
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("Google",1998,"Sundar Pichai");
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("MICROSOFT",1975,"Bill Gates");
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("Honor",2013,"George Zhao");
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("Samsung",1938,"Ki Nam Kim, Hyun Suk Kim, Dong Jin Koh");
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("MI",2010,"Jun Lei");
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("HUAWEI",1987,"Zhengfei Ren");
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("Apple",1976,"Tim Cook");
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("vivo",2009,"Wei Shen, YongPing Duan");
INSERT IGNORE INTO Brands(BrandName, YearEstablished, CEO) VALUES ("OPPO",2004,"Tony Chen");
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (16,"Mi 9T Pro","MI",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (17,"Mi A3","MI",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (12,"HUAWEI Nova 5T","HUAWEI",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (70,"XBOX","MICROSOFT",2013);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (15,"Redmi Note7","MI",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (9,"Honor View 20","Honor",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (11,"HUAWEI Mate 20 X","HUAWEI",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (19,"Reno2 F","OPPO",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (18,"Mi 9 SE","MI",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (7,"OnePlus 7 Pro","OnePlus",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (10,"HUAWEI P30 Pro","HUAWEI",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (4,"iPhone XR","Apple",2018);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (14,"Redmi 7A","MI",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (3,"iPhone XS","Apple",2018);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (0,"iPhone 7","Apple",2016);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (2,"iPhone X","Apple",2017);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (71,"XBOX ONE","MICROSOFT",2015);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (72,"XBOX TWO","MICROSOFT",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (20,"K3","OPPO",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (13,"HUAWEI P20","HUAWEI",2018);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (6,"Samsung Galaxy Note 9","Samsung",2018);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (8,"Google Pixel 3 XL","Google",2018);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (5,"Samsung Galaxy S10","Samsung",2019);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (1,"iPhone 8","Apple",2017);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (73,"XBOX THREE","MICROSOFT",2020);
INSERT IGNORE INTO Products(ProductId, ProductName, BrandName, YearReleased) VALUES (74,"XBOX IV","MICROSOFT",2024);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (0,0,3,4023);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (1,1,0,3338);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (2,2,17,5311);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (3,2,19,3899);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (4,2,5,4346);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (5,3,23,3773);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (6,4,3,3385);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (7,4,5,3829);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (8,5,23,4484);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (9,5,19,4322);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (10,5,15,4686);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (11,5,0,3476);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (12,6,13,5516);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (13,6,7,4169);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (14,6,12,4721);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (15,7,6,5341);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (16,8,9,3581);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (17,8,22,4230);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (18,8,12,4222);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (19,8,25,3525);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (20,9,21,3670);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (21,10,12,4979);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (22,10,13,5445);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (23,10,0,3557);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (24,11,1,5528);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (25,11,16,5484);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (26,11,4,4999);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (27,11,0,3949);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (28,11,12,4260);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (29,11,24,3445);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (30,12,14,3289);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (31,12,11,4411);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (32,12,19,5890);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (33,12,9,5039);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (34,13,5,5902);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (35,13,8,5038);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (36,13,15,3021);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (37,13,21,5656);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (38,13,2,3974);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (39,14,0,4599);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (40,14,17,4124);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (41,14,13,5126);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (42,14,3,3220);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (43,14,9,4385);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (44,15,13,5019);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (45,15,16,3057);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (46,15,9,3910);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (47,15,5,3622);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (48,16,6,5553);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (49,16,14,3985);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (50,17,23,4884);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (51,17,8,3946);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (52,17,16,3211);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (53,17,12,3581);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (54,17,22,4900);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (55,18,6,3677);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (56,18,21,5619);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (57,18,13,3758);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (58,18,2,5268);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (59,18,7,5116);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (60,19,3,5149);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (61,19,25,3733);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (62,19,9,3311);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (63,19,14,5204);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (64,20,15,3826);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (65,20,12,3172);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (66,21,20,4631);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (67,21,18,3775);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (68,21,2,4770);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (69,22,12,3796);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (70,23,14,5361);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (71,24,12,5732);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (72,24,13,5167);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (73,24,19,3266);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (74,24,24,4724);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (75,24,22,5689);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (76,24,15,3824);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (77,25,7,4039);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (78,25,13,4291);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (79,25,0,4615);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (80,25,14,3220);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (81,26,20,3400);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (82,26,15,3577);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (83,26,22,3566);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (84,26,23,3683);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (85,27,5,3985);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (86,27,22,3857);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (87,28,25,5218);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (88,28,16,4687);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (89,28,8,3979);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (90,28,13,5664);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (91,28,12,3731);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (92,28,21,3096);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (93,29,11,4372);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (94,29,14,3007);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (95,29,4,5667);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (96,29,20,3471);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (97,29,21,3428);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (98,29,7,5057);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (99,30,19,3004);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (100,30,10,4510);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (101,30,15,3458);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (102,30,7,4280);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (103,31,1,3162);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (104,31,0,5345);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (105,32,9,4051);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (106,32,22,3618);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (107,32,16,5800);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (108,32,5,4100);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (109,33,21,5196);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (110,33,12,5621);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (111,33,0,5295);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (112,34,14,4085);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (113,34,5,3682);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (114,34,0,3315);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (115,34,10,5132);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (116,34,20,4419);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (117,34,16,4129);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (118,35,22,5190);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (119,35,19,4117);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (120,35,21,3943);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (121,36,11,4263);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (122,36,14,4919);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (123,36,21,3363);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (124,36,7,4101);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (125,36,6,5031);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (126,37,6,5570);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (127,37,22,5624);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (128,37,2,3895);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (129,37,0,5866);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (130,37,15,5230);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (131,37,7,4025);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (132,38,3,3111);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (133,38,17,4761);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (134,38,5,5220);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (135,38,21,3600);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (136,39,8,5418);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (137,39,0,3755);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (138,40,13,3703);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (139,40,19,3562);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (140,40,1,3971);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (141,40,2,5229);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (142,40,24,3355);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (143,40,10,4088);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (144,41,0,4487);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (145,41,25,5897);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (146,41,19,5679);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (147,42,20,4448);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (148,43,13,5973);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (149,44,24,4592);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (150,44,6,4294);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (151,44,17,5234);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (152,44,8,3904);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (153,44,3,4182);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (154,45,22,4811);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (155,45,7,3829);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (156,46,22,5029);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (157,46,9,5630);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (158,46,19,3903);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (159,46,25,5118);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (160,47,17,5153);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (161,47,8,4840);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (162,47,21,5924);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (163,48,23,4863);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (164,49,11,4950);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (165,49,3,5825);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (166,49,18,4020);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (167,49,5,3668);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (168,49,14,3061);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (169,50,21,5171);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (170,50,16,4239);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (171,51,22,4301);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (172,51,24,4567);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (173,51,4,5512);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (174,51,16,4958);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (175,51,8,5280);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (176,51,12,3170);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (177,52,17,5383);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (178,52,21,3070);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (179,52,2,3961);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (180,53,1,4042);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (181,53,15,3431);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (182,53,18,3526);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (183,53,22,5534);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (184,54,15,3512);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (185,54,7,3407);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (186,54,8,5733);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (187,54,19,3968);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (188,54,9,4326);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (189,54,20,5986);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (190,55,22,3488);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (191,56,7,3588);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (192,56,22,3693);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (193,56,11,4717);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (194,57,19,3269);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (195,58,14,4745);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (196,58,7,3830);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (197,58,5,3289);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (198,58,17,4370);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (199,58,4,4239);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (200,59,4,4083);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (201,59,2,5527);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (202,60,4,3153);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (203,60,7,3913);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (204,61,16,5101);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (205,61,8,3968);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (206,61,1,3384);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (207,61,11,5579);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (208,62,2,5469);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (209,63,24,4939);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (210,63,20,4897);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (211,63,10,4151);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (212,63,18,3143);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (213,64,25,5427);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (214,65,10,5173);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (215,65,20,3155);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (216,65,8,4081);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (217,65,9,4501);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (218,66,11,3956);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (219,66,24,3752);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (220,66,2,5618);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (221,66,15,5279);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (222,66,25,5343);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (223,67,7,4036);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (224,67,16,5757);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (225,67,10,3185);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (226,67,25,3566);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (227,67,1,5629);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (228,67,14,5394);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (229,68,13,4769);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (230,68,17,5551);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (231,68,23,5719);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (232,69,3,5331);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (233,69,9,4981);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (234,69,22,3533);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (235,69,21,4515);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (236,69,16,5911);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (237,70,18,5116);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (238,70,22,3205);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (239,70,25,5060);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (240,70,3,3270);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (241,71,8,4489);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (242,71,17,4997);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (243,71,14,4217);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (244,72,8,3145);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (245,72,23,3714);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (246,72,7,5317);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (247,72,10,3235);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (248,73,23,3114);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (249,73,13,3356);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (250,73,15,4185);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (251,74,8,5157);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (252,74,24,5705);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (253,74,10,5430);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (254,74,0,5503);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (255,74,11,3262);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (256,75,4,5531);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (257,75,9,3855);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (258,75,12,5640);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (259,76,1,5709);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (260,77,12,3040);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (261,77,21,4019);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (262,77,10,4274);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (263,77,1,4446);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (264,77,13,4169);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (265,78,20,4423);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (266,78,4,5989);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (267,78,6,5436);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (268,79,23,5930);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (269,79,22,5780);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (270,80,11,3444);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (271,81,24,5002);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (272,81,23,3044);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (273,82,23,3547);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (274,82,9,3593);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (275,82,4,5009);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (276,82,20,4741);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (277,83,21,4459);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (278,83,24,5959);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (279,84,13,5872);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (280,84,12,3365);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (281,84,11,3218);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (282,84,19,3673);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (283,84,4,4525);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (284,85,18,4268);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (285,85,2,5344);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (286,85,11,3978);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (287,85,21,5159);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (288,86,16,5022);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (289,86,4,3994);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (290,86,20,3623);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (291,86,24,5704);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (292,86,5,5458);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (293,86,18,5756);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (294,87,19,3238);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (295,87,5,5036);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (296,87,13,5024);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (297,88,1,3598);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (298,88,20,3107);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (299,88,15,5030);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (300,88,17,4565);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (301,88,22,3304);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (302,88,19,3518);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (303,89,17,5452);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (304,89,13,4916);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (305,90,21,5868);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (306,90,4,4335);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (307,90,5,5531);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (308,91,17,3615);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (309,91,1,3246);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (310,91,20,3977);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (311,91,13,3847);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (312,91,25,4638);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (313,91,5,5973);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (314,92,21,5857);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (315,92,2,4815);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (316,92,16,3606);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (317,92,1,3102);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (318,93,18,3710);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (319,93,13,4494);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (320,94,25,3701);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (321,94,17,5173);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (322,94,23,4624);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (323,94,18,4058);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (324,94,13,3617);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (325,94,10,3573);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (326,95,23,5178);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (327,95,4,3938);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (328,95,20,5414);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (329,95,16,3657);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (330,96,6,4026);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (331,96,4,4956);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (332,96,22,5119);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (333,96,8,3704);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (334,97,3,5125);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (335,97,15,4916);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (336,97,17,5528);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (337,97,25,5597);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (338,97,4,3332);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (339,98,15,4588);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (340,98,5,4600);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (341,98,10,5116);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (342,98,17,3513);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (343,98,2,5108);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (344,99,13,3405);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (345,99,8,3969);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (346,99,10,3381);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (347,99,20,5208);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (348,99,6,3278);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (349,99,18,6985);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (350,99,18,4936);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (351,99,15,2152);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (352,99,17,4919);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (353,98,17,7027);
INSERT IGNORE INTO Purchases(PurchaseId, CustomerId, ProductId, Price) VALUES (354,99,15,5120);
