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


csv_file_name = "/home/poppy/resources/audio/list.csv"
mp3_dir = "/home/poppy/resources/audio/"


def find(reader, sentence):
    for row in reader:
        if row.get("text").decode('utf-8') == sentence:
            return row.get("file")

    return False




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

            if self._filename == None:
                print "pas de texte"
            else:
                print "START"
                print "self._text", type(self._text)
                
                """
                
                reader = csv.DictReader(file)
                file.seek(0)
                
                filename_temp = find(reader, self._text)
                
                filename = mp3_dir + filename_temp
                
                print filename
                """
                #filename_temp = self._filename
                
                filename = self._filename
                
                print filename
                
                #clip = mp3play.load(os.path.abspath('../utils/Phrase1.mp3'))
                #clip.play()
                
                #while clip.isplaying() is not False:
                #    time.sleep(0.5)
                
                
                pygame.mixer.init(24000)
                pygame.mixer.music.load(os.path.abspath(filename))
                pygame.mixer.music.set_volume(0.8)
                pygame.mixer.music.play()
                
            
                """    
                except:
                
                print "DEBUT GENERATION"
                tts = gTTS(self._text, lang='fr')
                tts.save(filename)
                
                
                print "nouvelle entrée"
                file = open(csv_file_name, "a+")
                new = (self._text.encode('utf-8'), filename_temp)
                print new
                w = csv.writer(file)
                w.writerow(new)
                
                print "FIN GENERATION"
                pygame.mixer.init(16000)
                pygame.mixer.music.load(os.path.abspath(filename))
                pygame.mixer.music.set_volume(2)
                pygame.mixer.music.play()

                file.close()
                """
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
                    
            
	@property
	def sentence_to_speak(self):
            return self._text

	@sentence_to_speak.setter
	def sentence_to_speak(self, text):
            if text == "":
                self._filename = None
            else:
                print "CHANGE TEXT"
                print type(text), text.encode('utf-8')
                #print text.decode('utf-8'), type(text.decode('utf-8'))
                print "FIN CHANGE TEXT"
                
                self._text = text
                
                file = open(csv_file_name, "a+")
                reader = csv.DictReader(file)
                file.seek(0)
                
                
                filename_temp = find(reader, self._text)
                
                if filename_temp:
                    self._filename = mp3_dir + filename_temp
                    
                else:
                    filename_temp = str(randint(1, 99999))+".mp3"
                    filename = mp3_dir + filename_temp
                    print "DEBUT GENERATION"
                    tts = gTTS(self._text, lang='fr')
                    tts.save(filename)
                    
                    
                    print "nouvelle entrée"
                    new = (self._text.encode('utf-8'), filename_temp)
                    print new
                    w = csv.writer(file)
                    w.writerow(new)
                    self._filename = filename
                    print "FIN GENERATION"
