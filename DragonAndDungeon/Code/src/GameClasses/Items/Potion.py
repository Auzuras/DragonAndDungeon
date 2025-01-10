from enum import Enum
from GameClasses.Items.Item import Item

# Potion type Enum
class PotionType(Enum):
    HEAL_POTION = 0
    DAMAGE_POTION = 1

class Potion(Item):
    def __init__(self, name, min_value, max_value, potion_type, x = 0, y = 0):
        self.__min_value = min_value
        self.__max_value = max_value
        self.__potion_type = potion_type
        super().__init__(name, x, y)

    @property
    def min_value(self):
        return self.__min_value

    @property
    def max_value(self):
        return self.__max_value

    @property
    def type(self):
        return self.__potion_type