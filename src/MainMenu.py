import pygame
import sys

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

pygame.display.set_caption("Yinsh")

blanc = (255, 255, 255)
noir = (0, 0, 0)
gris_clair = (200, 200, 200)

police_titre = pygame.font.Font(None, 74)
police_bouton = pygame.font.Font(None, 50)

texte_titre = police_titre.render("Yinsh", True, noir)
rect_texte_titre = texte_titre.get_rect()
rect_texte_titre.center = (largeur_fenetre // 2, hauteur_fenetre // 6)

boutons_principal = [
    {"label": "Jouer", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 - 60, 200, 50)},
    {"label": "Options", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2, 200, 50)},
    {"label": "Quitter", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 + 60, 200, 50)},
]

boutons_jouer = [
    {"label": "1 joueur", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 - 30, 200, 50)},
    {"label": "2 joueurs", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 + 30, 200, 50)},
    {"label": "Retour", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 + 90, 200, 50)},
]

mode_blitz = False

boutons_options = [
    {"label": f"Mode Blitz: {'oui' if mode_blitz else 'non'}", "rect": pygame.Rect(largeur_fenetre // 2 - 150, hauteur_fenetre // 2 - 30, 300, 50)},
    {"label": "Aide", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 + 30, 200, 50)},
    {"label": "Retour", "rect": pygame.Rect(largeur_fenetre // 2 - 100, hauteur_fenetre // 2 + 90, 200, 50)},
]

menu_actuel = "principal"

def afficher_boutons(boutons):
    for bouton in boutons:
        pygame.draw.rect(fenetre, gris_clair, bouton["rect"])
        texte_bouton = police_bouton.render(bouton["label"], True, noir)
        rect_texte_bouton = texte_bouton.get_rect(center=bouton["rect"].center)
        fenetre.blit(texte_bouton, rect_texte_bouton)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos_souris = pygame.mouse.get_pos()
            if menu_actuel == "principal":
                for bouton in boutons_principal:
                    if bouton["rect"].collidepoint(pos_souris):
                        if bouton["label"] == "Jouer":
                            menu_actuel = "jouer"
                        elif bouton["label"] == "Options":
                            menu_actuel = "options"
                        elif bouton["label"] == "Quitter":
                            pygame.quit()
                            sys.exit()
            elif menu_actuel == "jouer":
                for bouton in boutons_jouer:
                    if bouton["rect"].collidepoint(pos_souris):
                        if bouton["label"] == "1 joueur":
                            nombre_joueurs = 1
                            exec(main.py)
                        elif bouton["label"] == "2 joueurs":
                            nombre_joueurs = 2
                            exec(main.py)
                        elif bouton["label"] == "Retour":
                            menu_actuel = "principal"
            elif menu_actuel == "options":
                for bouton in boutons_options:
                    if bouton["rect"].collidepoint(pos_souris):
                        if bouton["label"].startswith("Mode Blitz"):
                            mode_blitz = not mode_blitz
                            bouton["label"] = f"Mode Blitz: {'oui' if mode_blitz else 'non'}"
                        elif bouton["label"] == "Aide":
                            pass
                        elif bouton["label"] == "Retour":
                            menu_actuel = "principal"

    fenetre.fill(blanc)

    if menu_actuel == "principal":
        fenetre.blit(texte_titre, rect_texte_titre)
        afficher_boutons(boutons_principal)
    elif menu_actuel == "jouer":
        afficher_boutons(boutons_jouer)
    elif menu_actuel == "options":
        afficher_boutons(boutons_options)

    pygame.display.flip()
