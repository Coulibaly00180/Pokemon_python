from django.shortcuts import render, redirect
from .models import Team, Pokemon

def create_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        if team_name:
            Team.createTeam(team_name)
            return redirect('some_view_to_redirect')  # Rediriger vers une vue appropriée
    return render(request, 'create_team.html')  # Renvoyer à la page de création d'équipe

def delete_team(request, team_name):
    Team.deleteTeam(team_name)
    return redirect('some_view_to_redirect')

def rename_team(request, old_name):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        if new_name:
            Team.renameTeam(old_name, new_name)
            return redirect('some_view_to_redirect')
    return render(request, 'rename_team.html', {'old_name': old_name})

def add_pokemon_to_team(request, team_name):
    team = Team.objects.get(name=team_name)
    if request.method == 'POST':
        pokemon_id = request.POST.get('pokemon_id')
        if pokemon_id:
            pokemon = Pokemon.objects.get(id=pokemon_id)
            team.addPokemonTeam(pokemon)
            return redirect('some_view_to_redirect')
    pokemons = Pokemon.objects.all()
    return render(request, 'add_pokemon_to_team.html', {'team': team, 'pokemons': pokemons})

def clear_pokemons_from_team(request, team_name):
    Team.clearAllPokemonTeam(team_name)
    return redirect('some_view_to_redirect')
