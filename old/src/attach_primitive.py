#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


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
from behavior.normal import NormalBehave
from behavior.salute import SaluteBehave
from behavior.think import ThinkBehave
from behavior.copyArm import CopyArmBehave
from behavior.bow import BowBehave
from behavior.talkOne import TalkOneBehave
from behavior.talkTwo import TalkTwoBehave
from behavior.talkThree import TalkThreeBehave
from behavior.talkFour import TalkFourBehave
from behavior.tracking import TrackingBehave
from behavior.sad import SadBehave
from behavior.extravertiArmsUp import ExtravertiArmsUpBehave
from behavior.rest import RestBehave
from behavior.me import MeBehave
from behavior.question import QuestionBehave
from behavior.hug import HugBehave
from behavior.laugh import LaughBehave
from behavior.meArm import MeArmBehave
from behavior.hunkers import HunkersBehave
from behavior.leftArms import LeftArmsBehave
from behavior.rightArms import RightArmsBehave
from behavior.rightHandUp import RightHandUpBehave
from behavior.showFrontHunkers import ShowFrontHunkersBehave
from behavior.showRightRest import ShowRightRestBehave
from behavior.restTilted import RestTiltedBehave
from behavior.leftArmUp import LeftArmUpBehave
from behavior.youAndMe import YouAndMeBehave
from behavior.littleLaugh import LittleLaughBehave
from behavior.sigh import SighBehave
from behavior.littleHug import LittleHugBehave
from behavior.restOpen import RestOpenBehave
from behavior.openArms import OpenArmsBehave
from behavior.pointArmLeft import PointArmLeftBehave
from behavior.openMove import OpenMoveBehave
from behavior.doubleMe import DoubleMeBehave
from behavior.swap import SwapBehave
from behavior.disappointment import DisappointmentBehave
from behavior.littleArmsUp import LittleArmsUpBehave
from behavior.seeYouSoon import SeeYouSoonBehave

#from vision.camera import Camera
#from vision.runLook import RunLook

def attach_primitives(cherry, isCamera=True):
    """ Attach all primitive to the robot.

    TO DO : Un parser pour faire automatiquement le nom afin de faire l'attachement seulement sur une boucle :
    for primitive in list_primitive:
        robot.attach_primitive(primitive(robot, 50), parser(primitive.name))

    Essayer aussi de se passer des imports ?
    """
    robot = cherry.robot

    robot.attach_primitive(UpperBodyIdleMotion(robot, 50), 'upper_body_idle')
    robot.attach_primitive(HeadIdleMotion(robot, 50), "head_idle")
    robot.attach_primitive(YesBehave(robot, 50), "yes_behave")
    robot.attach_primitive(WaveBehave(robot, 50), "wave_behave")
    robot.attach_primitive(NoBehave(robot, 50), "no_behave")
    robot.attach_primitive(CrossArmsBehave(robot), "cross_arms_behave")
    robot.attach_primitive(CrossHandsBehave(robot), "cross_hands_behave")
    robot.attach_primitive(ShowLeftBehave(robot), "show_left_behave")
    robot.attach_primitive(ShowRightBehave(robot), "show_right_behave")
    robot.attach_primitive(ShowFrontBehave(robot), "show_front_behave")
    robot.attach_primitive(TakeHeadBehave(robot), "take_head_behave")
    robot.attach_primitive(TakeLeftEarBehave(robot), "take_left_ear_behave")
    robot.attach_primitive(TakeRightEarBehave(robot), "take_right_ear_behave")
    robot.attach_primitive(RightHandMouvBehave(robot, 50), "right_hand_mouv_behave")
    robot.attach_primitive(ComeMouvBehave(robot, 50), "come_mouv_behave")
    robot.attach_primitive(KeepFrontMouvBehave(robot, 50), "keep_front_mouv_behave")
    robot.attach_primitive(NormalBehave(robot), "normal_behave")
    robot.attach_primitive(SaluteBehave(robot), "salute_behave")
    robot.attach_primitive(ThinkBehave(robot), "think_behave")
    robot.attach_primitive(CopyArmBehave(robot, 50), "copy_arm_behave")
    robot.attach_primitive(BowBehave(robot), "bow_behave")
    robot.attach_primitive(ExtravertiArmsUpBehave(robot),"extra_arms_up")
    robot.attach_primitive(RestBehave(robot),"rest_position")
    robot.attach_primitive(MeBehave(robot),"me_behave")
    robot.attach_primitive(QuestionBehave(robot),"question_behave")
    robot.attach_primitive(HugBehave(robot),"hug_behave")
    robot.attach_primitive(LaughBehave(robot),"laugh_behave")
    robot.attach_primitive(MeArmBehave(robot),"me_arm_behave")
    robot.attach_primitive(HunkersBehave(robot),"hunkers_behave")
    robot.attach_primitive(LeftArmsBehave(robot),"left_arms_behave")
    robot.attach_primitive(RightArmsBehave(robot),"right_arms_behave")
    robot.attach_primitive(RightHandUpBehave(robot),"right_hand_up_behave")
    robot.attach_primitive(ShowFrontHunkersBehave(robot),"show_front_hunkers_behave")
    robot.attach_primitive(ShowRightRestBehave(robot),"show_right_rest_behave")
    robot.attach_primitive(RestTiltedBehave(robot),"rest_tilted_behave")
    robot.attach_primitive(LeftArmUpBehave(robot),"left_arm_up_behave")
    robot.attach_primitive(YouAndMeBehave(robot),"you_and_me_behave")
    robot.attach_primitive(LittleLaughBehave(robot),"little_laugh_behave")
    robot.attach_primitive(SighBehave(robot),"sigh_behave")
    robot.attach_primitive(LittleHugBehave(robot),"little_hug_behave")
    robot.attach_primitive(RestOpenBehave(robot),"rest_open_behave")
    robot.attach_primitive(OpenArmsBehave(robot),"open_arms_behave")
    robot.attach_primitive(PointArmLeftBehave(robot),"point_arm_left_behave")
    robot.attach_primitive(OpenMoveBehave(robot),"open_move_behave")
    robot.attach_primitive(DoubleMeBehave(robot),"double_me_behave")
    robot.attach_primitive(SwapBehave(robot),"swap_behave")
    robot.attach_primitive(DisappointmentBehave(robot),"disappointment_behave")
    robot.attach_primitive(LittleArmsUpBehave(robot),"little_arms_up_behave")
    robot.attach_primitive(SeeYouSoonBehave(robot),"see_you_soon_behave")

    """
    if isCamera:
        robot.attach_primitive(TrackingBehave(robot, cherry.camera, 50), "tracking_behave")
        robot.attach_primitive(RunLook(robot, cherry.camera, 50), "run_look") 
    """
