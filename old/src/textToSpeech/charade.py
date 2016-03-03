#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive
import pypot.robot
import random
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak

class Charade(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        self._move = "../src/moveRecorded/charade.move"

    def run(self):

        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False

        print "robot"
        print "lancer vrai2 si le patient répond bien, faux si il se trompe."

        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(1.5)

        self._speak.start("J'ai une charade pour toi. Mon premier est un bruit malpoli. Mon deuxième est très joli. Mon tout est ce que je suis. Qui suis-je?")

        

        #while pas appuie sur o

        # while True :
        #     rep = raw_input()

        # #if appuie sur n
        #     if rep == "n" :

        #         with open(self._moven) as f :

        #          m = Move.load(f)
    
        #         move_player = MovePlayer(self.robot, m)
        #         move_player.start()
        
        #         time.sleep(1.5)

        #         self._speak.start("Non, ce n'est pas ça. Essaye encore!")

        # #if appuie sur r
        #     elif rep == "r" :

        #         with open(self._mover) as f :

        #             m = Move.load(f)
    
        #         move_player = MovePlayer(self.robot, m)
        #         move_player.start()
        
        #         time.sleep(1.5)

        #         self._speak.start("D'accord, je te répète la charade.")

        #         with open(self._move) as f :

        #             m = Move.load(f)
    
        #         move_player = MovePlayer(self.robot, m)
        #         move_player.start()
        
        #         time.sleep(1.5)

        #         self._speak.start("Mon premier est un bruit malpoli. Mon deuxième est très joli. Mon tout est ce que je suis!")

        # #sortie while
        #     elif rep == "o" :
        #         with open(self._moveo) as f :

        #             m = Move.load(f)
    
        #         move_player = MovePlayer(self.robot, m)
        #         move_player.start()
        
        #         time.sleep(1.5)

        #         self._speak.start("Bravo! C'est bien Robot!")
        #         break