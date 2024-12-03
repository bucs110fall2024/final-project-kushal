import pygame
from controller import Controller

pygame.init()

WIDTH, HEIGHT = 832, 672
controller = Controller(WIDTH, HEIGHT)

# this is the main loop
while True:
    controller.handle_events()
    controller.update()