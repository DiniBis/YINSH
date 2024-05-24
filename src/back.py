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
        self._joueur=1 if self._joueur==2 else 2

class Anneau:
    def __init__(self,joueur):
        self._joueur=joueur

    def getJoueur(self):
        return self._joueur

class Grille:
    def __init__(self):
        self._plateau = [""" -1: hors plateau / -2: case morte / 0: case libre"""
            [-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1], #0
            [-1,-1,-1, 0,-2, 0,-2, 0,-1,-1,-1], #1
            [-1,-1, 0,-2, 0,-2, 0,-2, 0,-1,-1], #2
            [-1, 0,-2, 0,-2, 0,-2, 0,-2, 0,-1], #3
            [-1,-2, 0,-2, 0,-2, 0,-2, 0,-2,-1], #4
            [-1, 0,-2, 0,-2, 0,-2, 0,-2, 0,-1], #5
            [ 0,-2, 0,-2, 0,-2, 0,-2, 0,-2, 0], #6
            [-2, 0,-2, 0,-2, 0,-2, 0,-2, 0,-2], #7
            [ 0,-2, 0,-2, 0,-2, 0,-2, 0,-2, 0], #8
            [-2, 0,-2, 0,-2, 0,-2, 0,-2, 0,-2], #9
            [ 0,-2, 0,-2, 0,-2, 0,-2, 0,-2, 0], #10
            [-2, 0,-2, 0,-2, 0,-2, 0,-2, 0,-2], #11
            [ 0,-2, 0,-2, 0,-2, 0,-2, 0,-2, 0], #12
            [-1, 0,-2, 0,-2, 0,-2, 0,-2, 0,-1], #13
            [-1,-2, 0,-2, 0,-2, 0,-2, 0,-2,-1], #14
            [-1, 0,-2, 0,-2, 0,-2, 0,-2, 0,-1], #15
            [-1,-1, 0,-2, 0,-2, 0,-2, 0,-1,-1], #16
            [-1,-1,-1, 0,-2, 0,-2, 0,-1,-1,-1], #17
            [-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1], #18
            ]

    def deplacerAnneau(self,joueur,ancienX,ancienY,nouveauX,nouveauY):
        """
            IN : Un pion et ses coordonnées
            Modifie l'emplacement d'un anneau aux coordonnées rentrées (si elles sont valides)
        """
        #Met un marqueur à l'ancien emplacement de l'anneau
        self._plateau[ancienX][ancienY]=Marqueur(joueur)
        #Si un anneau a des marqueurs autour de lui il peut aller jusqu'à après les marqueurs suivants
            #Si le marqueur est passé au dessus d'un ou plusieurs marqueurs ils sont retournés
        #NO CODE:
        #Selection de l'anneau à déplacer (la selection doit être un anneau)
        #Enregistrer la position pour y mettre un marqueur du joueur (retirer l'anneau)
        #Regarder à :
            #directions voisines
            #en enregistrant si l'un de ses emplacements est un marqueur voisin
        #Pour les directions n'ayant pas de voisin direct:
            #Continuer dans la direction jusqu'à ce que la case soit -1, un autre objet ou la limite
            #Enregistrer les emplacements possibles dans une liste
        #Pour les cases étant un voisin direct:
            #Continuer dans la direction du voisin direct jusqu'à ce qu'il y ait autre chose qu'un anneau
            #La dernière case après la suite d'anneaux est ajouté à la liste des emplacements possibles
        #La liste des emplacements possibles étant complète on regarde si l'emplacement séléctionné fait parti des emplacements possibles, sinon redemander l'input
        #Envoyer la liste des positions à l'affichage,
        #Récupérer l'emplacement qui a été choisi parmis la liste,
        #Effectuer le déplacement et si des marqueurs ont été survolés, les retourner avec marqueur.inverser
            #parcourir tous les emplacements entre initial / final, si c'est un marqueur: retourner
        pass

    def placerAnneau(self,joueur,x,y):
        """
            IN : Les coordonnées d'un anneau
        """
        #Si les coordonnées sont valides:
        if self._plateau[x][y]==0:
            #Placer l'anneau
            self._plateau[x][y]=Anneau(joueur)
        #Sinon, tant que les coordonnées ne sont pas valides:
            #demander à nouveau les coordonnées
        pass

    def alignement(self):
        """
            Vérifier s'il y a un alignement et faire les actions en conséquence
            OUT : Le joueur qui a un alignement (s'il y en a un)
        """
        taille_ligne=len(self._plateau)
        taille_colonne=len(self._plateau[0])
        alignementJ1=0
        alignementJ2=0
        for joueur in range(1,2):
            compteur=0
            #Vérification colonne
            for colonne in range(taille_colonne):
                #Si c'est une colonne paire, commencer à 0
                if colonne%2==0:
                    for ligne in range(0, taille_ligne, 2):
                        #Si c'est un marqueur du joueur, incrémenter le compteur, sinon relancer le compteur
                        if self._plateau[ligne][colonne]==Marqueur:
                            if self._plateau[ligne][colonne].getJoueur()==joueur:
                                compteur+=1
                                if compteur>=5 and joueur==1:
                                    alignementJ1+=1
                                elif compteur>=5 and joueur==2:
                                    alignementJ2+=1
                        else:
                            compteur=0
                #Si c'est une colonne impaire, commencer à 1
                else:
                    for ligne in range(1, taille_ligne, 2):
                        if self._plateau[ligne][colonne]==Marqueur:
                            if self._plateau[ligne][colonne].getJoueur()==joueur:
                                compteur+=1
                                if compteur>=5 and joueur==1:
                                    alignementJ1+=1
                                elif compteur>=5 and joueur==2:
                                    alignementJ2+=1
                        else:
                            compteur=0
            #Vérification diagonale ↙↗
            for ligne in range(taille_ligne):
                compteur=0
                for colonne in range(taille_colonne):
                    #Si on tombe sur un marqueur du joueur
                    if self._plateau[taille_ligne][taille_colonne]==Marqueur:
                        if self._plateau[ligne][colonne].getJoueur()==joueur:
                            compteur+=1
                            #Si une suite est lancée
                            while compteur>0:
                                if ligne+compteur<taille_ligne and colonne+compteur<taille_colonne:
                                    if self._plateau[ligne+compteur][colonne+compteur]==Marqueur and self._plateau[ligne+compteur][colonne+compteur].getJoueur()==joueur:
                                        compteur+=1
                                        if compteur>=5 and joueur==1:
                                            alignementJ1+=1
                                        elif compteur>=5 and joueur==2:
                                            alignementJ2+=1
                                    else:
                                        compteur=0
            #Vérification diagonale ↖↘
            for ligne in range(taille_ligne):
                compteur=0
                for colonne in range(taille_colonne,0,-1):
                    #Si on tombe sur un marqueur du joueur
                    if self._plateau[taille_ligne][taille_colonne]==Marqueur:
                        if self._plateau[ligne][colonne].getJoueur()==joueur:
                            compteur+=1
                            #Si une suite est lancée
                            while compteur>0:
                                if ligne+compteur<taille_ligne and colonne-compteur<0:
                                    if self._plateau[ligne+compteur][colonne-compteur]==Marqueur and self._plateau[ligne+compteur][colonne-compteur].getJoueur()==joueur:
                                        compteur+=1
                                        if compteur>=5 and joueur==1:
                                            alignementJ1+=1
                                        elif compteur>=5 and joueur==2:
                                            alignementJ2+=1
                                    else:
                                        compteur=0
            #S'il y a 1 alignement :
                #Le joueur qui possède ces 5 marqueurs les retire ainsi qu'un de ses anneaux (il choisit)
            #S'il y en a plus :
                #Le joueur qui selectionne l'alignement à retirer, ainsi qu'un seul de ses anneaux
            #ces dernières options sûrement dans une nouvelle fonction, où l'utilisateur selectionne une case et on supprime tous les marqueurs si c'est bien un alignement
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
        #selection des paramètres (Blitz, etc.) dans les menus
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
        #boucle principale
        while self.victoire(self._blitz,tourJoueur)==False:
            #INPUT de X et Y par le click
            #Le joueur du tour choisis un anneau qui sera déplacé
            #Placer un marqueur à X et Y
            #INPUT de nouvX et nouvY (un emplacement valide pour le déplacement de l'anneau) par le click
            #Regarder s'il y a un alignement
            plateau.alignement()
        pass
