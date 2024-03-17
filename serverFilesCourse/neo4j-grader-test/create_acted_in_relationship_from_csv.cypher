LOAD CSV WITH HEADERS
FROM 'file:///relationships-cypher.csv'
AS line
MERGE (actor:Actor {actor_id: toInteger(line.actor_id)})
MERGE (movie:Movie {movie_id: toInteger(line.movie_id)})
MERGE (actor)-[r:ACTED_IN]->(movie);