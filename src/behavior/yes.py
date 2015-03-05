import numpy
import time

import pypot.primitive
from pypot.primitive.utils import Sinus


class YesBehave(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

        self.my_sinus = Sinus(self.robot, 50, [self.robot.head_y, ], amp=8, freq=freq, offset=10)

    def setup(self):
        self.robot.head_y.compliant = False

        self.my_sinus.start()

    def teardown(self):
        self.my_sinus.stop()

    def update(self):
        pass

# class YesBehave(pypot.primitive.LoopPrimitive):
#     """Didn't work"""

#     def __init__(self, robot, freq):
#         pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

#         self._amp = 15
#         self._freq = freq

#     def update(self):
#         t = self.elapsed_time   
#         amp = self._amp
#         freq = self._freq
        
#         self.robot.head_y.goal_position = amp * numpy.sin(freq * 2 * t * numpy.pi)






# OLD VERSION :

# def run(robot):
#     center_position = 25
#     robot.head_y.goal_position = 90
#     t0 = time.time()
#     amp = 40
#     freq = 0.7
#     robot.head_y.goal_position = center_position
#     time.sleep(1)

#     while True:
#         t = time.time() - t0
#         if t > 7:
#             break
#         pos = amp * numpy.sin(2 * numpy.pi * freq * t) + center_position
#         robot.head_y.goal_position = pos 
#         time.sleep(0.02)
#     robot.head_y.goal_position = center_position

# if __name__ ==  "__main__":
#     print "debut du test"
#     poppy = virtual_robot("coucou")
#     print poppy.test
#     poppy.init()
#     print poppy.test
#     print "fin de l'init"
#     run(poppy.poppy)
#     print "ok"
#     time.sleep(5)