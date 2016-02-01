#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time

import pypot.primitive

class TakeLeftEarBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.head + poppy.l_arm:
            m.compliant = False

        poppy.head_y.goto_position(10, 3, wait=False)
        poppy.head_z.goto_position(-20, 3, wait=False)

        poppy.l_shoulder_x.goto_position(20, 3, wait=False)
        poppy.l_shoulder_y.goto_position(-100, 3, wait=False)
        
        poppy.l_arm_z.goto_position(-10, 3, wait=False)
        poppy.l_elbow_y.goto_position(-140, 3, wait=True)


