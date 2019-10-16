from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pokedex-home'),
    path('pokemon/', views.pokemonData, name='pokemon-data'),
]
