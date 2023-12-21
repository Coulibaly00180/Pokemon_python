from django.shortcuts import render
import requests
from django.http import JsonResponse


# Recupère 20 pokemons en premier
def get_paginated_pokemons(request):
    limit = request.GET.get('limit', 20)
    offset = request.GET.get('offset', 0)

    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    response = requests.get(url)
    if response.status_code != 200:
        return JsonResponse({'error': 'API error'}, status=response.status_code)

    pokemon_list = response.json()['results']
    detailed_pokemons = []

    for pokemon in pokemon_list:
        detail_url = pokemon['url']
        detail_response = requests.get(detail_url)
        if detail_response.status_code == 200:
            pokemon_details = detail_response.json()
            detailed_pokemons.append({
                'name': pokemon_details['name'],
                'number': pokemon_details['id'],
                'image': pokemon_details['sprites']['front_default']
            })

    return JsonResponse({'pokemons': detailed_pokemons})

# Afficher les informations d'un pokémon
def pokemon_detail_view(request, pokedex_number):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokedex_number}/"
    response = requests.get(url)

    if response.status_code != 200:
        return JsonResponse({'error': 'Pokémon not found or API error'}, status=response.status_code)

    pokemon_details = response.json()

    data = {
        'name': pokemon_details['name'],
        'image': pokemon_details['sprites']['other']['official-artwork']['front_default'],
        'types': [type['type']['name'] for type in pokemon_details['types']],
        'height': pokemon_details['height'],
        'weight': pokemon_details['weight'],
        'stats': [base_stat['stat']['name'] for base_stat in pokemon_details['stats']],
        'stats_of': [{'name': stat['stat']['name'], 'value': stat['base_stat']} for stat in pokemon_details['stats']],
    }

    return JsonResponse(data)

# Recherche pokemon
def search_pokemon_by_name(request):
    # Récupérer le nom du Pokémon depuis les paramètres de requête
    pokemon_name = request.GET.get('name', '').lower()
    if not pokemon_name:
        return JsonResponse({'error': 'No Pokémon name provided'}, status=400)

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)
    if response.status_code != 200:
        return JsonResponse({'error': 'Pokémon not found'}, status=response.status_code)

    pokemon_details = response.json()
    pokemon_data = {
        'name': pokemon_details['name'],
        'number': pokemon_details['id'],
        'image': pokemon_details['sprites']['front_default'],
    }

    return JsonResponse(pokemon_data)