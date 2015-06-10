#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive
import pypot.robot
import random
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak

class PlusMoins(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        self._move = "../src/moveRecorded/hello.move"
        self._movep = "../src/moveRecorded/hello.move"
        self._movem = "../src/moveRecorded/hello.move"
        self._movee = "../src/moveRecorded/hello.move"

    def run(self):

        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False

        num = random.randint(1,100)

        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(1.5)

        self._speak.start("Essaye de deviner à quel nombre je pense. Il est compris entre 1 et 100")

        print (num)
        print "appuyer sur + ou - ou = suivant la réponse du patient, puis sur entrée"

    

        while True :
            rep = raw_input()

        #si appuie sur +
            if rep == "+" :
                with open(self._movep) as f :

                    m = Move.load(f)
    
                move_player = MovePlayer(self.robot, m)
                move_player.start()
        
                time.sleep(1.5)

                self._speak.start("Hé non, mon nombre est plus grand. Essaye encore!")

        #else si appuie sur -
            elif rep == "-" :
                with open(self._movem) as f :

                    m = Move.load(f)
    
                move_player = MovePlayer(self.robot, m)
                move_player.start()
        
                time.sleep(1.5)

                self._speak.start("Dommage, mon nombre est plus petit. Essaye encore!")

        #fin while (appuie =)
            elif rep == "=" :

                with open(self._movee) as f :

                    m = Move.load(f)
    
                move_player = MovePlayer(self.robot, m)
                move_player.start()
        
                time.sleep(1.5)

                self._speak.start("Bien joué! On croirait presque que tu lis dans mes électrons!")
                break





       