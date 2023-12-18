from django.db import models
from django.contrib.auth.models import User
from pokedex.models import Pokemon

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemons = models.ManyToManyField(Pokemon)

    def __str__(self):
        return self.name
