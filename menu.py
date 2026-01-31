import pygame

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.options = ["Iniciar Jogo", "Sair"]
        self.controls = [
            "Use as setas do teclado para navegar no menu e enter para selecionar",
            "Em Jogo mire com o mouse e clique com o botão esquerdo do mouse para atirar",
            "Você tem 6 balas na pistola, a recarga é automática",
            "Perde uma vida ao deixar um alvo sair da tela",
            "O Score é calculado baseado na precisão do tiro, a cada 30 pontos ganha uma vida"
        ]
        self.selected_option = 0
        self.background = pygame.image.load('assets/img/background_menu.png')
        self.bigFont = pygame.font.Font(None, 72)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        for index, option in enumerate(self.options):
            color = (255, 0, 0) if index == self.selected_option else (255, 255, 255)
            text_surface = self.bigFont.render(option, True, color)
            rect = text_surface.get_rect(center=(self.screen.get_width() // 2, 300 + index * 70))
            pygame.draw.rect(self.screen, (50, 50, 50), rect)
            self.screen.blit(text_surface, rect)
        
        for index, control in enumerate(self.controls):
            controls_surface = self.font.render(control, True, (255, 255, 255))
            rect = controls_surface.get_rect(center=(self.screen.get_width() // 2, 500 + index * 30))
            pygame.draw.rect(self.screen, (50, 50, 50), rect)
            self.screen.blit(controls_surface, rect)

        creditos_surface = self.font.render("Desenvolvido por Marlon Lima, RU: 4590698", True, (255, 255, 255))
        rect = creditos_surface.get_rect(center=(self.screen.get_width() // 2, 680))
        pygame.draw.rect(self.screen, (50, 50, 50), rect)
        self.screen.blit(creditos_surface, rect)

        pygame.display.flip()

    def navigate(self, direction):
        self.selected_option = (self.selected_option + direction) % len(self.options)

    def get_selected_option(self):
        return self.options[self.selected_option]