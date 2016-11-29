#Type Grille

import TypeBateau

class Grille:
	def __init__(self,hauteur,largeur):
	#Creer une grille avec un nombre de ligne et de colonne donnés
	#pre : hauteur et largeur >0
	# -> Grille

	def ValeurCoord(self,colonne,ligne):
	#Renvoie la valeur de la coordonnée
	#pre : colonne et ligne >0
	#Grille x Int x Int -> Int

	def Touche(self,colonne,ligne):
	#Renvoie True si position donnée est occupée par un bateau
	#pre : colonne et ligne >0
	#Grille x Int x Int -> Bool

	def EnVue(self,colonne,ligne):
	#Renvoie True si un bateau est en vue
	#pre : colonne et ligne >0
	#Grille x Int x Int -> Bool

	def ModifVal(self,val,colonne,ligne):
	#Modifie la valeur aux coordonnées donné par la valeur donnée
	#pre : colonne et ligne >0
	#Grille x Int x Int x Int -> Grille 

	def Verification(self, bateau):
	#Renvoie True si le bateau peut être positionné
	#Grille x Bateau -> Bool

	def PositionnerBateau(self, bateau):
	#Place un bateau donné dans une grille donnée
	#Grille x Bateau -> Grille

	"""Propriétés:
	(1) : Positionnerbateau(b,g)  => Vérification(b,g) == True 
    (2) Touche(g,1,2) == True => ModifVal(g,0,1,2) """