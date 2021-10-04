import pygame
from pygame.locals import * # store value to pygame locals
import sys
from colors import *
from board import Board
from constants import *
from board_utility import *

pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()


SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Chess AI")


chess_board = Board(SCREEN )

all_pieces = pygame.sprite.Group()

for()



while True:
    # codes here
    
    
    pygame.display.update()

    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            print("Clcikecd:    ", str(pygame.mouse.get_pos()))
            print(pixel_to_coordinate(*pygame.mouse.get_pos()))    
    #pygame.display.flip()
    FramePerSec.tick(FPS)