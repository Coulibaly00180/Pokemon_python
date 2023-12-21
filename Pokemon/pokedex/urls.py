from django.urls import path
from .views import *

urlpatterns = [
    path('api/pokemons/', get_paginated_pokemons, name='paginated-pokemons'),
    path('api/pokemon/<int:pokedex_number>/', pokemon_detail_view, name='pokemon-detail'),
    path('api/pokemon/search-pokemon/', search_pokemon_by_name, name='search-pokemon-by-name'), # /api/search-pokemon/?name=charizard
]