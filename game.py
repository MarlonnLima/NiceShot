import pygame
from menu import Menu
from entities.Aim import Aim
from entities.Target import Target
from entities.Score import Score
from entities.Bullet import Bullet

class Game:
    
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

        # sons
        self.pistol_shot_sound = pygame.mixer.Sound('assets/sound/pistol_shot.mp3')
        self.gun_reload_sound = pygame.mixer.Sound('assets/sound/gun_reload.mp3')
        self.menu_song = pygame.mixer.Sound('assets/sound/menu_song.wav')
        self.gun_reload_sound.set_volume(0.05)
        self.pistol_shot_sound.set_volume(0.05)
        self.menu_song.set_volume(0.10)

        # configurações iniciais do jogo
        pygame.mouse.set_visible(False)

        # clock e variáveis de controle
        self.clock = pygame.time.Clock()
        self.running = True
        self.targets = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        for x in range(6):
            bullet = Bullet(screen, (60 + x * 40, 650))
            self.bullets.add(bullet)

        self.aim = Aim(screen, pygame.mouse.get_pos())
        self.score = Score(screen, font)
        self.spawn_delay = 600  # ms
        self.last_spawn = pygame.time.get_ticks()

        self.reloading = False
        self.gun_reload_time = 1000  # ms
        self.last_reload_request = pygame.time.get_ticks();
    
        self.in_menu = True
    
    def menu(self):
        menu = Menu(self.screen, self.font)
        self.menu_song.play(-1)  # Toca a música do menu em loop
        
        while self.in_menu:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.in_menu = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menu.navigate(-1)
                    elif event.key == pygame.K_DOWN:
                        menu.navigate(1)
                    elif event.key == pygame.K_RETURN:
                        selected = menu.get_selected_option()
                        if selected == "Iniciar Jogo":
                            self.in_menu = False
                            self.level1()
                        elif selected == "Como Jogar":
                            pass  # Implementar tela de instruções se necessário
                        elif selected == "Sair":
                            self.in_menu = False
                            self.running = False

            menu.draw()

            pygame.display.flip()
            self.clock.tick(60)         # Limita a 60 FPS

    def level1(self):
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
                self.targets.add(Target(self.screen, (-50, 250)))
                self.targets.add(Target(self.screen, (1330, 500), speed= - 6))

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