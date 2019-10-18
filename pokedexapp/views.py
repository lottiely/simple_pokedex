from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

import requests
import json

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
        'name': name.upper(),
        'gameIndex': gameIndex, 
        'genus': genus,
        'appearanceURL': appearanceURL,
        'flavortext': flavortext,
        'types': types,
    }

    return pokemondata

def home(request):
    context ={
        'title' : 'Pokedex'
    }
    return render(request, 'pokedexapp/home.html', context)

def pokemonData(request):
    query = request.GET.get('pokesearch').lower()
    #pokemon = Pokemon.objects.filter(name__iexact=query)
    pokemon = retrieveFromPokeAPI(query)

    context = {
        #'pokemon' : pokemon.first,
        'pokemon' : pokemon,
        'title' : query
    }
    return render(request, 'pokedexapp/pokedata.html', context)