import pygame
from pygame.locals import * # store value to pygame locals
import sys
from colors import *
from board import Board
from constants import *
from board_utility import *
from piece import *
from all_moves import *

pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

pygame.display.set_caption("Chess AI")


chess_board = Board(SCREEN )

all_pieces = pygame.sprite.Group()

# place all the pieces on board
for i in range(0,len(all_piece_pos)):
    for j in range(0,len(all_piece_pos[i])):
        # i is index towards x-axis , whereas j is index towards y-axis
        if isPiece(all_piece_pos[i][j]):
            image_path = 'images/'+all_piece_pos[i][j]+'.png'
            temp_piece = Piece(image_path)
            #print(i,j)
            temp_piece.set_center(coordinate_to_center_pixel(j,i))
            all_pieces.add(temp_piece)
chess_board.draw()


def select_draw_piece_square(selectedX, selectedY):
    s = pygame.Surface((TILE_WIDTH,TILE_HEIGHT))  
    s.set_alpha(128)                
    s.fill(SELECETED_COLOR)          
    SCREEN.blit(s, (selectedX*TILE_WIDTH,selectedY*TILE_HEIGHT))  


selectedX, selectedY = -1,-1


isAlreadySelect = False

while True:
    # codes here
    
    pygame.display.update()
    chess_board.draw()
    
    all_pieces.draw(SCREEN)
    

    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # print("Clcikecd:    ", str(pygame.mouse.get_pos()))
            
            
            if isAlreadySelect:
                selectedX, selectedY = -1,-1
                isAlreadySelect = not isAlreadySelect
            else:
                selectedX, selectedY = pixel_to_coordinate(*pygame.mouse.get_pos())


    if selectedX != -1 and selectedY != -1 and all_piece_pos[selectedY][selectedX] != EMPTY_PIECE:
        select_draw_piece_square(selectedX, selectedY)
        select_draw_possible_moves_square(selectedX, selectedY)
        isAlreadySelect = not isAlreadySelect

    

    FramePerSec.tick(FPS)


