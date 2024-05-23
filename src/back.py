class Joueur:
    def __init__(self):
        #Compteur d'anneaux retirés
        self._anneauRetire=0
    
    def getAnneauRetire(self):
        return self._anneauRetire

class Marqueur:
    def __init__(self,joueur):
        self._joueur=joueur

    def getJoueur(self):
        return self._joueur
    
    def inverser(self):
        #pour Sofyan
        self._joueur=1 if self._joueur==2 else 2

class Anneau:
    def __init__(self,joueur):
        self._joueur=joueur

    def getJoueur(self):
        return self._joueur

class Grille:
    def __init__(self):
        self._plateau = [

            ]

    def deplacerAnneau(self,nouveauX,nouveauY):
        """
            IN : Un pion et ses coordonnées
            Modifie l'emplacement d'un anneau aux coordonnées rentrées (si elles sont valides)
        """
        #Met un marqueur à l'ancien emplacement de l'anneau
        #Si un anneau a des marqueurs autour de lui il peut aller jusqu'à après les marqueurs suivants
            #Si le marqueur est passé au dessus d'un ou plusieurs marqueurs ils sont retournés
        
        #NO CODE:
        #Selection de l'anneau à déplacer (la selection doit être un anneau)
        #Enregistrer la position pour y mettre un marqueur du joueur (retirer l'anneau)
        #Regarder à :
            #directions voisines
            #en enregistrant si l'un de ses emplacements est un marqueur voisin
        #Pour les directions n'ayant pas de voisin direct:
            #Continuer dans la direction jusqu'à ce que la case soit None, un autre objet ou la limite
            #Enregistrer les emplacements possibles dans une liste
        #Pour les cases étant un voisin direct:
            #Continuer dans la direction du voisin direct jusqu'à ce qu'il y ait autre chose qu'un anneau
            #La dernière case après la suite d'anneaux est ajouté à la liste des emplacements possibles
        #La liste des emplacements possibles étant complète on regarde si l'emplacement séléctionné fait parti des emplacements possibles, sinon redemander l'input
        pass

    def placerAnneau(self,joueur,x,y):
        """
            IN : Les coordonnées d'un anneau
        """
        #C'est à Adam le GOAT de le faire
        pass

    def alignement(self):
        """
            Vérifier s'il y a un alignement et faire les actions en conséquence
        """
        #parcourir tout le plateau
        #si il y au moins 5 marqueur du même joueur à la suite en colonne, ligne, diagonale ↙↗
        #ajoute 1 au compteur d'alignement
        #S'il y a 1 alignement :
            #Le joueur qui possède ces 5 marqueurs les retire ainsi qu'un de ses anneaux (il choisit)
        #S'il y en a plus :
            #Le joueur qui selectionne l'alignement à retirer, ainsi qu'un seul de ses anneaux
        pass

class Jeu:
    def __init__(self):
        self._blitz=False

    def victoire(slef,blitz,joueur):
        if blitz==True:
            return joueur.getAnneauRetire()==1
        else:
            return joueur.getAnneauRetire()==3
    
    def boucleDeJeu(self):
        #selection des paramètres (Blitz, etc.)
        #création de la grille
        plateau=Grille()
        #chaque joueur place ses 5 anneaux
        tourJoueur=1
        for i in range(5):
            #INPUT de X et Y par le click
            x=0 #prendre l'input x du joueur
            y=0 #prendre l'input y du joueur
            plateau.placerAnneau(tourJoueur,x,y)
            tourJoueur=1 if tourJoueur==2 else 2
        while self.victoire(self._blitz,tourJoueur)==False:
            #INPUT de X et Y par le click
            #Le joueur du tour choisis un anneau qui sera déplacé
            #Placer un marqueur à X et Y
            #INPUT de nouvX et nouvY (un emplacement valide pour le déplacement de l'anneau) par le click
            #Regarder s'il y a un alignement
            plateau.alignement()
        pass