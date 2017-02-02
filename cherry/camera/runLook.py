import os
import sys
import cv2
import numpy as np
import utils
import pypot.primitive


import random as rand	
from scipy import ndimage


class RunLook(pypot.primitive.LoopPrimitive):
#class RunLook(pypot.primitive.Primitive):

    def __init__(self, robot, camera, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

        self.camera = camera

        print "init ok"


    def setup(self):
        print "setup"
        self.camera.setup()


    def update(self):
        self.camera.runCaptureLoop3()
        

    def teardown(self):
        pass

