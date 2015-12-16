#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from pypot.vrep import from_vrep
from pypot.robot import from_json
from poppy.creatures import PoppyHumanoid
from attach_primitive import attach_primitives

# from textToSpeech.speak import Speak
# from textToSpeech.say_hello import SayHello
# from textToSpeech.speech import Speech
# from textToSpeech.say_text import SayText
# from textToSpeech.bonnard_1 import Bonnard1
# from textToSpeech.bonnard_1 import Bonnard2
# from textToSpeech.bonnard_1 import Bonnard3
# from textToSpeech.bonnard_1 import Bonnard4
# from textToSpeech.bonnard_1 import Bonnard5
# from textToSpeech.bonnard_1 import Bonnard6


# #from textToSpeech.say_hyper import SayHyper

# from behavior.idle import UpperBodyIdleMotion, HeadIdleMotion
# from behavior.yes import YesBehave
# from behavior.wave import WaveBehave
# from behavior.no import NoBehave
# from behavior.crossArms import CrossArmsBehave
# from behavior.crossHands import CrossHandsBehave
# from behavior.showLeft import ShowLeftBehave
# from behavior.showRight import ShowRightBehave
# from behavior.showFront import ShowFrontBehave
# from behavior.takeHead import TakeHeadBehave
# from behavior.takeRightEar import TakeRightEarBehave
# from behavior.takeLeftEar import TakeLeftEarBehave
# from behavior.rightHandMouv import RightHandMouvBehave
# from behavior.comeMouv import ComeMouvBehave
# from behavior.keepFrontMouv import KeepFrontMouvBehave
# from behavior.normal import NormalBehave
# from behavior.salute import SaluteBehave
# from behavior.think import ThinkBehave
# from behavior.copyArm import CopyArmBehave
# from behavior.bow import BowBehave
# from behavior.talkOne import TalkOneBehave
# from behavior.talkTwo import TalkTwoBehave
# from behavior.talkThree import TalkThreeBehave
# from behavior.talkFour import TalkFourBehave
# from behavior.tracking import TrackingBehave
# from behavior.sad import SadBehave
from vision.camera import Camera
from vision.runLook import RunLook

# from screen.eyes import Eyes
# from screen.get_fond import Get_fond
# from screen.get_reaction import Get_reaction
# from screen.basic import Basic  #A SUPPRIMER QUAND TESTS FINIS

# from screen.blink import Blink
# from screen.surprise import Surprise
# from screen.sleepy import Sleepy
# from screen.happy import Happy
# from screen.sad import Sad

# from screen.neutral2sleep import Neutral2sleep
# from screen.sleep2neutral import Sleep2neutral
# from screen.neutral2surprise import Neutral2surprise
# from screen.surprise2neutral import Surprise2neutral
# from screen.neutral2happy import Neutral2happy
# from screen.happy2neutral import Happy2neutral
# from screen.neutral2sad import Neutral2sad
# from screen.sad2neutral import Sad2neutral

