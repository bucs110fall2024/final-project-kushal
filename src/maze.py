import pygame
from wall import Wall
from diamond import Diamond
from snake import Snake
from fire import Fire
from bush import Bush
from maze_data import maze_data

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = pygame.sprite.Group()
        self.diamonds = pygame.sprite.Group()
        self.snakes = pygame.sprite.Group()
        self.fires = pygame.sprite.Group()
        self.bushes = pygame.sprite.Group()
        self.start_pos = None
        self.end_pos = None
        self.background_image = pygame.image.load('../assets/graphics/grass.png').convert()
        self.background_image = pygame.transform.scale(self.background_image, (width, height))
        self.create_maze()

    def create_maze(self):
        wall_image = pygame.image.load('../assets/graphics/stone.png')
        wall_image = pygame.transform.smoothscale(wall_image, (32, 32))

        for row_index, row in enumerate(maze_data):
            for col_index, cell in enumerate(row):
                x = col_index * 32
                y = row_index * 32

                if cell == 'X':
                    wall = Wall(x, y, 32, 32, wall_image)
                    self.walls.add(wall)
                elif cell == 'D':
                    diamond = Diamond(x, y)
                    self.diamonds.add(diamond)
                elif cell == 'V':
                    snake = Snake(x, y, 'vertical_down')
                    self.snakes.add(snake)
                elif cell == 'H':
                    snake = Snake(x, y, 'horizontal_left')
                    self.snakes.add(snake)
                elif cell == 'F':
                    fire = Fire(x, y, (x, y))
                    self.fires.add(fire)
                elif cell == 'B':
                    bush = Bush(x, y)
                    self.bushes.add(bush)
                elif cell == 'S':
                    self.start_pos = (x, y)
                elif cell == 'K':
                    self.end_pos = (x, y)

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        self.walls.draw(screen)
        self.diamonds.draw(screen)
        self.snakes.draw(screen)
        self.fires.draw(screen)
        self.bushes.draw(screen)

    def update_snakes(self):
        for snake in self.snakes:
            snake.update(self.walls, self.bushes, self.diamonds)

    def update_fires(self):
        for fire in self.fires:
            fire.update(self.walls, self.fires)

    def reset(self):
        self.walls.empty()
        self.diamonds.empty()
        self.snakes.empty()
        self.fires.empty()
        self.bushes.empty()
        self.create_maze()