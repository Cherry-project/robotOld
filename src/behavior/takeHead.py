import numpy
import time

import pypot.primitive
from pypot.primitive.utils import Sinus

class TakeHeadBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        poppy.head_y.goto_position(45, 4, wait=False)

        poppy.r_shoulder_x.goto_position(-20, 4, wait=False)
        poppy.r_shoulder_y.goto_position(-100, 4, wait=False)

        poppy.l_shoulder_x.goto_position(20, 4, wait=False)
        poppy.l_shoulder_y.goto_position(-100, 4, wait=False)
        
        poppy.r_arm_z.goto_position(20, 4, wait=False)
        poppy.r_elbow_y.goto_position(-140, 4, wait=False)

        poppy.l_arm_z.goto_position(-20, 4, wait=False)
        poppy.l_elbow_y.goto_position(-140, 4, wait=True)
        
        time.sleep(1)


