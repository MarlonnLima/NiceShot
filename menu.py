import pygame

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.options = ["Iniciar Jogo", "Como Jogar", "Sair"]
        self.selected_option = 0
        self.background = pygame.image.load('assets/img/background_menu.png')
        self.bigFont = pygame.font.Font(None, 72)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        for index, option in enumerate(self.options):
            color = (255, 0, 0) if index == self.selected_option else (0, 0, 0)
            text_surface = self.bigFont.render(option, True, color)
            rect = text_surface.get_rect(center=(self.screen.get_width() // 2, 300 + index * 50))
            self.screen.blit(text_surface, rect)
        pygame.display.flip()

    def navigate(self, direction):
        self.selected_option = (self.selected_option + direction) % len(self.options)

    def get_selected_option(self):
        return self.options[self.selected_option]