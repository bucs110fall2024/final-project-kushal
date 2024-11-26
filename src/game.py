import pygame
import sys
from maze import Maze
from player import Player

pygame.init()

WIDTH, HEIGHT = 832, 672
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Diamond Rush")
clock = pygame.time.Clock()

maze = Maze(WIDTH, HEIGHT)
player = Player(128, 64, 32)

start_screen = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start_screen:
                start_screen = False

            if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                pos = player.rect.center
                player.player_input(event.key)
                if pygame.sprite.spritecollide(player, maze.walls, dokill=False):
                     player.rect.center = pos

    screen.fill((0, 0, 0))

    if start_screen:
        font = pygame.font.Font('../assets/font/Pixeltype.ttf',50)
        text = font.render("Press SPACE to start", False, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
    else:
        maze.draw(screen)
        player.draw(screen)


    pygame.display.update()
    clock.tick(60)
