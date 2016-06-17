#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pygame
from pygame.locals import *
import pypot.primitive



class Get_reaction(pypot.primitive.Primitive):

	def start(self):

		#Variable qui continue la boucle si = 1, stoppe si = 0
		continuer = 1
		reaction = 1

		f = file("../src/screen/get_fond.txt","r")    # ouvrir le fichier
		chaine = f.read()                   # le charger dans une chaine de caractères
		f.close()                           # fermer le fichier
		reaction = chaine[-1]
		
		return reaction	


