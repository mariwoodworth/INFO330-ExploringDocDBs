# Connects to mongodb & the appropriate collection:
import sqlite3  # This is the package for all sqlite3 access in Python
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Connecting to database, extracting values from pokemon db
connection = sqlite3.connect('pokemon.sqlite')
cursor = connection.cursor()
generalquery = "SELECT name, pokedex_number, hp, attack, defense, speed, sp_attack, sp_defense FROM pokemon;"

cursor.execute(generalquery)
pokemon_data = cursor.fetchall()

# Iterating through pokemon_data (gen query results)
for p in pokemon_data:
    # Selecting abilities
    abilityquery = "SELECT t1.name FROM ability as t1 JOIN pokemon_abilities AS t2 ON t1.id = t2.ability_id WHERE t2.pokemon_id = '" + str(p[1]) + "';"
    cursor.execute(abilityquery)
    abilities = cursor.fetchall()

    # New abilities array to take off ', and append abilities
    abilityArr = []
    for a in abilities:
        a2 = a[0].strip("',")
        abilityArr.append(a2)

    # Selecting types
    types = cursor.execute("SELECT type1, type2 FROM pokemon_types_view WHERE name=?", (p[0],)).fetchall()

    # New types array to append types together
    typeArr = []
    for t in types[0]:
        typeArr.append(t)

    pokemon = {
        "name": p[0],
        "pokedex_number": p[1],
        "types": typeArr,
        "hp": p[2],
        "attack": p[3],
        "defense": p[4],
        "speed": p[5],
        "sp_attack": p[6],
        "sp_defense": p[7],
        "abilities": abilityArr
    }

    pokemonColl.insert_one(pokemon) 

'''
for doc in pokemonColl.find({}):
    print(doc)
'''
    
