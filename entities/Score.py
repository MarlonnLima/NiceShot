import pygame

class Score():
    
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.value = 0
        self.font = font
        self.screen = screen
        self.text_surface = self.font.render(f'Score: {self.value}', True, (255, 255, 255))
    
    def update(self, newPoints):
        self.value += newPoints
        self.text_surface = self.font.render(f'Score: {self.value}', True, (255, 255, 255))
        pass
    
    def draw(self):
        self.screen.blit(self.text_surface, (10, 10))
        pass
    