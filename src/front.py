import pygame
import sys

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Yinsh')

plateau_image = pygame.image.load('Board.svg')
plateau_width, plateau_height = plateau_image.get_size()

plateau_x = (WINDOW_WIDTH - plateau_width) // 2
plateau_y = (WINDOW_HEIGHT - plateau_height) // 2

def afficher_plateau():
    window.blit(plateau_image, (plateau_x, plateau_y))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    afficher_plateau()

    pygame.display.update()
