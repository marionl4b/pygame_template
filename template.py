# pygame template - a new skeleton for pygame projects
# !/usr/bin/env python3
# coding: utf-8

import pygame

# Constants
WIDTH = 360
HEIGHT = 480
FPS = 30

# Rainbow colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (105, 60, 132)
BLUE = (55, 169, 204)
GREEN = (89, 188, 106)
YELLOW = (255, 223, 0)
ORANGE = (245, 130, 51)
RED = (198, 29, 38)

# Pygame and window init
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mon Jeux à moi")
clock = pygame.time.Clock()

# Event loop
running = True
while running:
    clock.tick(FPS)
    # Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Logic
    # Render
    screen.fill(BLACK)
    pygame.display.flip()

pygame.quit()
