#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time

import pypot.primitive

class TakeRightEarBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.head + poppy.r_arm:
            m.compliant = False

        poppy.head_y.goto_position(10, 3, wait=False)
        poppy.head_z.goto_position(20, 3, wait=False)

        poppy.r_shoulder_x.goto_position(-20, 3, wait=False)
        poppy.r_shoulder_y.goto_position(-100, 3, wait=False)
        
        poppy.r_arm_z.goto_position(10, 3, wait=False)
        poppy.r_elbow_y.goto_position(-140, 3, wait=True)


