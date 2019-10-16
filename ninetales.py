import requests
import json

def retrieveFromPokeAPI():

    # Retrieve flavortext
    response = requests.get("https://pokeapi.co/api/v2/pokemon-species/ninetales/")

    ninetalesobj = response.json()
    flavortext = ""

    for x in ninetalesobj["flavor_text_entries"]:
        if(x["language"]["name"] == "en" and x["version"]["name"] == "firered"):
            flavortext = x["flavor_text"]

    # Retrieve appearance
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ninetales")

    ninetalesobj = response.json()
    appearanceURL = ninetalesobj["sprites"]["front_default"]

    pokemondata = {
        'name': 'Ninetales',
        'appearanceURL' : appearanceURL,
        'flavortext': flavortext
    }
    
    print(flavortext)

retrieveFromPokeAPI()