from django.shortcuts import render
from django.http import HttpResponse

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

    return pokemondata


def home(request):
    context ={
        'title' : 'Pokedex Home'
    }
    return render(request, 'pokedexapp/home.html', context)

def pokemonData(request):
    pokemon = retrieveFromPokeAPI()

    context = {
        'pokemon' : pokemon,
        'title' : pokemon['name'] + '\'s Data'
    }
    return render(request, 'pokedexapp/pokedata.html', context)


""" BASE_URL = 'http://pokeapi.co'

def query_pokeapi(resource_uri):
    url = '{0}{1}'.format(BASE_URL, resource_uri)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    return None

ninetales = query_pokeapi('api/v2/pokemon/ninetales')
 """
# sprite_uri = ninetales['sprites'][0]['resource_uri']
# description_uri = ninetales['descriptions'][0]['resource_uri']

# sprite = query_pokeapi(sprite_uri)
# description = query_pokeapi(description_uri)

#print ninetales['name']
#print description['description']
#print BASE_URL + sprite['image']

