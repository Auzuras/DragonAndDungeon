from Code.src.GameClasses.Attack import Attack
from GameClasses.Characters.Character import *

class Enemy(Character):

    def __init__(self, name, x, y):
        super().__init__(name)
        self._x = x
        self._y = y
        self._attacks = [Attack("Fists", 5), Attack("Kick", 7)]

    def take_damage(self, damage_amount):
        return super().take_damage(damage_amount)

    def _death(self):
        return super()._death()

    def attack(self, player):

        if not self._is_alive:
            return

        self._attacks[0].attack(player, (self._strength // 2) * self._critical_multi)

    def update(self):
        pass

    def draw(self):
        pass

