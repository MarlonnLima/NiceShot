import pygame
from entities.BaseEntity import BaseEntity

class Target(BaseEntity):
    
    def __init__(self, screen, position):
        super().__init__(screen, position)
        self.image = pygame.image.load('assets/img/target.png')
        self.image = pygame.transform.smoothscale(self.image, (150, 150))
        
        self.rect = self.image.get_rect(center=position)
        self.speed = 6
    
    """Atualiza estado do objeto"""
    def update(self):
        self.rect.x += self.speed
        
        if self.rect.left > self.screen.get_width():
            self.kill()
        
    """ Desenha o objeto na tela """
    def draw(self):
        self.screen.blit(self.image, self.rect)
