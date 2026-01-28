import pygame
from entities.BaseEntity import BaseEntity

class Bullet(BaseEntity):
    
    def __init__(self, screen, position):
        super().__init__(screen, position)
        self.bulletImage = pygame.image.load('assets/img/bullet.png')
        self.bulletUsedImage = pygame.image.load('assets/img/bullet_used.png')

        self.bulletImage = pygame.transform.smoothscale(self.bulletImage, (20, 70))
        self.bulletUsedImage = pygame.transform.smoothscale(self.bulletUsedImage.convert_alpha(), (20, 70))

        # inicia em bullet Image
        self.image = self.bulletImage
        self.used = False
        self.rect = self.image.get_rect(center=position)
    
    """Atualiza estado do objeto"""
    def update(self):
        self.used = not self.used

        if(self.used):
            self.image = self.bulletUsedImage 
        else:
            self.image = self.bulletImage

    """ Desenha o objeto na tela """
    def draw(self):
        self.screen.blit(self.image, self.rect)