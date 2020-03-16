# git add <file name> <file 2>
# git commit -m "comment"
# git push origin master

import pygame
import sys
import random
import math

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Tic Tac Toe')

blue = (0,150,255)
green = (0,255,0)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
crashed = False
clock = pygame.time.Clock()
game_board = pygame.image.load('tic-tac-toe-board-png-2.png')
x_image = pygame.image.load('tictactoe_x.png')
o_image = pygame.image.load('tictactoe_o.png')
p1 = True
p2 = False
player_1_wins = False
player_2_wins = False
tieGame = False
allQuadrants = [0, 0, 0, 0, 0, 0, 0, 0, 0]
quadrantLocations = [(115,46),(315,46),(505,46),(115,220),(315,220),(505,220),(115,400),(315,400),(505,400)]

def findQuadrant(xy):
    x = xy[0]
    y = xy[1]
    column = math.ceil((x - 108)/187)
    row = math.ceil((y - 40)/165)
    quadrant = (row - 1) * 3 + column
    return quadrant

def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

def message_display(text, text_x, text_y, text_size, color):
        largeText = pygame.font.Font('freesansbold.ttf',text_size)
        TextSurf, TextRect = text_objects(text, largeText, color)
        TextRect.center = (text_x, text_y)
        gameDisplay.blit(TextSurf, TextRect)

# One iter of this while loop = basically 1 frame
while not crashed:

    # On a single frame, this for goes through each event made because multiple events could have been made
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if pygame.mouse.get_pressed()[0] == 1:
            currentQuadrant = findQuadrant(pygame.mouse.get_pos())
            if allQuadrants[currentQuadrant - 1] == 0 and p1 == True:
                allQuadrants[currentQuadrant - 1] = 1
                p1 = not p1
                p2 = not p2
            elif allQuadrants[currentQuadrant - 1] == 0 and p2 == True:
                allQuadrants[currentQuadrant - 1] = 4
                p1 = not p1
                p2 = not p2
            if allQuadrants[0] + allQuadrants[1] + allQuadrants[2] == 3 or allQuadrants[3] + allQuadrants[4] + allQuadrants[5] == 3 or allQuadrants[6] + allQuadrants[7] + allQuadrants[8] == 3 or allQuadrants[0] + allQuadrants[3] + allQuadrants[6] == 3 or allQuadrants[1] + allQuadrants[4] + allQuadrants[7] == 3 or allQuadrants[2] + allQuadrants[5] + allQuadrants[8] == 3 or allQuadrants[0] + allQuadrants[4] + allQuadrants[8] == 3 or allQuadrants[2] + allQuadrants[4] + allQuadrants[6] == 3:
                player_1_wins = True
                print("player 1 wins")
            elif allQuadrants[0] + allQuadrants[1] + allQuadrants[2] == 12 or allQuadrants[3] + allQuadrants[4] + allQuadrants[5] == 12 or allQuadrants[6] + allQuadrants[7] + allQuadrants[8] == 12 or allQuadrants[0] + allQuadrants[3] + allQuadrants[6] == 12 or allQuadrants[1] + allQuadrants[4] + allQuadrants[7] == 12 or allQuadrants[2] + allQuadrants[5] + allQuadrants[8] == 12 or allQuadrants[0] + allQuadrants[4] + allQuadrants[8] == 12 or allQuadrants[2] + allQuadrants[4] + allQuadrants[6] == 12:
                player_2_wins = True
                print("player 2 wins")
            elif (allQuadrants[0] + allQuadrants[1] + allQuadrants[2] + allQuadrants[3] + allQuadrants[4] + allQuadrants[5] + allQuadrants[6] + allQuadrants[7] + allQuadrants[8]) == 21:
                tieGame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and (player_1_wins == True or player_2_wins == True or tieGame == True):
                p1 = True
                p2 = False
                player_1_wins = False
                player_2_wins = False
                tieGame = False
                allQuadrants = [0,0,0,0,0,0,0,0,0]

# If it should run every frame it should be under this

    # All drawing should be under this
    gameDisplay.fill(blue)
    gameDisplay.blit(game_board, (0, 0))
    
    i = 0
    for elem in allQuadrants:
        if elem == 1:
            gameDisplay.blit(pygame.transform.scale(x_image,(150,150)), (quadrantLocations[i]))
        if elem == 4:
            gameDisplay.blit(pygame.transform.scale(o_image,(150,150)), ((quadrantLocations[i])))
        i += 1

    if player_1_wins == True:
        gameDisplay.fill(black)
        message_display('Player 1 Wins', 400, 200, 115, red)
        message_display('To restart press R', 400, 500, 20, red)
    elif player_2_wins == True:
        gameDisplay.fill(black)
        message_display('Player 2 Wins', 400, 200, 115, red)
        message_display('To restart press R', 400, 500, 20, red)
    elif tieGame == True:
        gameDisplay.fill(black)
        message_display('Tie Game', 400, 200, 115, red)
        message_display('To restart press R', 400, 500, 20, red)

    pygame.display.update()
    clock.tick(60)