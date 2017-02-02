#!/usr/bin/env python)
# -*- coding: utf-8 -*-

import time
import sys
import os
import pypot.primitive
from pypot.primitive.move import MoveRecorder, Move, MovePlayer
import json
from random import randint
from pprint import pprint


class PlayMove(pypot.primitive.Primitive):

	properties = pypot.primitive.Primitive.properties + ['movement']
	def __init__(self, robot, movement = None):
		
			pypot.primitive.Primitive.__init__(self, robot)
			self._movement  =None
			self._robot = robot

	#def start(self, text):
	def start(self):
		
			pypot.primitive.Primitive.start(self)


	def run(self):

		#time.sleep(1)
		move_player = MovePlayer(self._robot, self._movement)
		move_player.start()

					
	@property
	def movement(self):
		return self._movement
	@movement.setter
	def movement(self, movement):

		#if type(movement) == 'dict':
			#print "Ceci est un dict"
		print type(movement)
		#movement.encode('utf-8')
		pprint(movement)
		m = Move.create(movement)
		print type(m)
		self._movement = m
		#else:
		#	print "Ceci est une chaine de caractère"
		#	print movement
