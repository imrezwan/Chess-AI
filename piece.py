import pygame
from colors import * 

class Piece(pygame.sprite.Sprite):

    def __init__(self, picture_path):
        super().__init__() 
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def set_center(self, pos):
        self.rect.center = pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)    

