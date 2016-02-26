#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive
import pypot.robot
import random
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak

class Dictee(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        self._move = "../src/moveRecorded/dictee.move"

    def run(self):

        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False

        num1 = random.randint(1,10)
        

        if num1 == 1 :
            text1 = "Cherry"
        elif num1 == 2 :
            text1 = "papillon"
        elif num1 == 3 :
            text1 = "maison"
        elif num1 == 4: 
            text1 = "arbre"
        elif num1 == 5:
            text1 = "feuille"
        elif num1 == 6:
            text1 = "école"
        elif num1 == 7:
            text1 = "hôpital"
        elif num1 == 8:
            text1 = "lit"
        elif num1 == 9:
            text1 = "table"
        elif num1 == 10:
            text1 = "éléphant"
        else:
            text1 = "Cherry"

        print (text1)
        print "alancer vrai3 si le patient répond bien, faux si il se trompe."


        text = "Dis moi comment on écrit " + text1 + "."
        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(1)

        self._speak.start(text)
        

        # while True :
        #     rep = raw_input()
        #     #if appuie sur n
        #     if rep == "n" :

        #         with open(self._moven) as f :

        #             m = Move.load(f)
    
        #         move_player = MovePlayer(self.robot, m)
        #         move_player.start()
        
        #         time.sleep(1.5)

        #         self._speak.start("Non, ce n'est pas ça. Essaye encore!")

        #     elif rep == "o" :
        #         with open(self._moveo) as f :

        #             m = Move.load(f)
    
        #         move_player = MovePlayer(self.robot, m)
        #         move_player.start()
        
        #         time.sleep(1.5)

        #         self._speak.start("Bravo! Tu t'y connais en orthographe!")
        #         break