import numpy
import time


import pypot.primitive
from pypot.primitive.utils import Sinus

class KeepFrontMouvBehave(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

        self.my_sinus = Sinus(self.robot, 50, [self.robot.r_elbow_y], amp=20, freq=1, offset=-90)

    def setup(self):
        robot = self.robot

        for m in robot.r_arm:
            m.compliant = False
        
        robot.r_shoulder_x.goto_position(-20, 1, wait=False)
        robot.r_shoulder_y.goto_position(-50, 1, wait=True)
        
        time.sleep(1)

        self.my_sinus.start()

    def teardown(self):
        robot = self.robot

        self.my_sinus.stop()

        robot.r_arm_z.goto_position(0, 1)
        robot.r_shoulder_x.goto_position(0,1)
        robot.r_shoulder_y.goto_position(0,1)
        robot.r_elbow_y.goto_position(0,1)

        time.sleep(1)

    def update(self):
        pass
