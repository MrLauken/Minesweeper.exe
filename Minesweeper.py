import pygame
from pygame.locals import *
import random

board = []
boardpos = []

for x in range(0,64):
    z = random.randint(0,6)
    if z == 2:
        board.append("*")
    else:
        board.append(" ")


def game(screen):
    screen.fill((180, 180, 180))
    n = 40
    z=0
    for x in range(0,16):
        for z in range(0,16):
            pygame.draw.rect(screen, (145, 145, 145), pygame.Rect(5+n*z, 75+n*x, n, n))
            boardpos.append((5+n*z, 75+n*x))
    for x in range(0,17):
        for z in range(0,17):
            pygame.draw.line(screen, (40, 40, 40), (5+n*z,75+n*x), (5+n*9,75+n*x), 2)
            pygame.draw.line(screen, (40, 40, 40), (5+n*z,75+n*x), (5+n*z,75+n*9), 2)
    
            





pygame.init()
screen = pygame.display.set_mode([650, 730])
pygame.display.set_caption('Minesweeper.exe')
game(screen)
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            Lastclick = event.pos
            print(Lastclick)
           """ y=0
            for x in boardpos:
                if x.collidepoint(Lastclick):
                    print(board[y])
                y+=1"""
