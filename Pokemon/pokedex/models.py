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
