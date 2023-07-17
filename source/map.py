# Functions for creating and manipulating a map
# The map x and y positions use a coordinate grid, with (0, 0) in the middle, instead of normal graphic conventions

import pygame.image
from random import randint


class Map:
    """Main class that holds all map data."""

    def __init__(self):
        """Initialize basic map info."""
        self.start = StartTile()   # First dictionary is x positions, second is y positions and tile objects
        self.map_tiles = {0: {0: self.start}}

    def max_x_size(self):
        return len(self.map_tiles)

    def max_y_size(self):
        y_size = 0
        for x in self.map_tiles:
            if len(self.map_tiles[x]) > y_size:
                y_size = len(self.map_tiles[x])
        return y_size

    def get_tile(self, x, y):
        if x in self.map_tiles:
            if y in self.map_tiles[x]:
                return self.map_tiles[x][y]
        return None

    def neighboring_tiles(self, x, y):
        """Return the neighboring tiles and their positions."""
        neighbors = {"north": self.get_tile(x, y + 1), "east": self.get_tile(x + 1, y),
                     "south": self.get_tile(x, y - 1), "west": self.get_tile(x - 1, y)}
        return neighbors

    def create_new_tile(self, x, y):
        """Add a new tile to the map in the specified position."""
        if x not in self.map_tiles:
            self.map_tiles[x] = {}
        self.map_tiles[x][y] = Tile(x, y)

    def extend(self, x, y, direction):
        """Create a new adjacent tile in a specific direction, and add it to the map."""
        x_offset = 0
        y_offset = 0
        if direction == "north":
            y_offset = 1
        elif direction == "east":
            x_offset = 1
        elif direction == "south":
            y_offset = -1
        elif direction == "west":
            x_offset = -1
        self.create_new_tile(x+x_offset, y+y_offset)

    def fill_square(self, width, height, x_start, y_start):
        """Create a square of tiles based on a given size."""
        # x_start and y_start are the center of the square, middle is shifted towards positive values (north + east)
        # for conflicts (ex. with an even width and height) # Todo: Change algorithm to work nicely for even inputs?
        for x in range(int(x_start-width/2), int(x_start+width/2)):
            if x not in self.map_tiles:
                self.map_tiles[x] = {}
            for y in range(int(y_start+height/2), int(y_start-height/2), -1):
                if self.get_tile(x, y):
                    continue
                self.create_new_tile(x, y)

    def display_tiles(self, screen, scrn_width, scrn_height, tile_size):
        """Temporary: show all currently made tiles, connected."""
        for x_pos in self.map_tiles:
            for y_pos in self.map_tiles[x_pos]:
                screen.blit(self.map_tiles[x_pos][y_pos].image, (int(scrn_width/2 + x_pos*tile_size-tile_size/2),
                                                                 int(scrn_height/2 + y_pos*tile_size-tile_size/2)))

                print(f"Name: {self.map_tiles[x_pos][y_pos]}, X Offset: {x_pos}, Y Offset: {y_pos}")
                print(f"X Pixel Position: {int(scrn_width/2 + x_pos*tile_size)},"
                      f" Y Pixel Position: {int(scrn_height/2 + y_pos*tile_size)}")


class Tile:
    """Create a generated single map tile."""
    last_id = -1

    def __init__(self, x_pos, y_pos):
        """Give basic tile info and texture."""
        Tile.last_id += 1
        self.tile_id = Tile.last_id
        self.y_offset = y_pos   # Offset from the middle (origin), distance from (0, 0)
        self.x_offset = x_pos
        random_texture_test = randint(1, 4)   # This can be expanded to be more complex

        if random_texture_test < 3:
            self.image = pygame.image.load("../map_tiles/tests/test_orange.png").convert()
        elif random_texture_test == 3:
            self.image = pygame.image.load("../map_tiles/tests/test_green.png").convert()
        else:
            self.image = pygame.image.load("../map_tiles/tests/test_pink.png").convert()


class StartTile(Tile):
    """Create the starting tile for the map."""

    def __init__(self):
        """Make the starting tile a tile with specific parameters."""
        super().__init__(0, 0)
