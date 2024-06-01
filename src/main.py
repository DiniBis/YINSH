from back import * #import de toutes les fonctions en back
from front import * #import de toutes les fonctions d'affichage
import MainMenu #import des fonctions du MainMenu différent pour éviter les erreurs

#récupérer les infos des menus (blitz,multi,CPU)
if MainMenu.mode_blitz == true:
    blitz = true
if MainMenu.nombrejoueurs == 2:
    boucle_de_jeu()

#Pour 2 joueurs sur une même machine
def boucle_de_jeu():
    jeu=Jeu(blitz)
    #création de la grille
    plateau=Grille()
    #chaque joueur place ses 5 anneaux
    tourJoueur=1
    for i in range(10):
        #INPUT de X et Y par le clic
        x=0 #prendre l'input x du joueur
        y=0 #prendre l'input y du joueur
        est_place=plateau.placerAnneau(tourJoueur,x,y)
        while est_place==False:
            #Tant que le pion n'est pas placé, demander à nouveau
            x=0
            y=0
            est_place=plateau.placerAnneau(tourJoueur,x,y)
        tourJoueur=1 if tourJoueur==2 else 2
    #boucle principale
    while jeu.victoire(jeu.blitz,tourJoueur)==False:
        #INPUT de X et Y par le clic
        x=0 #prendre l'input x du joueur
        y=0 #prendre l'input y du joueur
        #Le joueur du tour choisis un anneau qui sera déplacé
        liste=plateau.deplacementPossible(tourJoueur,x,y)
        while liste==False:
            x, y = 0, 0
            liste=plateau.deplacementPossible(tourJoueur,x,y)
        #INPUT de nouvX et nouvY (un emplacement valide pour le déplacement de l'anneau) par le clic
        nouv_x=0 #prendre l'input x du joueur
        nouv_y=0 #prendre l'input y du joueur
        res=plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
        while res==False:
            x, y = 0, 0
            res=plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
        #Regarder s'il y a un alignement
        plateau.alignement()
        tourJoueur=1 if tourJoueur==2 else 2
    return tourJoueur #si la condition de victoire est remplie, envoyer le joueur du tour pour l'écran de fin

# Pour affronter un bot
def versus_cpu():
    jeu=Jeu(blitz)
    #création de la grille
    plateau=Grille()
    #chaque joueur place ses 5 anneaux
    tourJoueur=1
    for i in range(10):
        #entrée des coordonnées par le joueur ou le bot
        x, y = (0, 0) if tourJoueur == 1 else coordonnee_alea(len(plateau._plateau), len(plateau._plateau[0]))
        est_place=plateau.placerAnneau(tourJoueur,x,y)
        while est_place==False:
            #Tant que le pion n'est pas placé, demander à nouveau
            if tourJoueur==1:
                x=0 #prendre l'input x du joueur
                y=0 #prendre l'input y du joueur
            else:
                x, y = coordonnee_alea(len(plateau._plateau),len(plateau._plateau[0]))
            est_place=plateau.placerAnneau(tourJoueur,x,y)
        tourJoueur=1 if tourJoueur==2 else 2
    #boucle principale
    while jeu.victoire(plateau.anneau_retiréJ1, plateau.anneau_retiréJ2, blitz)==False:
        #entrée des coordonnées par le joueur ou le bot
        x, y = (0, 0) if tourJoueur == 1 else coordonnee_alea(len(plateau._plateau), len(plateau._plateau[0]))
        #Le joueur du tour choisis un anneau qui sera déplacé
        liste=plateau.deplacementPossible(tourJoueur,x,y)
        while liste==False:
            x, y = (0, 0) if tourJoueur == 1 else coordonnee_alea(len(plateau._plateau), len(plateau._plateau[0]))
            liste=plateau.deplacementPossible(tourJoueur,x,y)
        #INPUT de nouvX et nouvY (un emplacement valide pour le déplacement de l'anneau) par le clic
        nouv_x=0 #prendre l'input x du joueur
        nouv_y=0 #prendre l'input y du joueur
        plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
        #Regarder s'il y a un alignement
        tableau_alignement=plateau.alignement()
        #Si des alignements sont enregistrés
        if tourJoueur==1 and len(tableau_alignement)>0:
            res=jeu.retirer_alignement(tableau_alignement, x, y, False)
            if res!=False:
                #res est le numéro du joueur qui doit retirer son anneau
                #prendre un input de joueur, si c'est l'un de ses anneaux:
                    plateau.anneau_retiréJ1+=1
        elif tourJoueur==2 and len(tableau_alignement)>0:
            jeu.retirer_alignement(tableau_alignement, x, y, True)
        tourJoueur=1 if tourJoueur==2 else 2
    return tourJoueur #si la condition de victoire est remplie, envoyer le joueur du tour pour l'écran de fin
