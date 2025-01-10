from asyncio import WindowsProactorEventLoopPolicy
from random import randint
from GameClasses.Items.Weapon import Weapon
from GameClasses.Items.Potion import Potion, PotionType
from GameClasses.Characters.Character import Character
from GameClasses.Map.Grid import Grid
from GameClasses.Attack import Attack
from GameClasses.Characters.PlayerState import PlayerState

class Player(Character):

    def __init__(self, name, x, y):
        super().__init__(name)
        self._x = x
        self._y = y
        self._inventory = []    
        self.__xp = 0
        self.__max_xp = 100
        self.__player_state = PlayerState.WALKING
        self._weapon_inventory = []

    def move(self, result, game_map):

        new_x = self._x
        new_y = self._y

        if result.upper() == 'W':
            new_y -= 1
        if result.upper() == 'S':
            new_y += 1
        if result.upper() == 'A':
            new_x -= 1
        if result.upper() == 'D':
            new_x += 1

        if not game_map.grid[new_y][new_x].is_occupied:
            self._x = new_x
            self._y = new_y

    @property
    def player_state(self):
        return self.__player_state

    @player_state.setter
    def player_state(self, new_state):
        self.__player_state = new_state

    def __draw_infos(self):
        print("W - Up")
        print("S - Down")
        print("A - Left")
        print("D - Right")
        print(" ")
        print("Q - Quit")

    def __draw_combat(self):
        for i in range(len(self._weapon_inventory)):

            print(f"{i + 1} - {self._weapon_inventory[i].name}")

            for j in range(len(self._weapon_inventory[i].attacks)):

                print(f"    {j + 1} - {self._weapon_inventory[i].attacks[j].name} | {self._weapon_inventory[i].attacks[j].damages} damages ")

        if len(self._inventory) <= 0:
            return

        print(f"{len(self._weapon_inventory) + 1} - Inventory")

        for i in range(len(self._inventory)):
            print(f"    {i + 1} - {self._inventory[i].name}")

    def __draw_game_over(self):
        print("\033[93m -*- Game Over -*- \033[0m")
        print("\033[93mPress any key to restart...\033[0m")

    def take_damage(self, damage_amount):
        return super().take_damage(damage_amount)

    def pick_weapon(self, weapon):
        return super().pick_weapon(weapon)

    def pick_item(self, item):

        if type(item) == Weapon:
            filtered_weapons = list(filter(lambda w: w.name == item.name, self._weapon_inventory))

            if len(filtered_weapons) <= 0:
                self._weapon_inventory.append(item)
            return

        self._inventory.append(item)

    def _death(self):
        self.__player_state = PlayerState.GAME_OVER
        return super()._death()

    def attack(self, receiver, weapon = None, attack = None):

        if not self._is_alive:
            return []

        if len(self._weapon_inventory) == 0:
            return []

        if weapon < 1 and weapon > len(self._weapon_inventory) + len(self._inventory):
            return []

        # POTION case
        if weapon > len(self._weapon_inventory) and weapon <= len(self._weapon_inventory) + len(self._inventory):
            if attack >= 1 and attack <= len(self._inventory):
                use_item = self._inventory[attack - 1]

                value = self.use_potion(use_item)
                self._inventory.remove(use_item)

                return [use_item, use_item, value, True]

        #Checks if the input is over or bellow the array size
        if weapon <= 0 or weapon > len(self._weapon_inventory):
            return []

        # Checks if the input is over or bellow the array size
        if attack <= 0 or attack > len(self._weapon_inventory[weapon - 1].attacks):
            return []

        return super().attack(receiver, weapon - 1, attack - 1)

    def use_potion(self, potion):
       
        value = randint(potion.min_value, potion.max_value)

        if potion.type == PotionType.HEAL_POTION:
            self.__change_life(value)
            return value

        elif potion.type == PotionType.DAMAGE_POTION:
            self.__change_life(-value)
            return -value
    
    def __change_life(self, value):

        self._life += value

        if self._life > self._max_life:
            self._life = self._max_life

        elif self._life <= 0:
            self._life = 0
            self._death()

    def __draw_lvl_xp(self, renderer):
        xp_bar = "████████████████████"
        xp_bar_empty = "━━━━━━━━━━━━━━━━━━━━"

        percent = self.__xp / self.__max_xp
        value = int(round(len(xp_bar) * percent))

        final_bar = xp_bar[:value] + xp_bar_empty[value:]

        print(f"Level: {self._level}")
        print(f"Experience: \033[94m{final_bar}\033[0m   [{int(round(percent * 100))}%]")

    def gain_xp(self, value):
        lvl_nbr = value // self.__max_xp
        xp_nbr = value % self.__max_xp

        self.__xp += xp_nbr

        self.__add_level(lvl_nbr)

    def __level_up_random_ability(self):
        result = randint(1, 3)

        if result == 1:
            self._strength += 1
        elif result == 2:
            self._resistance += 1
        elif result == 3:
            self._initiative += 1

    def __add_level(self, level_nbr):
        self._level += level_nbr

        if level_nbr > 0:
            self.__xp = 0
            self.__level_up_random_ability()
        elif self.__xp >= self.__max_xp:
            self.__xp = 0
            self._level += 1
            self.__level_up_random_ability()

    # Update method
    def update(self, game_map):

        if self.__player_state == PlayerState.WALKING:
            result = input()

            if result.upper() == "Q":
                # not really good but import loop and no time to fix it
                import Core.Application as app
                app.Application.run_app = False

            self.move(result, game_map)     
   
    # Draw method
    def draw(self, renderer):
        self.__draw_lvl_xp(renderer)

        if not self.__player_state == PlayerState.INTERACTION:
            renderer.draw_line()

        if self.__player_state == PlayerState.WALKING:
            self.__draw_infos()
        elif self.__player_state == PlayerState.COMBAT:
            self.__draw_combat()
        elif self.__player_state == PlayerState.GAME_OVER:
            self.__draw_game_over()