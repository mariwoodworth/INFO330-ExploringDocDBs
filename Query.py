import sqlite3
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon named "Pikachu". (1pt)
print("1) Returns all pokemon named Pikachu")
pikachu = pokemonColl.find({"name":"Pikachu"})
for i in pikachu:
    print(i['name'])

# Write a query that returns all the Pokemon with an attack greater than 150. (1pt)
print("2) Returns all pokemon with an attack greater than 150")
attack150 = pokemonColl.find({"attack": {"$gt":150}})
for i in attack150:
    print(i['name'])

# Write a query that returns all the Pokemon with an ability of "Overgrow" (1pt)
print("3) Returns all pokemon with ability of Overgrow")
overgrowPoke = pokemonColl.find({"abilities":"Overgrow"})
for i in overgrowPoke:
    print(i['name'])