#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time


import pypot.primitive


class SaluteBehave(pypot.primitive.Primitive):  
        
    def run(self):

        poppy = self.robot

        for m in poppy.r_arm:
            m.compliant = False

        poppy.head_y.goto_position(10, 4, wait=False)
        poppy.r_arm_z.goto_position(0, 4, wait=False)
        poppy.r_elbow_y.goto_position(-30, 4, wait=False)
        poppy.r_shoulder_y.goto_position(-100, 4, wait=True)


        poppy.r_elbow_y.goto_position(0, 4, wait=False)
        poppy.r_shoulder_y.goto_position(0, 4, wait=True)



