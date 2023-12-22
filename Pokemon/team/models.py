from django.db import models
from pokedex.models import Pokemon

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    pokemons = models.ManyToManyField(Pokemon)

    def __str__(self):
        return self.name

    def createTeam(name_team):
        pass

    def deleteTeam(name_team):
        pass

    def renameTeam(name_team):
        pass

    def addPokemonTeam(pokemon):
        pass

    def clearAllPokemonTeam(name_team):
        pass
