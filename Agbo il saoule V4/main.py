#-*- coding: utf-8 -*-
from resultat import * 


def changerEtat(j): # changerEtat : Joueur -> Joueur
					# Fonction permettant de faire passer le joueur dans l'etat actif s'il etait inactif et inactif s'il etait actif.
	j.modif_etat()

	return j


def entrer_position(j): # entrer_position : Joueur -> Joueur
						# Fonction qui va permettre de placer les bateaux de chaque joueur.
						# Tour à tour ils vont avoir le choix de placer leur bateaux dans la grille fictive 21*21
						# Chaque joueur possède sa propre grille fictive. Il est donc possible que les deux joueur place un bateau sur la meme position.
						# Chaque joueur possède un ensemble de bateaux, 5 bateaux : un de taille 1, un de taille 2, 1 de taille 3, 2 de taille 4.
						# Le positionnement des bateaux de taille > 1 se realise en entrant toute ses positions. (exemple : un bateau de taille 2 a deux positions à placer)
						 # >> Le positionnement de tel bateaux implique de placer chaque positions a la suite les unes des autres pour ne pas creer un bateau disloqué.
	i = 0

	# Compare le nombre de bateaux présent dans l'ensemble, à la taille de l'ensemble de bateaux qui a été donné par l'utilisateur lors de la creation.
	while j.ensbateaux().nb_bat_safe() < j.ensbateaux().tailleEB():
		ep = Enspositions(taille[i])
		b = Bateau(ep)

		print "Entrez les coordonnees du bateau de taille ",taille[i]
		p = Position(-1,-1)

		#La boucle s'effectue tant que le joueur n'a pas placé toutes ses positions (pour un bateau, ils sont toutes placer quand le nombre de position placée est egale à la taille du bateau)
		# Verifie aussi si un bateau n'est pas deja present sur la position.
		while ep.nb_position_pres() < ep.tailleEP() and not(j.ensbateaux().est_present_pos(p)):
			
			# Verifie si la position est a l'interieur de la grille 21 x 21
			while not(p.est_valide_position()) : 
				
				# Demande a l'utilisateur les coordonnées du bateau a placer.
				print "X = "
				x = int(input())
				print "Y = "
				y = int(input())
				p = Position(x,y)

			# Verifie si la position entré par l'utilisateur n'est pas deja occupée.
			# Si la position entré précedemment etait deja presente, la position n'est pas ajouter a l'ensemble.
			if not(j.ensbateaux().est_present_pos(p)):
				ep.ajouterPosition(p)
			else :
				print "Cette position est déja utilisée. Bateau impossible a creer. Veuillez entrer d'autres positions pour votre bateau "

			#end while : la position entrée est valide, c-a-d elle est contenu dans la grille fictive 21x21

		#end while : Toutes les positions du bateau ont été placées à des places valide (pas de superposition ou hors grille).

		#Ajout du bateau dans l'ensemble du bateau du Joueur.
		# ! Ajout seulement si le bateau est bien formé, c'est à dire que ses positions se suivent !
		#b.setEnspositions(ep)
		if b.bat_bien_former() and (b.positions().tailleEP() == b.taillebat()):
			j.modif_Ensbateaux(b)
			i+=1

		else :
			print "Votre bateau est mal formé. Rerentrez toutes ses coordonnees"

	#end while : Tout les bateaux ont été placés, c'est à dire le retour de nb_bat_safe est égal à la taille de l'ensemble de bateau
	
	return j # renvoie du joueur

# Creation des instances :

# 1) Création et stockage des tailles et du nombre de bateaux des joueurs.
taille=[1,2,3,4,4] 

# 2) Création de l'ensemble de bateaux du joueur : on donne en paramètre la taille du tableau (nombre de bateau de chaque joueurs)
eb1 = Ensbateaux(len(taille)) 
eb2 = Ensbateaux(len(taille)) 

# 3) Création des joueurs : on donne en paramètre l'ensemble de bateaux, ainsi qu'un boolean qui va permettre de determiner quel joueur commence a jouer
j1 = Joueur(eb1,True) 
j2 = Joueur(eb2,False)

# Appel de la fonction entrer_position pour permettre a chaque joueur de placer leur bateaux.
j1 = entrer_position(j1)
j2 = entrer_position(j2)


# Boucle principale du programme qui va s'executer tant que l'un des deux joueurs n'a pas perdu, c-a-d tout les bateaux d'un joueur ne sont pas encore detruit.
while not(j1.perdu() or j2.perdu()) :

	# Le joueur 1 est actuellement le joueur actif : c'est donc a lui de tirer
	if j1.etat :
		print(" Joueur 1 : Entrer coordonnees à frapper ")
		print "X = "
		x = int(input())
		print "Y = "
		y = int(input())

		# Création du resultat du tir : on donne en paramètre le joueur adverse et les coordonées du tir.
		res = resultat(j2,x,y)

		# affichage de la chaine de caractère renvoyée par la fonction resultat_tir (touché, touché->coulé, en vue ou a l'eau)
		print res.resultat_tir(x,y)
		
	# Le joueur 2 est actuellement le joueur actif : c'est donc a lui de tirer	
	if j2.etat :
		print(" Joueur 2 : Entrer coordonnees à frapper ")
		print "X = "
		x = int(input())
		print "Y = "
		y = int(input())

		# Création du resultat du tir : on donne en paramètre le joueur adverse et les coordonées du tir.
		res = resultat(j1,x,y)

		# affichage de la chaine de caractère renvoyée par la fonction resultat_tir (touché, touché->coulé, en vue ou a l'eau)
		print res.resultat_tir(x,y)
	
	#Fin du tour : c'est a l'autre joueur de tirer maintenant !
	# On fait appel à la fonction de changement d'etat pour passer la main au joueur inactif : il devient donc actif ici.
	# Le joueur precedemment actif quant a lui devient inactif.
	j1 = changerEtat(j1)
	j2 = changerEtat(j2)	

# end while : L'un des deux joueur a perdu, tout ses bateaux ont été detruit .

# Message de fin de partie, donne le nom du gagnant :)
if j1.perdu :
	print "Le joueur 1 a perdu, Le joueur 2 est donc le GRAND GAGNANT"

if j2.perdu : 
	print "Le joueur 2 a perdu, Le joueur 1 est donc le GRAND GAGNANT"



