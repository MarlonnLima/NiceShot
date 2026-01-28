import pygame
from entities.Aim import Aim
from entities.Target import Target
from entities.Score import Score
from entities.Bullet import Bullet

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.pistol_shot_sound = pygame.mixer.Sound('assets/sound/pistol_shot.mp3')
        self.gun_reload_sound = pygame.mixer.Sound('assets/sound/gun_reload.mp3')
        self.gun_reload_sound.set_volume(0.10)
        self.pistol_shot_sound.set_volume(0.10)

        font = pygame.font.Font(None, 36)
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.targets = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        for x in range(6):
            bullet = Bullet(self.screen, (60 + x * 40, 650))
            self.bullets.add(bullet)

        self.aim = Aim(self.screen, pygame.mouse.get_pos())
        self.score = Score(self.screen, font)
        self.spawn_delay = 600  # ms
        self.last_spawn = pygame.time.get_ticks()

        self.reloading = False
        self.gun_reload_time = 2000  # ms
        self.last_reload_request = pygame.time.get_ticks();
    
    def loop(self):
        while self.running:
            self.screen.fill((216, 216, 191))  # Preenche o fundo
            


            if(self.bullets.sprites() and all(b.used for b in self.bullets.sprites()) and not self.reloading):
                self.reloading = True
                self.last_reload_request = pygame.time.get_ticks();

            # O evento de quit significa fechamento da janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for t in self.targets:
                        if t.rect.collidepoint(event.pos):
                            bulletSprites = self.bullets.sprites()
                            nonUsedBullets = [b for b in bulletSprites if not b.used]

                            if len(nonUsedBullets) > 0:
                                self.pistol_shot_sound.play();
                                self.score.update(10)
                                nonUsedBullets[-1].update()
                                t.kill()

            player_pos = pygame.mouse.get_pos()    
            
            now = pygame.time.get_ticks()

            if now - self.last_spawn >= self.spawn_delay:
                self.last_spawn = now
                self.targets.add(Target(self.screen, (-50, 360)))

            if self.reloading:
                if pygame.time.get_ticks() - self.last_reload_request >= self.gun_reload_time:
                    self.gun_reload_sound.play()
                    for bullet in self.bullets.sprites():
                        bullet.update()
                    self.reloading = False

            
            self.bullets.draw(self.screen)
            self.score.draw()
            
            self.targets.update()
            self.targets.draw(self.screen)
            
            self.aim.update()
            self.aim.draw()

            pygame.display.flip()   # Atualiza o frame na tela 
            self.clock.tick(60)         # Limita a 60 FPS