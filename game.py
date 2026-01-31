import pygame
from menu import Menu
from entities.Aim import Aim
from entities.Target import Target
from entities.Score import Score
from entities.Bullet import Bullet
from entities.Heart import Heart

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
        self.menu_song.play(-1)  # Toca a música do menu em loop

        # configurações iniciais do jogo
        pygame.mouse.set_visible(False)

        # clock e variáveis de controle
        self.clock = pygame.time.Clock()
        self.running = True
        self.targets = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()

        self.aim = Aim(screen, pygame.mouse.get_pos())
        self.score = Score(screen, font)
        self.spawn_delay = 600  # ms
        self.last_spawn = pygame.time.get_ticks()

        self.reloading = False
        self.gun_reload_time = 500  # ms
        self.last_reload_request = pygame.time.get_ticks();
    
        self.in_menu = True
    
    def menu(self):
        menu = Menu(self.screen, self.font)
        
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
                            self.running = True
                            self.level1()
                        elif selected == "Sair":
                            self.in_menu = False
                            self.running = False
                            pygame.quit()

            menu.draw()

            pygame.display.flip()
            self.clock.tick(60)         # Limita a 60 FPS

    def level1(self):
        self.set_level1_variables();
        while self.running:
            self.screen.fill((216, 216, 191))  # Preenche o fundo

            if(self.bullets.sprites() and all(b.used for b in self.bullets.sprites()) and not self.reloading):
                self.reloading = True
                self.last_reload_request = pygame.time.get_ticks();

            # O evento de fechar a tela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for t in self.targets:
                        center_x, center_y = t.rect.center
                        hit_x, hit_y = event.pos
                        distance = pygame.math.Vector2(hit_x, hit_y).distance_to((center_x, center_y))
                        max_radius = t.rect.width / 2
                        if t.rect.collidepoint(event.pos):
                            bulletSprites = self.bullets.sprites()
                            nonUsedBullets = [b for b in bulletSprites if not b.used]

                            if len(nonUsedBullets) > 0:
                                self.pistol_shot_sound.play();
                                if distance < max_radius:
                                    self.score.update(int((1 - (distance / max_radius)) * 20)) # Pontos baseados na precisão do tiro

                                if(self.score.value % 30 == 0): # a cada 30 pontos ganha 1 vida
                                    heartSprites = self.hearts.sprites()
                                    emptyHearts = [h for h in heartSprites if h.empty]
                                    if len(emptyHearts) > 0:
                                        emptyHearts[-(len(emptyHearts))].update()

                                nonUsedBullets[-1].update()
                                t.kill()

            player_pos = pygame.mouse.get_pos()    
            
            now = pygame.time.get_ticks()

            if now - self.last_spawn >= self.spawn_delay:
                self.last_spawn = now
                self.targets.add(Target(self.screen, (-50, 250), self.target_quit_screen))
                self.targets.add(Target(self.screen, (1330, 500), self.target_quit_screen, speed= - 6))

            if self.reloading:
                if pygame.time.get_ticks() - self.last_reload_request >= self.gun_reload_time:
                    self.gun_reload_sound.play()
                    for bullet in self.bullets.sprites():
                        bullet.update()
                    self.reloading = False

            self.hearts.draw(self.screen)
            self.bullets.draw(self.screen)
            self.score.draw()
            
            self.targets.update()
            self.targets.draw(self.screen)
            
            self.aim.update()
            self.aim.draw()

            pygame.display.flip()   # Atualiza o frame na tela 
            self.clock.tick(60)         # Limita a 60 FPS

    def target_quit_screen(self):
        heartSprites = self.hearts.sprites()
        fullHearts = [h for h in heartSprites if not h.empty]
        if len(fullHearts) > 0:
            fullHearts[-1].update()

        fullHearts = [h for h in heartSprites if not h.empty]
        if len(fullHearts) == 0:
            self.running = False
            self.in_menu = True
            self.menu()

    def set_level1_variables(self):
        self.targets.empty()
        self.bullets.empty()
        self.hearts.empty()
        self.score.reset()
        self.score.draw()
        for x in range(6):
            bullet = Bullet(self.screen, (60 + x * 40, 650))
            self.bullets.add(bullet)
        
        for x in range(10):
            heart = Heart(self.screen, (900 + x * 40, 20))
            self.hearts.add(heart)