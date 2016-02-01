#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
#import json
import time

# from pypot.vrep import from_vrep
#from init import virtual_robot

import pypot.primitive
from pypot.primitive.utils import Sinus

class NoBehave(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)
        
        self.my_sinus = Sinus(self.robot, 50, [self.robot.head_z, ], amp=20, freq=0.9, offset=0, phase=0)

    def setup(self):
        self.robot.head_y.compliant = False

        self.my_sinus.start()

    def teardown(self):
        self.my_sinus.stop()

    def update(self):
        pass

