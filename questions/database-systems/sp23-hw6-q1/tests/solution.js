db.Movies.aggregate([{$match: {
    $and: [
    {"country": "USA"},
    {"release_year": {$gte: 2000}}
  ]}
  }, {$group: {
  _id: "$genre",
  "avg_rating": {$avg: "$ratings"},
  "avg_year": {$avg: "$release_year"},
}}, {$project: {
  _id:0, 
  genre:"$_id", 
  avg_rating:1,
  avg_year:1,
}},
    {$sort: {genre: 1}}])
