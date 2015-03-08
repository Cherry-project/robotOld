import time

from pypot.vrep import from_vrep
from poppy.creatures import PoppyHumanoid

from behavior.idle import UpperBodyIdleMotion, HeadIdleMotion
from behavior.yes import YesBehave
from behavior.wave import WaveBehave
from behavior.no import NoBehave
from behavior.crossArms import CrossArmsBehave
from behavior.crossHands import CrossHandsBehave
from behavior.showLeft import ShowLeftBehave
from behavior.showRight import ShowRightBehave
from behavior.showFront import ShowFrontBehave
from behavior.takeHead import TakeHeadBehave
from behavior.takeRightEar import TakeRightEarBehave
from behavior.takeLeftEar import TakeLeftEarBehave
from behavior.rightHandMouv import RightHandMouvBehave
from behavior.comeMouv import ComeMouvBehave
from behavior.keepFrontMouv import KeepFrontMouvBehave


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


        #Attach your primitive here
        robot.attach_primitive(UpperBodyIdleMotion(robot, 50), 'upper_body_idle')
        robot.attach_primitive(HeadIdleMotion(robot, 50), "head_idle")
        robot.attach_primitive(YesBehave(robot, 1), "yes_behave")
        robot.attach_primitive(WaveBehave(robot, 0.5), "wave_behave")
        robot.attach_primitive(NoBehave(robot, 1), "no_behave")
        robot.attach_primitive(CrossArmsBehave(robot), "cross_arms_behave")
        robot.attach_primitive(CrossHandsBehave(robot), "cross_hands_behave")
        robot.attach_primitive(ShowLeftBehave(robot), "show_left_behave")
        robot.attach_primitive(ShowRightBehave(robot), "show_right_behave")
        robot.attach_primitive(ShowFrontBehave(robot), "show_front_behave")
        robot.attach_primitive(TakeHeadBehave(robot), "take_head_behave")
        robot.attach_primitive(TakeLeftEarBehave(robot), "take_left_ear_behave")
        robot.attach_primitive(RightHandMouvBehave(robot, 1), "right_hand_mouv_behave")
        robot.attach_primitive(ComeMouvBehave(robot, 1), "come_mouv_behave")
        robot.attach_primitive(KeepFrontMouvBehave(robot, 1), "keep_front_mouv_behave")





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
