import copy

from Core.Renderer.IRender import *
from GameClasses.Map.Grid import Grid
from GameClasses.Map.Tile import Tile
from GameClasses.Characters.Character import Character
from GameClasses.Characters.Enemy import Enemy
from GameClasses.Items.Potion import Potion
from GameClasses.Game import Game

class TerminalRender(IRender):
    def __init__(self):
        self.__player_char = 'o'
        self.__enemy_char = '&'
        self.__item_char = '*'

    def draw_map(self, game_map, player, enemies, potions):

        # creates a copy to draw the map to avoid chaging the data of the map directly
        temp_map = copy.deepcopy(game_map.grid)

        for enemy in enemies:
            temp_map[enemy.y][enemy.x] = f'\033[91m{self.__enemy_char}\033[0m'

        for potion in potions:
            temp_map[potion.y][potion.x] = f'\033[92m{self.__item_char}\033[0m'

        temp_map[player.y][player.x] = f'\033[94m{self.__player_char}\033[0m'

        # draws full map
        for row in temp_map:
            print(''.join(map(str, row)))


    def draw_line(self):
        print("xX-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Xx")