#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser
import pypot.primitive

class EyeBehave(pypot.primitive.Primitive):

	properties = pypot.primitive.Primitive.properties + ['color','mood']

	def __init__(self, robot,color = "blue",mood ="neutral"):
		pypot.primitive.Primitive.__init__(self, robot)
		self._robot = robot
		self._color = color
		self._mood = mood

	def run(self):
		poppy = self.robot
		#url = "127.0.0.1/eye.pih/" + self._mood + "/" + self._color
		#webbrowser.open(url)
		data = '{"color" : "'+self._color+'", "mood" : "'+self._mood+'"}';
		file = open("screen/eye.json","w")
		file.write(data)
		file.close()


	@property
	def color(self):
	    return self._color

	@color.setter
	def color(self,color):
		print color
		self._color = color

	@property
	def mood(self):
		return self._mood

	@mood.setter
	def mood(self,mood):
		print mood
		self._mood = mood