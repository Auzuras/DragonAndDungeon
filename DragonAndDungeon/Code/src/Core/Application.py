from Core.Renderer.IRender import *
from Core.Renderer.TerminalRender import *
import time

class Application:
    def __init__(self):
        self.terminal_render = TerminalRender()

    def update(self):
        while 1 > 0:
            print("\033c", end='')
            self.terminal_render.draw_grid()
            time.sleep(1)