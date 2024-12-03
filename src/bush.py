import pygame

class Bush(pygame.sprite.Sprite):
    """
    Bushes are static obstacles that the player can pass through without any issues.
    """

    def __init__(self, x, y):
        """
        Initialize the Bush with the given position.
        """
        super().__init__()
        self.image = pygame.image.load('../assets/graphics/bush.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))