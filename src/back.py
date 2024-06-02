import random

class Joueur:
    def __init__(self,numero):
        #Compteur d'anneaux retirés
        self.anneauRetire=0
        self.numero=numero
    
    def getAnneauRetire(self):
        return self.anneauRetire

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
        """ -1: hors plateau / -2: case morte / 0: case libre"""
        self._plateau = [
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
        self.anneau_retiréJ1=0
        self.anneau_retiréJ2=0

    def deplacementPossible(self,joueur,x,y):
        """
            IN : Un anneau et ses coordonnées
            OUT : La liste des emplacements de déplacements possibles, False si ce n'est pas une case valide
        """
        largeur=len(self._plateau[0])
        hauteur=len(self._plateau)
        #Selection de l'anneau à déplacer (la selection doit être un anneau)
        if isinstance(self._plateau[x][y],Anneau) and self._plateau[x][y].getJoueur()==joueur:
            liste=[]
            #Regarder aux directions voisines: ↙↓↘ ↖↑↗
            variations=[(-2,0),(2,0),(-1,-1),(-1,1),(1,-1),(1,1)]
            for var_x, var_y in variations:
                nouv_x, nouv_y = x+var_x, y+var_y
                #dans les plages du plateau, si c'est une case disponible
                while 0<=nouv_x<hauteur and 0<=nouv_y<largeur and self._plateau[nouv_x][nouv_y]==0:
                    liste.append([nouv_x,nouv_y])
                    nouv_x+=var_x
                    nouv_y+=var_y
                #si c'est un marqueur
                if 0<=nouv_x<hauteur and 0<=nouv_y<largeur and isinstance(self._plateau[nouv_x][nouv_y], Marqueur):
                    nouv_x+=var_x
                    nouv_y+=var_y
                    if 0<=nouv_x<hauteur and 0<=nouv_y<largeur and self._plateau[nouv_x][nouv_y]==0:
                        liste.append([nouv_x,nouv_y])
            return liste
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
        else:
            return False

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
            OUT : La liste des alignements
        """
        taille_ligne=len(self._plateau)
        taille_colonne=len(self._plateau[0])
        alignementJ1=0
        alignementJ2=0
        tableau_alignement=[]
        for joueur in range(1,2):
            compteur=0
            #Vérification colonne
            for colonne in range(taille_colonne):
                #Si c'est une colonne paire, commencer à 0
                if colonne%2==0:
                    for ligne in range(0, taille_ligne, 2):
                        ligne_alignement=[]
                        #Si c'est un marqueur du joueur, incrémenter le compteur, sinon relancer le compteur
                        if self._plateau[ligne][colonne]==Marqueur and self._plateau[ligne][colonne].getJoueur()==joueur:
                            ligne_alignement.append([ligne,colonne])
                            compteur+=1
                            if compteur>=5:
                                tableau_alignement.append(ligne_alignement)
                        else:
                            ligne_alignement=[]
                            compteur=0
                #Si c'est une colonne impaire, commencer à 1
                else:
                    for ligne in range(1, taille_ligne, 2):
                        if self._plateau[ligne][colonne]==Marqueur and self._plateau[ligne][colonne].getJoueur()==joueur:
                            ligne_alignement.append([ligne,colonne])
                            compteur+=1
                            if compteur>=5:
                                tableau_alignement.append(ligne_alignement)
                        else:
                            ligne_alignement=[]
                            compteur=0
            #Vérification diagonale ↙↗
            for ligne in range(taille_ligne):
                compteur=0
                for colonne in range(taille_colonne):
                    #Si on tombe sur un marqueur du joueur
                    if self._plateau[taille_ligne][taille_colonne]==Marqueur and self._plateau[ligne][colonne].getJoueur()==joueur:
                        compteur+=1
                        #Si une suite est lancée
                        while compteur>0:
                            if ligne+compteur<=taille_ligne and colonne+compteur<=taille_colonne:
                                if self._plateau[ligne+compteur][colonne+compteur]==Marqueur and self._plateau[ligne+compteur][colonne+compteur].getJoueur()==joueur:
                                    ligne_alignement.append([ligne,colonne])
                                    compteur+=1
                                    if compteur>=5:
                                        tableau_alignement.append(ligne_alignement)
                                else:
                                    ligne_alignement=[]
                                    compteur=0
            #Vérification diagonale ↖↘
            for ligne in range(taille_ligne):
                compteur=0
                for colonne in range(taille_colonne,0,-1):
                    #Si on tombe sur un marqueur du joueur
                    if self._plateau[taille_ligne][taille_colonne]==Marqueur and self._plateau[ligne][colonne].getJoueur()==joueur:
                        compteur+=1
                        #Si une suite est lancée
                        while compteur>0:
                            if ligne+compteur<=taille_ligne and colonne-compteur>=0:
                                if self._plateau[ligne+compteur][colonne-compteur]==Marqueur and self._plateau[ligne+compteur][colonne-compteur].getJoueur()==joueur:
                                    ligne_alignement.append([ligne,colonne])
                                    compteur+=1
                                    if compteur>=5:
                                        tableau_alignement.append(ligne_alignement)
                                else:
                                    ligne_alignement=[]
                                    compteur=0
        return tableau_alignement

def retirer_alignement(self, tableau_alignement, x, y, CPU):
    """
        IN : Les listes d'alignements des 2 joueurs, les coordonnées d'un marqueur, la présence d'un CPU
        OUT : False si le marqueur ne fait pas partie d'un alignement,
            Le joueur auquel appartenait l'alignement
        Si le marqueur fait bien partie d'un alignement, retirer cet alignement
    """
    #Connaître à qui appartient le pion
    joueur=self._plateau[x,y].getJoueur()
    if joueur==1 or (joueur==2 and CPU==False):
        #Si le joueur n'a pas séléctionné un de ses marqueurs
        if self._plateau[x,y]!=Marqueur:
            return False
        #Vérifier que x,y soit dans l'une des listes
        for listes in tableau_alignement:
            for liste in listes:
                if x in liste and y in liste:
                    alignement=listes
        #Retirer tous les marqueurs aux emplacements correspondants
        for positions in alignement:
            self._plateau[positions[0]][positions[1]]=0
        #Le joueur à qui appartenait le marqueur sélectionne un anneau à retirer
        return joueur
    #S'il appartient à un CPU
    if CPU==True:
        #Trouver un alignement appartenant au CPU
        for listes in tableau_alignement:
            for liste in listes:
                if self._plateau[liste[0],liste[1]].getJoueur()==2:
                    alignement=listes
        #Retirer tous les marqueurs aux emplacements correspondants
        for positions in alignement:
            self._plateau[positions[0]][positions[1]]=0
        #Retirer le premier anneau du CPU trouvé
        for ligne in range(len(self._plateau)):
            for colonne in range (len(self._plateau[0])):
                if self._plateau[ligne][colonne]==Anneau and self._plateau[ligne][colonne].getJoueur()==2:
                    #Augmenter le compteur d'anneaux retirés du CPU
                    self.anneau_retiréJ2+=1
                    self._plateau[ligne][colonne]=0
                    return 2
    return False

class Jeu:
    def __init__(self,blitz):
        self.blitz=blitz
  
    def victoire(alignementJ1,alignementJ2,blitz):
        if blitz==True:
            if alignementJ1>0:
                return 1
            elif alignementJ2>0:
                return 2
        else:
            if alignementJ1>2:
                return 1
            elif alignementJ2>2:
                return 2
        return False
        
def coordonnee_alea(max_x,max_y):
    """
        Prends en entrée les dimensions du plateau, renvoie des coordonnées aléatoires pour le bot
    """
    x = random.randint(0, max_x - 1)
    y = random.randint(0, max_y - 1)
    return x, y
