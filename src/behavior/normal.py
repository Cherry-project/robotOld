import time
import pypot.primitive

class NormalBehave(pypot.primitive.Primitive):
    "A behave to put all motors at 0"

    def run(self):
        for m in self.robot.motors:
            m.compliant = False
            m.goto_position(0, 2, wait=False)

        time.sleep(2)