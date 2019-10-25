from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

import requests
import json

def retrieveFromPokeAPI(pokemon_id):
    """
        Given either a Pokemon name or game index, this method will concatnate the identifier to the PokeAPI URI
        and make a get request for the Pokemon data. The output is a pokemonData object holding the name, game
        index, genus, appearance URL, flavor text, and type of the Pokemon.
        If the Pokemon isn't found, this method will return a null value.
    """
    species_uri = "https://pokeapi.co/api/v2/pokemon-species/"

    pokemon_uri = "https://pokeapi.co/api/v2/pokemon/"
    
    # Retrieve flavortext, genus
    response = requests.get(species_uri + pokemon_id)

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
    """
        The home view includes the search bar where the user can type the game index or the name of the Pokemon they want to look up.
        Once the user enters their input, the page will route to the pokemonData page.
    """
    context ={
        'title' : 'Pokedex'
    }
    return render(request, 'pokedexapp/home.html', context)

def pokemonData(request):
    """
        This page will retrieve the user input from the home page and will make a get request from PokeAPI for the Pokemon data.
        If the Pokemon data is found, this page will present the data to the user.
    """
    query = request.GET.get('pokesearch').lower()
    #pokemon = Pokemon.objects.filter(name__iexact=query)
    pokemon = retrieveFromPokeAPI(query)

    context = {
        #'pokemon' : pokemon.first,
        'pokemon' : pokemon,
        'title' : query
    }
    return render(request, 'pokedexapp/pokedata.html', context)
