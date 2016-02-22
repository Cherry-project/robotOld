#!/usr/bin/env python
#-*- coding: utf-8 -*-

import mp3play
import re
import time
from gtts import gTTS
import pypot.primitive
from threading import Thread, RLock
from textToSpeech.mp3Read import MP3Read

# Primitives déjà attachés au robot 
from behavior.yes import YesBehave
from behavior.restOpen import RestOpenBehave
from behavior.openArms import OpenArmsBehave
from behavior.openMove import OpenMoveBehave
from behavior.pointArmLeft import PointArmLeftBehave
from behavior.question import QuestionBehave
from behavior.doubleMe import DoubleMeBehave
from behavior.swap import SwapBehave
from behavior.showRightRest import ShowRightRestBehave
from behavior.disappointment import DisappointmentBehave
from behavior.littleArmsUp import LittleArmsUpBehave
from behavior.leftArms import LeftArmsBehave
from behavior.rightArms import RightArmsBehave
from behavior.showFrontHunkers import ShowFrontHunkersBehave




from speak import Speak

class TextBleu(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)
        
        self._robot = robot
        self._text = 'textToSpeech/video_bleu.txt'
        
        # Déjà attachés au robot
        self._robot.swap_behave = SwapBehave(robot)
        self._robot.point_arm_left_behave = PointArmLeftBehave(robot)
        self._robot.show_right_rest_behave = ShowRightRestBehave(robot)
        self._robot.disappointment_behave = DisappointmentBehave(robot)
        self._robot.little_arms_up_behave = LittleArmsUpBehave(robot)
        self._robot.question_behave = QuestionBehave(robot)
        self._robot.left_arms_behave = LeftArmsBehave(robot)
        self._robot.right_arms_behave = RightArmsBehave(robot)
        self._robot.open_move_behave = OpenMoveBehave(robot)
        self._robot.double_me_behave = DoubleMeBehave(robot)
        self._robot.rest_open_behave = RestOpenBehave(robot)
        self._robot.open_arms_behave = OpenArmsBehave(robot)    
        self._robot.show_front_hunkers_behave = ShowFrontHunkersBehave(robot)

    def start(self):
           
        pypot.primitive.Primitive.start(self)
        

    def run(self):
        while self.running:
            
            poppy = self._robot
            
            # IT
            phrase = 1
            
            
            filename = "../utils\Phrase_bleu.mp3"
            
            # Extraction des phrases en fonction des sauts de lignes
            data = open(self._text, 'r')
            texts = re.split(r'[\n\r]+', data.read())
            #texts = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', data.read())          
            for text in texts:           
                
                # utilisation de gtts
                _text = text.decode('utf-8', errors='replace')
                tts = gTTS(_text, lang='fr')
                tts.save(filename)

                clip =  MP3Read(filename)
    
                #comment t'appelles-tu?
                if phrase == 1:
                    # TÊTE
                    poppy.head_y.goto_position(20,1, wait=False)
                    
                    poppy.rest_open_behave.start()
                    clip.start()
                    time.sleep(1)
                    poppy.open_arms_behave.start()
                    time.sleep(2.5)                    
                    poppy.point_arm_left_behave.start()
                    time.sleep(1.5)
                    poppy.rest_open_behave.start()

                    time.sleep(2)

                # C'est la première fois...
                if phrase == 2:
                    poppy.open_move_behave.start()
                    clip.start()
                    time.sleep(2.5)
                    poppy.question_behave.start()
                    time.sleep(2.5)
                    poppy.rest_open_behave.start()

                    time.sleep(2)

                #comment tu te sens quand tu parles à un robot
                if phrase == 3:
                    #Tête
                    poppy.head_y.goto_position(-10,0.5, wait=True)
                    poppy.head_y.goto_position(20,0.5, wait=True)
                    time.sleep(0.5)

                    clip.start()
                    poppy.point_arm_left_behave.start()
                    time.sleep(2)
                    poppy.rest_open_behave.start()

                    time.sleep(2)

                # j'aimerai bien avoir des emotions  
                if phrase == 4:
                    # Tête
                    poppy.head_y.goto_position(-10,0.5, wait=True)
                    poppy.head_y.goto_position(20,0.5, wait=True)
                    time.sleep(0.5)

                    poppy.swap_behave.start()
                    time.sleep(0.7)
                    clip.start()
                    time.sleep(1.3)
                    poppy.double_me_behave.start()
                    time.sleep(3)
                    poppy.rest_open_behave.start()

                    time.sleep(2)

                # j'ai une devinette ca te dit? 
                if phrase == 5:
                    poppy.question_behave.start()
                    time.sleep(0.2)
                    clip.start()
                    time.sleep(2.5)
                    poppy.rest_open_behave.start()

                    time.sleep(2)

                # quelle est la monnaie des poissons   
                if phrase == 6:
                    clip.start()

                    time.sleep(2.5)

                # les sous-marins  
                if phrase == 7:
                    clip.start()
                    time.sleep(1.1)
                    poppy.double_me_behave.start()
                    time.sleep(1.7)
                    poppy.rest_open_behave.start()
                    time.sleep(0.7)
                    
                    #Tête
                    poppy.head_y.goto_position(-10,0.5, wait=True)
                    poppy.head_y.goto_position(20,0.5, wait=True)
                    time.sleep(2)

                # sais tu qui je suis  
                if phrase == 8:
                    clip.start()
                    poppy.question_behave.start()
                    time.sleep(1.5)
                    poppy.rest_open_behave.start()
                    time.sleep(2)

                # blabla 
                if phrase == 9:
                    poppy.double_me_behave.start()
                    time.sleep(0.5)
                    clip.start()
                    time.sleep(1)
                    poppy.question_behave.start()
                    time.sleep(2.5)
                    poppy.swap_behave.start()
                    time.sleep(4)
                    poppy.little_arms_up_behave.start()
                    time.sleep(2.5)
                    poppy.question_behave.start()
                    time.sleep(2)
                    poppy.rest_open_behave.start()


                # tu veux en savoir plus?
                if phrase == 10:
                    clip.start()
                    poppy.question_behave.start()
                    time.sleep(2)
                    poppy.rest_open_behave.start()

                    time.sleep(1.5)

                # Précisions blabla
                if phrase == 11:
                    clip.start()
                    time.sleep(1)
                    poppy.left_arms_behave.start()

                    time.sleep(2)
                    poppy.right_arms_behave.start()

                    time.sleep(2.5)
                    poppy.rest_open_behave.start()

                    time.sleep(2.5)
                    poppy.open_move_behave.start()

                    time.sleep(1.5)
                    poppy.rest_open_behave.start()

                    #Tête
                    poppy.head_y.goto_position(-10,0.5, wait=True)
                    poppy.head_y.goto_position(20,0.5, wait=True)

                # tu serais content de jouer avec moi   
                if phrase == 12:
                    clip.start()
                    poppy.question_behave.start()
                    time.sleep(2.5)
                    poppy.rest_open_behave.start()
                    time.sleep(2)

                # Super
                if phrase == 13:
                    poppy.little_arms_up_behave.start()
                    time.sleep(0.7)
                    clip.start()
                    time.sleep(1)
                    poppy.rest_open_behave.start()
                    time.sleep(1)

                # Maintenant il faut laisser la place   
                if phrase == 14:
                    clip.start()
                    time.sleep(2.5)
                    poppy.question_behave.start()
                    time.sleep(1.5)
                    poppy.show_front_hunkers_behave.start()

                    time.sleep(2.5)
                    poppy.show_right_rest_behave.start()

                    time.sleep(2.2)
                    poppy.rest_open_behave.start()

                clip.join()
                phrase = phrase+1

    def teardown(self):
        self.running = False
        print("Fin de la primitive")
            
