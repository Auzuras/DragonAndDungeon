from GameClasses.Characters.PlayerState import PlayerState
from GameClasses.Characters.Player import Player
from GameClasses.Items.Item import Item

class InteractionSystem:
    def __init__(self, player, item):
        self.__player = player
        self.__item = item

    def update(self, items):
        result = input()
        
        if result == "1":
            self.__player.pick_item(self.__item)
            self.__player.gain_xp(10)

        elif result == "2":
            self.__player.use_potion(self.__item)
            self.__player.gain_xp(10)
        else:
            return

        items.remove(self.__item)
        self.__player.player_state = PlayerState.WALKING

    def draw(self):
        print(f"\033[95m    -*-     {self.__item.name}      -*-\033[0m")




