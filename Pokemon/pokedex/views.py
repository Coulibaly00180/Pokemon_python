from django.shortcuts import render
import requests

from django.core.paginator import Paginator

# Recuperer 10 pokemon
def get_pokemons(page=1, limit=10):
    offset = (page - 1) * limit
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}')
    return response.json()

def get_pokemon_details(pokedex_number):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokedex_number}/"
    response = requests.get(url)
    pokemon_details = response.json()
    return {
        'name': pokemon_details['name'],
        'image': pokemon_details['sprites']['other']['official-artwork']['front_default'],
        'types': [type['type']['name'] for type in pokemon_details['types']],
        'height': pokemon_details['height'],
        'weight': pokemon_details['weight'],
        'stats': [base_stat['stat']['name'] for base_stat in pokemon_details['stats']],
        'stats_of': [{'name': stat['stat']['name'], 'value': stat['base_stat']} for stat in pokemon_details['stats']],
    }

def recherche_pokemon(search_query, page=1, limit=10):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit=1000')  # Obtenez une grande liste de Pokémon
    all_pokemons = response.json()['results']

    # Filtrer les Pokémon par le nom de recherche
    filtered_pokemons = [pokemon for pokemon in all_pokemons if search_query.lower() in pokemon['name'].lower()]

    # Pagination
    paginator = Paginator(filtered_pokemons, limit)
    pokemons_page = paginator.get_page(page)

    return {
        'results': pokemons_page.object_list,
        'count': paginator.count
    }


# Create your views here. Affichez les pokemons
def index_pokedex(request):
    search_query = request.GET.get('search', '')
    page = int(request.GET.get('page', 1))
    if search_query:
        data = recherche_pokemon(search_query, page)
    else:
        data = get_pokemons(page)
    total_pokemon = data['count']
    total_pages = (total_pokemon + 9) // 10

    pokemons = []
    for pokemon in data['results']:
        detail_response = requests.get(pokemon['url'])
        detail_data = detail_response.json()

        sprites = detail_data.get('sprites', {})
        pokemons.append({
            'name': detail_data['name'],
            'image': sprites.get('front_default', 'default-image-url'),
            'pokedex_number': detail_data['id']
        })

    return render(request, 'pokedex/index.html', {
        'pokemons': pokemons,
        'current_page': page,
        'total_pages': total_pages,
        'total_pokemon': total_pokemon
    })

def detail_pokemon_view(request, pokedex_number):
    pokemon_details = get_pokemon_details(pokedex_number)
    return render(request, 'pokedex/detail_pokemon.html', {'pokemon': pokemon_details})