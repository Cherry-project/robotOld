#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer
from speak import Speak


class Bonnard1(pypot.primitive.Primitive):

    def __init__(self, robot):

        pypot.primitive.Primitive.__init__(self, robot)
        self._speak = Speak(robot)
        self._text = "Bonjour Christophe. Bienvenue au pôle innovation. Nous allons te présenter nos différents projets en cours. Commençons par Yvon, qui va te présenter le projet Octobre Bleu."
        self._move = "../src/moveRecorded/bonnard1.move"


    def run(self):


        ### Geste
        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False
        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(0)

        ### Son
        
        self._speak.start(self._text)






class Bonnard2(pypot.primitive.Primitive):

    def __init__(self, robot):

        pypot.primitive.Primitive.__init__(self, robot)
        self._speak = Speak(robot)
        self._text = "Le projet suivant est celui d'Axel"
        self._move = "../src/moveRecorded/bonnard2.move"


    def run(self):


        ### Geste
        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False
        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(1.5)

        ### Son
        
        self._speak.start(self._text)






class Bonnard3(pypot.primitive.Primitive):

    def __init__(self, robot):

        pypot.primitive.Primitive.__init__(self, robot)
        self._speak = Speak(robot)
        self._text = "Maintenant, voici le projet de reconnaissance biométrique de Jérôme"
        self._move = "../src/moveRecorded/bonnard3.move"


    def run(self):


        ### Geste
        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False
        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(0.5)

        ### Son
        
        self._speak.start(self._text)







class Bonnard4(pypot.primitive.Primitive):

    def __init__(self, robot):

        pypot.primitive.Primitive.__init__(self, robot)
        self._speak = Speak(robot)
        self._text = "Enfin, je suis le projet tchéri. Je suis actuellement en développement. Je laisse mes concepteurs t'en parler."
        self._move = "../src/moveRecorded/bonnard4.move"


    def run(self):


        ### Geste
        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False
        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(0.2)

        ### Son
        
        self._speak.start(self._text)




class Bonnard5(pypot.primitive.Primitive):

    def __init__(self, robot):

        pypot.primitive.Primitive.__init__(self, robot)
        self._speak = Speak(robot)
        self._text = "Je n'ai pas pu venir te rencontrer à Paris pour la cérémonie. A propos, ai-je le droit à une médaille?"
        self._move = "../src/moveRecorded/bonnard5.move"


    def run(self):


        ### Geste
        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False
        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(0.5)

        ### Son
        
        self._speak.start(self._text)




class Bonnard6(pypot.primitive.Primitive):

    def __init__(self, robot):

        pypot.primitive.Primitive.__init__(self, robot)
        self._speak = Speak(robot)
        self._text = "Si quelque chose ne va pas, n'hésite pas à me le dire, et j'appellerai les infirmières."
        self._move = "../src/moveRecorded/bonnard6.move"


    def run(self):


        ### Geste
        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False
        
        with open(self._move) as f :

            m = Move.load(f)
    
        move_player = MovePlayer(self.robot, m)
        move_player.start()
        
        time.sleep(0.5)

        ### Son
        
        self._speak.start(self._text)