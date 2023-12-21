from django.db import models
# Importations du model pokemon qui se trouve dans Pokedex

# Classe du terrain de combat
class Dungeon:
    def __init__(self, size):
        self.size = size
        self.map = self.generate_dungeon()
        self.player = self.place_player()

    def generate_dungeon(self):
        pass

    def place_player(self):
        pass


    def move_player(self, player_position, new_position):
        pass