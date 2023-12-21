from django.urls import path
from .views import *

urlpatterns = [
    path('api/create-team', create_team, name='create-team'),
    path('api/add-pokemon-team/<int:team_id>/<int:pokedex_number>/', add_pokemon_team, name='add-pokemon-team'),
    path('api/delete-poke-team/', delete_poke_team, name='delete-poke-team'),
    path('api/rename-team/', rename_team, name='rename-team'),
]

'''
create-team
{
    "name": "Team Rocket"
}
'''

'''
add-pokemon-team
{
    "team_id": 1,
    "pokemon_id": 25
}
'''


'''
Rename_team
{
    "team_id": 1,
    "new_name": "Nouveau Nom d'Équipe"
}
'''