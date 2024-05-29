from back import * #import de toutes les fonctions en back
from front import * #import de toutes les fonctions d'affichage

#récupérer les infos des menus (blitz,multi,CPU)

def boucle_de_jeu(blitz,multi,CPU):
        jeu=Jeu(blitz)
        #création de la grille
        plateau=Grille()
        #chaque joueur place ses 5 anneaux
        tourJoueur=1
        for i in range(5):
            #INPUT de X et Y par le clic
            x=0 #prendre l'input x du joueur
            y=0 #prendre l'input y du joueur
            plateau.placerAnneau(tourJoueur,x,y)
            tourJoueur=1 if tourJoueur==2 else 2
        #boucle principale
        while jeu.victoire(jeu._blitz,tourJoueur)==False:
            #INPUT de X et Y par le clic
            x=0 #prendre l'input x du joueur
            y=0 #prendre l'input y du joueur
            #Le joueur du tour choisis un anneau qui sera déplacé
            liste=plateau.deplacementPossible(tourJoueur,x,y)
            #INPUT de nouvX et nouvY (un emplacement valide pour le déplacement de l'anneau) par le clic
            nouv_x=0 #prendre l'input x du joueur
            nouv_y=0 #prendre l'input y du joueur
            plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
            #Regarder s'il y a un alignement
            plateau.alignement()
            tourJoueur=1 if tourJoueur==2 else 2
        return tourJoueur #si la condition de victoire est remplie, envoyer le joueur du tour pour l'écran de fin
