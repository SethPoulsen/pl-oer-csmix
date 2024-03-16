MATCH (c:City)<-[:LOCATED_IN]-(r:Restaurant)-[:SERVES]->(cu:Cuisine)
WITH c.city_id AS CityID, c.city_name AS City, count(DISTINCT cu) AS CuisineCount
MATCH (r:Restaurant)-[:LOCATED_IN]->(c)
WHERE r.ratings > 6 AND c.city_id = CityID
WITH City,CuisineCount, collect(r.restaurant_name) AS bigStars, count(DISTINCT r) AS Count
RETURN City, CuisineCount, bigStars, Count
ORDER BY CuisineCount ASC, City ASC
LIMIT 5;


