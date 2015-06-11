#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive
import pypot.robot
import random
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak

class Egal(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        self._move = "../src/moveRecorded/vrai1.move"


    def run(self):

        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False

        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(1.5)
        self._speak.start("Bien joué! On croirait presque que tu lis dans mes électrons!")