import time
import pypot.primitive
from pypot.primitive.utils import Sinus

class ShowFrontBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot
        
        poppy.r_shoulder_y.goto_position(-90, 2, wait=False)
        poppy.r_arm_z.goto_position(-70, 2, wait=True)
        
        time.sleep(1)
