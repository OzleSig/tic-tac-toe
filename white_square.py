import pygame

from pygame.locals import *

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surf = pygame.Surface((100,100))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

pygame.init()

screen = pygame.display.set_mode((800,800))

square1 = Square()

run = True

while run:
    for event in pygame.event.get():
        screen.blit(square1.surf, (350,350))
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                run = False

pygame.display.flip()