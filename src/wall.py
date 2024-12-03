import pygame

class Wall(pygame.sprite.Sprite):
    """
    Walls are static obstacles that the player cannot pass through.
    """

    def __init__(self, x, y, width, height, image):
        """
        Wall with the given position, size, and image.
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y