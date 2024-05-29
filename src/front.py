import pygame
import sys
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
blue = [20, 20, 250]
yellow = [250, 250, 0]
white = [250, 250, 250]
black = [0, 0, 0]
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(blue)
pygame.display.set_caption('Yinsh')

plateau_image = pygame.image.load('Board.svg')
plateau_width, plateau_height = plateau_image.get_size()

plateau_x = (WINDOW_WIDTH - plateau_width) // 2
plateau_y = (WINDOW_HEIGHT - plateau_height) // 2

font = pygame.font.SysFont(None, 55)


def afficher_plateau():
    window.blit(plateau_image, (plateau_x, plateau_y))

def afficher_ath():
    text = font.render(f"Tour du joueur 1",True, white)
    text_rect = text.get_rect(center=(150,50))
    window.blit(text,text_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    afficher_plateau()
    afficher_ath()
    pygame.display.update()
