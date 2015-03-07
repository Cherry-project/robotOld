import time
import pypot.primitive
from pypot.primitive.utils import Sinus

class ShowRightBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot
        poppy.l_shoulder_x.goto_position(20, 2, wait=False)
        poppy.l_shoulder_y.goto_position(-30, 2, wait=True)
        poppy.l_arm_z.goto_position(-100, 2, wait=False)
        poppy.l_elbow_y.goto_position(-100, 2, wait=False)
        
        poppy.r_shoulder_x.goto_position(-90, 2, wait=True)
        poppy.r_arm_z.goto_position(-90, 2, wait=True)
        
        time.sleep(1)
