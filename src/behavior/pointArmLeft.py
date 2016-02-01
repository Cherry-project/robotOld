#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time

import pypot.primitive

class PointArmLeftBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.arms :
            m.compliant = False

        poppy.r_shoulder_y.moving_speed = abs(0 - poppy.r_shoulder_y.present_position)
        poppy.r_shoulder_x.moving_speed = abs(-10 - poppy.r_shoulder_x.present_position)
        poppy.r_arm_z.moving_speed = abs(20 - poppy.r_arm_z.present_position)
        poppy.r_elbow_y.moving_speed = abs(5 - poppy.r_elbow_y.present_position)


        poppy.l_shoulder_y.moving_speed = abs(-60 - poppy.l_shoulder_y.present_position)
        poppy.l_shoulder_x.moving_speed = abs(10 - poppy.l_shoulder_x.present_position)
        poppy.l_arm_z.moving_speed = abs(-20 - poppy.l_arm_z.present_position)
        poppy.l_elbow_y.moving_speed = abs(30 - poppy.l_elbow_y.present_position)

        
        poppy.r_shoulder_y.goal_position = 0
        poppy.r_shoulder_x.goal_position = -10
        poppy.r_arm_z.goal_position = 20
        poppy.r_elbow_y.goal_position = 5

        poppy.l_shoulder_y.goal_position = -60
        poppy.l_shoulder_x.goal_position = 10
        poppy.l_arm_z.goal_position = -20
        poppy.l_elbow_y.goal_position = 30

        """
        poppy.r_shoulder_y.goto_position(0, 1.5, wait=False)
        poppy.r_shoulder_x.goto_position(-10, 1.5, wait=False)
        poppy.r_arm_z.goto_position(20, 1.5, wait=False)
        poppy.r_elbow_y.goto_position(5, 1.5, wait=False)

        poppy.l_shoulder_y.goto_position(-60, 1.5, wait=False)
        poppy.l_shoulder_x.goto_position(10, 1.5, wait=False)
        poppy.l_arm_z.goto_position(-20, 1.5, wait=False)
        poppy.l_elbow_y.goto_position(30, 1.5, wait=False)

        """
        time.sleep(0.5)