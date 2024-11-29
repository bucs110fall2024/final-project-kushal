import pygame

class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.direction = direction
        self.speed = 32
        self.timer = 0
        self.load_images()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect(topleft=(x, y))

    def load_images(self):
        self.images = {
            'vertical_down': pygame.image.load('../assets/graphics/snake/snake_down.png').convert_alpha(),
            'vertical_up': pygame.transform.flip(pygame.image.load('../assets/graphics/snake/snake_down.png').convert_alpha(), False, True),
            'horizontal_right': pygame.image.load('../assets/graphics/snake/snake_left.png').convert_alpha(),
            'horizontal_left': pygame.transform.flip(pygame.image.load('../assets/graphics/snake/snake_left.png').convert_alpha(), True, False)
        }
        for key in self.images:
            self.images[key] = pygame.transform.smoothscale(self.images[key], (32, 32))

    def update(self, walls, bushes, diamonds):
        self.timer += 1
        if self.timer >= 60:  # Move every second
            self.timer = 0
            next_pos = self.rect.move(0, self.speed) if self.direction in ['vertical_down', 'vertical_up'] else self.rect.move(self.speed, 0)
            temp_sprite = pygame.sprite.Sprite()
            temp_sprite.rect = next_pos
            if pygame.sprite.spritecollideany(temp_sprite, walls) or pygame.sprite.spritecollideany(temp_sprite, bushes) or pygame.sprite.spritecollideany(temp_sprite, diamonds):
                self.flip_direction()
                next_pos = self.rect.move(0, self.speed) if self.direction in ['vertical_down', 'vertical_up'] else self.rect.move(self.speed, 0)
            self.rect = next_pos

    def flip_direction(self):
        if self.direction == 'vertical_down':
            self.direction = 'vertical_up'
            self.speed = -32
        elif self.direction == 'vertical_up':
            self.direction = 'vertical_down'
            self.speed = 32
        elif self.direction == 'horizontal_left':
            self.direction = 'horizontal_right'
            self.speed = -32
        elif self.direction == 'horizontal_right':
            self.direction = 'horizontal_left'
            self.speed = 32
        self.image = self.images[self.direction]