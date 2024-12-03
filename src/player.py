import pygame

class Player(pygame.sprite.Sprite):
    """
    This class manages the player's movement and interactions within the game.
    """

    def __init__(self, x, y, speed):
        """
        Player with the given position and speed.
        """
        super().__init__()
        player_image = pygame.image.load('../assets/graphics/Player/player_walk_1.png').convert_alpha()
        player_image = pygame.transform.smoothscale(player_image, (32, 32))

        self.image = player_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.game_active = False

    def player_input(self, dir):
        """
        Handle player input for movement.
        """
        if dir == pygame.K_RIGHT:
            self.rect.x += self.speed
            self.moving = True
        elif dir == pygame.K_LEFT:
            self.rect.x -= self.speed
            self.moving = True
        elif dir == pygame.K_UP:
            self.rect.y -= self.speed
            self.moving = True
        elif dir == pygame.K_DOWN:
            self.rect.y += self.speed
            self.moving = True

    def update(self):
        """
        Update the player's state based on input.
        """
        self.player_input()
        keys = pygame.key.get_pressed()
        if not any(keys):
            self.moving = False

    def draw(self, screen):
        """
        Draw the player on the screen.
        """
        screen.blit(self.image, self.rect)