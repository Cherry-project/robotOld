#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time


import pypot.primitive
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


from speak import Speak

text = """﻿Bonjour, je m'appelle Cherry. Je suis là pour t'aider pendant ton séjour à l'hopital.
Je vais t'expliquer comment les choses fonctionnent ici.
Ici c'est ta chambre,c'est ici que tu vas te reposer et dormir.
C'est aussi ici que ta famille et tes amis pourront te rendre visite pendant la journée.
Bien entendu tes parents peuvent rester dormir avec toi le soir, dans un petit lit que l'on peut installer à côté du tien.
Les médecins vont passer régulièrement t'examiner, et décider de la meilleure façon de te soigner.
Les infirmières sont là pour les aider en faisant les soins, et elles sont aussi là pour t'aider si tu as besoin de quelque chose.
Pour les appeler, à côté de ton lit, il y a une sonnette.
Si tu appuies dessus, elles sauront que tu as besoin d'elles et viendront te voir.
Pour te distraire, tu peux utiliser l'ordinateur qui est dans ta chambre, ou jouer avec moi.
Si tu n'as pas compris quelque chose ou que tu as des questions, surtout n'hésites pas à demander aux gens de l'hopital.
"""

class SayText(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._speak = Speak(robot)
        

    def start(self, textfile):
        # self._text = textfile
        # print textfile
        # file = open(self._text, 'r')

        # for line in file :
            
        #     # print "ligne!"
        #     # phrase = line.split('.')
        #     # for item in phrase :
        #     #     print item



        #     print '_______________________________________________________________________________________'
        #     print line
        #     print '_______________________________________________________________________________________'

        #     self.robot.speak.start(line)

        
        # text = file.readlines()

        # print text

        self.robot.speak.start(text)

    def run(self):

        print "run"
        
       
