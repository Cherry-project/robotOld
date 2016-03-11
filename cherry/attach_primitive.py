#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from behavior.restOpen import RestOpenBehave
from behavior.pointArmLeft import PointArmLeftBehave
from behavior.question import QuestionBehave
from behavior.doubleMe import DoubleMeBehave
from behavior.swap import SwapBehave
from behavior.leftArmUp import LeftArmUpBehave
from behavior.hunkers import HunkersBehave

from textToSpeech.speak import Speak
from textToSpeech.say_text import SayText


def attach_primitives(robot, isCamera=True):
    """ Attach all primitive to the robot.

    TO DO : Un parser pour faire automatiquement le nom afin de faire l'attachement seulement sur une boucle :
    for primitive in list_primitive:
        robot.attach_primitive(primitive(robot, 50), parser(primitive.name))

    Essayer aussi de se passer des imports ?
    """
	poppy.attach_primitive(RestOpenBehave(poppy),"rest_open_behave")
	poppy.attach_primitive(PointArmLeftBehave(poppy),"point_arm_left_behave")
	poppy.attach_primitive(QuestionBehave(poppy,),"question_behave")
	poppy.attach_primitive(DoubleMeBehave(poppy,),"double_me_behave")
	poppy.attach_primitive(SwapBehave(poppy),"swap_behave")
	poppy.attach_primitive(LeftArmUpBehave(poppy,),"left_arm_up_behave")
	poppy.attach_primitive(HunkersBehave(poppy,),"hunkers_behave")

    robot.attach_primitive(Speak(robot),"speak")
    robot.attach_primitive(SayText(robot),"say_text")
