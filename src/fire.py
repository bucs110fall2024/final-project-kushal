import pygame

class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../assets/graphics/fire.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.timer = 0
        self.spread = 0

    def update(self):
        self.timer += 1
        if self.timer >= 60:  # Spread every second
            self.timer = 0
            self.spread += 1
            if self.spread == 1:
                self.image = pygame.transform.smoothscale(self.image, (64, 32))
            elif self.spread == 2:
                self.image = pygame.transform.smoothscale(self.image, (96, 32))