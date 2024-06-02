import pygame
import sys

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
green = [0, 250, 0]
dark_green = [0, 100, 0]
white = [250, 250, 250]
black = [0, 0, 0]
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(black)
pygame.display.set_caption('Yinsh 2049')

plateau_image = pygame.image.load('Board.svg')
plateau_width, plateau_height = plateau_image.get_size()

plateau_x = (WINDOW_WIDTH - plateau_width) // 2 + 6
plateau_y = (WINDOW_HEIGHT - plateau_height) // 2 + 4

font = pygame.font.SysFont(None, 55)
placement = 0

cercles = []

grille = [
    [-1, -1, -1, -1, 0, -1, 0, -1, -1, -1, -1],  # 0
    [-1, -1, -1, 0, -2, 0, -2, 0, -1, -1, -1],  # 1
    [-1, -1, 0, -2, 0, -2, 0, -2, 0, -1, -1],  # 2
    [-1, 0, -2, 0, -2, 0, -2, 0, -2, 0, -1],  # 3
    [-1, -2, 0, -2, 0, -2, 0, -2, 0, -2, -1],  # 4
    [-1, 0, -2, 0, -2, 0, -2, 0, -2, 0, -1],  # 5
    [0, -2, 0, -2, 0, -2, 0, -2, 0, -2, 0],  # 6
    [-2, 0, -2, 0, -2, 0, -2, 0, -2, 0, -2],  # 7
    [0, -2, 0, -2, 0, -2, 0, -2, 0, -2, 0],  # 8
    [-2, 0, -2, 0, -2, 0, -2, 0, -2, 0, -2],  # 9
    [0, -2, 0, -2, 0, -2, 0, -2, 0, -2, 0],  # 10
    [-2, 0, -2, 0, -2, 0, -2, 0, -2, 0, -2],  # 11
    [0, -2, 0, -2, 0, -2, 0, -2, 0, -2, 0],  # 12
    [-1, 0, -2, 0, -2, 0, -2, 0, -2, 0, -1],  # 13
    [-1, -2, 0, -2, 0, -2, 0, -2, 0, -2, -1],  # 14
    [-1, 0, -2, 0, -2, 0, -2, 0, -2, 0, -1],  # 15
    [-1, -1, 0, -2, 0, -2, 0, -2, 0, -1, -1],  # 16
    [-1, -1, -1, 0, -2, 0, -2, 0, -1, -1, -1],  # 17
    [-1, -1, -1, -1, 0, -1, 0, -1, -1, -1, -1],  # 18
]

# Taille d'une case (à adapter selon votre plateau)
case_width = plateau_width // 11
case_height = plateau_height // 19
tour_joueur = 1


def afficher_plateau():
    window.blit(plateau_image, (plateau_x, plateau_y))

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

def dessiner_anneau(mouse_x,mouse_y):
    grille_x = (mouse_x - plateau_x) // case_width
    grille_y = (mouse_y - plateau_y) // case_height

    if 0 <= grille_x < len(grille[0]) and 0 <= grille_y < len(grille):
        if grille[grille_y][grille_x] == 0:
            cercle_pos = grille_to_window_coords(grille_y, grille_x)
            cercles.append(cercle_pos)
            if tour_joueur == 1:
                grille[grille_y][grille_x] = 1
            else:
                grille[grille_y][grille_x] = 2
    for pos in cercles:
        pygame.draw.circle(window, couleur_joueur(tour_joueur), pos, 20, 5)
        pygame.draw.circle(window, black, pos, 20, 1)
        pygame.draw.circle(window, black, pos, 15, 1)
        return True
def anneau_possede(mouse_x,mouse_y):
    grille_x = (mouse_x - plateau_x) // case_width
    grille_y = (mouse_y - plateau_y) // case_height

    if 0 <= grille_x < len(grille[0]) and 0 <= grille_y < len(grille):
        if grille[grille_y][grille_x] == tour_joueur:
            pos = grille_to_window_coords(grille_y,grille_x)
            pygame.draw.circle(window, couleur_joueur(tour_joueur), pos, 20, 6)
            return True

def deplacement_anneau(mouse_x,mouse_y,mouse_x2,mouse_y2):
    grille_x = (mouse_x - plateau_x) // case_width
    grille_y = (mouse_y - plateau_y) // case_height
    grille_x2 = (mouse_x2 - plateau_x) // case_width
    grille_y2 = (mouse_y2 - plateau_y) // case_height

    if 0 <= grille_x2 < len(grille[0]) and 0 <= grille_y2 < len(grille):
        if grille[grille_y2][grille_x2] == 0:
            if grille_y2 > grille_y and grille_x2 > grille_x:
                for i in range(grille_x, grille_x2, 1):
                    for j in range(grille_y, grille_y2, 12):
                        cercle_pos = grille_to_window_coords(j, i)
                        cercles.append(cercle_pos)
                for pos in cercles:
                    pygame.draw.circle(window, couleur_joueur(tour_joueur), pos, 20)
        return True




afficher_plateau()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if placement == 10:
                if anneau_possede(mouse_x,mouse_y):
                    print("anneau possédé")
                    pygame.event.clear()
                    pygame.event.wait()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x2, mouse_y2 = event.pos
                        deplacement_anneau(mouse_x,mouse_y,mouse_x2,mouse_y2)
                        if deplacement_anneau(mouse_x,mouse_y,mouse_x2,mouse_y2):
                            print("déplacement de l'anneau")
                            tour_joueur = 3 - tour_joueur



            else:
                dessiner_anneau(mouse_x, mouse_y)
                if dessiner_anneau(mouse_x, mouse_y):
                    tour_joueur = 3 - tour_joueur
                    placement += 1
                cercles = []


    afficher_ath(tour_joueur)
    pygame.display.update()

