# Test file to run map functions

import pygame
import map as map_import

window_size = (1000, 800)
tile_size = 38

background_color = (2, 212, 252)

screen = pygame.display.set_mode((window_size[0], window_size[1]))
pygame.display.set_caption('Firehold')
screen.fill(background_color)


# This is a test that extends the map and shows it
# main_map = map_import.Map()
# main_map.extend(0, 0, 'west')
# main_map.display_tiles(screen, window_size[0], window_size[1], tile_size)
# print(main_map.map_tiles)

# This is a test that tests a single tile, old
# main_map = map_import.Map()
# main_map.extend(main_map.start, 'east')
# ### main_map.test_tile(main_map.map_tiles[1][0], screen, (30, 500))
# ### screen.blit(main_map.map_tiles[1][0].tile_surface)
#
# main_map.display_tiles(screen)

# This is a test that fills the screen with tiles
full_map = map_import.Map()
full_map.fill_square(int(window_size[0]/38)+2, int(window_size[1]/38)+1, 0, 0)
full_map.display_tiles(screen, window_size[0], window_size[1], tile_size)
pygame.display.update()

pygame.display.update()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
