import SqlParser

query = "Select * from table where id = (Select id2 from table where id1 = 2 and id2 = (Select id2 from table where id3 = 2))"
print(SqlParser.getConstraints(query))
