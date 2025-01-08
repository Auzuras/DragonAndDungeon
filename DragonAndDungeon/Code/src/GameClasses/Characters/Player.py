from typing import Self
from GameClasses.Characters.Character import Character
from GameClasses.Map.Grid import Grid
from GameClasses.Attack import Attack

class Player(Character):

    def __init__(self, name, x, y):
        super().__init__(name)
        self._x = x
        self._y = y
        self._inventory = {}    
        self.__xp = 0
        self.__max_xp = 100
        self._attacks = [Attack("Fists", 10)]

    def move(self, game_map):

        result = input()

        new_x = self._x
        new_y = self._y

        if result.upper() == 'W':
            new_y -= 1
        if result.upper() == 'S':
            new_y += 1
        if result.upper() == 'A':
            new_x -= 1
        if result.upper() == 'D':
            new_x += 1

        if not game_map.grid[new_y][new_x].is_occupied:
            self._x = new_x
            self._y = new_y

    @property
    def x(self):
        return self._x;

    @property
    def y(self):
        return self._y;

    def draw_move(self):
        print("W - Up")
        print("S - Down")
        print("A - Left")
        print("D - Right")

    def take_damage(self, damage_amount):
        return super().take_damage(damage_amount)

    def _death(self):
        return super().death()


    def update(self, game_map):
        self.move(game_map)
   
    def draw(self):
        self.draw_move()
        pass

    def take_item(self, item):
        pass