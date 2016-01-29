#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import time

import pypot.primitive
from pypot.primitive.utils import Sinus


class YesBehave(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

        self.my_sinus = Sinus(self.robot, 50, [self.robot.head_y, ], amp=8, freq=1, offset=10)

    def setup(self):
        self.robot.head_y.compliant = False

        self.my_sinus.start()

    def teardown(self):
        self.my_sinus.stop()

    def update(self):
        pass