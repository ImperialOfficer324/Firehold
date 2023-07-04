# Test file to run map functions

import pygame
import map as map_import

window_size = (1000, 800)
# Test tile size: 38

        # ### Below are temperary tests for map classes and functions ###
        #
        # main_map = map_import.Map()
        # main_map.extend(main_map.start, 'west')
        # print(main_map.display_tiles())
        # print(main_map.map_tiles[-1][0].connections)
        #
        # ### End of Testing Area ###


background_color = (2, 212, 252)

screen = pygame.display.set_mode((window_size[0], window_size[1]))
pygame.display.set_caption('Firehold')
screen.fill(background_color)
pygame.display.update()
running = True

# main_map = map_import.Map()
# main_map.extend(main_map.start, 'east')
# ### main_map.test_tile(main_map.map_tiles[1][0], screen, (30, 500))
# ### screen.blit(main_map.map_tiles[1][0].tile_surface)
#
# main_map.display_tiles(screen)

map_import.create_full_map(window_size[0], window_size[1], screen)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
