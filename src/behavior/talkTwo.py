#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time


import pypot.primitive


class TalkTwoBehave(pypot.primitive.Primitive):  
        
    def run(self):

        poppy = self.robot

        for m in poppy.r_arm:
            m.compliant = False

        poppy.r_shoulder_x.goto_position(-20, 4, wait=False)
        poppy.r_elbow_y.goto_position(-20, 3, wait=False)
        poppy.r_shoulder_y.goto_position(-50, 3, wait=True)

        poppy.r_elbow_y.goto_position(-100, 3, wait=False)
        poppy.r_arm_z.goto_position(-40, 3, wait=True) #-
        
        poppy.r_elbow_y.goto_position(-60, 3, wait=False)
        poppy.r_arm_z.goto_position(20, 3, wait=True) #-

        

       


        # poppy.r_shoulder_x.goto_position(-10, 4, wait=False)
        # poppy.r_shoulder_y.goto_position(-20, 4, wait=False)
        
        # poppy.l_shoulder_x.goto_position(10, 3, wait=False)
        # poppy.l_shoulder_y.goto_position(-20, 3, wait=False)
        
        # poppy.r_arm_z.goto_position(70, 4, wait=False)
        # poppy.r_elbow_y.goto_position(-100, 4, wait=False)

        # poppy.l_arm_z.goto_position(-100, 3, wait=False)
        # poppy.l_elbow_y.goto_position(-120, 3, wait=True)



