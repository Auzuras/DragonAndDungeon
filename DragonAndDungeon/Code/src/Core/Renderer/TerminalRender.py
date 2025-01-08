from Core.Renderer.IRender import *
from GameClasses.Map.Grid import Grid
from GameClasses.Map.Tile import Tile

class TerminalRender:
    def __init__(self):
        pass

    def draw_grid(self, game_map):
        for row in game_map.grid:
            print(''.join(tile.tile_char for tile in row))

    def draw_line(self):
        print("xX-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Xx")

    def draw_ui(self):
        pass