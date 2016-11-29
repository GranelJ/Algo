#Type Flotte

import TypeBateau

class Flotte:
	def __init__(self,bateau1,bateau2,bateau3,bateau4,bateau5):
	#Creer une flotte de 5 bateaux
	# -> Flotte


	def Coule(self,numbateau,grille):
	#Renvoie True si le bateau de numero donne est coule et modifie le nombre de bateaux restants
	#Flotte x Bateau x Grille -> Bool

	def BateauxRestants(self):
	#Renvoie le nombre de bateaux restants
	#Flotte -> Int

	"""Proprietes:
	(1) Coule (f,1) == True => BateauxRestants(f) = BateauxRestants(f) - 1"""