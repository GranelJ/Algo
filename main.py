import TypeGrille
import TypeBateau
import TypeFlotte
import TypeJoueur

def Main():
    print("Joueur1 veuillez posez vos bateaux :")
    GrilleJoueur1=TypeGrille.Grille(21,21)
    Joueur1=InitJoueur(GrilleJoueur1)
    GrilleJoueur1.Affichage()
    print("Joueur2 veuillez posez vos bateaux :")
    GrilleJoueur2=TypeGrille.Grille(21,21)
    Joueur2=InitJoueur(GrilleJoueur2)
    GrilleJoueur2.Affichage()
    cpt=1
    while Joueur1.FlotteJoueur().BateauxRestants()>0 and Joueur2.FlotteJoueur().BateauxRestants()>0:
        if cpt%2==1:
            print("C'est au tour de Joueur 1")
            Joueur2=TourDeJeu(Joueur2)
        else:
            print("C'est au tour de Joueur 2")
            Joueur1=TourDeJeu(Joueur1)
        cpt=cpt+1
    if Joueur1.FlotteJoueur().BateauxRestants()==0:
        print("Jeu terminé ! Victoire de Joueur 2 !")
    else:
        print("Jeu terminé ! Victoire de Joueur 1 !")


def TourDeJeu(joueur):
#Données : Prend le joueur auquel ce n'est pas le tour
#Résultat : Effectue un tour de jeu : demande des coordonnées de tir, vérifie si le tir est touché, à l'eau ou en vue. Dans le cas où le bateau est touché, verifie si ce bateau est coulé. Renvoie le joueur modifié.
    print("Donnez la coordonnée X de tir :")
    TirX=int(input())
    print("Donnez la coordonnée Y de tir :")
    TirY=int(input())
    if joueur.GrilleJoueur().Touche(TirX,TirY):
        tmp=joueur.GrilleJoueur().ValeurCoord(TirX,TirY)
        joueur.GrilleJoueur().ModifVal(0,TirX,TirY)
        print("Touché !")
        if joueur.FlotteJoueur().Coule(tmp,joueur.GrilleJoueur()):
            print("Coulé !")
            print("Nombre de bateaux restants : ",end=" ")
            print(joueur.FlotteJoueur().BateauxRestants())
    elif joueur.GrilleJoueur().EnVue(TirX,TirY):
        print("En Vue !")
    else:
        print("A l'eau !")
    return joueur
    
        
    
        
def InitJoueur(Grille):
#Données: prend une grille
#Résultat : retourne un joueur qui a une flotte et une grille avec les 5 bateaux placés
    Bateau1=AjouterBateau(1,1,Grille)
    Grille.PositionnerBateau(Bateau1)
    Bateau2=AjouterBateau(2,2,Grille)
    Grille.PositionnerBateau(Bateau2)
    Bateau3=AjouterBateau(3,3,Grille)
    Grille.PositionnerBateau(Bateau3)
    Bateau4=AjouterBateau(3,4,Grille)
    Grille.PositionnerBateau(Bateau4)
    Bateau5=AjouterBateau(4,5,Grille)
    Grille.PositionnerBateau(Bateau5)
    Flotte=TypeFlotte.Flotte(Bateau1,Bateau2,Bateau3,Bateau4,Bateau5)
    Joueur=TypeJoueur.Joueur(Flotte,Grille)
    return Joueur


def AjouterBateau(taille,numero,grille):
#Données: prend une taille de bateau, un numéro de bateau et une grille
#Résultat: Demande les coordonnées et la direction d'un bateau et renvoie le bateau créer si la position est valide, retourne la fonction sinon
#P1 : taille>0
#P2 : numero>0
    print("Entrez la colonne du bateau numero ",end=" ")
    print(numero,end=" ")
    print(" de taille ",end=" ")
    print(taille)
    PosX=int(input())
    print("Entrez la ligne du bateau numero ",end=" ")
    print(numero,end=" ")
    print(" de taille ",end=" ")
    print(taille)
    PosY=int(input())
    print("Entrez la direction du bateau numero ",end=" ")
    print(numero,end=" ")
    print(" de taille ",end=" ")
    print(taille,end=" ")
    print("(0 pour horizontale et 1 pour verticale)")
    Direction=int(input())
    Bateau=TypeBateau.Bateau(PosX,PosY,taille,numero,Direction)
    if grille.Verification(Bateau):
        print("Bateau bien positionner")
        return Bateau
    else:
        print("Position invalide, recommencer")
        return AjouterBateau(taille,numero,grille)

    
if __name__ == '__main__':
    Main()
