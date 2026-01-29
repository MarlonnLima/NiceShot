from game import Game
import pygame
# Inicializações do Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Configuração da tela e fonte
pygame.display.set_caption("Nice Shot - Shooter game!")
pygame.display.set_icon(pygame.image.load('assets/img/cowboy_hat.png'))
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font(None, 36)

game = Game(screen, font).menu()