from Core.Renderer.IRender import *
from Core.Renderer.TerminalRender import *
from GameClasses.Game import Game
import time

class Application:
    width = 960
    height = 540
    tile_size = 30

    def __init__(self, width = 960, height = 540, tile_size = 30):
        self.renderer = TerminalRender()

        self.width_tile = width / tile_size
        self.height_tile = height / tile_size

        self.game = Game(self.renderer, self.width_tile, self.height_tile)

        Application.width = width
        Application.height = height
        Application.tile_size = 30

    def update(self):
        while True:
            print("\033[H\033[J", end="")
            self.game.draw()
            self.game.update()