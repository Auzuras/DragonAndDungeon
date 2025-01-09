from GameClasses.Items.Item import *
from GameClasses.Attack import *

class Weapon(Item):
    def __init_(self, name, x = 0, y = 0):
        super().__init__(name, x, y)
        self.__attacks = []
        self.__damage_multi = 1

    @property
    def attacks(self):
        return self.__attacks

    @attacks.setter
    def attacks(self, attacks):
        self.__attacks = attacks

    @property
    def damage_multi(self):
        return self.__damage_multi;

    @damage_multi.setter
    def damage_multi(self, new_value):
        self.__damage_multi = new_value