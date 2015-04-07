#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time


import pypot.primitive
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak

class SayText(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        

    def start(self, textfile):
        self._text = textfile
        print textfile
        file = open(self._text, 'r')

        for line in file :
            
            print "ligne!"
            phrase = line.split('.')
            for item in phrase :
                print item

                self._speak.start(item)

        file.close()

    def run(self):

        print "run"
        
       
