from Core.Renderer.IRender import *
from Core.Renderer.TerminalRender import TerminalRender
from GameClasses.Game import Game
import time

class Application:
    run_app = True

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
        while Application.run_app:
            self.game.update()
            self.game.draw()