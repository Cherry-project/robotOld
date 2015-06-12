#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive
import pypot.robot
import random
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak

class Mime(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        self._move = "../src/moveRecorded/mime.move"
        self._movem1 = "../src/moveRecorded/singe.move"
        self._movem2 = "../src/moveRecorded/poulet.move"
        self._movem3 = "../src/moveRecorded/nager.move"
        self._movem4 = "../src/moveRecorded/manger.move"
        #self._moveo = "../src/moveRecorded/faux.move"
        #self._moven = "../src/moveRecorded/vrai4.move"

    def run(self):

        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False

        num1 = random.randint(1,4)
        

        if num1 == 1 :
            text1 = "singe"
            mouvement = self._movem1
        elif num1 == 2 :
            text1 = "poulet"
            mouvement = self._movem2
        elif num1 == 3 :
            text1 = "nager"
            mouvement = self._movem3
        elif num1 == 4: 
            text1 = "manger"
            mouvement = self._movem4
        else:
            text1 = "singe"
            mouvement = self._movem1

        print (text1)
        print "lancer vrai4 si le patient répond bien, faux si il se trompe."


        text = "Devine ce que je mime."
        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(0.5)

        self._speak.start(text)

        time.sleep(3)

        with open(mouvement) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        

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

        #         self._speak.start("Bravo! Tu as vu comme je suis bon acteur?")
        #         break