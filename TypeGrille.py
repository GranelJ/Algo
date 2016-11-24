#Type Grille


import "TypeBateau"


class Grille:
	"""docstring for Grille"""
	def __init__(self,hauteur,largeur):
	#Creer une grille avec un nombre de ligne et de colonne donnés
	#pre:hauteur et largeur >0

	

	def ValeurCoord(self,colonne,ligne):
	#Renvoie la valeur de la coordonnée
	#colonne et ligne >0

	def Touche(self,colonne,ligne):
	#Renvoie True si position donnée est occupée par un bateau et modifie l’état de cette positionne
	#colonne et ligne >0

	def EnVue(self,colonne,ligne):
	#Renvoie True si un bateau est en vue
	#colonne et ligne >0

	def ModifVal(self,val,colonne,ligne):
	#Modifie la valeur aux coordonnées donné par la valeur donnée
	#colonne et ligne >0

	def Verification(self, bateau):
	#Renvoie True si le bateau peut être positionné

	def PositionnerBateau(self, bateau):
	#Place un bateau donné dans une grille donnée

	"""(1) : Positionnerbateau(b,g)  => Vérification(b,g) == True 
	   (2) Touche(1,2,g) == True => ModifVal(1,2,0,g) """
