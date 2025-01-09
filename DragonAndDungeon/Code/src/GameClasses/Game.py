from random import randint
from unittest import defaultTestLoader
from Code.src.GameClasses.Attack import Attack
from GameClasses.Characters.PlayerState import PlayerState
from GameClasses.Map.Grid import Grid
from GameClasses.Map.Tile import Tile
from GameClasses.Characters.Player import Player
from GameClasses.Characters.Enemy import Enemy
from GameClasses.Items.Weapon import Weapon
from GameClasses.FightArea import FightArea
from Core.Renderer.IRender import *
from Core.Renderer.TerminalRender import *

import json

class Game:
    # Default Game class constructor
    def __init__(self, renderer, width, height):
        self.renderer = renderer
        self.game_map = Grid(width, height)
        self.player = Player("Player", 5, 5)
        self.__map_width = width
        self.__map_height = height
        self.enemies = []
        self.__fight_area = None
        self.init_enemies()
        self.load_weapons()

    # Inits a random number of enemies for the game
    def init_enemies(self):

        with open('Assets/Enemies.json', 'r') as f:
            enemies_data = json.load(f)

        value = randint(3, 5)

        for i in range(value):

            is_position_occupied = True

            while is_position_occupied == True:
                x_pos =  randint(1, self.__map_width - 1)
                y_pos = randint(1, self.__map_height - 1)

                is_position_occupied = self.game_map.grid[y_pos][x_pos].is_occupied
            
            value = randint(0, len(enemies_data) - 1)

            new_enemy = Enemy(enemies_data[value]["name"], x_pos, y_pos)
            new_enemy.level = enemies_data[value]["level"]
            new_enemy.strength = enemies_data[value]["strength"]
            new_enemy.resistance = enemies_data[value]["resistance"]
            new_enemy.initiative = enemies_data[value]["initiative"]
            new_enemy.dexterity = enemies_data[value]["dexterity"]
            new_enemy.critical_multi = enemies_data[value]["critical_multi"]

            self.enemies.append(new_enemy)

    def load_weapons(self):
        with open('Assets/Weapons.json', 'r') as f:
            weapons_data = json.load(f)

        all_weapons = []

        for data in weapons_data:

            new_weapon = Weapon(data["name"])
            weapon_attacks = []
            new_weapon.attacks = weapon_attacks

            for attack in data["attacks"]:
                weapon_attacks.append(Attack(attack["name"], attack["damages"]))

            all_weapons.append(new_weapon)

        for enemie in self.enemies:
            value = randint(0, len(weapons_data) - 1)
            enemie.pick_weapon(all_weapons[value])

        self.player.pick_weapon(all_weapons[4])


    # Starts a combat between a player and an enemy
    def __start_combat(self, player, enemy):
        self.__fight_area = FightArea(player, enemy)

    # Checks collisions between a player position and an enemy position
    def check_enemy_collisions(self, player, enemies):

        if self.player.player_state == PlayerState.COMBAT:
            return

        for enemy in enemies:
            if enemy.x == player.x and enemy.y == player.y and enemy.is_alive == True:
                player.player_state = PlayerState.COMBAT
                self.__start_combat(player, enemy)

    # Update method of the game
    def update(self):
        self.player.update(self.game_map)

        if self.player.player_state == PlayerState.COMBAT:
            self.__fight_area.update(self.enemies)

        self.check_enemy_collisions(self.player, self.enemies)
    
    # Draw method of the game
    def draw(self):
        print("\033[H\033[J", end="")

        self.renderer.draw_map(self.game_map, self.player, self.enemies)

        if self.player.player_state == PlayerState.COMBAT:
           self.__fight_area.draw(self.renderer)

        self.renderer.draw_line()
        self.player.draw()
        self.renderer.draw_line()