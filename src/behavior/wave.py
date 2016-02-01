#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time


import pypot.primitive
from pypot.primitive.utils import Sinus

class WaveBehave(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

        self.my_sinus = Sinus(self.robot, 50, [self.robot.l_elbow_y, ], amp=30, freq=1, offset=-90)

    def setup(self):
        robot = self.robot

        for m in robot.l_arm:
            m.compliant = False

        robot.l_arm_z.goto_position(90, 1, wait=False)
        robot.l_shoulder_x.goto_position(90,1, wait=True)

        self.my_sinus.start()

    def teardown(self):
        robot = self.robot

        self.my_sinus.stop()

        self.robot.normal_behave.start()
    def update(self):
        pass
