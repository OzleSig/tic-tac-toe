import pygame

from pygame.locals import *

pygame.init()

surface = pygame.display.set_mode((800,800))
colour = (255, 255,255)

running = True

size_of_boxes = 200
position = (100,100)
x = position[0]
y = position[1]

while running:
    surface.fill((0, 0, 0))
    pygame.draw.line(surface, colour, (x, y+size_of_boxes), (x+size_of_boxes*3, y+size_of_boxes), width= 5)
    pygame.draw.line(surface, colour, (x+size_of_boxes, y), (x+size_of_boxes, y+size_of_boxes*3), width= 5)
    pygame.draw.line(surface, colour, (x, y+size_of_boxes*2), (x+size_of_boxes*3, y+size_of_boxes*2), width= 5)
    pygame.draw.line(surface, colour, (x+size_of_boxes*2, y), (x+size_of_boxes*2, y+size_of_boxes*3), width= 5)
    pygame.display.flip()
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
