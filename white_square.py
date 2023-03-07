import pygame

from pygame.locals import *

pygame.init()

surface = pygame.display.set_mode((800,800))
colour = (255, 255,255)

running = True

left = 350
top = 350

sustained_up = False
sustained_down = False
sustained_right = False
sustained_left = False
sustained_h = False

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
    pygame.draw.rect(surface, colour, pygame.Rect(top, left, 100, 100))
    pygame.display.flip()
    if sustained_h:
        print('Hello World!')
    if sustained_down:
        if left < 700:
            left +=0.5
    if sustained_up:
        if left > 0:
            left -=0.5
    if sustained_right:
        if top < 700:
            top +=0.5
    if sustained_left:
        if top > 0:
            top -=0.5
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                sustained_up = True
            elif event.key == K_h:
                sustained_h = True
            elif event.key == K_DOWN:
                sustained_down = True
            elif event.key == K_RIGHT:
                sustained_right = True
            elif event.key == K_LEFT:
                sustained_left = True
        elif event.type == KEYUP:
            if event.key == K_UP:
                sustained_up = False
            elif event.key == K_h:
                sustained_h = False
            elif event.key == K_DOWN:
                sustained_down = False
            elif event.key == K_RIGHT:
                sustained_right = False
            elif event.key == K_LEFT:
                sustained_left = False
        elif event.type == QUIT:
            running = False
    
