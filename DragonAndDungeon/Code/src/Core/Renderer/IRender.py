from abc import ABC, abstractmethod

class IRender(ABC):

    @abstractmethod
    def draw_map(self, game_map, player, enemies):
        pass