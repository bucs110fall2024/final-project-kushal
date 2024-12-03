import pygame

class Diamond(pygame.sprite.Sprite):
    """
    Diamonds are collectibles that increases the player's score when collected.
    """

    def __init__(self, x, y):
        """
        Initialize the Diamond with the given position.
        """
        super().__init__()
        self.image = pygame.image.load('../assets/graphics/diamond.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))