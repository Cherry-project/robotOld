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
        print "debut setup camera"
        print "heuuuuu"
        print "et la ?"
        print "non plus ?"
        self.camera.setup()
        print "fin setup camera"


    def update(self):
        print "debut update"
        self.camera.RunLook()
        print "fin update"


    def teardown(self):
        pass

