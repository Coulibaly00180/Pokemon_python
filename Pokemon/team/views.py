from django.shortcuts import render, redirect
from .models import Team, Pokemon, Attack

def create_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        if team_name:
            Team.createTeam(team_name)
            return redirect('create_team')  
    return render(request, 'create_team.html')  

def delete_team(request, team_name):
    Team.deleteTeam(team_name)
    teams = Team.objects.all()
    for team in teams:
        print(team.name)  # or use logging

    return render(request, 'all_teams.html', {'teams': teams})

def rename_team(request, old_name):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        if new_name:
            Team.renameTeam(old_name, new_name)
            return redirect('some_view_to_redirect')
    return render(request, 'rename_team.html', {'old_name': old_name})

def add_pokemon_to_team(request, team_id):
    team = Team.objects.get(id=team_id)
    pokemons = Pokemon.objects.all()
    attacks = Attack.objects.all()  

    if request.method == 'POST':
        pokemon_id = request.POST.get('pokemon_id')
        selected_attacks = request.POST.getlist('attacks')

        if pokemon_id and len(selected_attacks) <= 4:
            pokemon = Pokemon.objects.get(id=pokemon_id)
            added_successfully = team.addPokemonTeam(pokemon, selected_attacks)

            if added_successfully:
                return redirect('team_detail', team_id=team.id)  # Redirige vers une page de détail de l'équipe
            else:
                # Gérer le cas où l'ajout échoue (par exemple, l'équipe a déjà 6 Pokémon)
                pass

    return render(request, 'add_pokemon_to_team.html', {
        'team': team,
        'pokemons': pokemons,
        'attacks': attacks
    })

def clear_pokemons_from_team(request, team_name):
    Team.clearAllPokemonTeam(team_name)
    return redirect('some_view_to_redirect')

def showAllTeam(request):
    teams = Team.objects.all()  # Récupère toutes les équipes
    return render(request, 'all_teams.html', {'teams': teams})

def showTeam(request, id):
    team = Team.objects.get(id=id)  # Récupère l'équipe spécifique par son ID
    pokemons = team.pokemons.all()  # Récupère tous les Pokémon dans cette équipe
    return render(request, 'team_detail.html', {'team': team, 'pokemons': pokemons})