#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time


import pypot.primitive
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak
from say_text import SayText

class DiscMed(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        self._saytext = SayText(robot)
        self._move = "../src/moveRecorded/arrivee.move"
        self._move2 = "../src/moveRecorded/arrive_tete.move"

    def start(self):

        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)

        with open(self._move2) as f :

            m = Move.load(f)
    
        move_player2 = MovePlayer(self.robot, m)

        move_player.start()
        move_player2.start()

        time.sleep(1.5)

        # print "1"
        # phrase="Je vais te parler de l’Hyperthyroïdie. Ne t’inquiète pas, ce n’est pas très compliqué ! Je vais t’expliquer ce que c’est, pourquoi ça arrive et comment les médecins le soignent."
        # self._speak.start(phrase)
        # print "2"
        # phrase="Dans ton cou, juste au-dessous de la pomme d’Adam, se trouve ta glande thyroïde. Cette glande aide à contrôler la vitesse à laquelle ton corps travaille. Elle le fait en envoyant un message à tes organes grâce à l’hormone Thyroxine."
        # print phrase
        # self._speak.start(phrase)
        # phrase="Si la glande thyroïde envoie trop de thyroxine, ton corps travaille trop vite. Si elle en envoie trop peu, ton corps travaille trop lentement. Pour que ton corps travaille bien, il te faut une quantité normale de thyroxine."
        # self._speak.start(phrase)
        # phrase="""Quand ta glande thyroïde produit trop de thyroxine, on appelle cela l’hyperthyroïdie."""
        # self._speak.start(phrase)
        # phrase="""Les médecins peuvent diagnostiquer l’hyperthyroïdie grâce à un prélèvement de sang, qui leur permet de savoir quelle quantité d’hormones tu as."""
        # self._speak.start(phrase)
        # phrase="""Pour traiter ton hyperthyroïdie, les médecins vont te prescrire des comprimés. Ces comprimés vont diminuer la quantité de tes hormones thyroïdiennes. Il est très important que tu prennes bien tes médicaments tous les jours."""
        # self._speak.start(phrase)
        # phrase="""Si, après quelques années, les médicaments ne suffisent pas pour te guérir, il est possible que tu reviennes pour un nouveau traitement."""
        # self._speak.start(phrase)
        # phrase="""J’espère que tu comprends mieux l’hyperthyroïdie maintenant. Si tu as des questions, ou des choses que tu n’as pas bien comprises, n’hésite pas à en parler à ton médecin ou à une autre personne de l’hôpital. Ils pourront t’aider et t’expliquer."""
        # self._speak.start(phrase)
        self._saytext.start("textToSpeech/disc_med.txt")

    def run(self):

        print "run"
        
       
