from random import randint
from GameClasses.Map.Grid import Grid
from GameClasses.Map.Tile import Tile
from GameClasses.Characters.Player import Player
from GameClasses.Characters.Enemy import Enemy
from Core.Renderer.IRender import *
from Core.Renderer.TerminalRender import *

class Game:
    # default Game class constructor
    def __init__(self, renderer, width, height):
        self.renderer = renderer
        self.game_map = Grid(width, height)
        self.player = Player("Joe", 2, 3)
        self.__map_width = width
        self.__map_height = height
        self.enemies = []
        self.init_enemies()

    # inits a random number of enemies for the game
    def init_enemies(self):
        value = randint(3, 5)

        for i in range(value):

            is_position_occupied = True

            while is_position_occupied == True:
                x_pos =  randint(1, self.__map_width - 1)
                y_pos = randint(1, self.__map_height - 1)

                is_position_occupied = self.game_map.grid[y_pos][x_pos].is_occupied

            self.enemies.append(Enemy("Bad Guy", x_pos, y_pos))

    # starts a combat between a player and an enemy
    def __start_combat(self, player, enemies):
        pass

    # checks collisions between a player position and an enemy position
    def check_enemy_collisions(self, player, enemies):

        for enemy in enemies:
            if enemy.x == player.x and enemy.y == player.y:
                self.__start_combat(player, enemy)

    # update method of the game
    def update(self):
        self.player.update(self.game_map)

        self.check_enemy_collisions(self.player, self.enemies)
    
    # draw method of the game
    def draw(self):
        self.renderer.draw_map(self.game_map, self.player, self.enemies)

        self.renderer.draw_line()
        self.player.draw()
        self.renderer.draw_line()