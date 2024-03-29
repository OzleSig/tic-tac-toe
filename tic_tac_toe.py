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
hover_grey = (105, 105, 105)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
margin_size = window_size*0.2
size_of_boxes = (window_size-margin_size*2)/3
position_of_box = (margin_size, margin_size)
x0 = position_of_box[0]
y0 = position_of_box[1]
x1 = x0+size_of_boxes
y1 = y0+size_of_boxes
x2 = x0+size_of_boxes*2
y2 = y0+size_of_boxes*2
x3 = x0+size_of_boxes*3
y3 = y0+size_of_boxes*3
font_size_xo = round(window_size*0.16)
font_xo =  pygame.font.Font(".\PixeloidSans-JR6qo.ttf", font_size_xo)

player_O_score_int = 0
player_X_score_int = 0
running = True

def update_grid(pos, player_char):
    y = pos[0]
    x = pos[1]
    current = game_state[y][x]
    if y == -1 and x == -1:
        return False
    if (current==' '):
        game_state[y][x]=player_char
        return True
    return False

def check_verticle():
    for x in range(3):
        if not ((game_state[x][0]==' ')):
            if game_state[x][0]==game_state[x][1]==game_state[x][2]:
                return True, x

def check_horizontal():
    for x in range(3):
        if not ((game_state[0][x]==' ')):
            if game_state[0][x]==game_state[1][x]==game_state[2][x]:
                return True, x

def check_diagonal():
    if not game_state[1][1]== ' ':
        if game_state[0][0]==game_state[1][1]==game_state[2][2]: 
            return True, -1
        elif game_state[2][0]==game_state[1][1]==game_state[0][2]: 
            return True, 1

def check_for_winner():
    return check_diagonal() or check_horizontal() or check_verticle()
    
def x_or_o(player):
    if player == 'O':
        player = 'X'
    elif player == 'X':
        player = 'O'
    return player

def score_change(x_or_o):
    global player_O_score_int
    global player_X_score_int
    if x_or_o == 'O':
        player_O_score_int+=1
    else:
        player_X_score_int+=1

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
    if x == -1 or y == -1:
        y = -1        
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

def game_draw():
    surface.fill(black)
    pygame.draw.line(surface, white, (x0, y1), (x3, y1), width= 5)
    pygame.draw.line(surface, white, (x1, y0), (x1, y3), width= 5)
    pygame.draw.line(surface, white, (x0, y2), (x3, y2), width= 5)
    pygame.draw.line(surface, white, (x2, y0), (x2, y3), width= 5)

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
    colour = white
    for y_index, row in enumerate(game_state):
        if check_verticle() and check_for_winner()[1] == y_index:
            colour = red    
        else:
            colour = white
        for x_index, item in enumerate(row):
            if not check_verticle() and check_diagonal():
                    if check_diagonal()[1] == -1 and x_index == y_index:
                        colour = red
                    elif check_diagonal()[1] == 1:
                        indexes = (x_index, y_index)
                        if indexes == (1,1) or indexes == (0,2) or indexes == (2,0):
                            colour = red
                        else:
                            colour = white
                    else: 
                        colour = white
            elif check_horizontal():
                if check_for_winner()[1] == x_index:
                    colour = red
                else: 
                    colour = white
            if not item == '_':
                xo = font_xo.render(item, True, colour)
                xy = list(grid_to_list((y_index, x_index)))
                xy[0] += size_of_boxes*0.27
                xy[1] += size_of_boxes*0.02
                surface.blit(xo, xy)

def x_o_hover(mouse_pos, x_or_o):
    xo = font_xo.render(x_or_o, True, hover_grey)
    if not check_for_winner():
        if not mouse_pos is None:
            mouse_pos = list(mouse_pos)
            mouse_pos[0] += size_of_boxes*0.27
            mouse_pos[1] += size_of_boxes*0.02
            surface.blit(xo, mouse_pos)  

def game_loop():
    global running
    global game_state
    global player_X_score_int
    global player_O_score_int
    player = 'O' 
    turn = 0
    while running:
        game_draw()
        game_text(player_O_score_int, player_X_score_int)
        mouse_pos = pygame.mouse.get_pos()
        x_o_hover(grid_to_list(check_mouse_on_grid(mouse_pos)), player)
        x_o_draw(game_state)
        if check_for_winner():
            winner = x_or_o(player)
            play_again(check_mouse_YN(mouse_pos))
        pygame.display.flip()
        for event in pygame.event.get():
            if not check_for_winner() and turn == 9:
                game_state = copy.deepcopy(game_state_empty)
            if check_for_winner() and event.type == MOUSEBUTTONDOWN:
                turn = 0
                if check_mouse_YN(mouse_pos):
                    game_state = copy.deepcopy(game_state_empty)
                    score_change(winner)
                elif check_mouse_YN(mouse_pos) == False:
                        check_mouse_YN(mouse_pos)
                        running = False
            if not check_for_winner() and event.type == MOUSEBUTTONDOWN and update_grid(check_mouse_on_grid(mouse_pos), player):
                turn += 1
                player = x_or_o(player)
            if event.type == QUIT:
                running = False  
game_loop()