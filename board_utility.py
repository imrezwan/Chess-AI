from constants import *

def pixel_to_coordinate( pixel_x, pixel_y):
    pos_x = int(pixel_x/TILE_WIDTH)
    pos_y = int(pixel_y/TILE_HEIGHT)
    return (pos_x, pos_y)

def coordinate_to_top_left_pixel(pos_x, pos_y):
    pixel_x = pos_x * TILE_WIDTH
    pixel_y = pos_y * TILE_HEIGHT
    return (pixel_x, pixel_y) 

def pixel_to_pixel_top_left(pixel_x, pixel_y):
    pos_x , pos_y = pixel_to_coordinate( pixel_x, pixel_y )
    pixel_x = pos_x * TILE_WIDTH
    pixel_y = pos_y * TILE_HEIGHT
    return (pixel_x, pixel_y) 

def pixel_to_center_pixel(pixel_x, pixel_y):
    pos_x , pos_y = pixel_to_coordinate( pixel_x, pixel_y )
    pixel_x = pos_x * TILE_WIDTH + int(TILE_WIDTH/2)
    pixel_y = pos_y * TILE_HEIGHT+ int(TILE_HEIGHT/2)
    return (pixel_x, pixel_y)