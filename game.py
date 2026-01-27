import pygame
from entities.Aim import Aim
from entities.Target import Target
from entities.Score import Score

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.font.init()
        font = pygame.font.Font(None, 36)
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.target = Target(self.screen, (-50, 360))  
        self.targets = pygame.sprite.Group()
        self.aim = Aim(self.screen, pygame.mouse.get_pos())
        self.score = Score(self.screen, font)
        self.spawn_delay = 1200  # ms
        self.last_spawn = pygame.time.get_ticks()
    
    def loop(self):
        while self.running:
            self.screen.fill((216, 216, 191))  # Preenche o fundo
            
            # O evento de quit significa fechamento da janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for t in self.targets:
                        if t.rect.collidepoint(event.pos):
                            self.score.update(10)
                            t.kill()

            player_pos = pygame.mouse.get_pos()    
            
            now = pygame.time.get_ticks()

            if now - self.last_spawn >= self.spawn_delay:
                self.last_spawn = now
                self.targets.add(Target(self.screen, (-50, 360)))
            
            self.score.draw()
            
            self.targets.update()
            self.targets.draw(self.screen)
            
            self.aim.update()
            self.aim.draw()

            pygame.display.flip()   # Atualiza o frame na tela 
            self.clock.tick(60)         # Limita a 60 FPS