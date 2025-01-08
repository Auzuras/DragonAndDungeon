import copy

from Core.Renderer.IRender import *
from GameClasses.Map.Grid import Grid
from GameClasses.Map.Tile import Tile
from GameClasses.Characters.Player import Player
from GameClasses.Characters.Enemy import Enemy

class TerminalRender:
    def __init__(self):
        pass

    def draw_map(self, game_map, player, enemies):

        # creates a copy to draw the map to avoid chaging the data of the map directly
        temp_map = copy.deepcopy(game_map.grid)

        for enemy in enemies:
            temp_map[enemy.y][enemy.x] = '&'

        temp_map[player.y][player.x] = 'o'

        # draws full map
        for row in temp_map:
            print(''.join(map(str, row)))


    def draw_line(self):
        print("xX-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Xx")

    def draw_ui(self):
        pass