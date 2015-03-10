import numpy
import time


import pypot.primitive


class ThinkBehave(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)
        
        
    def setup(self):

        poppy = self.robot
        
        poppy.head_y.compliant = False
        poppy.head_z.compliant = False

        for m in poppy.r_arm:
            m.compliant = False
        print "1"

        poppy.head_y.goto_position(-10, 4, wait=False)
        poppy.head_z.goto_position(-20, 4, wait=False)
        
        
        poppy.r_arm_z.goto_position(35, 4, wait=False)
        poppy.r_elbow_y.goto_position(-130, 4, wait=False)
        poppy.r_shoulder_y.goto_position(-60, 4, wait=False)
##        time.sleep(4)
##        poppy.r_elbow_y.goto_position(0, 4, wait=False)
##        poppy.r_shoulder_y.goto_position(0, 4, wait=False)



    def teardown(self):
        pass

    def update(self):
        pass
