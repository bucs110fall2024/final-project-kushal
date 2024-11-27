import pygame

class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, initial_pos):
        super().__init__()
        self.image = pygame.image.load('../assets/graphics/fire.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.initial_pos = initial_pos
        self.timer = 0
        self.spread_timer = 0
        self.spreading = True

    def update(self, walls, fire_group):
        self.timer += 1
        if self.timer >= 60:  # Spread every second
            self.timer = 0
            if self.spreading:
                next_pos = self.rect.move(32, 0)
                temp_sprite = pygame.sprite.Sprite()
                temp_sprite.rect = next_pos
                if pygame.sprite.spritecollideany(temp_sprite, walls):
                    self.spreading = False
                    self.spread_timer = 60  # Wait for 1 second before restarting the cycle
                    fire_group.empty()  # Remove all fires
                    fire_group.add(Fire(self.initial_pos[0], self.initial_pos[1], self.initial_pos))  # Restart the cycle with the original fire
                else:
                    new_fire = Fire(next_pos.x, next_pos.y, self.initial_pos)
                    fire_group.add(new_fire)
            else:
                self.spread_timer -= 1
                if self.spread_timer <= 0:
                    self.spreading = True
                    self.spread_timer = 0