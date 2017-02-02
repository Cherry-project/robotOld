#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# Movement
from primitives.restOpen import RestOpenBehave
from primitives.pointArmLeft import PointArmLeftOldBehave
from primitives.question import QuestionBehave
from primitives.doubleMe import DoubleMeBehave
from primitives.swap import SwapBehave
from primitives.leftArmUp import LeftArmUpBehave
from primitives.hunkers import HunkersBehave
from primitives.littleArmsUp import LittleArmsUpBehave
from primitives.showRightRest import ShowRightRestBehave
from primitives.head import LookLeftBehave, LookRightBehave
from primitives.arms import OpenArmsBehave, PointArmsBehave
from primitives.leftArm import ShowLeftBehave, ShowLeftUpBehave, PointArmLeftBehave
from primitives.rightArm import ShowRightBehave, ShowRightUpBehave, PointArmRightBehave
from primitives.idle import UpperBodyIdleMotion, HeadIdleMotion, TorsoIdleMotion

# Play Movement
from primitives.play_move import PlayMove

# Speak
from textToSpeech.speak import Speak
#from textToSpeech.speak_windows import Speak
from textToSpeech.say_text import SayText
# Reset audio system
from textToSpeech.reset_audio import ResetAudio

# Send IP
from primitives.send_ip import SendIp

# Test Gtts service
from primitives.test_gtts import TestGTTS

#Screen Management (EYES)
from screen.eye import EyeBehave
from screen.eyeAngry import EyeAngryBehave
from screen.eyeHappy import EyeHappyBehave

# STT
from chatterbot.STT import Listen
#from stt.listen_old import Listen

def attach_primitives(robot, isCamera=True):
    """ Attach all primitive to the robot.

    TO DO : Un parser pour faire automatiquement le nom afin de faire l'attachement seulement sur une boucle :
    for primitive in list_primitive:
        robot.attach_primitive(primitive(robot, 50), parser(primitive.name))

    Essayer aussi de se passer des imports ?
    """
    robot.attach_primitive(RestOpenBehave(robot),"rest_open_behave")
    robot.attach_primitive(PointArmLeftOldBehave(robot),"point_arm_left_old_behave")
    robot.attach_primitive(QuestionBehave(robot),"question_behave")
    robot.attach_primitive(DoubleMeBehave(robot),"double_me_behave")
    robot.attach_primitive(SwapBehave(robot),"swap_behave")
    robot.attach_primitive(LeftArmUpBehave(robot),"left_arm_up_behave")
    robot.attach_primitive(HunkersBehave(robot),"hunkers_behave")
    robot.attach_primitive(LittleArmsUpBehave(robot),"little_arms_up_behave")
    robot.attach_primitive(ShowRightRestBehave(robot),"show_right_rest_behave")
    robot.attach_primitive(LookRightBehave(robot),"look_right_behave")
    robot.attach_primitive(LookLeftBehave(robot),"look_left_behave")
    robot.attach_primitive(OpenArmsBehave(robot),"open_arms_behave")
    robot.attach_primitive(PointArmsBehave(robot),"point_arms_behave")
    robot.attach_primitive(ShowRightBehave(robot),"show_right_behave")
    robot.attach_primitive(ShowRightUpBehave(robot),"show_right_up_behave")
    robot.attach_primitive(PointArmRightBehave(robot),"point_arm_right_behave")
    robot.attach_primitive(ShowLeftBehave(robot),"show_left_behave")
    robot.attach_primitive(ShowLeftUpBehave(robot),"show_left_up_behave")
    robot.attach_primitive(PointArmLeftBehave(robot),"point_arm_left_behave")

    robot.attach_primitive(PlayMove(robot),"play_movement")

    robot.attach_primitive(UpperBodyIdleMotion(robot, 50), 'upper_body_idle_motion')
    robot.attach_primitive(HeadIdleMotion(robot, 50), 'head_idle_motion')
    robot.attach_primitive(TorsoIdleMotion(robot, 50), 'torso_idle_motion')

    robot.attach_primitive(Speak(robot),"speak")
    robot.attach_primitive(SayText(robot),"say_text")

    #robot.attach_primitive(SendIp(robot),"send_ip")
    robot.attach_primitive(TestGTTS(robot),"test_gtts")
    

    robot.attach_primitive(EyeBehave(robot),"eye_behave")
    robot.attach_primitive(EyeAngryBehave(robot),"eye_angry_behave")
    robot.attach_primitive(EyeHappyBehave(robot),"eye_happy_behave")

    robot.attach_primitive(Listen(robot),"listen")
