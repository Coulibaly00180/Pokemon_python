from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Team, Pokemon
from django.views.decorators.http import require_http_methods

# Create your views here.

# Création d'une équipe pokemon
@csrf_exempt
def create_team(request):
    # Vérifier si la requête est POST
    if request.method == 'POST':
        try:
            # Décoder les données JSON à partir du corps de la requête
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        # Extraire le nom de l'équipe à partir des données JSON
        name = data.get('name')

        # Validation du nom
        if not name:
            return JsonResponse({'error': 'Team name is required'}, status=400)

        # Création de l'équipe
        team, created = Team.objects.get_or_create(name=name)

        # Vérifier si l'équipe a été nouvellement créée ou existait déjà
        if created:
            return JsonResponse({'success': f"Team '{team.name}' was created successfully"})
        else:
            return JsonResponse({'notice': f"Team '{team.name}' already exists"})

    # Si la requête n'est pas POST, renvoyer une erreur
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Modification du nom de la team
@csrf_exempt
def rename_team(request):
    # S'assurer que la méthode est POST
    if request.method == 'POST':
        # Extraire et décoder les données JSON
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        team_id = data.get('team_id')
        new_name = data.get('new_name')

        # Valider les données
        if not team_id or not new_name:
            return JsonResponse({'error': 'Both team_id and new_name are required'}, status=400)

        # Rechercher l'équipe et renommer
        try:
            team = Team.objects.get(id=team_id)
            team.name = new_name
            team.save()
            return JsonResponse({'success': f"Team renamed to '{new_name}'"})
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Team not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Suppression d'une équipe pokemon
@require_http_methods(["DELETE"])
def delete_team(request, team_id):
    try:
        # Rechercher l'équipe avec l'identifiant fourni
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        return JsonResponse({'error': 'Team not found'}, status=404)

    # Supprimer l'équipe
    team.delete()
    return JsonResponse({'success': f"Team with id {team_id} was deleted successfully"})

# Voir toutes teams et les pokemons à l'interrieur des teams c'est à dire renvoyer un json de ce genre
'''
{
    "team": "Vert"
    "pokemons": [
        {
            "name": "bulbasaur"
            "image": "url_image"
        },
        {
            "name": "bulbasaur"
            "image": "url_image"
        }
    ]
}
'''
def showAllTeamsPokemon():
    pass



# Voir les pokemons d'une team
def showTeamPokemon():
    pass

# Ajout d'un pokemon dans une team
@csrf_exempt
def add_pokemon_team(request, team_id, pokedex_number):
    # Vérifier la taille de l'équipe
    team = Team.objects.get(id=team_id)
    if team.pokemons.count() >= 6:
        return JsonResponse({'error': 'The team is already full'}, status=400)

    # Vérifier si le Pokémon existe déjà dans la BD
    pokemon, created = Pokemon.objects.get_or_create(number=pokedex_number)
    if created:
        # Récupérer les données du Pokémon depuis l'API PokéAPI
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokedex_number}")
        if response.status_code != 200:
            return JsonResponse({'error': 'Pokémon not found in PokéAPI'}, status=404)

        pokemon_data = response.json()
        pokemon.name = pokemon_data['name']
        pokemon.type1 = pokemon_data['types'][0]['type']['name']
        pokemon.type2 = pokemon_data['types'][1]['type']['name'] if len(pokemon_data['types']) > 1 else ''
        pokemon.hp = pokemon_data['stats'][0]['base_stat']
        pokemon.attack = pokemon_data['stats'][1]['base_stat']
        pokemon.defense = pokemon_data['stats'][2]['base_stat'],
        pokemon.special_attack = pokemon_data['stats'][3]['base_stat']
        pokemon.special_defense = pokemon_data['stats'][4]['base_stat']
        pokemon.speed = pokemon_data['stats'][5]['base_stat']
        pokemon.save()

    # Ajouter le Pokémon à l'équipe
    team.pokemons.add(pokemon)
    return JsonResponse({'success': f"Pokemon {pokemon.name} added to team {team.name}"})

# Suppression d'un pokemon dans une team
@csrf_exempt
def delete_poke_team(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        team_id = data.get('team_id')
        pokemon_id = data.get('pokemon_id')

        if not team_id or pokemon_id is None:
            return JsonResponse({'error': 'Team ID and Pokémon ID are required'}, status=400)

        try:
            team = Team.objects.get(id=team_id)
            pokemon = Pokemon.objects.get(id=pokemon_id)
            if pokemon not in team.pokemons.all():
                return JsonResponse({'error': 'Pokémon is not in the team'}, status=400)

            team.pokemons.remove(pokemon)
            return JsonResponse({'success': f"Pokémon {pokemon.name} removed from team {team.name}"})
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Team not found'}, status=404)
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokémon not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=405)