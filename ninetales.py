import requests
import json

def retrieveFromPokeAPI():

    # Retrieve flavortext, genus
    response = requests.get("https://pokeapi.co/api/v2/pokemon-species/ninetales/")

    ninetalesobj = response.json()
    flavortext = ""
    genus = ""

    for x in ninetalesobj["flavor_text_entries"]:
        if(x["language"]["name"] == "en" and x["version"]["name"] == "firered"):
            flavortext = x["flavor_text"]
    
    for x in ninetalesobj["genera"]:
        if(x["language"]["name"] == "en"):
            genus = x["genus"]

    # Retrieve game index, appearance
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ninetales")

    ninetalesobj = response.json()

    appearanceURL = ninetalesobj["sprites"]["front_default"] 

    gameIndex = -1

    types = []

    for x in ninetalesobj["game_indices"]:
        if(x["version"]["name"] == "firered"):
            gameIndex = f'{x["game_index"]:03}'

    for x in ninetalesobj["types"]:
        types.append(x["type"]["name"].upper())

    pokemondata = {
        'name': 'Ninetales',
        'gameIndex': gameIndex, 
        'genus': genus,
        'appearanceURL': appearanceURL,
        'flavortext': flavortext,
        'types': types,
    }

    return pokemondata