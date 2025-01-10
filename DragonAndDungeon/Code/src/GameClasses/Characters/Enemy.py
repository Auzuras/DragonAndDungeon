from random import randint
from types import ClassMethodDescriptorType
from GameClasses.Attack import Attack
from GameClasses.Characters.Character import *

class Enemy(Character):

    def __init__(self, name, x, y):
        super().__init__(name)
        self._x = x
        self._y = y
        self._weapon_inventory = []

    def take_damage(self, damage_amount):
        return super().take_damage(damage_amount)

    def _death(self):
        return super()._death()

    def attack(self, receiver, weapon = None, attack = None):

        if not self._is_alive:
            return

        weapon_index = randint(0, len(self._weapon_inventory) - 1)
        attack_index = randint(0, len(self._weapon_inventory[weapon_index].attacks) - 1)

        return super().attack(receiver, weapon_index, attack_index)

    def pick_weapon(self, weapon):
        return super().pick_weapon(weapon)

    def update(self):
        pass

    def draw(self):
        pass

