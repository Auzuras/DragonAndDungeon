from random import randint
from tkinter import SEL
from unittest import defaultTestLoader
from GameClasses.Attack import Attack
from GameClasses.Characters.PlayerState import PlayerState
from GameClasses.Map.Grid import Grid
from GameClasses.Map.Tile import Tile
from GameClasses.Characters.Player import Player
from GameClasses.Characters.Enemy import Enemy
from GameClasses.Items.Weapon import Weapon
from GameClasses.FightArea import FightArea
from GameClasses.Items.Potion import Potion, PotionType
from GameClasses.InteractionSystem import InteractionSystem
from Core.Renderer.IRender import *
from Core.Renderer.TerminalRender import *

import json

class Game:
    # Default Game class constructor
    def __init__(self, renderer, width, height):
        self.max_enemies = 3
        self.max_items = 4
        self.curent_round = 1
        self.renderer = renderer
        self.game_map = Grid(width, height)
        self.player = Player("Player", 5, 5)
        self.__map_width = width
        self.__map_height = height
        self.enemies = []
        self.items = []
        self.__fight_area = None
        self.__interaction_system = None
        self.init_enemies()
        self.load_data()

        # first draw to have a scene before the first update
        self.draw()

    # Inits a random number of enemies for the game
    def init_enemies(self):

        with open('Assets/Enemies.json', 'r') as f:
            enemies_data = json.load(f)

        value = randint(1, self.max_enemies)

        for i in range(value):

            is_position_occupied = True

            while is_position_occupied == True:
                x_pos =  randint(1, self.__map_width - 1)
                y_pos = randint(1, self.__map_height - 1)

                is_position_occupied = self.game_map.grid[y_pos][x_pos].is_occupied
            
            enemy_type = randint(0, len(enemies_data) - 1)

            new_enemy = Enemy(enemies_data[enemy_type]["name"], x_pos, y_pos)
            new_enemy.level = enemies_data[enemy_type]["level"]
            new_enemy.strength = enemies_data[enemy_type]["strength"]
            new_enemy.resistance = enemies_data[enemy_type]["resistance"]
            new_enemy.initiative = enemies_data[enemy_type]["initiative"]
            new_enemy.critical_multi = enemies_data[enemy_type]["critical_multi"]

            self.enemies.append(new_enemy)

    def create_items(self, weapons, potions):

        value = randint(1, self.max_items)

        for i in range(value):

            is_position_occupied = True

            while is_position_occupied == True:
                x_pos =  randint(1, self.__map_width - 1)
                y_pos = randint(1, self.__map_height - 1)

                is_position_occupied = self.game_map.grid[y_pos][x_pos].is_occupied
            
            item_type = randint(1, 2)

            new_item = None

            if item_type == 1:
                potion_type = randint(0, len(potions) - 1)
                potion_data = potions[potion_type]

                if potion_data["type"] == 0:
                    new_item = Potion(potion_data["name"], potion_data["min_value"], potion_data["max_value"], PotionType.HEAL_POTION)
                else:
                    new_item = Potion(potion_data["name"], potion_data["min_value"], potion_data["max_value"], PotionType.DAMAGE_POTION)
            elif item_type == 2:
                weapon_type = randint(0, len(weapons) - 1)
                new_item = weapons[weapon_type]

            new_item.x = x_pos
            new_item.y = y_pos

            self.items.append(new_item)

    def __restart(self):
        # The game is pretty light this is why I just clear all the data and recreate it rather than reseting values
        # It is also because of the time limit
        self.game_map = None
        self.player = None
        self.game_map = Grid(self.__map_width, self.__map_height)
        self.player = Player("Player", 5, 5)
        self.enemies = []
        self.items = []
        self.__fight_area = None
        self.__interaction_system = None
        self.init_enemies()
        self.load_data()

         # first draw to have a scene before the first update
        self.draw()

    def __reload_level(self):
        self.max_enemies += 1
        self.max_items += 1
        self.curent_round += 1
        self.enemies = []
        self.items = []
        self.init_enemies()
        self.load_data()

        # first draw to have a scene before the first update
        self.draw()

    def load_data(self):
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

        with open('Assets/Potions.json', 'r') as f:
            potion_data = json.load(f)

        #####

        self.__give_enemies_weapons(all_weapons)
        if  len(self.player._weapon_inventory) <= 0:
            self.player.pick_weapon(all_weapons[randint(0, len(all_weapons) - 1)])
        self.create_items(all_weapons, potion_data)

    def __give_enemies_weapons(self, weapons):

         for enemie in self.enemies:
            value = randint(0, len(weapons) - 1)
            enemie.pick_weapon(weapons[value])

    # Starts a combat between a player and an enemy
    def __start_combat(self, player, enemy):
        index = 0
        if player.initiative < enemy.initiative:
            index = 1

        self.__fight_area = FightArea(player, enemy, index)

    # Checks collisions between a player position and an enemy position
    def check_enemy_collisions(self, player, enemies):

        if self.player.player_state == PlayerState.COMBAT or self.player.player_state == PlayerState.GAME_OVER:
            return

        for enemy in enemies:
            if enemy.x == player.x and enemy.y == player.y and enemy.is_alive == True:
                player.player_state = PlayerState.COMBAT

                self.__start_combat(player, enemy)

    def check_item_collisions(self, player, items):

        if self.player.player_state == PlayerState.COMBAT or self.player.player_state == PlayerState.GAME_OVER:
            return

        for potion in items:
            if potion.x == player.x and potion.y == player.y:
                player.player_state = PlayerState.INTERACTION
                self.__interaction_system = InteractionSystem(player, potion)

    # Update method of the game
    def update(self):

        if len(self.enemies) == 0 and len(self.items) == 0:
            self.__reload_level()

        if self.player.player_state == PlayerState.GAME_OVER:
            restart = input()
            self.__restart()

        self.player.update(self.game_map)

        if self.player.player_state == PlayerState.COMBAT:
            self.__fight_area.update(self.enemies)

        if self.player.player_state == PlayerState.INTERACTION:
            self.__interaction_system.update(self.items)

        self.check_enemy_collisions(self.player, self.enemies)
        self.check_item_collisions(self.player, self.items)
    
    # Draw method of the game
    def draw(self):

        print("\033c", end='')

        self.renderer.draw_map(self.game_map, self.player, self.enemies, self.items)

        if self.player.player_state == PlayerState.COMBAT or self.player.player_state == PlayerState.GAME_OVER:
           self.__fight_area.draw(self.renderer)

        self.renderer.draw_line()
        print(f"Current round: {self.curent_round}")
        self.player.draw(self.renderer)
        self.renderer.draw_line()

        if self.player.player_state == PlayerState.INTERACTION:
            self.__interaction_system.draw(self.renderer)