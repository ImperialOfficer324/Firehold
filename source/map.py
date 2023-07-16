# Functions for creating and manipulating a map
# The map x and y positions use a coordinate grid, with (0, 0) in the middle, instead of normal graphic conventions

import pygame.image
from random import randint


class Map:
    """Main class that holds all map data."""

    def __init__(self):
        """Initialize basic map info."""
        self.start = StartTile()
        self.map_tiles = {0: {0: self.start}}  # First dictionary is x positions, second is y positions and tile objects

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

    def map_fix_connections(self, *tiles):
        """Go through each tile (half-matrix) and make sure all tile-level connections are correct."""
        # Todo: create this function

    def extend(self, current_tile, direction):
        """Tell a tile to create a new tile in a specific direction, and add it to the map."""
        new_tile = current_tile.create_new_tile(direction)
        self.map_tiles[new_tile.x_offset] = {new_tile.y_offset: new_tile}

    # def test_tile(self, tile, screen, pixel_position):
    #     """Draw a single tile."""
    #     screen.blit(tile.image, pixel_position)

    def fill_square(self, width, height, x_start, y_start):
        """Create a square of tiles based on a given size."""
        # x_start and y_start are the center of the square, middle is shifted towards positive values (north + east)
        # for conflicts (ex. with an even width and height) Todo: Make this work for even inputs
        for x in range(int(x_start-width/2), int(x_start+width/2)):
            if x not in self.map_tiles:
                self.map_tiles[x] = {}
            for y in range(int(y_start+height/2), int(y_start-height/2), -1):
                if self.get_tile(x, y):
                    continue
                self.map_tiles[x][y] = Tile(x, y)
        self.map_fix_connections()

    def display_tiles(self, screen):
        """Temporary: show all currently made tiles, connected."""
        for xpos in self.map_tiles:
            for ypos in self.map_tiles[xpos]:
                screen.blit(self.map_tiles[xpos][ypos].image, (int(500+xpos*38-19), int(400+ypos*38-19)))
                # Todo: remove constants here, temporary?
                print(f"Name: {self.map_tiles[xpos][ypos]}, X Offset: {xpos}, Y Offset: {ypos}")
                print(f"X Pixel Position: {int(500+xpos*38)}, Y Pixel Position: {int(400+ypos*38)}")


class Tile:
    """Create a single map tile that is aware of connections to other tiles."""
    last_id = -1

    def __init__(self, x_pos, y_pos, **connected):
        """Give basic tile info and awareness to other tiles."""
        # **connected takes in the direction and tile ID of each known, connected tile
        Tile.last_id += 1
        self.tile_id = Tile.last_id
        self.y_offset = y_pos   # Offset from the middle (origin), distance from (0, 0)
        self.x_offset = x_pos
        random_texture_test = randint(1, 4)

        if random_texture_test < 3:
            self.image = pygame.image.load("../map_tiles/tests/test_orange.png").convert()
        elif random_texture_test == 3:
            self.image = pygame.image.load("../map_tiles/tests/test_green.png").convert()
        else:
            self.image = pygame.image.load("../map_tiles/tests/test_pink.png").convert()
        # self.tile_surface = pygame.Surface((38, 38))
        # self.tile_surface.blit(self.image, self.tile_surface)

        # Make a set of empty connections, then fill in any known connections
        self.connections = {'north': '', 'east': '', 'south': '', 'west': ''}   # Are empty keys necessary here?
        self.connections.update(connected)

    def create_new_tile(self, direction):
        """Add a new tile to the map in the specified direction."""
        # Adding .lower() to the tile directions below could improve stability,
        # but capitalized directions should never be passed to the function in the first place
        if direction == 'north':
            new_tile = Tile(self.x_offset, self.y_offset - 1, south=self.tile_id)
        elif direction == 'east':
            new_tile = Tile(self.x_offset + 1, self.y_offset, west=self.tile_id)
        elif direction == 'south':
            new_tile = Tile(self.x_offset, self.y_offset + 1, north=self.tile_id)
        elif direction == 'west':
            new_tile = Tile(self.x_offset - 1, self.y_offset, east=self.tile_id)
        else:
            new_tile = None
            print("Direction does not exist")
        return new_tile

    def display_connections(self):
        """Display all connections that this tile has to other tiles"""
        # Todo: create this function?


class StartTile(Tile):
    """Create the starting tile for the map."""

    def __init__(self):
        """Make the starting tile a tile with specific parameters."""
        super().__init__(0, 0)


# def spiral_map(width, height, screen):
#     """Create and show the entire map."""
#     full_map = Map()
#     while len(full_map.map_tiles) < width/38 and len(full_map.map_tiles[int(width/38)] < height/38):
#         # Todo: remove constants, (and make this work)
#         increment = 1
#
#         for i in range(1, increment):
#             full_map.extend(full_map.map_tiles[0][0], "east")
#             full_map.extend(full_map.map_tiles[0][0], "north")
#         increment += 1
#
#         for i in range(1, increment):
#             full_map.extend(full_map.map_tiles[0][0], "west")
#             full_map.extend(full_map.map_tiles[0][0], "south")
#         increment += 1
#
#     # Todo: Add tiles until map is finished, in a spiral starting from the middle.
#     #  The above extensions need to not all be based on the start tile
#     full_map.display_tiles(screen)   # Use a different method: overwrite entire map, then add starting tile back?
