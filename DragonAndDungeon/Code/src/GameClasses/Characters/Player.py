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
        self._attacks = [Attack("Fists", 10)]
        self.__player_state = PlayerState.WALKING

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
        print(type(self.__player_state))
        self.__player_state = new_state
        print(type(self.__player_state))

    def __draw_move(self):
        print("W - Up")
        print("S - Down")
        print("A - Left")
        print("D - Right")

    def __draw_combat(self):
        for i in range(len(self._attacks)):
            print(f"{i + 1} - {self._attacks[i].name}")

    def take_damage(self, damage_amount):
        return super().take_damage(damage_amount)

    def _death(self):
        return super()._death()

    def attack(self, result, enemy):

        if not self._is_alive:
            return

        # Checks if the input is over or bellow the array size
        if result <= 0 or result >= len(self._attacks) + 1:
            return

        self._attacks[result - 1].attack(enemy, (self._strength // 2) * self._critical_multi)

    # Update method
    def update(self, game_map):

        if self.__player_state == PlayerState.WALKING:
            self.move(game_map)
   
    # Draw method
    def draw(self):
        if self.__player_state == PlayerState.WALKING:
            self.__draw_move()
        else:
            self.__draw_combat()
        pass

    def take_item(self, item):
        pass