#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive

from speak import Speak

class SayHello(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        self._name = 'Maximilien'

    def start(self, name):
        self._name = name

        pypot.primitive.Primitive.start(self)

    def run(self):

        text = "Bonjour, " + self._name + ". Comment vas tu aujourd'hui?"

        self._speak.start(text)