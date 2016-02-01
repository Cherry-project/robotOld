#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pypot.primitive

class NormalBehave(pypot.primitive.Primitive):
    "A behave to put all motors at 0"

    def run(self):
        
        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False

        for m in poppy.torso + poppy.head:
            m.goto_position(0, 2)

        poppy.l_shoulder_y.goto_position(-8, 2)
        poppy.l_shoulder_x.goto_position(10, 2)
        poppy.l_arm_z.goto_position(20, 2)
        poppy.l_elbow_y.goto_position(-25, 2)

        poppy.r_shoulder_y.goto_position(-8, 2)
        poppy.r_shoulder_x.goto_position(-10, 2)
        poppy.r_arm_z.goto_position(-20, 2)
        poppy.r_elbow_y.goto_position(-25, 2, wait=True)

        for m in poppy.arms:
            m.compliant = True