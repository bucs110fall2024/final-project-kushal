import pygame
import sys

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Diamond Rush")

# Load tile images
wall_tile = pygame.image.load('assets/graphics/dimond.png')
floor_tile = pygame.image.load('assets/graphics/fire.png')

# Define maze layout
maze_layout = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Tile size
tile_size = 60

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the maze
    for row in range(len(maze_layout)):
        for col in range(len(maze_layout[row])):
            if maze_layout[row][col] == 1:
                screen.blit(wall_tile, (col * tile_size, row * tile_size))
            else:
                screen.blit(floor_tile, (col * tile_size, row * tile_size))

    pygame.display.flip()

pygame.quit()
sys.exit()
