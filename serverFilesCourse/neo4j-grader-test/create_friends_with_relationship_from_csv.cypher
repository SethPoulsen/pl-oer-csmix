LOAD CSV WITH HEADERS
FROM 'file:///friendRelationships-cypher.csv'
AS line
MATCH (actor1:Actor {actor_id: toInteger(line.person1_id)}), (actor2:Actor {actor_id: toInteger(line.person2_id)})
MERGE (actor1)-[:FRIENDS_WITH]-(actor2);