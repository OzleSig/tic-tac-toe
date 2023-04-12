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

window_size = 900
surface = pygame.display.set_mode((window_size,window_size))

margin_size = window_size*0.2
size_of_boxes = (window_size-margin_size*2)/3
position_of_box = (margin_size, margin_size)

running = True

hover_grey = (105, 105, 105)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

player_O_score_int = 0
player_X_score_int = 0

x0 = position_of_box[0]
y0 = position_of_box[1]
x1 = x0+size_of_boxes
y1 = y0+size_of_boxes
x2 = x0+size_of_boxes*2
y2 = y0+size_of_boxes*2
x3 = x0+size_of_boxes*3
y3 = y0+size_of_boxes*3

pos_multiplier = size_of_boxes*0.1

def update_grid(pos,player_char):
    y = pos[0]
    x = pos[1]
    current = game_state[y][x]
    if y == -1 and x == -1:
        return False
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

def score_change(x_or_o):
    global player_O_score_int
    global player_X_score_int
    if x_or_o == 'O':
        player_O_score_int+=1
    else:
        player_X_score_int+=1


def game_text(player_O_score_int, player_X_score_int):
    font_size_header = round(window_size*0.06)
    font_size_player = round(font_size_header*.5)
    font_header = pygame.font.Font(".\PixeloidSans-JR6qo.ttf", font_size_header)
    font_players = pygame.font.Font(".\PixeloidSans-JR6qo.ttf", font_size_player)
    text_header = font_header.render('TIC TAC TOE', True, white)
    player_O = font_players.render('Player O', True, white)
    player_O_score = font_players.render(str(player_O_score_int), True, white)
    player_X = font_players.render('Player X', True, white)
    player_X_score = font_players.render(str(player_X_score_int), True, white)
    surface.blit(text_header, (window_size*0.3, window_size*0.03))
    surface.blit(player_O, (window_size*0.05, window_size*0.0375))
    surface.blit(player_O_score, (window_size*0.05, window_size*0.0875))
    surface.blit(player_X, (window_size- window_size*0.17, window_size*0.0375))
    surface.blit(player_X_score, (window_size-window_size*0.17, window_size*0.0875))

def x_o_draw(game_state):
    font_size_xo = round(window_size*0.16)
    font_xo =  pygame.font.Font(".\PixeloidSans-JR6qo.ttf", font_size_xo)
    for y_index, row in enumerate(game_state):
        for x_index, item in enumerate(row):
            if not item == '_':
                xo = font_xo.render(item, True, white)
                xy = list(grid_to_list((y_index, x_index)))
                xy[0] += size_of_boxes*0.27
                xy[1] += size_of_boxes*0.02
                surface.blit(xo, xy)
                

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

def check_mouse_YN(mouse_pos):
    play_again = True
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    if mouse_y > window_size*0.875 and mouse_y<window_size*0.9625:
        if mouse_x>window_size*0.425 and mouse_x<window_size*0.4625:
            return play_again
        elif mouse_x>window_size*0.525 and mouse_x<window_size*0.5625:
            return not play_again
            

def play_again(hover):
    if hover == True:
        colourY = red
        colourN = white
    elif hover == False:
        colourN = red
        colourY = white
    else: 
        colourY = white
        colourN = white
    play_again_font = pygame.font.Font(".\PixeloidSans-JR6qo.ttf", round(window_size*0.05))
    play_again_render = play_again_font.render('Play again?', True, white)
    play_answer_Y = play_again_font.render('Y', True, colourY)
    play_answer = play_again_font.render('/', True, white)
    play_answer_N = play_again_font.render('N', True, colourN)
    surface.blit(play_again_render, (window_size*0.35, (window_size-window_size*0.1875)))
    surface.blit(play_answer_Y, (window_size*0.425, (window_size-window_size*0.125)))
    surface.blit(play_answer, (window_size*0.475, (window_size-window_size*0.125)))
    surface.blit(play_answer_N, (window_size*0.525, (window_size-window_size*0.125)))

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

def winning_text(who_won):
    winner_font = pygame.font.Font(".\PixeloidSans-JR6qo.ttf", round(window_size*0.05))
    winner = winner_font.render('Player ' + who_won + ' wins!', True, red)
    pygame.draw.rect(surface, black, pygame.Rect(round(window_size*.1), round(window_size*.43), round(window_size*.8), round(window_size*.15)))
    surface.blit(winner, (round(window_size*.32), round(window_size*.47)))

def game_loop():
    global running
    global game_state
    global player_X_score_int
    global player_O_score_int
    player = 0 
    while running:
        game_draw()
        game_text(player_O_score_int, player_X_score_int)
        mouse_pos = pygame.mouse.get_pos()
        hover_draw(grid_to_list(check_mouse_on_grid(mouse_pos)))
        x_o_draw(game_state)
        if check_for_winner():
            winner = player+1
            winning_text(x_or_o(winner))
            play_again(check_mouse_YN(mouse_pos))
        pygame.display.flip()
        for event in pygame.event.get():
            if check_for_winner() and event.type == MOUSEBUTTONDOWN:
                if check_mouse_YN(mouse_pos):
                        game_state = copy.deepcopy(game_state_empty)
                        score_change(x_or_o(winner))
                elif check_mouse_YN(mouse_pos) == False:
                        check_mouse_YN(mouse_pos)
                        running = False
            if not check_for_winner() and event.type == MOUSEBUTTONDOWN and update_grid(check_mouse_on_grid(mouse_pos), x_or_o(player)):
                player+=1
            if event.type == QUIT:
                running = False  
game_loop()