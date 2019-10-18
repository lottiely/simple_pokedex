from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Pokemon

def home(request):
    context ={
        'title' : 'Pokedex'
    }
    return render(request, 'pokedexapp/home.html', context)

def pokemonData(request):
    query = request.GET.get('pokesearch')
    pokemon = Pokemon.objects.filter(name__iexact=query)

    context = {
        'pokemon' : pokemon.first,
        'title' : query
    }
    return render(request, 'pokedexapp/pokedata.html', context)