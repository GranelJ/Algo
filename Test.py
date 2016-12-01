#Test unitaire

import TypeBateau
import TypeJoueur 
import TypeFlotte
import TypeGrille

def Main():
        test_bateau()
        test_Joueur()
        test_Grille()
        test_Flotte()

        
def test_bateau():
	bateau = TypeBateau.Bateau(11,10,3,1,0)
	assert bateau.NumeroBateau() == 1
	assert bateau.TailleBateau() == 3
	assert bateau.DirectionBateau() == 0
	assert bateau.LigneBateau() == 10
	assert bateau.ColonneBateau() == 11
	print("Test Bateau validé !")
	return True



def test_Joueur():
	bateau1 = TypeBateau.Bateau(1,5,1,1,0)
	bateau2 = TypeBateau.Bateau(3,10,2,2,0)
	bateau3 = TypeBateau.Bateau(10,15,3,3,1)
	bateau4 = TypeBateau.Bateau(15,17,3,4,0)
	bateau5 = TypeBateau.Bateau(8,9,4,5,1)
	grille = TypeGrille.Grille(21,21)
	flotte = TypeFlotte.Flotte(bateau1,bateau2,bateau3,bateau4,bateau5)
	joueur = TypeJoueur.Joueur(flotte,grille)
	assert joueur.FlotteJoueur() == flotte
	assert joueur.GrilleJoueur() == grille
	print("Test Joueur validé !")
	return True

def test_Grille():
	grille = TypeGrille.Grille(21,21)
	bateau1 = TypeBateau.Bateau(1,5,1,1,0)
	bateau2 = TypeBateau.Bateau(20,1,1,2,1)
	assert grille.Verification(bateau1) == True
	assert grille.Verification(bateau2) == True
	grille.PositionnerBateau(bateau1)
	assert grille.ValeurCoord(1,5) == 1
	assert grille.ValeurCoord(20,20) == 0
	assert grille.EnVue(1,8) == True
	assert grille.EnVue(12,5) == True
	assert grille.EnVue(12,15) == False
	grille.ModifVal(4,15,15)
	assert grille.ValeurCoord(15,15) == 4
	assert grille.ValeurCoord(1,5)== 1
	assert grille.Touche(1,5) == True
	print("Test Grille validé !")
	return True

def test_Flotte():
	bateau1 = TypeBateau.Bateau(1,5,1,1,0)
	bateau2 = TypeBateau.Bateau(3,10,2,2,0)
	bateau3 = TypeBateau.Bateau(10,15,3,3,1)
	bateau4 = TypeBateau.Bateau(15,17,3,4,0)
	bateau5 = TypeBateau.Bateau(8,9,4,5,1)
	grille = TypeGrille.Grille(21,21)
	grille.PositionnerBateau(bateau1)
	grille.PositionnerBateau(bateau2)
	grille.PositionnerBateau(bateau3)
	grille.PositionnerBateau(bateau4)
	grille.PositionnerBateau(bateau5)
	flotte = TypeFlotte.Flotte(bateau1,bateau2,bateau3,bateau4,bateau5)
	assert flotte.BateauxRestants() == 5
	grille.ModifVal(0,1,5)
	assert flotte.Coule(1,grille) == True
	assert flotte.BateauxRestants() == 4
	assert flotte.Coule(4,grille) == False
	print("Test Flotte validé !")
	return True

if __name__=='__main__':
        Main()
