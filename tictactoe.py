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
p2 = True

def findQuadrant(xy):
    x = xy[0]
    y = xy[1]
    column = (x - 109)/187
    row = (y - 42)/165
    quadrant = (row - 1) * 3 + column
    return quadrant


# One iter of this while loop = basically 1 frame
while not crashed:

    # On a single frame, this for goes through each event made because multiple events could have been made
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    # If it should run every frame it should be under this
        if pygame.mouse.get_pressed()[0] == 1:
            print(pygame.mouse.get_pos())
            print(math.ceil(findQuadrant(pygame.mouse.get_pos())))

    # All drawing should be under this
    gameDisplay.fill(blue)
    gameDisplay.blit(game_board, (0, 0)) 


    pygame.display.update()
    clock.tick(60)