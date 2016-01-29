#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time


import pypot.primitive


class ThinkBehave(pypot.primitive.Primitive):  
        
    def run(self):

        poppy = self.robot
       
        poppy.head_y.compliant = False
        poppy.head_z.compliant = False

        for m in poppy.r_arm:
           m.compliant = False

        poppy.head_y.goto_position(-10, 4, wait=False)
        poppy.head_z.goto_position(-20, 4, wait=False)
        
        
        poppy.r_arm_z.goto_position(35, 4, wait=False)
        poppy.r_elbow_y.goto_position(-130, 4, wait=False)
        poppy.r_shoulder_y.goto_position(-60, 4, wait=True)

