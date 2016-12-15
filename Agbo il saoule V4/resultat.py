#-*- coding: utf-8 -*-
from joueur import *

class Resultat : 
	def __init__(self,joueur,x,y): 	# creer_resultat : Joueur x Int * Int -> Resultat
		self.player = joueur
		self.coordtirX = x
		self.coordtirY = y							# Creation d'un resultat qui prend en paramètre le joueur adverse ainsi que les coordonnées du tir du joueur actif.

		

	def joueur(self): # joueur : Resultat -> Joueur
					  # Renvoie le joueur adverse sur lequel on veut travailler.
		return self.joueur

					  # Propiétés du type 
					  # Le joueur visé est forcement inactif au moment de l'appel de resultat. 
					  # joueur(creer_resultat(j,x,y)) = j 

	

	def absice_tir(self): # absice_tir : Resultat -> Int
		return self.coordtirX			  # Renvoi l'absice x du tir.
						  # absice_tir(creer_resultat(j,x,y)) = x

	def ordonnee_tir(self): # ordonnee_tir : Resultat -> Int
		return self.coordtirY				    # Renvoi l'ordonnee x du tir.
						    # ordonnee_tir(creer_resultat(j,x,y)) = y

	def resultat_tir(self): # resultat_tir : Resultat -> String 
		p = Position(self.absice_tir(),self.ordonnee_tir())
		if p.est_valide_position() :
			for k in range (0,((self.player).ensbateaux()).tailleEB()):
				if ((self.player).ensbateaux().bateaux()[k].est_toucher(self.absice_tir(),self.ordonnee_tir())) :
					l = (self.player).ensbateaux().bateaux()[k].positions() #liste des positions du bateau k
					i = int(0)
					while (Position.absice(l[i]) != self.absice_tir()) or (Position.ordonnee(l[i]) != self.ordonnee_tir()) :
						i = i + 1
					if Position.toucher(l[i]) :
						return "Touché"
						if (self.player).ensbateaux().bateaux()[k].est_detruit() :
							return "Coulé"
					else :
						return "A l'eau"
				elif (self.player).ensbateaux().bateaux()[k].est_envue(self.absice_tir(),self.ordonnee_tir()) :
					return "En Vue"
				else :
					return "A l'eau"
		else :
			return "A l'eau"				 # Renvoie une chaine de caractère pouvant correspondre a :
								 # - Si les coordonnees de tir sont a l'interieur de la grille
								 	# - Si le tir correspond extactement a l'une des positions d'un des bateaux du joueur adverse (verifier pour chaque bateau dans leur ensemble de position -> fonction dans la classe bateau) ALORS	
								 		# Si la position n'a pas deja été touché
								 			#	>>> RENVOIE "Touché"" <<<
								 			# Si apres toute les positions du bateaux on été touché ALORS
								 				# >>> RENVOIE "coulé "<<<

								 		# - Sinon 
								 			# >>> RENVOIE "a l'eau "<<<


									# - Sinon Si le tir a touché l'une des deux coordonnées d'une position d'un bateau du joueur adverse ALORS
								 			# >>> RENVOIE "En Vue" <<<
								 	# - Sinon 
							 				# >>> RENVOIE "a l'eau" <<<
							 	# - Sinon
							 			# >>> RENVOIE "a l'eau" <<<

								# PS: La chaine sera ensuite affiché dans le main, l'affichage ne se fait pas ici !


#Test unitaire
'''
ensp = Enspositions(2)
p = Position(1,2)
p2 = Position(5,6)
ensp.ajouterPosition(p)
ensp.ajouterPosition(p2)
bat = Bateau(ensp)
eb = Ensbateaux(1)
eb.ajouterBateau(bat)
j = Joueur(eb,False)
res = Resultat(j,6,8)
res2 = Resultat(j,1,4)
res3 = Resultat(j,1,2)
#print res.joueur().etat() # Doit renvoyer False car on travaille sur le joueur inactif
print res.resultat_tir() # Doit renvoyer a l'eau
print res2.resultat_tir() # Doit renvoyer En vue
print res3.resultat_tir() # Doit renvoyer Touché coulé'''






		



				
