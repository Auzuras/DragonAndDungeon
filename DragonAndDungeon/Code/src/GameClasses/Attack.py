from GameClasses.Characters.Character import Character

class Attack:
    def __init__(self, name, damages, weapon = None):
        self.__name = name
        self.__damages = damages
        self.__weapon = weapon

    def attack(self, character, additional_damages):

        # Use weapon if present
        if self.__weapon == None:
            pass

        character.take_damage(self.__damages + additional_damages)

    @property
    def name(self):
        return self.__name




