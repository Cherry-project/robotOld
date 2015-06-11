#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive
import pypot.robot
import random
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak

class MultipRand(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        self._move = "../src/moveRecorded/multip.move"

    def run(self):

        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False

        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        sol = num2*num1

        if num1 == 1 :
            text1 = "un"
        elif num1 == 2 :
            text1 = "deux"
        elif num1 == 3 :
            text1 = "trois"
        elif num1 == 4: 
            text1 = "quatre"
        elif num1 == 5:
            text1 = "cinq"
        elif num1 == 6:
            text1 = "six"
        elif num1 == 7:
            text1 = "sept"
        elif num1 == 8:
            text1 = "huit"
        elif num1 == 9:
            text1 = "neuf"
        elif num1 == 10:
            text1 = "dix"
        else:
            text1 = "un"

        if num2 == 1:
            text2 = "un"
        elif num2 == 2:
            text2 = "deux"
        elif num2 == 3:
            text2 = "trois"
        elif num2 == 4:
            text2 = "quatre"
        elif num2 == 5:
            text2 = "cinq"
        elif num2 == 6:
            text2 = "six"
        elif num2 == 7:
            text2 = "sept"
        elif num2 == 8:
            text2 = "huit"
        elif num2 == 9:
            text2 = "neuf"
        elif num2 == 10:
            text2 = "dix"
        else:
            text2 = "un"


        print (sol)
        print "Lancer vrai1 si le patient répond bien, faux il se trompe."

        text = "Dis moi, combien font " + text1 + "fois " + text2 + "?"
        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(0.5)

        self._speak.start(text)
        
        # while True :
        #     rep = raw_input()
        #     #rep=input("réponse :")

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

        #         self._speak.start("Bravo! Quel génie mathématique!")
        #         break
