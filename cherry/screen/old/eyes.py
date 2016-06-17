#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pygame
from pygame.locals import *
import pypot.primitive



class Eyes(pypot.primitive.Primitive):

	def start(self):

		pygame.init()

		#Création de la fenêtre
		fenetre = pygame.display.set_mode((800, 480))  #résolution manga screen ok prévoir supprimer resizable, FULLSCREEN  ??

		#charge et colle le fond 
		#".convert" : affichage plus rapide
		im_neutral = pygame.image.load("../src/screen/static/neutral.jpg").convert()
		im_sleepy = pygame.image.load("../src/screen/static/sleepy.jpg").convert()
		im_angry = pygame.image.load("../src/screen/static/angry.jpg").convert()
		im_happy = pygame.image.load("../src/screen/static/happy.jpg").convert()
		im_sad = pygame.image.load("../src/screen/static/sad.jpg").convert()
		im_surprise = pygame.image.load("../src/screen/static/surprised.jpg").convert()
		
		fond = im_surprise

		fenetre.blit(fond, (0,0))	
		pygame.display.flip()  



		#Variable qui continue la boucle si = 1, stoppe si = 0
		continuer = 1
		f_old = 1 #expression neutre de base
		r_old = 0 #pas de reaction de base
		
		#BOUCLE INFINIE
		while continuer:

			time.sleep(0.2)
			#Appel fonction qui check f (fond) et r (réaction) pour actualisation
			r = self.robot.get_reaction.start()
			f = self.robot.get_fond.start()
			
			#AFFICHAGE FOND
			if f != f_old:
				print("b")

				if f == "1":
					print("c")
					#appel fonction transition d'expression
					fond = im_neutral
					print("neutral")
					
				if f == "2":
					print("d")
					self.robot.neutral2sleep.start(fenetre)
					print("e")
					fond = im_sleepy
					print("sleepy")
					
				if f == "3":
					#appel fonction transition d'expression
					fond = im_surprise
					print("surprise")
					
				if f == "4":
					#appel fonction transition d'expression
					fond = im_happy
					
				if f == "5":
					#appel fonction transition d'expression
					fond = im_angry
					
				if f == "6":
					#appel fonction transition d'expression
					fond = im_sad
				
				print("f")	
				f_old = f
				print("g")		
				fenetre.blit(fond, (0,0))
				print("h")	
				pygame.display.flip()
				print("i")

				

		# Valeures de f
		# 	f=1 fond neutre
		# 	f=2 fond sleep
		# 	f=3 fond surprise
		# 	f=4 fond heureux
		# 	f=5 fond en colère
		# 	f=6 fond triste


			# #AFFICHAGE REACTION PONCTUELLE
			# if r != r_old:

			# 	print(r)

			# 	if r == "1":
			# 		if f == "1":  #si fond neutre
			# 			#appel fonction blink
			# 			self.robot.blink.start(fenetre)
			# 		if f == "3":
			# 			#appel blink surprise
			# 			print("f=3 et je blink de surprise")

			# 	if r == "2":
			# 		#appel fonction wink_r
			# 		print("f=3 et wink_r")
				
			# 	if r == "3":
			# 		#appel fonction wink_l
			# 		print("f=3 et wink_l")

			# 	if r == "4":
			# 		self.robot.sad.start(fenetre)
			# 		print("f=3 et sad")

			# 	if r == "5":
			# 		#appel fonction angry
			# 		print("f=3 et je suis en colère")

			# 	if r == "6":
			# 		self.robot.surprise.start(fenetre)
			# 		print("f=3 et je suis surpris")

			# 	if r == "7":
			# 		self.robot.happy.start(fenetre)
			# 		print("f=3 et je suis heureux")

			# 	r_old = r

			# 	fenetre.blit(fond, (0,0))	
			# 	pygame.display.flip()

		# Valeures de r
		# 	? r=0 rien ne se passe
		# 	r=1 blink (neutral et surprise)
		# 	r=2 wink_r
		# 	r=3 wink_l
		# 	r=4 sad qques secondes
		# 	r=5 angry qques secondes
		# 	r=6 surpris qques secondes
		# 	r=7 happy qques secondes


			


