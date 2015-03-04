import time

from pypot.vrep import from_vrep
from poppy.creatures import PoppyHumanoid

from behavior.idle import UpperBodyIdleMotion, HeadIdleMotion



class Cherry():
    def __init__(self):
        # if simulator is None:
        #     print "Cherry ne marche que sur simulateur pour le moment. Utiliser Cherry(simulator='vrep')"

        # else:
        self.robot = PoppyHumanoid(simulator='vrep')

    def setup(self):

        robot = self.robot

        for m in robot.motors:
            m.compliant_behavior = 'safe'
            m.goto_behavior = 'minjerk'

        robot.attach_primitive(UpperBodyIdleMotion(robot, 50), 'upper_body_idle')
        robot.attach_primitive(HeadIdleMotion(robot, 50), "head_idle")



# print "test"

# cherry = PoppyHumanoid(simulator='vrep')


# print "debut de simulation"

# print "primitive : ", cherry.active_primitives


# idle_body = UpperBodyIdleMotion(cherry, 50)
# idle_head = HeadIdleMotion(cherry, 50)


# idle_head.start()
# idle_body.start()

# print "primitive : ", cherry.active_primitives




# time.sleep(20)
# # idle_head.wait_to_stop()
# # idle_body.wait_to_stop()
# print "fin de simulation"
# cherry.stop_simulation()