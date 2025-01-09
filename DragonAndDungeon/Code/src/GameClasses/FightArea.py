from GameClasses.Characters.Player import Player
from GameClasses.Characters.Enemy import Enemy
from GameClasses.Characters.PlayerState import PlayerState
from Core.Renderer.IRender import *

class FightArea:
    def __init__(self, player, enemy):
        self.__player = player
        self.__enemy = enemy
        self.__index = 0

    def update(self, enemies):

        if self.__index % 2 == 1:
            self.__enemy.attack(self.__player)
            self.__index += 1

            if self.__player.is_alive == False:
                self.__player.player_state = PlayerState.GAME_OVER

            return

        # Try to convert the input to an int
        try:
            result = int(input())
            self.__player.attack(result, self.__enemy)
            self.__index += 1

            if self.__enemy.is_alive == False:
                self.__player.player_state = PlayerState.WALKING
                enemies.remove(self.__enemy)

            return
        # If failed to convert the input because of a wrong input, just ignore
        except ValueError:
            return

    def draw(self, renderer):
        life_bar = "████████████████████"
        life_bar_empty = "━━━━━━━━━━━━━━━━━━━━"

        # Calculates the percent of the player's life
        percent = self.__player.life / self.__player.max_life
        value = int(round(len(life_bar) * percent))

        # Creates a life bar text with the first one from 0 to the percent value
        # and with the second life bar from the percent value to the end
        final_bar = life_bar[:value] + life_bar_empty[value:]

        renderer.draw_line()
        print(" -*- Combat -*- \n")

        print(f"{self.__player.name}'s life (Level {self.__player.level}):")
        print(f"\033[32m{final_bar}\033[0m   [{int(round(percent * 100))}%]\n")

        # Same here but for the enemy's life
        percent = self.__enemy.life / self.__enemy.max_life
        value = int(round(len(life_bar) * percent))

        final_bar = life_bar[:value] + life_bar_empty[value:]

        print(f"{self.__enemy.name}'s life (Level {self.__enemy.level}):")
        print(f"\033[31m{final_bar}\033[0m   [{int(round(percent * 100))}%]")
        renderer.draw_line()




