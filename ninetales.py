""" This is a test script to test the functionality of requesting from PokeAPI
"""

import requests
import json

""" 
Given the pokemon id which can be a number or a name, a request for the pokemon data is made to pokeAPI.
The output will be a pokemondata object with the name, game index, genus, appearance URL, flavor text, and type of the pokemon.
"""
def retrieveFromPokeAPI(pokemon_id):
    species_uri = "https://pokeapi.co/api/v2/pokemon-species/"

    pokemon_uri = "https://pokeapi.co/api/v2/pokemon/"
    
    # Retrieve flavortext, genus
    response = requests.get(species_uri + pokemon_id)

    print(species_uri + pokemon_id)

    if response.status_code == 200:
        data = response.json()
    else:
        return ""

    flavortext = ""
    genus = ""

    for x in data["flavor_text_entries"]:
        if(x["language"]["name"] == "en"):
            flavortext = x["flavor_text"]
            break
    
    for x in data["genera"]:
        if(x["language"]["name"] == "en"):
            genus = x["genus"]

    # Retrieve game index, appearance
    response = requests.get(pokemon_uri + pokemon_id)

    if response.status_code == 200:
        data = response.json()
    else:
        return ""

    name = data['name']
    appearanceURL = data["sprites"]["front_default"] 
    gameIndex = f'{data["game_indices"][0]["game_index"]:03}'
    types = []

    for x in data["types"]:
        types.append(x["type"]["name"].upper())

    pokemondata = {
        'name': name,
        'gameIndex': gameIndex, 
        'genus': genus,
        'appearanceURL': appearanceURL,
        'flavortext': flavortext,
        'types': types,
    }

    return pokemondata

print(json.dumps(retrieveFromPokeAPI("uxie"), indent=4))