#!/usr/bin/env python)
# -*- coding: utf-8 -*-

import time
import sys
import os
import pypot.primitive
#import pyglet
#from pyglet.media import avbin
#import mp3play

import pygame.mixer

from gtts import gTTS
#from subprocess import call

class Speak(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._text = u'coucou'

    def start(self, text):
        
        self._text = text.decode('utf-8', errors='replace')
        pypot.primitive.Primitive.start(self)


    def run(self):

        
        filename = 'Phrase1.mp3'
                
        tts = gTTS(self._text, lang='fr')
        tts.save(filename)
              
        #call (['play', path])
        #call (['play', '../utils/Phrase1.mp3'])
        #os.startfile('../utils/Phrase1.mp3')
        # OR
        #call(os.path.abspath('../utils/Phrase1.mp3'), shell=True)

        #clip = mp3play.load(os.path.abspath('../utils/Phrase1.mp3'))
        #clip.play()
        #
        #while clip.isplaying() is not False:
        #   time.sleep(0.5)
        
        #mp3 = pyglet.media.load(filename)
        #mp3.play()
        
        pygame.mixer.init(16000)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pass
        

        # wait until terminated 
        #time.sleep(mp3.duration)
            
        
        
        
