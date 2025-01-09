from enum import Enum

class PlayerState(Enum):
    MENU = 0
    WALKING = 1
    COMBAT = 2
    INTERACTION = 3
    GAME_OVER = 4