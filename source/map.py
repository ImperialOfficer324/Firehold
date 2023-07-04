# Functions for the map
import pygame.image
from random import randint


class Map:
    """Main class that holds all map data."""

    def __init__(self):
        """Initialize basic map info."""
        self.start = StartTile()
        self.map_tiles = {0: {0: self.start}}  # First dictionary is x positions, second is y positions and tile names

    def extend(self, current_tile, direction):
        """Tell a tile to create a new tile in a specific direction, and add it to the map."""
        new_tile = current_tile.create_new_tile(direction)
        self.map_tiles[new_tile.x_offset] = {new_tile.y_offset: new_tile}

    def display_tiles(self, screen):
        """Show all currently made tiles, connected."""
        for xpos in self.map_tiles:
            for ypos in self.map_tiles[xpos]:
                screen.blit(self.map_tiles[xpos][ypos].image, (int(500+xpos*38-19), int(400+ypos*38-19)))   # Todo: remove constants
                print(f"Name: {self.map_tiles[xpos][ypos]}, X Offset: {xpos}, Y Offset: {ypos}")
                print(f"X Pixel Position: {int(500+xpos*38)}, Y Pixel Position: {int(400+ypos*38)}")

    # def test_tile(self, tile, screen, pixel_position):
    #     """Draw a single tile."""
    #     screen.blit(tile.image, pixel_position)

    def neighboring_tiles(self, tile_id):
        """Return the neighboring tiles and their positions"""
        # Todo: create this function

class Tile:
    """Create a single map tile that is aware of connections to other tiles."""

    def __init__(self, tile_id, x_pos, y_pos, **connected):
        """Give basic tile info and awareness to other tiles."""
        # **connected takes in the direction and tile ID of each known, connected tile
        self.tile_id = tile_id
        self.y_offset = y_pos
        self.x_offset = x_pos
        random_texture_test = randint(1, 4)
        print(random_texture_test)

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
        if direction.lower() == 'north':
            new_tile = Tile(self.tile_id + 1, self.x_offset, self.y_offset - 1, south=self.tile_id)
        elif direction.lower() == 'east':
            new_tile = Tile(self.tile_id + 1, self.x_offset + 1, self.y_offset, west=self.tile_id)
        elif direction.lower() == 'south':
            new_tile = Tile(self.tile_id + 1, self.x_offset, self.y_offset + 1, north=self.tile_id)
        elif direction.lower() == 'west':
            new_tile = Tile(self.tile_id + 1, self.x_offset - 1, self.y_offset, east=self.tile_id)
        else:
            new_tile = None
            print("Direction does not exist")
        return new_tile


class StartTile(Tile):
    """Create the starting tile for the map."""

    def __init__(self):
        """Make the starting tile a tile with specific parameters."""
        super().__init__(0, 0, 0)


def create_full_map(width, height, screen):
    """Create and show the entire map."""
    full_map = Map()
    # Todo: Add tiles until map is finished
    full_map.display_tiles(screen)
