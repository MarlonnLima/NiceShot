import pygame
from entities.BaseEntity import BaseEntity
class Aim(BaseEntity):
    
    def __init__(self, screen, position):
        super().__init__(screen, position)
        self.image = pygame.image.load('assets/img/aim.png')
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        
        self.rect = self.image.get_rect(center=position)
        
    """Atualiza estado do objeto"""
    def update(self):
       x, y = pygame.mouse.get_pos()
       self.rect.x = x - self.rect.width / 2
       self.rect.y = y - self.rect.height / 2
    
    """ Desenha o objeto na tela """
    def draw(self):
        self.screen.blit(self.image, self.rect)
