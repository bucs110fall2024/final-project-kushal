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
player = Player(maze.start_pos[0], maze.start_pos[1], 32)

start_screen = True
end_screen = False
score = 0
font = pygame.font.Font('../assets/font/Pixeltype.ttf', 36)
diamond_image = pygame.image.load('../assets/graphics/diamond.png').convert_alpha()
text_height = font.get_height()
diamond_image = pygame.transform.smoothscale(diamond_image, (text_height, text_height))

def draw_score():
    score_text = font.render(f"Score: {score}", False, (255, 255, 255))
    screen.blit(diamond_image, (10, 10))
    screen.blit(score_text, (10 + text_height + 10, 10))

def draw_start_screen():
    start_text = font.render("Press SPACE to Play", False, (255, 255, 255))
    text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(start_text, text_rect)

def draw_end_screen():
    end_text = font.render(f"Game Over! Score: {score}", False, (255, 255, 255))
    text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(end_text, text_rect)

    restart_text = font.render("Press SPACE to Restart", False, (255, 255, 255))
    text_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_text, text_rect)

def draw_restart_message():
    restart_text = font.render("Press R to Restart", False, (255, 255, 255))
    text_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT - 30))
    screen.blit(restart_text, text_rect)

def reset_game():
    global player, score, start_screen, end_screen
    player = Player(maze.start_pos[0], maze.start_pos[1], 32)
    score = 0
    start_screen = False
    end_screen = False
    maze.reset()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (start_screen or end_screen):
                reset_game()
            elif event.key == pygame.K_r:
                reset_game()

            if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                pos = player.rect.center
                player.player_input(event.key)
                if pygame.sprite.spritecollide(player, maze.walls, dokill=False):
                    player.rect.center = pos

    screen.fill((0, 0, 0))

    if start_screen:
        draw_start_screen()
    elif end_screen:
        draw_end_screen()
    else:
        maze.draw(screen)
        player.draw(screen)

        # Update snakes and fire
        maze.update_snakes()
        maze.update_fires()

        # Check for collisions with diamonds
        if pygame.sprite.spritecollide(player, maze.diamonds, dokill=True):
            score += 1

        # Check for collisions with snakes
        if pygame.sprite.spritecollide(player, maze.snakes, dokill=False):
            end_screen = True

        # Check for collisions with fire
        if pygame.sprite.spritecollide(player, maze.fires, dokill=False):
            end_screen = True

        # Check for collisions with bushes
        if pygame.sprite.spritecollide(player, maze.bushes, dokill=True):
            pass  # Handle bush breaking logic here

        # Check if the player reaches the end point
        if player.rect.collidepoint(maze.end_pos):
            end_screen = True

        draw_score()
        draw_restart_message()

    pygame.display.update()
    clock.tick(60)