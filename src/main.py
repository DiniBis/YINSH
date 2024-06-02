import pygame.mixer

from back import * #import de toutes les fonctions en back
from front import * #import de toutes les fonctions d'affichage
from MainMenu import *#import des fonctions du MainMenu différent pour éviter les erreurs


#récupérer les infos des menus (blitz,multi,CPU)
nombre_joueurs, blitz = Menu()


#Pour 2 joueurs sur une même machine
def boucle_de_jeu(blitz):
    #création de la grille
    plateau=Grille()
    #chaque joueur place ses 5 anneaux
    tourJoueur=1
    afficher_plateau(plateau._plateau, tourJoueur, 1)
    for i in range(10):
        x,y = clic()
        est_place=plateau.placerAnneau(tourJoueur,x,y)
        while est_place==False:
            x,y = clic()
            est_place=plateau.placerAnneau(tourJoueur,x,y)
        tourJoueur = 1 if tourJoueur == 2 else 2
        afficher_plateau(plateau._plateau, tourJoueur, 1)

    #boucle principale
    while victoire(plateau.anneau_retiréJ1, plateau.anneau_retiréJ2, blitz)==False:
        afficher_plateau(plateau._plateau, tourJoueur, 2)
        #INPUT de X et Y par le clic
        x,y = clic()
        #Le joueur du tour choisis un anneau qui sera déplacé
        liste=plateau.deplacementPossible(tourJoueur,x,y)
        while liste==False:
            x, y = clic()
            liste=plateau.deplacementPossible(tourJoueur,x,y)
        afficher_plateau(plateau._plateau, tourJoueur, 2)
        #INPUT de nouvX et nouvY (un emplacement valide pour le déplacement de l'anneau) par le clic
        nouv_x, nouv_y = clic()
        res=plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
        while res==False:
            nouv_x, nouv_y = clic()
            res=plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
        #Regarder s'il y a un alignement
        tableau_alignement=plateau.alignement()
        #Si des alignements sont enregistrés
        if len(tableau_alignement)>0:
            afficher_plateau(plateau._plateau, tourJoueur, 3)
            x, y = clic()
            if [x,y] in tableau_alignement:
                res=plateau.retirer_alignement(tableau_alignement, x, y, False)
            else:
                while [x,y] not in tableau_alignement:
                    x, y = clic()
                    res = plateau.retirer_alignement(tableau_alignement, x, y, False)
            #res est le numéro du joueur qui doit retirer son anneau
            if res==1:
                #prendre un input de joueur et si c'est l'un de ses anneaux le retirer:
                x, y = clic()
                if isinstance(plateau._plateau[x][y],Anneau) and plateau._plateau[x][y].getJoueur()==1:
                    plateau._plateau[x][y]=0
                    plateau.anneau_retiréJ1+=1
                    pygame.mixer.Sound.play(align_sound)
                else:
                    while not (isinstance(plateau._plateau[x][y],Anneau) and plateau._plateau[x][y].getJoueur()==1):
                        x, y = clic()
                        plateau._plateau[x][y] = 0
                        plateau.anneau_retiréJ1 += 1
                        pygame.mixer.Sound.play(align_sound)
            elif res==2:
                #idem pour J2
                x, y = clic()
                if isinstance(plateau._plateau[x][y],Anneau) and plateau._plateau[x][y].getJoueur()==2:
                    plateau._plateau[x][y]=0
                    plateau.anneau_retiréJ2+=1
                    pygame.mixer.Sound.play(align_sound)
                else:
                    while not (isinstance(plateau._plateau[x][y],Anneau) and plateau._plateau[x][y].getJoueur()==2):
                        x, y = clic()
                        plateau._plateau[x][y] = 0
                        plateau.anneau_retiréJ1 += 1
                        pygame.mixer.Sound.play(align_sound)
        tourJoueur=1 if tourJoueur==2 else 2
    return plateau.anneau_retiréJ1, plateau.anneau_retiréJ2 #si la condition de victoire est remplie, envoyer les resultat pour l'écran de fin

# Pour affronter un bot
def versus_cpu(blitz):
    #création de la grille
    plateau=Grille()
    #chaque joueur place ses 5 anneaux
    tourJoueur=1
    afficher_plateau(plateau._plateau, tourJoueur, 1)
    for i in range(10):
        #entrée des coordonnées par le joueur ou le bot
        x, y = clic() if tourJoueur == 1 else coordonnee_alea(len(plateau._plateau), len(plateau._plateau[0]))
        est_place=plateau.placerAnneau(tourJoueur,x,y)
        while est_place==False:
            #Tant que le pion n'est pas placé, demander à nouveau
            if tourJoueur==1:
                x, y = clic() #prendre l'input y du joueur
            else:
                x, y = coordonnee_alea(len(plateau._plateau),len(plateau._plateau[0]))
            est_place=plateau.placerAnneau(tourJoueur,x,y)
        tourJoueur=1 if tourJoueur==2 else 2
        afficher_plateau(plateau._plateau, tourJoueur, 1)
    #boucle principale
    while victoire(plateau.anneau_retiréJ1, plateau.anneau_retiréJ2, blitz)==False:
        #entrée des coordonnées par le joueur ou le bot
        afficher_plateau(plateau._plateau, tourJoueur, 2)
        x, y = clic() if tourJoueur == 1 else coordonnee_alea(len(plateau._plateau), len(plateau._plateau[0]))
        #Le joueur du tour choisis un anneau qui sera déplacé
        liste=plateau.deplacementPossible(tourJoueur,x,y)
        while liste==False:
            x, y = clic() if tourJoueur == 1 else coordonnee_alea(len(plateau._plateau), len(plateau._plateau[0]))
            liste=plateau.deplacementPossible(tourJoueur,x,y)
        #INPUT de nouvX et nouvY (un emplacement valide pour le déplacement de l'anneau) par le clic
        nouv_x, nouv_y = clic()
        res=plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
        while res==False:
            x, y = clic()
            res=plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
        afficher_plateau(plateau._plateau, tourJoueur, 2)
        #Regarder s'il y a un alignement
        tableau_alignement=plateau.alignement()
        #Si des alignements sont enregistrés
        if len(tableau_alignement)>0:
            res=plateau.retirer_alignement(tableau_alignement, x, y, True)
            afficher_plateau(plateau._plateau, tourJoueur, 3)
            if res==1:
                #prendre un input de joueur et si c'est l'un de ses anneaux le retirer:
                x, y = clic()
                if isinstance(plateau._plateau[x][y],Anneau) and plateau._plateau[x][y].getJoueur()==1:
                    plateau._plateau[x][y]=0
                    plateau.anneau_retiréJ1+=1
                    pygame.mixer.Sound.play(align_sound)
                else:
                    while not (isinstance(plateau._plateau[x][y],Anneau) and plateau._plateau[x][y].getJoueur()==1):
                        x, y = clic()
                        plateau._plateau[x][y] = 0
                        plateau.anneau_retiréJ1 += 1
                        pygame.mixer.Sound.play(align_sound)
            #pas d'opérations pour le CPU ici, les actions sont déjà réalisées dans la fonction
        tourJoueur=1 if tourJoueur==2 else 2
    return plateau.anneau_retiréJ1, plateau.anneau_retiréJ2 #si la condition de victoire est remplie, envoyer les resultat pour l'écran de fin


if nombre_joueurs == 2:
    boucle_de_jeu(blitz)
elif nombre_joueurs == 1:
    versus_cpu(blitz)

