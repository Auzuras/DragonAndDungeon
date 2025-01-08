from GameClasses.Characters.Character import Character
from GameClasses.Map.Grid import Grid

class Player(Character):

    def __init__(self, name, x, y):
        super().__init__(name)
        self.x = x
        self.y = y

    def move(self):

        result = input()

        new_x = self.x
        new_y = self.y

        if result.upper() == 'W':
            new_x += 1
        if result.upper() == 'S':
            new_x -= 1
        if result.upper() == 'A':
            new_y -= 1
        if result.upper() == 'D':
            new_y += 1

        return [new_x, new_y]

    def draw_move(self):
        print("W - Up")
        print("S - Down")
        print("A - Left")
        print("D - Right")

    def update(self, game_map):

        new_pos = self.move()
        game_map.grid[self.x][self.y].tile_char = ' '

        self.x = new_pos[0]
        self.y = new_pos[1]

        game_map.grid[self.x][self.y].tile_char = 'o'

    
   
    def draw(self):
        self.draw_move()
        pass