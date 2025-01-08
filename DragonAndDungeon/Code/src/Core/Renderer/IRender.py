from abc import ABC, abstractmethod

class IRender(ABC):

    @abstractmethod
    def draw_grid(self, game_map):
        pass

    @abstractmethod
    def draw_ui(self):
        pass