class Cherry():

    def __init__(self, simulator=None):
        if simulator is not None:

            self.robot = PoppyHumanoid(simulator='vrep')
            self.isCamera = False

        #Vrai :
        else:
            self.robot = from_json("../utils/poppy_torso_config.json")
            self.robot.start_sync()

            for m in self.robot.motors:
                m.moving_speed = 60

            for m in self.robot.torso:
                m.compliant = False
				
            imagePath = "../utils/img/"
            cascadePath = "haarcascade_frontalface_default.xml"
            self.camera = Camera( self.robot, imagePath, cascadePath)
            self.isCamera = True




    def setup(self):

        robot = self.robot

        for m in robot.motors:
            m.compliant_behavior = 'safe'
            m.goto_behavior = 'minjerk'


        #Attach your primitive here
        # robot.attach_primitive(UpperBodyIdleMotion(robot, 50), 'upper_body_idle')
        # robot.attach_primitive(HeadIdleMotion(robot, 50), "head_idle")
        # robot.attach_primitive(YesBehave(robot, 50), "yes_behave")
        # robot.attach_primitive(WaveBehave(robot, 50), "wave_behave")
        # robot.attach_primitive(NoBehave(robot, 50), "no_behave")
        # robot.attach_primitive(CrossArmsBehave(robot), "cross_arms_behave")
        # robot.attach_primitive(CrossHandsBehave(robot), "cross_hands_behave")
        # robot.attach_primitive(ShowLeftBehave(robot), "show_left_behave")
        # robot.attach_primitive(ShowRightBehave(robot), "show_right_behave")
        # robot.attach_primitive(ShowFrontBehave(robot), "show_front_behave")
        # robot.attach_primitive(TakeHeadBehave(robot), "take_head_behave")
        # robot.attach_primitive(TakeLeftEarBehave(robot), "take_left_ear_behave")
        # robot.attach_primitive(TakeRightEarBehave(robot), "take_right_ear_behave")
        # robot.attach_primitive(RightHandMouvBehave(robot, 50), "right_hand_mouv_behave")
        # robot.attach_primitive(ComeMouvBehave(robot, 50), "come_mouv_behave")
        # robot.attach_primitive(KeepFrontMouvBehave(robot, 50), "keep_front_mouv_behave")
        # robot.attach_primitive(NormalBehave(robot), "normal_behave")
        # robot.attach_primitive(SaluteBehave(robot), "salute_behave")
        # robot.attach_primitive(ThinkBehave(robot), "think_behave")
        # robot.attach_primitive(CopyArmBehave(robot, 50), "copy_arm_behave")
        # robot.attach_primitive(BowBehave(robot), "bow_behave")
        # robot.attach_primitive(TalkOneBehave(robot), "talk_one_behave")
        # robot.attach_primitive(TalkTwoBehave(robot), "talk_two_behave")
        # robot.attach_primitive(TalkThreeBehave(robot), "talk_three_behave")
        # robot.attach_primitive(TalkFourBehave(robot), "talk_four_behave")
        # robot.attach_primitive(TrackingBehave(robot, self.camera, 50), "tracking_behave")
        # robot.attach_primitive(Speak(robot), "speak")
        # robot.attach_primitive(SayHello(robot), "say_hello")
        # robot.attach_primitive(SayText(robot), "say_text")
        # robot.attach_primitive(SadBehave(robot), "sad_behave")
        # robot.attach_primitive(RunLook(robot, self.camera, 50), "run_look") 
        # robot.attach_primitive(Speech(robot), "speech")
        # robot.attach_primitive(Bonnard1(robot), "bonnard_1")
        # robot.attach_primitive(Bonnard2(robot), "bonnard_2")
        # robot.attach_primitive(Bonnard3(robot), "bonnard_3")
        # robot.attach_primitive(Bonnard4(robot), "bonnard_4")
        # robot.attach_primitive(Bonnard5(robot), "bonnard_5")
        # robot.attach_primitive(Bonnard6(robot), "bonnard_6")


        # # robot.attach_primitive(Eyes(robot), "eyes")
        # # robot.attach_primitive(Get_reaction(robot), "get_reaction")
        # # robot.attach_primitive(Get_fond(robot), "get_fond")
        # # robot.attach_primitive(Basic(robot), "basic")
        # # robot.attach_primitive(Blink(robot), "blink")
        # # robot.attach_primitive(Neutral2sleep(robot), "neutral2sleep")
        # # robot.attach_primitive(Sleep2neutral(robot), "sleep2neutral")
        # # robot.attach_primitive(Neutral2surprise(robot), "neutral2surprise")
        # # robot.attach_primitive(Surprise2neutral(robot), "surprise2neutral")
        # # robot.attach_primitive(Surprise(robot), "surprise")
        # # robot.attach_primitive(Sleepy(robot), "sleepy")
        # # robot.attach_primitive(Happy(robot), "happy")
        # # robot.attach_primitive(Neutral2happy(robot), "neutral2happy")
        # # robot.attach_primitive(Happy2neutral(robot), "happy2neutral")
        # # robot.attach_primitive(Neutral2sad(robot), "neutral2sad")
        # # robot.attach_primitive(Sad2neutral(robot), "sad2neutral")
        # # robot.attach_primitive(Sad(robot), "sad")

        attach_primitives(self, self.isCamera)

