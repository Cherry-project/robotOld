#!/usr/bin/env python)
# -*- coding: utf-8 -*-

import time
import sys
import os
import pypot.primitive
import pygame.mixer
#import pyglet
#from pyglet.media import avbin
#import mp3play

from gtts import gTTS
#from subprocess import call

class Speak(pypot.primitive.Primitive):

	properties = pypot.primitive.Primitive.properties + ['sentence_to_speak']
	def __init__(self, robot, text = 'coucou'):
        
			pypot.primitive.Primitive.__init__(self, robot)

			self._text = text
	#def start(self, text):
	def start(self):
        
			#self._text = text.decode('utf-8', errors='replace')
			pypot.primitive.Primitive.start(self)


	def run(self):

        
                filename = 'Phrase1.mp3'

                if self._text in "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 bonjour pas":
                        filename = "/home/poppy/resources/audio/tts/" + self._text + ".mp3"

                else:
                        tts = gTTS((self._text), lang='fr')
                        tts.save(filename)

                #clip = mp3play.load(os.path.abspath('../utils/Phrase1.mp3'))
                #clip.play()

                #while clip.isplaying() is not False:
                #    time.sleep(0.5)

                pygame.mixer.init(16000)
                pygame.mixer.music.load(os.path.abspath(filename))
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    time.sleep(0.5)
                
                #pygame.mixer.music.stop()
                #pygame.mixer.quit()
                
                #mp3 = pyglet.media.load(filename)
                #mp3.play()

                # wait until terminated 
                #time.sleep(mp3.duration)
            
	@property
	def sentence_to_speak(self):
			return self._text

	@sentence_to_speak.setter
	def sentence_to_speak(self, text):
            print text
            self._text = text

        
        
