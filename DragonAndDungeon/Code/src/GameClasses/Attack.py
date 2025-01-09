class Attack:
    def __init__(self, name, damages):
        self.__name = name
        self.__damages = damages
        self.__last_damages = 0

    @property
    def name(self):
        return self.__name

    @property
    def damages(self):
        return self.__damages

    @property
    def last_damages(self):
        return self.__last_damages

    @last_damages.setter
    def last_damages(self, value):
        self.__last_damages = value