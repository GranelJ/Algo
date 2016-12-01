#Test unitaire

import TypeBateau
import TypeJoueur 
import TypeFlotte
import TypeGrille

def test_bateau():
	bateau = TypeBateau.Bateau(11,10,3,1,0)
	assert TypeBateau.NumeroBateau(bateau) == 1
	assert TypeBateau.TailleBateau(bateau) == 3
	assert TypeBateau.DirectionBateau(bateau) == 0
	assert TypeBateau.LigneBateau(bateau) == 10
	assert TypeBateau.ColonneBateau(bateau) == 11
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
	assert TypeJoueur.Flottejoueur() == flotte
	assert TypeJoueur.Grillejoueur() == grille
	return True

def test_Grille():
	grille = TypeGrille.Grille(21,21)
	bateau1 = TypeBateau.Bateau(1,5,1,1,0)
	bateau2 = TypeBateau.Bateau(21,1,1,1)
	assert TypeGrille.Verification(bateau1) == True
	assert TypeGrille.Verification(bateau2) == False
	TypeBateau.PositionnerBateau(bateau1)
	assert TypeGrille.ValeurCoord(1,5) == 1
	assert TypeGrille.ValeurCoord(21,21) == 0
	assert TypeGrille.EnVue(1,8) == True
	assert TypeGrille.EnVue(12,5) == True
	assert TypeGrille.EnVue(12,15) == False
	TypeGrille.ModifVal(4,15,15)
	assert TypeGrille.ValeurCoord(15,15) == 4
	assert TypeGrille.Touche(1,5) == True
	assert TypeGrille.ValeurCoord(1,5) == 0
	return True

def test_Flotte():
	bateau1 = TypeBateau.Bateau(1,5,1,1,0)
	bateau2 = TypeBateau.Bateau(3,10,2,2,0)
	bateau3 = TypeBateau.Bateau(10,15,3,3,1)
	bateau4 = TypeBateau.Bateau(15,17,3,4,0)
	bateau5 = TypeBateau.Bateau(8,9,4,5,1)
	grille = TypeGrille.Grille(21,21)
	flotte = TypeFlotte.Flotte(bateau1,bateau2,bateau3,bateau4,bateau5)
	assert TypeFlotte.BateauxRestants() == 5
	grille = TypeGrille.ModifVal(0,1,5)
	assert TypeFlotte.Coule(1,grille) == True
	assert TypeFlotte.BateauxRestants() == 4
	assert TypeFlotte.Coule(4,grille) == False
	return True