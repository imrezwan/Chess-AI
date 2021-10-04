import pygame

from colors import *
from constants import *


class Board:

    def __init__(self, SCREEN) -> None:
        self.screen = SCREEN

    def draw(self):
        # Draw chess board
        toggle = True
        for i in range(0, ROW):
            for j in range(0, COLUMN):
                if toggle:
                    pygame.draw.rect(self.screen , WHITE,  (j*TILE_WIDTH,i*TILE_HEIGHT, TILE_WIDTH,TILE_HEIGHT))
                    toggle = not toggle
                else:
                    pygame.draw.rect(self.screen ,BLACK,   (j*TILE_WIDTH,i*TILE_HEIGHT, TILE_WIDTH,TILE_HEIGHT) )
                    toggle = not toggle  
            toggle = not toggle
        
