import pygame
from entities.BaseEntity import BaseEntity

class Target(BaseEntity):
    
    def __init__(self, screen, position, onQuitScreen, speed = 6):
        super().__init__(screen, position)
        self.image = pygame.image.load('assets/img/target.png')
        self.image = pygame.transform.smoothscale(self.image, (150, 150))
        
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.justSpawned = True
        self.onQuitScreen = onQuitScreen
    
    """Atualiza estado do objeto"""
    def update(self):
        self.rect.x += self.speed
        
        if(self.rect.right > 0 and self.rect.left < self.screen.get_width()):
            self.justSpawned = False

        if(not self.justSpawned):
            if self.rect.left > self.screen.get_width():
                self.onQuitScreen()
                self.kill()
            elif self.rect.right < 0:
                self.onQuitScreen()
                self.kill()
        
    """ Desenha o objeto na tela """
    def draw(self):
        self.screen.blit(self.image, self.rect)
