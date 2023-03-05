import pygame

pygame.init()

surface = pygame.display.set_mode((800,800))
colour = (255, 255,255)

while 1:
    pygame.draw.rect(surface, colour, pygame.Rect(350, 350, 100, 100))
    pygame.display.flip()