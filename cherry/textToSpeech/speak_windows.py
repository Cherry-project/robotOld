#!/usr/bin/env python)
# -*- coding: utf-8 -*-

import time
import sys
import os
import pypot.primitive
import pygame.mixer
#import pyglet
#from pyglet.media import avbin
import mp3play

#TTS engines
from gtts import gTTS
from tts_watson.TtsWatson import TtsWatson


class Speak(pypot.primitive.Primitive):

    properties = pypot.primitive.Primitive.properties + ['sentence_to_speak','language', 'tts_engine']
    
    def __init__(self, robot, text = 'coucou', lang='fr', ttsengine='google'):
        
            pypot.primitive.Primitive.__init__(self, robot)

            self._text = text.decode('utf-8')
            self._lang = lang.decode('utf-8')
            self._ttsengine = ttsengine.decode('utf-8')

            self.ttsWatson = TtsWatson('c18c9e2a-25ae-4e3d-9cb0-7281a19d1f7b', 'Tc5kBRiUuTz5', 'fr-FR_ReneeVoice')

    def start(self):
        
            #self._text = text.decode('utf-8', errors='replace')
            pypot.primitive.Primitive.start(self)


    def run(self):

        
                filename = 'Phrase1.mp3'

                # Use GOOGLE as a tts engine
                if(self._ttsengine == "google"):
                    tts = gTTS((self._text), lang=self._lang)
                    tts.save(filename)
                    print "Play with Google"

                # Use WATSON as a tts engine
                if(self._ttsengine == "watson"):
                    #ttsWatson = TtsWatson('c18c9e2a-25ae-4e3d-9cb0-7281a19d1f7b', 'Tc5kBRiUuTz5', 'fr-FR_ReneeVoice')
                    self.ttsWatson.save(filename, (self._text))
                    #ttsWatson.play((self._text))
                    print "Play with Watson"


                clip = mp3play.load(os.path.abspath('Phrase1.mp3'))
                clip.play()

                while clip.isplaying() is not False:
                    time.sleep(0.5)

                #pygame.mixer.init(16000)
                #pygame.mixer.music.load(os.path.abspath(filename))
                #pygame.mixer.music.set_volume(0.8)
                #pygame.mixer.music.play()
                
                #while pygame.mixer.music.get_busy():
                #    time.sleep(0.5)
                
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
            text.encode('utf-8')
            self._text = text
    
    @property
    def language(self):
            return self._lang
    @language.setter
    def language(self, lang):
            print "Now, I speak " + lang
            lang.encode('utf-8')
            self._lang = lang 

    @property
    def tts_engine(self):
            return self._ttsengine
    @tts_engine.setter
    def tts_engine(self, engine):
            print "Now, my TTS engine is: " + engine
            engine.encode('utf-8')
            self._ttsengine = engine 


