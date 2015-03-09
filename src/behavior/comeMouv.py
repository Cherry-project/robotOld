import numpy
import time


import pypot.primitive
from pypot.primitive.utils import Sinus

class ComeMouvBehave(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)
        
        robot = self.robot
        self.my_sinus = Sinus(self.robot, 50, [robot.r_elbow_y], amp=40, freq=1, offset=-90)

    def setup(self):
        robot = self.robot

        for m in robot.r_arm:
            m.compliant = False
        
        robot.r_shoulder_x.goto_position(-40, 1, wait=False)
        robot.r_shoulder_y.goto_position(-50, 1, wait=False)
        robot.r_arm_z.goto_position(40, 2, wait=True)
        #robot.r_elbow_y.goto_position(-100, 2, wait=True)

        self.my_sinus.start()

    def teardown(self):
        robot = self.robot

        self.my_sinus.stop()

        robot.r_arm_z.goto_position(0, 1, wait=False)
        robot.r_shoulder_x.goto_position(0, 1, wait=False)
        robot.r_shoulder_y.goto_position(0, 1, wait=False)
        robot.r_elbow_y.goto_position(0, 1, wait=True)


    def update(self):
        pass
