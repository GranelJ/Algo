#Type Grille

import TypeBateau

class Grille:
	def __init__(self,hauteur,largeur):
	#Creer une grille avec un nombre de ligne et de colonne donnes
	#pre : hauteur et largeur > 0
	# -> Grille

	def ValeurCoord(self,colonne,ligne):
	#Renvoie la valeur de la coordonnee
	#pre : colonne et ligne >0
	#Grille x Int x Int -> Int

	def Touche(self,colonne,ligne):
	#Renvoie True si position donnee est occupee par un bateau et modifie la valeur de la position à 0
	#pre : colonne et ligne >0
	#Grille x Int x Int -> Bool

	def EnVue(self,colonne,ligne):
	#Renvoie True si un bateau est en vue
	#pre : colonne et ligne >0
	#Grille x Int x Int -> Bool

	def ModifVal(self,val,colonne,ligne):
	#Modifie la valeur aux coordonnees donne par la valeur donnee
	#pre : colonne et ligne >0
	#Grille x Int x Int x Int -> Grille 

	def Verification(self, bateau):
	#Renvoie True si le bateau peut etre positionne
	#Grille x Bateau -> Bool

	def PositionnerBateau(self, bateau):
	#Place un bateau donne dans une grille donnee
	#Grille x Bateau -> Grille


	"""Propriétés:
	(1) : Positionnerbateau(b,g)  => Vérification(b,g) == True 
    (2) Touche(g,1,2) == True => ModifVal(g,0,1,2) """