from entities.BaseEntity import BaseEntity
import pygame

class Heart(BaseEntity):
    
    def __init__(self, screen, position):
        super().__init__(screen, position)
        self.heartImage = pygame.image.load('assets/img/heart.png')
        self.heartImageEmpty = pygame.image.load('assets/img/heart_empty.png')

        self.heartImage = pygame.transform.smoothscale(self.heartImage, (30, 30))
        self.heartImageEmpty = pygame.transform.smoothscale(self.heartImageEmpty.convert_alpha(), (30, 30))


        # inicia em heart Image
        self.image = self.heartImage
        self.empty = False;
        self.rect = self.image.get_rect(center=position)
    
    """Atualiza estado do objeto"""
    def update(self):
        self.empty = not self.empty

        if(self.empty):
            self.image = self.heartImageEmpty 
        else:
            self.image = self.heartImage

    """ Desenha o objeto na tela """
    def draw(self):
        self.screen.blit(self.image, self.rect)
