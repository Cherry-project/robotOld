#!/usr/bin/env python)
# -*- coding: utf-8 -*-

import time
import sys
import os
import pypot.primitive
import pygame.mixer
import csv
from random import randint
#import pyglet
#from pyglet.media import avbin
#import mp3play

from gtts import gTTS
#from subprocess import call


csv_file_name = "list.csv"
mp3_dir = "audio"


def find(reader, sentence):
    for row in reader:
        print("csv text : "+row.get("text").decode('utf-8'))
        if row.get("text").decode('utf-8') == sentence:
            return row.get("file")

    return str(randint(1, 99999))+".mp3"




class Speak(pypot.primitive.Primitive):

	properties = pypot.primitive.Primitive.properties + ['sentence_to_speak']
	def __init__(self, robot, text = 'coucou'):
        
			pypot.primitive.Primitive.__init__(self, robot)
                        self._text = text.decode('utf-8')

                        print "INIT"
                        print text, type(text)
                        print text.decode('utf-8'), type(text.decode('utf-8'))
                        print "FIN INIT"


	#def start(self, text):
	def start(self):
        
			#self._text = text.decode('utf-8', errors='replace')
			pypot.primitive.Primitive.start(self)


	def run(self):

            if self._text != "":
                print "START"
                print "self._text", type(self._text)
            
                file = open(csv_file_name, "a+")
                reader = csv.DictReader(file)
                file.seek(0)
            
                filename_temp = find(reader, self._text)
                
                filename = mp3_dir + filename_temp
            
                print "filename : "+filename
            
                #clip = mp3play.load(os.path.abspath('../utils/Phrase1.mp3'))
                #clip.play()
            
                #while clip.isplaying() is not False:
                #    time.sleep(0.5)
                try:
                    pygame.mixer.init(16000)
                    pygame.mixer.music.load(os.path.abspath(filename))
                    pygame.mixer.music.set_volume(0.8)
                    pygame.mixer.music.play()
                
                    print "déjà connu"
                
                except:
                
                    print "DEBUT GENERATION"
                    tts = gTTS(self._text, lang='fr')
                    tts.save(filename)
                    
                    print "nouvelle entrée"
                    new = (self._text.encode('utf-8'), filename_temp)
                    print new
                    w = csv.writer(file)
                    w.writerow(new)
                
                    print "FIN GENERATION"
                    pygame.mixer.init(16000)
                    pygame.mixer.music.load(os.path.abspath(filename))
                    pygame.mixer.music.set_volume(0.8)
                    pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    time.sleep(0.5)
                
                file.close()

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
            print "CHANGE TEXT"
            print type(text), text.encode('utf-8')
            #print text.decode('utf-8'), type(text.decode('utf-8'))
            print "FIN CHANGE TEXT"

            self._text = text

        
        
