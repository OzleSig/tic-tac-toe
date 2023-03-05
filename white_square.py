import pygame

from pygame.locals import *

pygame.init()

surface = pygame.display.set_mode((800,800))
colour = (255, 255,255)

running = True

while running:
    pygame.draw.rect(surface, colour, pygame.Rect(350, 350, 100, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_h:
                print("Hello world!")
        elif event.type == QUIT:
            running = False
