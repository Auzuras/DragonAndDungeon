from abc import ABC, abstractmethod

class Item(ABC):
    __x = 0
    __y = 0
    __name = None

    def __init__(self, name, x = 0, y = 0):
        self.__name = name
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x;

    @property
    def y(self):
        return self.__y;

    @property
    def name(self):
        return self.__name




