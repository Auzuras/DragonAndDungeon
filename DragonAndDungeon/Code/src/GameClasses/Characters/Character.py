from abc import ABC, abstractmethod

class Character(ABC):
    _name = "None"

    _life = 100
    _max_life = 100

    _xp = 0
    _max_xp = 100

    _level = 1

    _strength = 1
    _resistance = 1
    _initiative = 1
    _dexterity = 1

    _critical_multi = 1.1

    _weapon_inventory = {}

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def take_damage(self, damage_amount):
        _life -= damage_amount

        if _life <= 0:
            _life = 0
            self.death()

    @abstractmethod
    def _death(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass