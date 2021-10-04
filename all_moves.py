import pygame
from constants import *
from colors import *
from board_utility import *


def draw_single_possible_square(selectedX, selectedY):
    pygame.draw.circle(SCREEN,SELECETED_COLOR,coordinate_to_center_pixel(selectedX, selectedY),15)

def draw_pawn_moves(selectedX,selectedY ):

    if all_piece_pos[selectedY][selectedX] == WHITE_PAWN:
        for i in range(1, 3):
            if (selectedY+i) < len(all_piece_pos) and all_piece_pos[selectedY+i][selectedX]  == EMPTY_PIECE:
                draw_single_possible_square(selectedX, selectedY+i)

    elif all_piece_pos[selectedY][selectedX] == BLACK_PAWN:
        for i in range(1, 3):
            if (selectedY-i) < len(all_piece_pos) and all_piece_pos[selectedY-i][selectedX]  == EMPTY_PIECE:
                draw_single_possible_square(selectedX, selectedY-i)

def draw_rook_moves(selectedX,selectedY ):
    #print(selectedX, selectedY)
    if all_piece_pos[selectedY][selectedX] == WHITE_ROOK or  all_piece_pos[selectedY][selectedX] == BLACK_ROOK:

        # bottom 
        for i in range(selectedY+1, 8):
            if all_piece_pos[i][selectedX] != EMPTY_PIECE:
                break
            if is_the_position_on_board(selectedX,i) :
                draw_single_possible_square(selectedX, i)
        # top
        for i in range(selectedY-1, -1, -1):
            if all_piece_pos[i][selectedX] != EMPTY_PIECE:
                break
            if is_the_position_on_board(selectedX, i):
                draw_single_possible_square( selectedX, i)  
        # right         
        for i in range(selectedX+1, 4):
            if all_piece_pos[selectedY][i] != EMPTY_PIECE:
                break
            if is_the_position_on_board( i, selectedY):
                draw_single_possible_square( i, selectedY)    

        # left
        for i in range(selectedX-1, -1, -1):
            if all_piece_pos[selectedY][i] != EMPTY_PIECE:
                break
            if is_the_position_on_board( i, selectedY):
                draw_single_possible_square(  i, selectedY)            

        # bishop moves ==> 
        # (1,1)=>diagonal bottom-right , (-1,-1)=>diagonal top-left,
        # (-1, 1)=>diagonal right  , (1, -1)=>diagonal right  ,
        # , (-1, 1) => diagonal top-right, (1, -1)=> diagonal bottom-left
        for d in [(1,1), (-1,-1), (1,-1), (-1, 1)]:
            newX = selectedX
            newY = selectedY
            for i in range(0, 8):
                newX = newX+d[1]
                newY = newY+d[0]
                if not is_the_position_on_board(newX, newY) or all_piece_pos[newY][newX] != EMPTY_PIECE:
                    break
                elif is_the_position_on_board(newX, newY):
                    draw_single_possible_square(newX, newY)   
                else:
                    break    

                
def draw_king_moves(selectedX,selectedY ):

    if all_piece_pos[selectedY][selectedX] == WHITE_KING or  all_piece_pos[selectedY][selectedX] == BLACK_KING:


        for d in [(1,1), (-1,-1), (1,-1), (-1, 1), (1, 0), (-1, 0), (0,1), (0,-1)]:
            newX = selectedX+d[1]
            newY = selectedY+d[0]
            if not is_the_position_on_board(newX, newY) or all_piece_pos[newY][newX] != EMPTY_PIECE:
                break
            elif is_the_position_on_board(newX, newY):
                draw_single_possible_square(newX, newY)   
            else:
                break

def draw_queen_moves(selectedX,selectedY ):
    if all_piece_pos[selectedY][selectedX] == WHITE_QUEEN or  all_piece_pos[selectedY][selectedX] == BLACK_QUEEN:

        # bottom 
        for i in range(selectedY+1, 8):
            if all_piece_pos[i][selectedX] != EMPTY_PIECE:
                break
            if is_the_position_on_board(selectedX,i) :
                draw_single_possible_square(selectedX, i)
        # top
        for i in range(selectedY-1, -1, -1):
            if all_piece_pos[i][selectedX] != EMPTY_PIECE:
                break
            if is_the_position_on_board(selectedX, i):
                draw_single_possible_square( selectedX, i)  
        # right         
        for i in range(selectedX+1, 4):
            if all_piece_pos[selectedY][i] != EMPTY_PIECE:
                break
            if is_the_position_on_board( i, selectedY):
                draw_single_possible_square( i, selectedY)    

        # left
        for i in range(selectedX-1, -1, -1):
            if all_piece_pos[selectedY][i] != EMPTY_PIECE:
                break
            if is_the_position_on_board( i, selectedY):
                draw_single_possible_square(  i, selectedY)    

        # diagonal moves        
        for d in [(1,1), (-1,-1), (1,-1), (-1, 1)]:
            newX = selectedX
            newY = selectedY
            for i in range(0, 8):
                newX = newX+d[1]
                newY = newY+d[0]
                if not is_the_position_on_board(newX, newY) or all_piece_pos[newY][newX] != EMPTY_PIECE:
                    break
                elif is_the_position_on_board(newX, newY):
                    draw_single_possible_square(newX, newY)   
                else:
                    break                  

        # knight moves 
        for d in [(-2, -1), (-2, 1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            newX = selectedX
            newY = selectedY
            for i in range(0, 8):
                newX = newX+d[1]
                newY = newY+d[0]
                if not is_the_position_on_board(newX, newY) or all_piece_pos[newY][newX] != EMPTY_PIECE:
                    break
                elif is_the_position_on_board(newX, newY):
                    draw_single_possible_square(newX, newY)   
                else:
                    break    


def select_draw_possible_moves_square(selectedX, selectedY):
    draw_pawn_moves(selectedX,selectedY )
    draw_rook_moves(selectedX,selectedY )
    draw_king_moves(selectedX,selectedY )
    draw_queen_moves(selectedX,selectedY )

    