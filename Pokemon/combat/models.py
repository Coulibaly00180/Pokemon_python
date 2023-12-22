from django.db import models
# Importations du model pokemon qui se trouve dans Pokedex

# Classe du terrain de combat
class battlefield:
    def __init__(self):
        self.grid_size = 7
        self.grid = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.turns_limit = 10
        self.current_turn = 0

    def place_pokemon(self, pokemon, position):
        # Placer un Pokémon à une position spécifique sur le terrain
        pass

    def move_pokemon(self, pokemon, new_position):
        # Déplacer un Pokémon à une nouvelle position
        pass

    def attack(self, attacker, defender):
        # Gérer l'attaque d'un Pokémon sur un autre
        pass

    def is_adjacent(self, pos1, pos2):
        # Vérifie si deux positions sont adjacentes (pour les attaques)
        pass

    def next_turn(self):
        # Passer au prochain tour
        self.current_turn += 1
        if self.current_turn > self.turns_limit:
            # Gérer la fin du jeu (par exemple, déterminer le gagnant)
            pass

    def get_turn_order(self, pokemons):
        # Retourne les Pokémon dans l'ordre de leur vitesse
        return sorted(pokemons, key=lambda p: p.speed, reverse=True)

    def perform_action(self, pokemon, action, target=None):
        # Exécute une action pour un Pokémon (déplacer, attaquer, etc.)
        pass

    def determine_order(self, player1_team, player2_team):
        # Créer une liste combinée de tous les Pokémon
        combined_team = player1_team + player2_team

        # Trier la liste par vitesse
        ordered_pokemons = sorted(combined_team, key=lambda p: p.speed, reverse=True)

        return ordered_pokemons
    
    '''
    def game_loop(player1, player2, battlefield):
        while battlefield.current_turn <= battlefield.turns_limit:
            # Déterminer l'ordre des Pokémon pour ce tour
            turn_order = battlefield.determine_order(player1.team, player2.team)

            for pokemon in turn_order:
                # Obtenez l'action pour ce Pokémon (déplacer, attaquer, etc.)
                # Exécutez l'action

            battlefield.next_turn()
    '''

'''
class Player:
    def __init__(self, name):
        self.name = name
        self.team = []  # Liste pour stocker les Pokémon de l'équipe
'''