import pygame
import sys
from back import*

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
green = [0, 250, 0]
dark_green = [0, 100, 0]
white = [250, 250, 250]
black = [0, 0, 0]
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Yinsh 2049')

plateau_image = pygame.image.load('board.svg')
plateau_width, plateau_height = plateau_image.get_size()
plateau_x = (WINDOW_WIDTH - plateau_width) // 2
plateau_y = (WINDOW_HEIGHT - plateau_height) // 2

font = pygame.font.SysFont(None, 55)
placement = 0



# Taille d'une case (à adapter selon votre plateau)
case_width = plateau_width // 11
case_height = plateau_height // 19
tour_joueur = 1


def afficher_plateau(plateau, tour_joueur):
    window.fill(black)
    afficher_ath(tour_joueur)
    window.blit(plateau_image, (plateau_x, plateau_y))
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if isinstance(plateau[i][j], Marqueur):
                joueur = plateau[i][j].getJoueur()
                pos = grille_to_window_coords(i, j)
                pygame.draw.circle(window,couleur_joueur(joueur),pos,10)
            if isinstance(plateau[i][j], Anneau):
                joueur = plateau[i][j].getJoueur()
                pos = grille_to_window_coords(i, j)
                pygame.draw.circle(window, couleur_joueur(joueur), pos, 20, 5)
                pygame.draw.circle(window, black, pos, 20, 1)
                pygame.draw.circle(window, black, pos, 15, 1)
    pygame.display.update()


def couleur_joueur(tour_joueur):
    return green if tour_joueur == 1 else dark_green

def afficher_ath(tour_joueur):
    text = font.render(f"Tour du joueur {3 - tour_joueur}", True, black)
    text_rect = text.get_rect(center=(150, 50))
    window.blit(text, text_rect)

    text = font.render(f"Tour du joueur {tour_joueur}", True, white)
    text_rect = text.get_rect(center=(150, 50))
    window.blit(text, text_rect)


def grille_to_window_coords(ligne, colonne):
    x = plateau_x + colonne * case_width + case_width // 2
    y = plateau_y + ligne * case_height + case_height // 2
    return x, y


def clic():
    x, y = 0, 0
    for event in pygame.event.get():
        pygame.event.clear(eventtype= pygame.MOUSEBUTTONDOWN)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                x = (mouse_x - plateau_x) // case_width
                y = (mouse_y - plateau_y) // case_height

    if 0 <= y <= 19 and 0 <= x <= 11:
        return y,x
    else:
        return 0, 0
