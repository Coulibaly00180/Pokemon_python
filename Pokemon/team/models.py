from django.db import models
from pokedex.models import Pokemon, Attack

class Team(models.Model):
    name = models.CharField(max_length=30)
    pokemons = models.ManyToManyField(Pokemon)

    def __str__(self):
        return self.name

    @staticmethod
    def createTeam(name_team):
        team = Team(name=name_team)
        team.save()
        return team

    @staticmethod
    def deleteTeam(name_team):
        try:
            team = Team.objects.get(name=name_team)
            team.delete()
            return True
        except Team.DoesNotExist:
            return False

    @staticmethod
    def renameTeam(old_name, new_name):
        try:
            team = Team.objects.get(name=old_name)
            team.name = new_name
            team.save()
            return True
        except Team.DoesNotExist:
            return False

    def addPokemonTeam(self, pokemon, selected_attacks):
        if self.pokemons.count() < 6:
            # Enregistrez ou sélectionnez les attaques
            for attack_name in selected_attacks:
                attack, created = Attack.objects.get_or_create(name=attack_name)
                pokemon.attacks.add(attack)

            # Ajoutez le Pokémon à l'équipe
            self.pokemons.add(pokemon)
            return True
        else:
            return False


    @staticmethod
    def clearAllPokemonTeam(name_team):
        try:
            team = Team.objects.get(name=name_team)
            team.pokemons.clear()
            return True
        except Team.DoesNotExist:
            return False
