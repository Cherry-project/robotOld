#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


class Devinette(pypot.primitive.Primitive):
    def __init__(self, robot):
            pypot.primitive.Primitive.__init__(self, robot)
            self._robot = robot
        

    def start(self):
            
            pypot.primitive.Primitive.start(self)

    def run(self):
     
                move = '/home/poppy/cherry/resources/optional/move/devinette.move'
        
                with open(move) as f:
                    m = Move.load(f)
                    
                self._robot.compliant = False
                
                speak.start("J’ai une devinette pour toi, ça te dis ?" ) 
                
                move_player = MovePlayer(self._robot, m)
                time.sleep(1)
                move_player.start()
