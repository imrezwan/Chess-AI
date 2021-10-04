from colors import SELECETED_COLOR
from constants import *

def pixel_to_coordinate( pixel_x, pixel_y):
    pos_x = int(pixel_x/TILE_WIDTH)
    pos_y = int(pixel_y/TILE_HEIGHT)
    return (pos_x, pos_y)

def coordinate_to_top_left_pixel(pos_x, pos_y):
    pixel_x = pos_x * TILE_WIDTH
    pixel_y = pos_y * TILE_HEIGHT
    return (pixel_x, pixel_y) 

def coordinate_to_center_pixel(pos_x, pos_y):
    pixel_x = pos_x * TILE_WIDTH + int(TILE_WIDTH/2)
    pixel_y = pos_y * TILE_HEIGHT + int(TILE_HEIGHT/2)
    return (pixel_x, pixel_y) 

def pixel_to_pixel_top_left(pixel_x, pixel_y):
    pos_x , pos_y = pixel_to_coordinate( pixel_x, pixel_y )
    pixel_x = pos_x * TILE_WIDTH
    pixel_y = pos_y * TILE_HEIGHT
    return (pixel_x, pixel_y) 

def pixel_to_center_pixel(pixel_x, pixel_y):
    pos_x , pos_y = pixel_to_coordinate( pixel_x, pixel_y )
    pixel_x , pixel_y = coordinate_to_center_pixel(pos_x, pos_y)
    return (pixel_x, pixel_y)

def is_the_position_on_board(x,y):
    if x < 4 and x>=0 and y<8 and y>=0:
        return True
    else:
        return False    


def isPiece(piece):
    if piece == EMPTY_PIECE:
        return False
    else:
        return True    

