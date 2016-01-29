#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time


import pypot.primitive


class BowBehave(pypot.primitive.Primitive):

    def run(self):

        poppy = self.robot

        for m in poppy.r_arm:
            m.compliant = False

        poppy.head_y.goto_position(0, 4, wait=False)

        poppy.r_arm_z.goto_position(90, 4, wait=False)
        poppy.r_elbow_y.goto_position(-100, 4, wait=False)
        poppy.r_shoulder_y.goto_position(-80, 4, wait=False)

        poppy.l_shoulder_x.goto_position(60, 4, wait=False)
        poppy.l_arm_z.goto_position(70, 4, wait=True)


        poppy.head_y.goto_position(30, 4, wait=False)
        poppy.r_shoulder_y.goto_position(-90, 4, wait=False)
        poppy.bust_y.goto_position(40, 4, wait=True)
