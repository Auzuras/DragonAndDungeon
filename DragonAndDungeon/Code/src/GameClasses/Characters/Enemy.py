from GameClasses.Characters.Character import *

class Enemy(Character):

    def __init__(self, name, x, y):
        super().__init__(name)
        self._x = x
        self._y = y


    @property
    def x(self):
        return self._x;

    @property
    def y(self):
        return self._y;

    def take_damage(self, damage_amount):
        return super().take_damage(damage_amount)

    def _death(self):
        return super().death()


    def update(self):
        pass

    def draw(self):
        pass

