from abc import ABC, abstractmethod

class IRender(ABC):

    @abstractmethod
    def draw_grid(self):
        pass