#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time

import pypot.primitive

class CopyArmBehave(pypot.primitive.LoopPrimitive):
    """ Apply the motion made on the right arm to the left arm. """
    def setup(self):

        for m in self.robot.l_arm:
            m.compliant = False

        for m in self.robot.r_arm:
            m.compliant = True

    def update(self):
        # for lm in self.robot.l_arm:
        #     for rm in self.robot.r_arm:
        #         lm.goal_position = rm.present_position * (1 if rm.direct else -1)

        robot = self.robot

        robot.l_arm_z.goal_position = robot.r_arm_z.present_position * -1
        robot.l_shoulder_x.goal_position = robot.r_shoulder_x.present_position * -1
        robot.l_shoulder_y.goal_position = robot.r_shoulder_y.present_position
        robot.l_elbow_y.goal_position = robot.r_elbow_y.present_position

    """
    def teardown(self):
        #self.robot.normal_behave.start()
    """
