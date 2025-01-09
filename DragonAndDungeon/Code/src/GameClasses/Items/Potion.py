from enum import Enum
from GameClasses.Items.Item import Item

# Potion type Enum
class PotionType(Enum):
    HEAL_POTION = 0
    DAMAGE_POTION = 1

class Potion(Item):
    def __init__(self, name, min_value, max_value, potion_type, x = 0, y = 0):
        super().__init__(name, x, y)
        self.__min_value = min_value
        self.__max_value = max_value
        self.__potion_type = potion_type

    @property
    def min_value(self):
        return self.__min_value

    @property
    def min_value(self):
        return self.__max_value