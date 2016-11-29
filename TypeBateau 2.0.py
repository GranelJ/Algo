#Type Bateau

class Bateau:
	def __init__(self,colonne,ligne,taille,num,direction): 
	#Creer un bateau de taille donnee, avec un numero donne, une direction donnee, aux coordonnees donnees
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
