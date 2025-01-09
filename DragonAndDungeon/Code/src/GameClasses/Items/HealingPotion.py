from GameClasses.Items.Item import Item

class HealingPotion(Item):
    def __init__(self, name, heal_value, x = 0, y = 0):
        super().__init__(name, x, y)
        self.__heal_value = heal_value

    @property
    def heal_value(self):
        return self.__heal_value