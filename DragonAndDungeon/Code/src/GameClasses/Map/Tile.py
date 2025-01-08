class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tile_char = ' '
        self.is_occupied = False

    def __str__(self):
        return self.tile_char