#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive


class ShowLeftBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.r_arm + [poppy.l_arm_z, poppy.l_shoulder_x]:
            m.compliant = False

        poppy.r_shoulder_x.goto_position(-20, 1, wait=False)
        poppy.r_shoulder_y.goto_position(-30, 1, wait=True)
        poppy.r_arm_z.goto_position(100, 2, wait=False)
        poppy.r_elbow_y.goto_position(-100, 2, wait=False)
        
        poppy.l_shoulder_x.goto_position(90, 2, wait=False)
        poppy.l_arm_z.goto_position(90, 2, wait=True)