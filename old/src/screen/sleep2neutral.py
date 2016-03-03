#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pygame
from pygame.locals import *
import pypot.primitive


class Sleep2neutral(pypot.primitive.Primitive):

	def start(self, fenetre):

		#Chargement et collage image supplémentaire
		im1 = pygame.image.load("../src/screen/animation/sleepy_a/im1.jpg").convert_alpha()
		im2 = pygame.image.load("../src/screen/animation/sleepy_a/im2.jpg").convert_alpha()
		im2_5 = pygame.image.load("../src/screen/animation/sleepy_a/im2_5.jpg").convert_alpha()
		im3 = pygame.image.load("../src/screen/animation/sleepy_a/im3.jpg").convert_alpha()
		im4 = pygame.image.load("../src/screen/animation/sleepy_a/im4.jpg").convert_alpha()
		im5 = pygame.image.load("../src/screen/animation/sleepy_a/im5.jpg").convert_alpha()
		im5_5 = pygame.image.load("../src/screen/animation/sleepy_a/im5_5.jpg").convert_alpha()
		im6 = pygame.image.load("../src/screen/animation/sleepy_a/im6.jpg").convert_alpha()
		im7 = pygame.image.load("../src/screen/animation/sleepy_a/im7.jpg").convert_alpha()
		im8 = pygame.image.load("../src/screen/animation/sleepy_a/im8.jpg").convert_alpha()

		t1 = 0.09
		t2 = 0.3
		t3 = 0.2


		fenetre.blit(im8, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t3)

		fenetre.blit(im7, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t3)

		fenetre.blit(im6, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t3)

		fenetre.blit(im5_5, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t3)

		fenetre.blit(im5, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t3)

		fenetre.blit(im5_5, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t3)

		fenetre.blit(im6, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t3)

		fenetre.blit(im7, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t2)

		fenetre.blit(im6, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t1)

		fenetre.blit(im5_5, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t1)

		fenetre.blit(im5, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t1)

		fenetre.blit(im4, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t1)

		fenetre.blit(im3, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t1)

		fenetre.blit(im2_5, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t1)

		fenetre.blit(im2, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t1)

		fenetre.blit(im1, (0,0))  #afficher aux coordonnées (,)
		pygame.display.flip()  
		time.sleep(t1)