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
        
        tableau = []
        for y in range(int(height)):
            ligne = []
            for x in range(int(height)):
                tile = Tile(x, y)
                if y == 0 or y == height - 1:
                    tile.tile_char = '='
                    tile.is_occupied = True
                if x == 0 or x == height - 1:
                    tile.tile_char = '|'
                    tile.is_occupied = True
                ligne.append(tile)
            tableau.append(ligne)
        
        self.grid = tableau