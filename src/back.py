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

    def deplacementPossible(self,joueur,x,y):
        """
            IN : Un anneau et ses coordonnées
            OUT : La liste des emplacements de déplacements possibles, False si ce n'est pas une case valide
        """
        largeur=len(self._plateau[0])
        hauteur=len(self._plateau)
        #Selection de l'anneau à déplacer (la selection doit être un anneau)
        if self._plateau[x][y]==Anneau and self._plateau[x][y].getJoueur()==joueur:
            liste=[]
            #Regarder aux directions voisines: ↙↓↘ ↖↑↗
            for var_x in range(-1,1):
                for var_y in range(-1,1):
                    #dans les plages du plateau
                    if 0<= x+var_x <= hauteur and 0 <= y+var_y <= largeur:
                        #si c'est une case disponible
                        if self._plateau[x+var_x][y+var_y]==self._plateau==0:
                            #l'ajouter à la liste 
                            liste.append([x+var_x][y+var_y])
                            #Continuer dans la direction jusqu'à ce que la case soit -1, un autre objet ou la limite
                            suite=2
                            while 0<=x+var_x*suite<=hauteur and 0<=y+var_y*suite<=largeur and self._plateau[x+var_x*suite][y+var_y*suite]==0:
                                liste.append([x+var_x*suite][y+var_y*suite])
                                suite+=1
                        #si c'est un marqueur
                        if self._plateau[x+var_x][y+var_y]==Marqueur:
                            #Continuer dans la direction du voisin direct jusqu'à ce qu'il y ait autre chose qu'un marqueur
                            suite=2
                            while 0<=x+var_x*suite<=hauteur and 0<=y+var_y*suite<=largeur and self._plateau[x+var_x*suite][y+var_y*suite]==Marqueur:
                                suite+=1
                            #La dernière case après la suite d'anneaux est ajoutée à la liste des emplacements possibles
                            liste.append([x+var_x*suite][y+var_y*suite])
        else:
            #La case choisie n'est pas un anneau du joueur
            return False

    def deplacerAnneau(self,joueur,liste,ancienX,ancienY,nouveauX,nouveauY):
        """
            IN : L'emplacement vers lequel l'anneau se déplace
            Modifie l'emplacement d'un anneau aux coordonnées rentréees (si elles sont valides)
            Effectue le retournement des marqueurs entre les 2 emplacements
        """
        #Si le nouvel emplacement est une case possible (fait partie de la liste)
        n_emplacement=[nouveauX][nouveauY]
        if n_emplacement in liste:
            #Met un marqueur à l'ancien emplacement de l'anneau
            self._plateau[ancienX][ancienY]=Marqueur(joueur)
            #Effectuer le déplacement
            self._plateau[nouveauX][nouveauY]=Anneau(joueur)
            #Connaître la direction pour aller de l'ancien au nouvel emplacement
            pas_x=-1 if (nouveauX - ancienX) < 0 else 1
            pas_y=-1 if (nouveauY - ancienY) < 0 else 1
            #parcourir tous les emplacements entre initial / final, si c'est un marqueur: retourner
            for ligne in range(ancienX,nouveauX,pas_x):
                for colonne in range(ancienY,nouveauY,pas_y):
                    if self._plateau[ligne][colonne]==Marqueur:
                        self._plateau[ligne][colonne].inverser()
        pass

    def placerAnneau(self,joueur,x,y):
        """
            IN : Les coordonnées d'un anneau
            OUT : False si l'emplacement n'est pas valide
            Effectue le placement d'un anneau si l'emplacement choisi est valide
        """
        #Si les coordonnées sont valides:
        if self._plateau[x][y]==0:
            #Placer l'anneau
            self._plateau[x][y]=Anneau(joueur)
        #Sinon, tant que les coordonnées ne sont pas valides:
        else:
            #préviens si le placement n'a pas été fait pour que l'anneau soit placé ailleurs
            return False

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