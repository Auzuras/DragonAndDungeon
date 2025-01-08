from GameClasses.Map.Grid import Grid
from GameClasses.Characters.Player import Player
from Core.Renderer.IRender import *
from Core.Renderer.TerminalRender import *

class Game:
    def __init__(self, renderer, width, height):
        self.renderer = renderer
        self.game_map = Grid(width, height)
        self.player = Player("Joe", 2, 3)

    def update(self):
        self.renderer.draw_line()
        self.player.update(self.game_map)
        self.renderer.draw_line()

    def draw(self):
        self.renderer.draw_grid(self.game_map)