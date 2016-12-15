#-*- coding: utf-8 -*-
from bateau import *

class Ensbateaux :


	def __init__(self,tailleEB): 
		self.taille = tailleEB
		self.lbateaux = []
		self.Bateaux_Restants=0		 # creer_Ensbateaux : int  -> Ensbateau
				 # renvoie un ensemble de bateaux vide avec comme taille l'entier passé en parametre
								 # le nombre de bateaux present a la creation est de 0 et le nombre de bateaux vivant est egalement 0 
		

	def tailleEB(self) : # taille : Ensbateaux -> int
		return	self.taille		 # Renvoi la taille de l'ensemble de bateaux passé en paramètre
					     # tailleEB(creer_Ensbateau(n)) = n

	def bateaux(self): # bateau : Ensbateaux -> [Bateau]
		return	self.lbateaux	   # Renvoie l'ensemble de bateaux contenue dans le tye Ensbateaux passé en paramètre


	def ajouterBateau(self,bateau): # ajouterBateau : Ensbateaux * Bateau -> Ensbateaux
		self.lbateaux=self.lbateaux+[bateau]
		self.augmente_nb_bat_safe()
		self.taille=self.taille+1
		return	self.lbateaux			    # Ajoute le bateau passé en parametre à la liste des bateau et renvoi l'ensbateaux modifié
									# ajouterBateau(bat) -> 0 < nb_bat_safe() < tailleEB
									# Le nombre de bateaux non détruit est incrémenté de 1

	def safe_bateau(self,Bateau): # safe_bateaux : Ensbateaux * Bateau -> bool 
		for i in range(0,len(self.lbateaux)):
			if self.lbateaux[i]==Bateau:
				return not self.lbateaux[i].est_detruit()
		return	False		  		  # Renvoi TRUE si le bateau présent dans l'ensemble de bateaux n'est pas détruit, FALSE si le bateau n'est pas détruit ou n'appartient pas a l'ensemble
					  			  # safe_bateau(bat) == TRUE --> nb_bat_safe() > 0 
					  			  # safe_bateau(bat) == FALSE --> On ne verifie plus ses position lors d'un tir

	def est_present_pos(self,position): # est_present_pos : Ensbateaux * Position -> bool
		for i in range(0,len(self.lbateaux)):
			if (self.lbateaux[i]).position_appartient(position):
				return True
		return False					# Renvoi TRUE si la position passee en paramètre appartient a un bateau de l'ensemble de bateaux. FALSE sinon. Sera utile pour le tir et pour verifier si une position n'est pas déja utilisée par un bateau
										# est_present_pos(pos) == TRUE -> pos n'appartient pas a un bateau detruit

	def nb_bat_safe(self): # nb_bat_safe : Ensbateaux -> Int
		return	self.Bateaux_Restants	   # Renvoi le nombre de bateaux de l'ensemble de bateaux qui ne sont pas encore détruit. Utile pour savoir si un joueur n'as plus de bateaux valides. Sert egalement lors de l'ajout des bateaux a la flotte
						   # nb_bat_safe(creer_Ensbat()) = 0

	def reduire_nb_bat_safe(self): # modif_nb_bat_safe : Ensbateaux -> Ensbateaux
		self.Bateaux_Restants=self.Bateaux_Restants-1
		return self		     # Modifie le nombre de bateaux non détruit dans l'ensemble de bateaux passé en paramètre 
								 # Décremente le nombre de bateaux non détruit


	def augmente_nb_bat_safe(self) : # augmente_nb_bat_safe : Ensbateaux -> Ensbateaux
		self.Bateaux_Restants=self.Bateaux_Restants+1
		return self				     # Modifie le nombre de bateaux non détruit dans l'ensemble de bateaux passé en paramètre 
								 	 # Incremente le nombre de bateaux non détruit
								 	 # Lorsqu'on ajoute un bateau on fait appel a cette fonction

# Test unitaires

"""
ensp= Enspositions(2)
p=Position(1,2)
p2=Position(5,6)
ensp.ajouterPosition(p)
ensp.ajouterPosition(p2)
bat = Bateau(ensp)
eb = Ensbateaux(1)
eb.ajouterBateau(bat)
print eb.tailleEB()==2 # Doit renvoyer True
print eb.safe_bateau(bat) # Doit renvoyer True
print eb.est_present_pos(p) # Doit renvoyer True
print eb.nb_bat_safe()  == 1 # Doit renvoyer True
	"""

	
	
	
	
	

				
