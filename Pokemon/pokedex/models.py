from typing import Any
from django.db import models

''' Je dois ajouter les moves (attaques des pokemons)'''
class Pokemon(models.Model):
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=30)
    type1 = models.CharField(max_length=20)
    type2 = models.CharField(max_length=20, blank=True, null=True)
    hp_max = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField()
    defense = models.PositiveSmallIntegerField()
    special_attack = models.PositiveSmallIntegerField()
    special_defense = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()

        
    

    def __str__(self):
        return self.name


    # Attaque du pokemon (Vérification du type adverse pour infligé +0.5 ou -0.5 de dégâts)
    # Déduction des dégâts en fonction de mon attaque et de la defense advers
    # Peut être créer une fonction pour vérifier le type des pokemons serait mieux
    def attaque(self, enemy):
        pass

    # Pareil que attaque mais avec l'attaque spéciale
    def attaque_specialt(self, enemy):
        pass

    # Vérifiér si le pokemon est mort pour l'éffacer du terrain, on vérifie l'hp max restant restant
    def death(self):
        pass

