import pygame

class BaseEntity(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, position: tuple):
        super().__init__()
        
        self.screen = screen
        self.position = position
