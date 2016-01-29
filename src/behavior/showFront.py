#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive


class ShowFrontBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot
        
        poppy.r_shoulder_y.compliant = False
        poppy.r_arm_z.compliant = False
        poppy.r_shoulder_y.goto_position(-90, 2, wait=False)
        poppy.r_arm_z.goto_position(-70, 2, wait=True)
