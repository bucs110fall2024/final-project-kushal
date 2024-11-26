import pygame
from wall import Wall

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = pygame.sprite.Group()
        self.create_maze()

    def create_maze(self):
        # 26 x 21
        maze_data = [
            "XXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXX      XXXX           X",
            "XXX       XXXX     X     X",
            "XXX    X   XXXX         XX",
            "XXX        XXXXX       XXX",
            "XXX  X     XXXXXX     XXXX",
            "XXX     X       XX   XXXXX",
            "XX         XXXX XXX XXXXXX",
            "XX X  XXXXXXXXX XXX XXXXXX",
            "XX                        ",
            "XXXX    XXXXX XXXXXXXXXXXX",
            "XXXXXXXXXXXXX          XXX",
            "XXXXXXXXXXXXX           XX",
            "XXXXXXXXXXXXX XX         X",
            "XXXXXXX      XXXXXXXX    X",
            "XXXXXX       XXXXXXXX    X",
            "XXXXXX       XX     X    X",
            "X                        X",
            "XXXXXX                   X",
            "XXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXX"
        ]

        wall_image = pygame.image.load('../assets/graphics/stone.png')
        wall_image = pygame.transform.smoothscale(wall_image, (32, 32))

        for row_index, row in enumerate(maze_data):
            for col_index, cell in enumerate(row):
                x = col_index * 32
                y = row_index * 32

                if cell == 'X':
                    wall = Wall(x, y, 32, 32, wall_image)
                    self.walls.add(wall)

    def draw(self, screen):
        self.walls.draw(screen)
