from abc import ABC, abstractmethod
from GameClasses.Items.Weapon import Weapon

class Character(ABC):
    _name = "None"

    _life = 100
    _max_life = 100

    _level = 3

    _strength = 5
    _resistance = 2
    _initiative = 1
    _dexterity = 3

    _critical_multi = 1.2

    _is_alive = True

    _weapon_inventory = []

    _x = 0
    _y = 0

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def life(self):
        return self._life

    @property
    def max_life(self):
        return self._max_life

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        self._strength = strength

    @property
    def resistance(self):
        return self._resistance

    @resistance.setter
    def resistance(self, resistance):
        self._resistance = resistance

    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, initiative):
        self._initiative = initiative

    @property
    def dexterity(self):
        return self._dexterity

    @dexterity.setter
    def dexterity(self, dexterity):
        self._dexterity = dexterity

    @property
    def critical_multi(self):
        return self._critical_multi

    @critical_multi.setter
    def critical_multi(self, critial_multi):
        self._critical_multi = critial_multi

    @property
    def is_alive(self):
        return self._is_alive

    @property
    def x(self):
        return self._x;

    @property
    def y(self):
        return self._y;

    @abstractmethod
    def take_damage(self, damage_amount):

        if not self._is_alive:
            return

        value = damage_amount - (self._resistance // 2)

        self._life -= damage_amount

        if self._life <= 0:
            self._life = 0
            self._death()

    @abstractmethod
    def _death(self):
        self._is_alive = False

    @abstractmethod
    def pick_weapon(self, weapon):
        self._weapon_inventory.append(weapon)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass