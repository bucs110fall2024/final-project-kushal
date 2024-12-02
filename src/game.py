import pygame
import sys
from maze import Maze
from player import Player

pygame.init()

WIDTH, HEIGHT = 832, 672
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Diamond Dash")
clock = pygame.time.Clock()

current_level = 1
maze = Maze(WIDTH, HEIGHT, current_level)
player = Player(maze.start_pos[0], maze.start_pos[1], 32)

start_screen = True
end_screen = False
score = 0
font = pygame.font.Font('../assets/font/Pixeltype.ttf', 36)
diamond_image = pygame.image.load('../assets/graphics/diamond.png').convert_alpha()
text_height = font.get_height()
diamond_image = pygame.transform.smoothscale(diamond_image, (text_height, text_height))

point_collect_sound = pygame.mixer.Sound('../assets/sounds/point_collect.wav')

logo_image = pygame.image.load('../assets/graphics/logo.png').convert_alpha()
logo_image = pygame.transform.smoothscale(logo_image, (200, 200))  

def draw_score():
    score_text = font.render(f"Score: {score}", False, (255, 255, 255))
    screen.blit(diamond_image, (10, 10))
    screen.blit(score_text, (10 + text_height + 10, 10))

def draw_start_screen():
    logo_rect = logo_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(logo_image, logo_rect)

    start_text = font.render("Press SPACE to Play", False, (255, 255, 255))
    text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(start_text, text_rect)

def draw_end_screen():
    if player.rect.collidepoint(maze.end_pos):
        if current_level < 2:
            end_text = font.render(f"Level {current_level} Complete! Score: {score}", False, (255, 255, 255))
            text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            screen.blit(end_text, text_rect)

            next_level_text = font.render(f"Press SPACE to Move to Level {current_level + 1}", False, (255, 255, 255))
            text_rect = next_level_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            screen.blit(next_level_text, text_rect)
        else:
            end_text = font.render(f"Congratulations! You've completed all levels!", False, (255, 255, 255))
            text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
            screen.blit(end_text, text_rect)

            score_text = font.render(f"Final Score: {score}", False, (255, 255, 255))
            text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            screen.blit(score_text, text_rect)

            thank_you_text = font.render("Thank you for playing!", False, (255, 255, 255))
            text_rect = thank_you_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(thank_you_text, text_rect)

            restart_text = font.render("Press SPACE to Start from Level 1", False, (255, 255, 255))
            text_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            screen.blit(restart_text, text_rect)
    else:
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
    global player, score, start_screen, end_screen, current_level, maze
    if player.rect.collidepoint(maze.end_pos):
        if current_level < 2:
            current_level += 1
        else:
            current_level = 1
    maze = Maze(WIDTH, HEIGHT, current_level)
    player = Player(maze.start_pos[0], maze.start_pos[1], 32)
    score = 0
    start_screen = False
    end_screen = False

# this is your main loop
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

        maze.update_snakes()
        maze.update_fires()

        if pygame.sprite.spritecollide(player, maze.diamonds, dokill=True):
            score += 1
            point_collect_sound.play()

        if pygame.sprite.spritecollide(player, maze.snakes, dokill=False):
            end_screen = True

        if pygame.sprite.spritecollide(player, maze.fires, dokill=False):
            end_screen = True

        if pygame.sprite.spritecollide(player, maze.bushes, dokill=True):
            pass  

        if player.rect.collidepoint(maze.end_pos):
            end_screen = True

        draw_score()
        draw_restart_message()

    pygame.display.update()
    clock.tick(60)
