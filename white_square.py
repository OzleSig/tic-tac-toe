import pygame
import copy
from pygame.locals import *
pygame.init()

game_state =    [[' ',' ',' '], 
                [' ',' ',' '],
                [' ',' ',' ']]

game_state_empty =      [[' ',' ',' '], 
                        [' ',' ',' '],
                        [' ',' ',' ']]

window_size = 800
surface = pygame.display.set_mode((window_size,window_size))

margin_size = window_size*0.2
size_of_boxes = (window_size-margin_size*2)/3
position_of_box = (margin_size, margin_size)

running = True

hover_grey = (105, 105, 105)
white = (255, 255, 255)
black = (0, 0, 0)

player_1_score_int = 0
player_2_score_int = 0

x0 = position_of_box[0]
y0 = position_of_box[1]
x1 = x0+size_of_boxes
y1 = y0+size_of_boxes
x2 = x0+size_of_boxes*2
y2 = y0+size_of_boxes*2
x3 = x0+size_of_boxes*3
y3 = y0+size_of_boxes*3

def update_grid(pos,player_char):
    y = pos[0]
    x = pos[1]
    current = game_state[y][x]
    if (current==' '):
        game_state[y][x]=player_char
        return True
    return False

def check_horizontals():
    for x in range(3):
        if not ((game_state[x][0]==' ')):
            if game_state[x][0]==game_state[x][1]==game_state[x][2]:
                return True

def check_verticles():
    for x in range(3):
        if not ((game_state[0][x]==' ')):
            if game_state[0][x]==game_state[1][x]==game_state[2][x]:
                return True

def check_diagonal():
    if not game_state[1][1]== ' ':
        if (game_state[0][0]==game_state[1][1]==game_state[2][2]) or (game_state[2][0]==game_state[1][1]==game_state[0][2]):
            return True

def check_for_winner():
    if check_diagonal() or check_horizontals() or check_verticles():
        return True
    
def x_or_o(player):
    if player%2 == 0:
        player_char = 'O'
    elif player%2 == 1:
        player_char = 'X'
    return player_char

def game_text(player_1_score_int, player_2_score_int):
    font_size_header = 50
    font_size_player = round(font_size_header*.5)
    font_header = pygame.font.Font(".\PixeloidSans-JR6qo.ttf", font_size_header)
    font_players = pygame.font.Font(".\PixeloidSans-JR6qo.ttf", font_size_player)
    text_header = font_header.render('TIC TAC TOE', True, white)
    player_1 = font_players.render('Player 1', True, white)
    player_1_score = font_players.render(str(player_1_score_int), True, white)
    player_2 = font_players.render('Player 2', True, white)
    player_2_score = font_players.render(str(player_2_score_int), True, white)
    surface.blit(text_header, (250, 20))
    surface.blit(player_1, (window_size*0.05, 30))
    surface.blit(player_1_score, (window_size*0.05, 70))
    surface.blit(player_2, (window_size-margin_size, 30))
    surface.blit(player_2_score, (window_size-margin_size, 70))

def x_o_draw(game_state):
    font_size_xo = 100
    font_xo =  pygame.font.Font(".\PixeloidSans-JR6qo.ttf", font_size_xo)
    for y_index, row in enumerate(game_state):
        for x_index, item in enumerate(row):
            if not item == '_':
                xo = font_xo.render(item, True, white)
                surface.blit(xo, grid_to_list((y_index, x_index)))

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

#def check_grid_click(mouse_pos):
    

def grid_to_list(mouse_pos):
    grid_pos = (x0, y0)
    if not mouse_pos == (-1, -1):
        if mouse_pos == (0, 0):
            grid_pos = (x0, y0)
        elif mouse_pos == (0, 1):
            grid_pos = (x0, y1)
        elif mouse_pos == (0, 2):
            grid_pos = (x0, y2)
        elif mouse_pos == (1, 0):
            grid_pos = (x1, y0)
        elif mouse_pos == (1, 1):
            grid_pos = (x1, y1)
        elif mouse_pos == (1, 2):
            grid_pos = (x1, y2)
        elif mouse_pos == (2, 0):
            grid_pos = (x2, y0)
        elif mouse_pos == (2, 1):
            grid_pos = (x2, y1)
        elif mouse_pos == (2, 2):
            grid_pos = (x2, y2)
        return grid_pos

def hover_draw(grid_pos):
    if not grid_pos is None:
        hover_size = size_of_boxes*0.8
        pos_multiplier = size_of_boxes*0.1
        pygame.draw.rect(surface, hover_grey, pygame.Rect(grid_pos[0]+pos_multiplier, grid_pos[1]+pos_multiplier, hover_size, hover_size))

def game_draw():
    surface.fill(black)
    pygame.draw.line(surface, white, (x0, y1), (x3, y1), width= 5)
    pygame.draw.line(surface, white, (x1, y0), (x1, y3), width= 5)
    pygame.draw.line(surface, white, (x0, y2), (x3, y2), width= 5)
    pygame.draw.line(surface, white, (x2, y0), (x2, y3), width= 5)


def game_loop():
    global running
    player = 0 
    while running:
        game_draw()
        game_text(player_1_score_int, player_2_score_int)
        mouse_pos = pygame.mouse.get_pos()
        hover_draw(grid_to_list(check_mouse_on_grid(mouse_pos)))
        x_o_draw(game_state)
        pygame.display.flip()
        for event in pygame.event.get():
            if not check_for_winner():
                if event.type == MOUSEBUTTONDOWN:
                    update_grid(check_mouse_on_grid(mouse_pos), x_or_o(player))  
                    print(game_state)
                    player+=1
            if event.type == QUIT:
                running = False
game_loop()