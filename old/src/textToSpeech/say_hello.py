#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak

class SayHello(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        self._name = 'Maximilien'
        self._move = "../src/moveRecorded/hello.move"

    def start(self, name):
        self._name = name

        pypot.primitive.Primitive.start(self)

    def run(self):

        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False

        text = "Bonjour, " + self._name + ". Comment vas tu aujourd'hui?"
        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(1.5)

        self._speak.start(text)
