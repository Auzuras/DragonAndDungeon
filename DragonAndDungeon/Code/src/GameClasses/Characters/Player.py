from GameClasses.Characters.Character import Character
from GameClasses.Map.Grid import Grid
from GameClasses.Attack import Attack
from GameClasses.Characters.PlayerState import PlayerState

class Player(Character):

    def __init__(self, name, x, y):
        super().__init__(name)
        self._x = x
        self._y = y
        self._inventory = {}    
        self.__xp = 0
        self.__max_xp = 100
        self.__player_state = PlayerState.WALKING
        self._weapon_inventory = []

    def move(self, game_map):

        result = input()

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

    def __draw_move(self):
        print("W - Up")
        print("S - Down")
        print("A - Left")
        print("D - Right")

    def __draw_combat(self):

        for i in range(len(self._weapon_inventory)):

            print(f"{i + 1} - {self._weapon_inventory[i].name}")

            for j in range(len(self._weapon_inventory[i].attacks)):

                print(f"    {j + 1} - {self._weapon_inventory[i].attacks[j].name} | {self._weapon_inventory[i].attacks[j].damages} damages ")

    def __draw_interaction(self):
        print("1 - Pick item")
        print("2 - Use item")

    def __draw_game_over(self):
        print("\033[93m -*- Game Over -*- \033[0m")
        print("\033[93mPress any key to restart...\033[0m")


    def take_damage(self, damage_amount):
        return super().take_damage(damage_amount)

    def pick_weapon(self, weapon):
        return super().pick_weapon(weapon)

    def _death(self):
        return super()._death()

    def attack(self, weapon, attack, enemy):

        if not self._is_alive:
            return []

        if len(self._weapon_inventory) == 0:
            return []

        #Checks if the input is over or bellow the array size
        if weapon <= 0 or weapon > len(self._weapon_inventory):
            return []

        # Checks if the input is over or bellow the array size
        if attack <= 0 or attack > len(self._weapon_inventory[weapon - 1].attacks):
            return []

        next_weapon = self._weapon_inventory[weapon - 1]
        next_attack = next_weapon.attacks[attack - 1]

        dmg_value = next_attack.damages + (self._strength // 2) * self._critical_multi

        enemy.take_damage(dmg_value)

        next_attack.last_damages = dmg_value

        return [next_weapon, next_attack]

    # Update method
    def update(self, game_map):

        if self.__player_state == PlayerState.WALKING:
            self.move(game_map)
            
   
    # Draw method
    def draw(self):
        if self.__player_state == PlayerState.WALKING:
            self.__draw_move()
        elif self.__player_state == PlayerState.COMBAT:
            self.__draw_combat()
        elif self.__player_state == PlayerState.INTERACTION:
            self.__draw_interaction()
        elif self.__player_state == PlayerState.GAME_OVER:
            self.__draw_game_over()

    def take_item(self, item):
        pass