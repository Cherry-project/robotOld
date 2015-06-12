#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import tkSimpleDialog

import pypot.primitive
import pypot.robot
import random
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak

class Faux(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        self._move = "../src/moveRecorded/faux.move"


    def run(self):

        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False
        
        with open(self._move) as f :
            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(2)

        self._speak.start("Non, ce n'est pas ça. Essaye encore!")