#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser
import pypot.primitive

class EyeHappyBehave(pypot.primitive.Primitive):

	def __init__(self, robot):
		pypot.primitive.Primitive.__init__(self, robot)
		self._robot = robot
		self.color = 'blue'
		self.eye = 'neutral'

	def run(self):
		poppy = self.robot
		webbrowser.open("127.0.0.2:8888/eye.pih/happy/blue")