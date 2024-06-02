from back import * #import de toutes les fonctions en back
from front import * #import de toutes les fonctions d'affichage
import MainMenu #import des fonctions du MainMenu différent pour éviter les erreurs


if MainMenu.mode_blitz == True:
    blitz = True
else:
    blitz = False

#Pour 2 joueurs sur une même machine
def boucle_de_jeu():
    x = 0
    y = 0
    #création de la grille
    plateau=Grille()
    #chaque joueur place ses 5 anneaux
    tourJoueur=1
    for i in range(10):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
            est_place=plateau.placerAnneau(tourJoueur,x,y)
            while est_place==False:
                est_place=plateau.placerAnneau(tourJoueur,x,y)
                dessiner_anneau(x, y)
                cercles = []
            tourJoueur=1 if tourJoueur==2 else 2
    #boucle principale
    while victoire(plateau.anneau_retiréJ1, plateau.anneau_retiréJ2, blitz)==False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
            liste=plateau.deplacementPossible(tourJoueur,x,y)
            while liste==False:
                liste=plateau.deplacementPossible(tourJoueur,x,y)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                nouv_x, nouv_y = event.pos
            res=plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
            while res==False:
                res=plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
        #Regarder s'il y a un alignement
        tableau_alignement=plateau.alignement()
        #Si des alignements sont enregistrés
        if len(tableau_alignement)>0:
            res=Grille.retirer_alignement(tableau_alignement, x, y, False)
            #res est le numéro du joueur qui doit retirer son anneau
            if res==1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                if isinstance(plateau._plateau[x][y],Anneau) and plateau._plateau[x][y].getJoueur()==1:
                    plateau._plateau[x][y]=0
                    plateau.anneau_retiréJ1+=1
            elif res==2:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                if isinstance(plateau._plateau[x][y],Anneau) and plateau._plateau[x][y].getJoueur()==2:
                    plateau._plateau[x][y]=0
                    plateau.anneau_retiréJ2+=1
        tourJoueur=1 if tourJoueur==2 else 2
    return plateau.anneau_retiréJ1, plateau.anneau_retiréJ2 #si la condition de victoire est remplie, envoyer les resultat pour l'écran de fin

# Pour affronter un bot
def versus_cpu():
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
    while victoire(plateau.anneau_retiréJ1, plateau.anneau_retiréJ2, blitz)==False:
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
        res=plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
        while res==False:
            x, y = 0, 0
            res=plateau.deplacerAnneau(tourJoueur,liste,x,y,nouv_x,nouv_y)
        #Regarder s'il y a un alignement
        tableau_alignement=plateau.alignement()
        #Si des alignements sont enregistrés
        if len(tableau_alignement)>0:
            res=Grille.retirer_alignement(tableau_alignement, x, y, True)
            if res==1:
                #prendre un input de joueur et si c'est l'un de ses anneaux le retirer:
                x, y = 0, 0
                if isinstance(plateau._plateau[x][y],Anneau) and plateau._plateau[x][y].getJoueur()==1:
                    plateau._plateau[x][y]=0
                    plateau.anneau_retiréJ1+=1
            #pas d'opérations pour le CPU ici, les actions sont déjà réalisées dans la fonction
        tourJoueur=1 if tourJoueur==2 else 2
        afficher_ath(tour_joueur)
        pygame.display.update()
    return plateau.anneau_retiréJ1, plateau.anneau_retiréJ2 #si la condition de victoire est remplie, envoyer les resultat pour l'écran de fin

#récupérer les infos des menus (blitz,multi,CPU)

if MainMenu.nombre_joueurs == 2:
    boucle_de_jeu()
