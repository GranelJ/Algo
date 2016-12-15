#-*- coding: utf-8 -*-
from ensbateaux import *
class Joueur:
	
	def __init__(self,Ensbateaux,etat): # creer_joueur : Ensbateaux x Bool -> Joueur
										# Creation d'un joueur qui prend en paramètre l'ensemble de bateaux du joueur et un boolean qui permet de savoir si c'est au tour du joueur de jouer (if TRUE)
		self.bat = Ensbateaux
		self.state = etat 							
							# Initialisé a faux au depart

	def ensbateaux(self): # ensbateaux : Joueur -> Ensbateaux
						  # Renvoie l'ensemble de bateaux du joueur
		return self.bat 

	def etat(self): # etat : Joueur -> Bool
					# Renvoie l'etat dans lequel se trouve le joueur actuellement.
		return self.state		# True s'il est actif, False sinon
					# etat(creer_joueur(eb,false)) = false
		

	def modif_Ensbateaux(self,bateaux): # modif_Ensbateaux : Bateau -> Ensbateaux
										# Permet d'ajouter le bateau passé en parametre à l'ensemble de bateaux du Joueur

		return Ensbateaux.ajouterBateau(self.bat, bateaux)

	def modif_etat(self):  # modif_etat : Joueur -> Joueur
						   # Renvoi le joueur avec son état passé a inactif si il était actif et a actif s'il était inactif
		if self.etat() :
			self.state = False
		else :
			self.state = True
		return self 
		

 	def perdu(self): # perdu : Joueur -> Bool
 					 # Renvoie True si le joueur a perdu c'est a dire que tout ses bateaux ont été touchés.
 		return Ensbateaux.nb_bat_safe(self.bat)	== 0

	

#Test unitaire
"""
ensp= Enspositions(2)
p=Position(1,2)
p2=Position(5,6)
ensp.ajouterPosition(p)
ensp.ajouterPosition(p2)
bat = Bateau(ensp)
eb = Ensbateaux(1)
eb.ajouterBateau(bat)
j = Joueur(eb,False)
print j.etat() # Doit renvoyer False
j.modif_etat()
print j.etat() # Doit renvoyer True
print j.perdu() # Doit renvoyer False"""

		
		


