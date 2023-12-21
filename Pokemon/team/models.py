from django.db import models
from pokedex.models import Pokemon

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    pokemons = models.ManyToManyField(Pokemon)

    def __str__(self):
        return self.name