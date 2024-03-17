LOAD CSV WITH HEADERS
FROM 'file:///movie-nodes-cypher.csv'
AS line
MERGE (movie:Movie {movie_id: toInteger(line.movie_id),
                    movie_name: line.movie_name,
                    release_year: toInteger(line.release_year),
                    ratings: toInteger(line.ratings),
                    genre: line.genre});