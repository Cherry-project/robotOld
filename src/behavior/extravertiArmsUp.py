#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time

import pypot.primitive

class ExtravertiArmsUpBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        """
        poppy.r_shoulder_x.goto_position(-55, 1.0, wait=False)
        poppy.r_shoulder_y.goto_position(-135, 1.0, wait=False)
        poppy.r_arm_z.goto_position(30, 1.0, wait=False)
        poppy.r_elbow_y.goto_position(50, 1.0, wait=False)

        poppy.l_shoulder_y.goto_position(-135, 1.0, wait=False)
        poppy.l_shoulder_x.goto_position(55, 1.0, wait=False)
        poppy.l_arm_z.goto_position(-30, 1.0, wait=False)
        poppy.l_elbow_y.goto_position(50, 1.0, wait=False)
        """

        for m in poppy.arms :
            m.compliant = False

        poppy.r_shoulder_y.moving_speed = abs(-135 - poppy.r_shoulder_y.present_position)
        poppy.r_shoulder_x.moving_speed = abs(-55 - poppy.r_shoulder_x.present_position)
        poppy.r_arm_z.moving_speed = abs(30 - poppy.r_arm_z.present_position)
        poppy.r_elbow_y.moving_speed = abs(50 - poppy.r_elbow_y.present_position)


        poppy.l_shoulder_y.moving_speed = abs(-135 - poppy.l_shoulder_y.present_position)
        poppy.l_shoulder_x.moving_speed = abs(55 - poppy.l_shoulder_x.present_position)
        poppy.l_arm_z.moving_speed = abs(-30 - poppy.l_arm_z.present_position)
        poppy.l_elbow_y.moving_speed = abs(50 - poppy.l_elbow_y.present_position)


        poppy.r_shoulder_y.goal_position = -135
        poppy.r_shoulder_x.goal_position = -55
        poppy.r_arm_z.goal_position = 30
        poppy.r_elbow_y.goal_position = 50

        poppy.l_shoulder_y.goal_position = -135
        poppy.l_shoulder_x.goal_position = 55
        poppy.l_arm_z.goal_position = -30
        poppy.l_elbow_y.goal_position = 50

        time.sleep(0.5)
