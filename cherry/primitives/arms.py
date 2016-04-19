import pypot.primitive
import time

class OpenArmsBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.arms :
            m.compliant = False

        t =time.time()

        poppy.r_shoulder_y.goto_position(-50, 1, wait=False)
        poppy.r_shoulder_x.goto_position(-15, 1, wait=False)
        poppy.r_arm_z.goto_position(-30, 1, wait=False)
        poppy.r_elbow_y.goto_position(15, 1, wait=False)

        poppy.l_shoulder_y.goto_position(-50, 1, wait=False)
        poppy.l_shoulder_x.goto_position(15, 1, wait=False)
        poppy.l_arm_z.goto_position(30, 1, wait=False)
        poppy.l_elbow_y.goto_position(15, 1, wait=True)

        el = time.time() - t
        print el

class PointArmsBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.arms :
            m.compliant = False

        t =time.time()

        poppy.r_shoulder_y.goto_position(-45, 1, wait=False)
        poppy.r_shoulder_x.goto_position(10, 1, wait=False)
        poppy.r_arm_z.goto_position(15, 1, wait=False)
        poppy.r_elbow_y.goto_position(15, 1, wait=False)

        poppy.l_shoulder_y.goto_position(-45, 1, wait=False)
        poppy.l_shoulder_x.goto_position(-10, 1, wait=False)
        poppy.l_arm_z.goto_position(-15, 1, wait=False)
        poppy.l_elbow_y.goto_position(15, 1, wait=True)

        el = time.time() - t
        print el