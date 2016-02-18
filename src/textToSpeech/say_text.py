#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import pypot.primitive
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer

import re

from speak import Speak

# texts = [
# """Bonjour, je m'appelle Cherry. Je suis là pour t'aider pendant ton séjour à l'hopital.""",

# """Ici c'est ta chambre,c'est ici que tu vas te reposer et dormir.
# Ta famille pourra te rendre visite pendant la journée, ou même dormir avec toi le soir.""",

# """Si tu as besoin de quelque chose, il y a une sonnette à côté de ton lit.
# Tu peux appuyer dessus pour appeler les infirmières.
# Elle sont là pour t'aider et assister les médecins.""",

# """Pour t'occuper, tu peux utiliser l'ordinateur qui est dans ta chambre, ou jouer avec moi.""",

# """Si tu n'as pas compris quelque chose ou que tu as des questions, surtout n'hésites pas à demander aux gens de l'hopital."""]

class SayText(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self.robot._speak = Speak(robot)

    def start(self, textfile):
       
        data = open(textfile, 'r')

        texts = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', data.read())

        for text in texts:           
            self.robot._speak.start(text)
            print(text)
            time.sleep(0.5)

    def run(self):

        print "run"


