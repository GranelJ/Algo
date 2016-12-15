#-*- coding: utf-8 -*-
from position import *

class Enspositions :
	def __init__(self,tailleEP): # creer_ensposition : Int -> Ensposition
		self.taille = tailleEP
		self.liste_positions = []
		self.nb_position_restantes = 0
				 # Constructeur du type Ensposition. Permet d'avoir l'ensemble de positions d'un bateau.
								 # nb_position_pres(creer_Ensposition()) = 0
		
	def positions(self):# positions : Ensposition -> [ Position ].
		return self.liste_positions			# C'est l'ensemble des positions présentes dans le type posiiton. Il est vide lorsqu'on crée un Enspositions 
						# positions(creer_Ensposition(t : Int)) -> vide

	def tailleEP(self): # tailleEP : Enspositions -> int
		return self.taille			# C'est la taille de l'ensemble de positions. Donc le nombre de position max
						# tailleEP(creer_Ensposition(t : Int)) = t

	def ajouterPosition(self,Position): # ajouterPosition : Ensposition * Position -> Ensposition 
		if len(self.liste_positions) > self.taille or not Position.est_valide_position():
			print("Nombre de positions maximal atteint ou Position invalide")
			return self
		else :
			self.liste_positions = self.liste_positions + [Position]
			self.nb_position_restantes=self.nb_position_restantes+1
			return self.liste_positions						# Renvoie l'ensemble de position d'un bateau avec la positionn passée en parametre rajoutée a cet ensemble
									    # ajouterPosition(Ensp , position) ->  0 < nb_position_pres(Ensp) < tailleEP(Ensp)
										# Si la position n'est pas bonne ne l'ajoute pas dans l'ensemble

	def est_present_posit(self,Position): # est_present_posit : Ensposition * Position -> bool
		for k in range(len(self.liste_positions)):
			if (self.liste_positions[k].absice() == Position.absice()) and (self.liste_positions[k].ordonnee() == Position.ordonnee()) :
				return True
		return False							  # permet de vérifier qu'une position appartient a l'ensemble de positions passé en parametre
										  # est_present_posit(creer_Ensposition(),Position) = False


	def nb_position_pres(self): # nb_position_pres : Ensposition -> Int 
		return self.nb_position_restantes
							    # Renvoi le nombre de positions non touchées de l'ensemble de position
								# nb_position_pres(Ensp) = 0 --> toutes les position touchées ou aucune position dans l'ensemble de positions
								# nb_position_pres(creer_Ensposition()) = 0
								# S'incremente lorqu'on rajoute une position dans l'ensemble de positions

	def reduire_nb_position_pres(self): # modif_nb_position_pres : Ensposition -> Ensposition
		self.nb_position_restantes=self.nb_position_restantes-1
		return self
							  # Modifie le nombre de positions presente dans l'ensemble de positions passé en paramètre.
									  # Diminue de 1 le nombre de position presentes dans l'ensemble de position
									  # nb_position_pres(Ensp) = 0 --> reduire_nb_position_pres(self)  = erreur





						
	

#Tests unitaires
"""
Ens = Enspositions(3)
p = Position(1,2)
pos1 = Position(2,3)
pos2 = Position(2,26)
Ens.ajouterPosition(p)
Ens.ajouterPosition(pos1)
Ens.ajouterPosition(pos2) 
print Ens.est_present_posit(p)  # Doit renvoyer True
print Ens.est_present_posit(pos1) # Doit renvoyer True
print Ens.est_present_posit(pos2) # Doit renvoyer False
print Ens.nb_position_pres() == 2 # Doit renvoyer True
Ens.reduire_nb_position_pres();
print Ens.nb_position_pres() == 1 
print Ens.tailleEP() == 3 # Doit renvoyer True"""