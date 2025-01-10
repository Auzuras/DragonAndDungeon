from random import randint
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

    def attack(self, player):

        if not self._is_alive:
            return

        weapon_index = randint(0, len(self._weapon_inventory) - 1)
        attack_index = randint(0, len(self._weapon_inventory[weapon_index].attacks) - 1)

        next_weapon = self._weapon_inventory[0]
        next_attack = next_weapon.attacks[attack_index]

        dmg_value = next_attack.damages + (self._strength // 2) * self._critical_multi

        player.take_damage(dmg_value)

        next_attack.last_damages = dmg_value

        return [next_weapon, next_attack, dmg_value]

    def pick_weapon(self, weapon):
        return super().pick_weapon(weapon)

    def update(self):
        pass

    def draw(self):
        pass

