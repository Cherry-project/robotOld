import pypot.primitive
import time

class LookRightBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.head :
            m.compliant = False

        t =time.time()

        poppy.head_z.goto_position(-50, 1, wait=False)
        poppy.head_y.goto_position(0, 1, wait=True)

        poppy.head_z.goto_position(0, 1, wait=False)
        poppy.head_y.goto_position(0, 1, wait=True)

        el = time.time() - t
        print el

class LookLeftBehave(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.head :
            m.compliant = False

        t =time.time()

        poppy.head_z.goto_position(50, 1, wait=False)
        poppy.head_y.goto_position(0, 1, wait=True)

        poppy.head_z.goto_position(0, 1, wait=False)
        poppy.head_y.goto_position(0, 1, wait=True)

        el = time.time() - t
        print el
