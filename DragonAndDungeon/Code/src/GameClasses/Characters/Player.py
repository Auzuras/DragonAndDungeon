from GameClasses.Characters.Character import Character
from GameClasses.Map.Grid import Grid

class Player(Character):

    def __init__(self, name, x, y):
        super().__init__(name)
        self.x = x
        self.y = y

    def move(self):
        print("W - Up")
        print("S - Down")
        print("A - Left")
        print("D - Right")
        print("\n")
        result = input()

        if result.upper() == 'W':
            self.y += 1
        if result.upper() == 'S':
            self.y -= 1
        if result.upper() == 'A':
            self.x -= 1
        if result.upper() == 'D':
            self.x += 1

    def update(self, game_map):
        self.move()
        game_map.grid[self.x][self.y].tile_char = 'o'
    
    def draw(self):
        pass