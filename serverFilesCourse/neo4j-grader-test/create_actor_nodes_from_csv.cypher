LOAD CSV WITH HEADERS
FROM 'file:///actor-nodes-cypher.csv'
AS line
MERGE (actor:Actor {actor_id: toInteger(line.actor_id),
                    actor_name: line.actor_name,
                    birth_year: toInteger(line.birth_year),
                    birth_country: line.birth_country});