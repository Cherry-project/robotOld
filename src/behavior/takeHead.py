#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time

import pypot.primitive


class TakeHeadBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.l_arm + poppy.r_arm:
            m.compliant = False

        poppy.head_y.goto_position(45, 4, wait=False)

        poppy.r_shoulder_x.goto_position(-20, 4, wait=False)
        poppy.r_shoulder_y.goto_position(-100, 4, wait=False)

        poppy.l_shoulder_x.goto_position(20, 4, wait=False)
        poppy.l_shoulder_y.goto_position(-100, 4, wait=False)
        
        poppy.r_arm_z.goto_position(20, 4, wait=False)
        poppy.r_elbow_y.goto_position(-140, 4, wait=False)

        poppy.l_arm_z.goto_position(-20, 4, wait=False)
        poppy.l_elbow_y.goto_position(-140, 4, wait=True)


