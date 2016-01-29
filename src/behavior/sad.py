#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time


import pypot.primitive


class SadBehave(pypot.primitive.Primitive):  
        
    def run(self):

        poppy = self.robot

        for m in poppy.r_arm:
            m.compliant = False

        poppy.head_y.goto_position(20, 3, wait=False)
        poppy.bust_y.goto_position(20, 3, wait=False)

        poppy.r_arm_z.goto_position(30, 3, wait=False)
        poppy.r_elbow_y.goto_position(-130, 3, wait=False)
        poppy.r_shoulder_y.goto_position(-65, 3, wait=False)
        poppy.r_shoulder_x.goto_position(10, 3, wait=False)

        poppy.l_arm_z.goto_position(-30, 3, wait=False)
        poppy.l_elbow_y.goto_position(-130, 3, wait=False)
        poppy.l_shoulder_y.goto_position(-60, 3, wait=False)
        poppy.l_shoulder_x.goto_position(-10, 3, wait=True)
        
        




