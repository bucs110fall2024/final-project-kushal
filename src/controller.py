import pygame
import sys
from maze import Maze
from player import Player

class Controller:
    """
    The Controller class manages the game logic, including handling events,
    updating the game, and drawing the game elements.
    """

    def __init__(self, width, height):
        """
        Initialize the Controller with the given screen width and height.
        """
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Diamond Dash")

        self.clock = pygame.time.Clock()

        self.current_level = 1

        self.maze = Maze(width, height, self.current_level)
        self.player = Player(self.maze.start_pos[0], self.maze.start_pos[1], 32)

        self.start_screen = True
        self.end_screen = False
        self.score = 0

        self.font = pygame.font.Font('../assets/font/Pixeltype.ttf', 36)
        self.text_height = self.font.get_height()

        self.diamond_image = pygame.image.load('../assets/graphics/diamond.png').convert_alpha()
        self.diamond_image = pygame.transform.smoothscale(self.diamond_image, (self.text_height, self.text_height))

        self.point_collect_sound = pygame.mixer.Sound('../assets/sounds/point_collect.wav')

        self.logo_image = pygame.image.load('../assets/graphics/logo.png').convert_alpha()
        self.logo_image = pygame.transform.smoothscale(self.logo_image, (200, 200))

    def draw_score(self):
        """
        Draw the current score on the screen.
        """
        score_text = self.font.render(f"Score: {self.score}", False, (255, 255, 255))
        self.screen.blit(self.diamond_image, (10, 10))
        self.screen.blit(score_text, (10 + self.text_height + 10, 10))

    def draw_start_screen(self):
        """
        Draw the start screen with the game logo and instructions.
        """
        logo_rect = self.logo_image.get_rect(center=(self.width // 2, self.height // 2 - 100))
        self.screen.blit(self.logo_image, logo_rect)

        start_text = self.font.render("Press SPACE to Play", False, (255, 255, 255))
        text_rect = start_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
        self.screen.blit(start_text, text_rect)

    def draw_end_screen(self):
        """
        Draw the end screen with the final score and instructions.
        """
        if self.player.rect.collidepoint(self.maze.end_pos):
            if self.current_level < 2:
                end_text = self.font.render(f"Level {self.current_level} Complete! Score: {self.score}", False, (255, 255, 255))
                text_rect = end_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
                self.screen.blit(end_text, text_rect)

                next_level_text = self.font.render(f"Press SPACE to Move to Level {self.current_level + 1}", False, (255, 255, 255))
                text_rect = next_level_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
                self.screen.blit(next_level_text, text_rect)
            else:
                end_text = self.font.render(f"Congratulations! You've completed all levels!", False, (255, 255, 255))
                text_rect = end_text.get_rect(center=(self.width // 2, self.height // 2 - 100))
                self.screen.blit(end_text, text_rect)

                score_text = self.font.render(f"Final Score: {self.score}", False, (255, 255, 255))
                text_rect = score_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
                self.screen.blit(score_text, text_rect)

                thank_you_text = self.font.render("Thank you for playing!", False, (255, 255, 255))
                text_rect = thank_you_text.get_rect(center=(self.width // 2, self.height // 2))
                self.screen.blit(thank_you_text, text_rect)

                restart_text = self.font.render("Press SPACE to Start from Level 1", False, (255, 255, 255))
                text_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
                self.screen.blit(restart_text, text_rect)
        else:
            end_text = self.font.render(f"Game Over! Score: {self.score}", False, (255, 255, 255))
            text_rect = end_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
            self.screen.blit(end_text, text_rect)

            restart_text = self.font.render("Press SPACE to Restart", False, (255, 255, 255))
            text_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
            self.screen.blit(restart_text, text_rect)

    def draw_restart_message(self):
        """
        Draw the restart message at the bottom of the screen.
        """
        restart_text = self.font.render("Press R to Restart", False, (255, 255, 255))
        text_rect = restart_text.get_rect(center=(self.width // 2, self.height - 30))
        self.screen.blit(restart_text, text_rect)

    def reset_game(self):
        """
        Reset the game state to the initial conditions.
        """
        if self.player.rect.collidepoint(self.maze.end_pos):
            if self.current_level < 2:
                self.current_level += 1
            else:
                self.current_level = 1

        self.maze = Maze(self.width, self.height, self.current_level)
        self.player = Player(self.maze.start_pos[0], self.maze.start_pos[1], 32)

        self.score = 0

        self.start_screen = False
        self.end_screen = False

    def handle_events(self):
        """
        Handle all the events such as key presses and window close.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and (self.start_screen or self.end_screen):
                    self.reset_game()
                elif event.key == pygame.K_r:
                    self.reset_game()
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                    pos = self.player.rect.center
                    self.player.player_input(event.key)
                    if pygame.sprite.spritecollide(self.player, self.maze.walls, dokill=False):
                        self.player.rect.center = pos

    def update(self):
        """
        Update the game state and draw all elements on the screen.
        """
        self.screen.fill((0, 0, 0))
        if self.start_screen:
            self.draw_start_screen()
        elif self.end_screen:
            self.draw_end_screen()
        else:
            self.maze.draw(self.screen)
            self.player.draw(self.screen)

            self.maze.update_snakes()
            self.maze.update_fires()
            if pygame.sprite.spritecollide(self.player, self.maze.diamonds, dokill=True):
                self.score += 1
                self.point_collect_sound.play()
            if pygame.sprite.spritecollide(self.player, self.maze.snakes, dokill=False):
                self.end_screen = True
            if pygame.sprite.spritecollide(self.player, self.maze.fires, dokill=False):
                self.end_screen = True
            if pygame.sprite.spritecollide(self.player, self.maze.bushes, dokill=True):
                pass
            if self.player.rect.collidepoint(self.maze.end_pos):
                self.end_screen = True
            self.draw_score()
            self.draw_restart_message()

            
        pygame.display.update()
        self.clock.tick(60)