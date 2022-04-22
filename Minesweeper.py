import pygame 
import random

board = []
boardpos = []
k=6

for x in range(0,256):
    z = random.randint(0,k)
    if z == 1 or 0:
        board.append("*")
        k=3
    else:
        board.append(" ")
        k=4



def game(screen):
    screen.fill((180, 180, 180))
    n = 40
    for x in range(0,16):
        for z in range(0,16):
            boardpos.append(pygame.draw.rect(screen, (145, 145, 145), pygame.Rect(5+n*z, 75+n*x, n, n)))
    for x in range(0,17):
        for z in range(0,17):
            pygame.draw.line(screen, (40, 40, 40), (5+n*z,75+n*x), (5+n*9,75+n*x), 2)
            pygame.draw.line(screen, (40, 40, 40), (5+n*z,75+n*x), (5+n*z,75+n*9), 2)
    pygame.display.flip()
    
            

def loosegame(screen):
    screen.fill((180, 180, 180))
    n = 40
    fontgrid = pygame.font.Font('freesansbold.ttf', 40)
    p=0
    for x in range(0,16):
        for z in range(0,16):
            boardpos.append(pygame.draw.rect(screen, (145, 145, 145), pygame.Rect(5+n*z, 75+n*x, n, n)))
            k = fontgrid.render(str(board[p]), True, (164, 126, 115))   
            screen.blit(k, (20+n*z, 90+n*x))
            p+=1
    for x in range(0,17):
        for z in range(0,17):
            pygame.draw.line(screen, (40, 40, 40), (5+n*z,75+n*x), (5+n*9,75+n*x), 2)
            pygame.draw.line(screen, (40, 40, 40), (5+n*z,75+n*x), (5+n*z,75+n*9), 2)
    pygame.display.flip()


def showsquares(screen, rect):
    pygame.draw.rect(screen, (200, 200, 200), rect)
    revealem(screen,rect)
    pygame.display.flip()

def revealem(screen, rect):
    k = boardpos.index(rect)
    if board[k-1] != "*":
        a=True
        while a:
            if board[k-1] != "*":
                pygame.draw.rect(screen, (200, 200, 200), boardpos[k-1])
                k-=1
            elif k>3:
                a = False
            else:
                a=False
        k = boardpos.index(rect)
    if board[k+1]!="*":
        a=True
        while a:
            if board[k+1] != "*":
                pygame.draw.rect(screen, (200, 200, 200), boardpos[k+1])
                k+=1
            elif k>3:
                a = False
            else:
                a=False
        k = boardpos.index(rect)
    if board[k+16]!="*":
        a=True
        while a:
            if board[k+16] != "*":
                pygame.draw.rect(screen, (200, 200, 200), boardpos[k+16])
                k+=16
            elif k>3:
                a = False
            else:
                a=False
        k = boardpos.index(rect)
    if board[k-16]!="*":
        a=True
        while a:
            if board[k-16] != "*":
                pygame.draw.rect(screen, (200, 200, 200), boardpos[k-16])
                k-=16
            elif k>3:
                a = False
            else:
                a=False
        k = boardpos.index(rect)
            


    pygame.display.flip()


    



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
            for x in boardpos:
                if x.collidepoint(Lastclick):
                    if board[boardpos.index(x)]=="*":
                        loosegame(screen)
                        break
                    else:
                        showsquares(screen, x)
                        
