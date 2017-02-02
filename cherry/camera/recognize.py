import os
import sys
import cv2
import numpy as np
import utils
import pypot.primitive
from poppy.creatures import PoppyHumanoid
import time

from scipy import ndimage


class CheckSomeone(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, camera, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

        self.camera = camera
        self.robot = robot

        self.peopleSaw

   
    def setup(self):
    	self.camera.setup()


    def update(self):
    	self.camera.runCapture()
    	if(self.camera.isSomebody and self.camera.name != "unknow"):
    		buffName = self.camera.name
    	time.sleep(1)
    	self.camera.runCapture()
    	if (self.camera.isSomebody && buffName == self.camera.name and (self.camera.name in self.peapleSaw) == False):
            self.robot.say_hello(self.camera.name)
            self.peopleSaw.append(self.camera.name)









    	





