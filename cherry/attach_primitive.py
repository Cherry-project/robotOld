#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from primitives.bonjourCaVa import BonjourCaVa
from primitives.devinette import Devinette
from primitives.explicationsPlus import ExplicationsPlus
from primitives.monnaiePoissons import MonnaiePoissons
from primitives.premiereFoisRobot import PremiereFoisRobot
from primitives.reponseSousmarins import ReponseSousmarins
from primitives.super import Super
from primitives.commentTuTeSens import CommentTuTeSens
from primitives.emotionsCommeToi import EmotionsCommeToi
from primitives.explications import Explications
from primitives.merciDeTaVisite import MerciDeTaVisite
from primitives.parlerAvecMoi import ParlerAvecMoi
from primitives.quiJeSuis import QuiJeSuis
from primitives.savoirPlus import SavoirPlus

from textToSpeech.speak import Speak
from textToSpeech.say_text import SayText


def attach_primitives(robot, isCamera=True):
    """ Attach all primitive to the robot.

    TO DO : Un parser pour faire automatiquement le nom afin de faire l'attachement seulement sur une boucle :
    for primitive in list_primitive:
        robot.attach_primitive(primitive(robot, 50), parser(primitive.name))

    Essayer aussi de se passer des imports ?
    """


    robot.attach_primitive(BonjourCaVa(robot),"bonjour_ca_va")
    robot.attach_primitive(Devinette(robot),"devinette")
    robot.attach_primitive(ExplicationsPlus(robot),"explications_plus")
    robot.attach_primitive(MonnaiePoissons(robot),"monnaie_poissons")
    robot.attach_primitive(PremiereFoisRobot(robot),"premiere_fois_robot")
    robot.attach_primitive(ReponseSousmarins(robot),"reponse_sous_marins")
    robot.attach_primitive(Super(robot),"super")
    robot.attach_primitive(CommentTuTeSens(robot),"comment_tu_te_sens")
    robot.attach_primitive(EmotionsCommeToi(robot),"emotions_comme_toi")
    robot.attach_primitive(Explications(robot),"explications")
    robot.attach_primitive(MerciDeTaVisite(robot),"merci_de_ta_visite")
    robot.attach_primitive(ParlerAvecMoi(robot),"parler_avec_moi")
    robot.attach_primitive(QuiJeSuis(robot),"qui_je_suis")
    robot.attach_primitive(SavoirPlus(robot),"savoir_plus")



    robot.attach_primitive(Speak(robot),"speak")
    robot.attach_primitive(SayText(robot),"say_text")
