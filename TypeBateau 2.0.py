#Type Bateau

class Bateau:
	def __init__(self,colonne,ligne,taille,num,dir): 
	#Creer un bateau de taille donnée, avec un numéro donné, une direction donnée, aux coordonnées données
	#pre : 21 > colonne >= 0
	#pre : 21 > ligne  >= 0
	#pre : 0 < taille < 5
	#pre : dir = 0 si le bateau est horizontal, 1 sinon
	# -> Bateau

	def NumeroBateau(self):
	#Renvoie le numero du bateau
	#Bateau -> Int

	def TailleBateau(self):
	#Renvoie la taille du bateau
	#Bateau -> Int

	def DirectionBateau(self):
	#Renvoie 0 si le bateau est horizontal, 1 sinon
	#Bateau -> Int

	def LigneBateau(self):
	#Renvoie la ligne du bateau
	#Bateau -> Int
	
	def ColonneBateau(self):
	#Renvoie la colonne du bateau
	#Bateau -> Int

	def ModifLigneBateau(self, Nligne):
	#Modifie la ligne du bateau
	#pre: 21 > Nligne >= 0
	
	def ModifColonneBateau(self, Ncolonne):
	#Modifie la colonne du bateau
	#pre: 21 > Ncolonne >= 0