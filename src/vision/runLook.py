import os
import sys
import cv2
import numpy as np
import utils
import pypot.primitive


import random as rand	
from scipy import ndimage


class RunLook(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, camera, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

        self.camera = camera

        print "init ok"


    def setup(self):
        self.camera.setup()


    def update(self):
        self.camera._runCaptureLoop2()


    def teardown(self):
        pass

