import pygame
from pygame.locals import *
pygame.init()

surface = pygame.display.set_mode((800,800))
colour = (169, 169, 169)
running = True
size_of_boxes = 200
position_of_box = (100,100)
x0 = position_of_box[0]
y0 = position_of_box[1]
x1 = x0+size_of_boxes
y1 = y0+size_of_boxes
x2 = x0+size_of_boxes*2
y2 = y0+size_of_boxes*2
x3 = x0+size_of_boxes*3
y3 = y0+size_of_boxes*3

def check_mouse_on_grid(mouse_pos):
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    x = -1
    y = -1
    if mouse_x > x0:
        if mouse_x < x1:
            x = 0
        elif mouse_x < x2:
            x = 1
        elif mouse_x < x3:
            x = 2
    if mouse_y > y0:
        if mouse_y < y1:
            y = 0
        elif mouse_y < y2:
            y = 1
        elif mouse_y < y3:
            y = 2
#mouse is never (-1, y) or (x, -1)
    if x == -1:
        y = -1
    elif y == -1:
        x = -1
    return x,y

def draw_hover(mouse_pos):
    hover_size = size_of_boxes*0.8
    hover_pos = (x0, y0)
    pos_multiplier = size_of_boxes*0.1
    if not mouse_pos == (-1, -1):
        if mouse_pos == (0, 0):
            hover_pos = (x0, y0)
        elif mouse_pos == (0, 1):
            hover_pos = (x0, y1)
        elif mouse_pos == (0, 2):
            hover_pos = (x0, y2)
        elif mouse_pos == (1, 0):
            hover_pos = (x1, y0)
        elif mouse_pos == (1, 1):
            hover_pos = (x1, y1)
        elif mouse_pos == (1, 2):
            hover_pos = (x1, y2)
        elif mouse_pos == (2, 0):
            hover_pos = (x2, y0)
        elif mouse_pos == (2, 1):
            hover_pos = (x2, y1)
        elif mouse_pos == (2, 2):
            hover_pos = (x2, y2)
        pygame.draw.rect(surface, colour, pygame.Rect(hover_pos[0]+pos_multiplier, hover_pos[1]+pos_multiplier, hover_size, hover_size))

def game_draw():
    global running
    while running:
        surface.fill((0, 0, 0))
        pygame.draw.line(surface, colour, (x0, y1), (x3, y1), width= 5)
        pygame.draw.line(surface, colour, (x1, y0), (x1, y3), width= 5)
        pygame.draw.line(surface, colour, (x0, y2), (x3, y2), width= 5)
        pygame.draw.line(surface, colour, (x2, y0), (x2, y3), width= 5)
        mouse_pos = pygame.mouse.get_pos()
        draw_hover(check_mouse_on_grid(mouse_pos))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
game_draw()
