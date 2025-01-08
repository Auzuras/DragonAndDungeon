from GameClasses.Map.Tile import Tile

class Grid:
    def __init__(self, width, height):
        self.grid = [[]]
        self.width_tile = width
        self.height_tile = height
        self.create_grid(self.width_tile, self.height_tile)

    def create_grid(self, width, height):

        if height < 2 or width < 2:
            raise ValueError("Width or Height of the map are under 2")
        
        array = []
        for y in range(int(height)):
            row = []
            for x in range(int(width)):
                tile = Tile(x, y)
                if y == 0 or y == height - 1:
                    tile.tile_char = '='
                    tile.is_occupied = True
                if x == 0 or x == width - 1:
                    tile.tile_char = '|'
                    tile.is_occupied = True
                row.append(tile)
            array.append(row)
        
        self.grid = array