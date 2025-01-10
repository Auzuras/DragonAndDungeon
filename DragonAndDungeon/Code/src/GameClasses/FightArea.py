from re import S
from GameClasses.Characters.Player import Player
from GameClasses.Characters.Enemy import Enemy
from GameClasses.Characters.PlayerState import PlayerState
from Core.Renderer.IRender import *

class FightArea:
    def __init__(self, player, enemy, index):
        self.__player = player
        self.__enemy = enemy
        self.__index = index
        self.__combat_log = []

    def update(self, enemies):

        # Array that will return the data of the attack, indexes:
        # 0 - Weapon
        # 1 - Attack
        # 2 - Damages
        # 3 - bool is attack use item

        attack_infos = []

        if self.__index % 2 == 1:
            attack_infos = self.__enemy.attack(self.__player)
            self.__index += 1

            text = f"\033[0;37m<\033[0m \033[31m{self.__enemy.name}\033[0m attacks \033[32m{self.__player.name}\033[0m with {attack_infos[0].name} using {attack_infos[1].name} ({attack_infos[2]}pv)"
            self.__combat_log.append(text)

            if self.__player.is_alive == False:
                self.__player.player_state = PlayerState.GAME_OVER

            return

        # Try to convert the input to an int
        try:
            p_weapon = int(input())
            p_attack = int(input())

            attack_infos = self.__player.attack(self.__enemy, p_weapon, p_attack)

            if len(attack_infos) <= 0:
                return

            self.__index += 1

            if self.__enemy.is_alive == False:
                self.__player.player_state = PlayerState.WALKING
                enemies.remove(self.__enemy)

            text = ""

            if attack_infos[3] == True:
                text = f"\033[1;30m>\033[0m \033[32m{self.__player.name}\033[0m uses {attack_infos[0].name} ({attack_infos[2]}pv)"
            else:
                text = f"\033[1;30m>\033[0m \033[32m{self.__player.name}\033[0m attacks \033[31m{self.__enemy.name}\033[0m with {attack_infos[0].name} using {attack_infos[1].name} ({attack_infos[2]}pv)"
            
            self.__player.gain_xp(15)

            self.__combat_log.append(text)

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

        for log in self.__combat_log:
            print(log)




