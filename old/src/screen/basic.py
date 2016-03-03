#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pygame
from pygame.locals import *
import pypot.primitive



class Basic(pypot.primitive.Primitive):

	def start(self):

		pygame.init()
		
		#Création de la fenêtre
		fenetre = pygame.display.set_mode((800, 480))  #résolution manga screen ok prévoir supprimer resizable, FULLSCREEN  ??

		#charge et colle le fond 
		#".convert" : affichage plus rapide
		fond = pygame.image.load("../src/screen/static/neutral.jpg").convert()
		fenetre.blit(fond, (0,0))	
		pygame.display.flip()

		#Variable qui continue la boucle si = 1, stoppe si = 0
		continuer = 1
		
		
		#BOUCLE INFINIE
		while continuer:
			
			for event in pygame.event.get():  

			# !!!!!!! CLAVIER EN QWERTY !!!!!!!!!!!
				if event.type == KEYDOWN:
					
					if event.key == K_q: #touche a 
						continuer = 0
					
					if event.key == K_w:  #touche z
						print("sad")
						fond = pygame.image.load("../src/screen/static/sad.jpg").convert()

					if event.key == K_e: #touche e
						print("surprise")
						self.robot.surprise.start(fenetre)

					if event.key == K_r:  #touche r
						print("blink")
						self.robot.blink.start(fenetre)

					if event.key == K_t: #touche t
						print("happy")
						fond = pygame.image.load("../src/screen/static/happy.jpg").convert()

					if event.key == K_y:  #touche y
						print("sleepy")
						self.robot.sleepy.start(fenetre)

					if event.key == K_u: #touche u
						print("n2happy")
						self.robot.neutral2happy.start(fenetre)

					if event.key == K_i: #touche i
						print("n2sad")
						self.robot.neutral2sad.start(fenetre)

				fenetre.blit(fond, (0,0))	
				pygame.display.flip()



#----------------------------------------------------------------------------------------
# pygame.init()


# #Création de la fenêtre
# fenetre = pygame.display.set_mode((800, 480))  #résolution manga screen ok prévoir supprimer resizable, FULLSCREEN  ??

# #charge et colle le fond 
# #".convert" : affichage plus rapide
# fond = pygame.image.load("static/neutral.jpg").convert()
# fenetre.blit(fond, (0,0))	

# #rafraichissement écran
# pygame.display.flip()  


# #Variable qui continue la boucle si = 1, stoppe si = 0
# continuer = 1

# #BOUCLE INFINIE
# continuer = 1
# while continuer:
# 	for event in pygame.event.get():  

# # !!!!!!! CLAVIER EN QWERTY !!!!!!!!!!!
# 		if event.type == KEYDOWN:
			
# 			if event.key == K_q: #touche a 
# 				continuer = 0
			
# 			if event.key == K_w:  #touche z
# 				print("blink")
				
# 			if event.key == K_e: #touche e
# 				print("sleepy")
				
					

# 			#remettre fond après un délais
# 			fenetre.blit(fond, (0,0))		
# 			time.sleep(0.4)
# 			pygame.display.flip()  











