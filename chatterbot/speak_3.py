#!/usr/bin/env python)
# -*- coding: utf-8 -*-

import time
import sys
import os
import pypot.primitive
import pygame.mixer
import csv
from random import randint
import subprocess
#import pyglet
#from pyglet.media import avbin
#import mp3play

#TTS engines
from gtts import gTTS
from tts_watson.TtsWatson import TtsWatson


csv_file_name = "/home/poppy/resources/audio/list.csv"
mp3_dir = "/home/poppy/resources/audio/"


def find(reader, sentence, language, tts_engine):
	for row in reader:
		print("csv text : "+row.get("text").decode('utf-8'))
		if row.get("text").decode('utf-8') == sentence:
			if( language in row.get("file") and tts_engine in row.get("file")):
				return row.get("file")

	return False




class Speak(pypot.primitive.Primitive):

	properties = pypot.primitive.Primitive.properties + ['sentence_to_speak','language', 'tts_engine']
	def __init__(self, robot, text = 'coucou', lang= 'fr', ttsengine='watson'):
		
			pypot.primitive.Primitive.__init__(self, robot)
			self._text = text.decode('utf-8')
			self._lang = lang.decode('utf-8')

			# TTS
			self._ttsengine = ttsengine.decode('utf-8')
			self.ttsWatson = TtsWatson('28d3342c-5436-4cdb-a587-40da89f80afa', 'EKNVJxa0KbZB', 'fr-FR_ReneeVoice')

			self._rate = 24000


			
			print "INIT"
			print text, type(text)
			print text.decode('utf-8'), type(text.decode('utf-8'))
			print "FIN INIT"


	#def start(self, text):
	def start(self):
		
			#self._text = text.decode('utf-8', errors='replace')
			pypot.primitive.Primitive.start(self)


	def run(self):

			if self._text == None:
				print "pas de texte"
			else:
				print "START"
				print "self._text", type(self._text)
				print "Bitrate: " + str(self._rate)
				
				filename_temp = find(reader, self._text)
                
				filename = mp3_dir + filename_temp
				
				#filename = self._filename
				
				#print filename
				
				
				
				pygame.mixer.init(self._rate)
				pygame.mixer.music.load(os.path.abspath(filename))
				pygame.mixer.music.set_volume(0.8)
				pygame.mixer.music.play()
				
				while pygame.mixer.music.get_busy():
					time.sleep(0.1)

				pygame.mixer.quit()
					
			
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
				
				
				filename_temp = find(reader, self._text, self._lang, self._ttsengine)
				
				if filename_temp:
					self._filename = mp3_dir + filename_temp
					
				else:
					filename_temp = self._ttsengine + "_" + self._lang + "_" + str(randint(1, 99999))+".mp3"
					filename = mp3_dir + filename_temp
					print "DEBUT GENERATION"
					
					if(self._ttsengine == "google"):
						tts = gTTS(self._text, lang=self._lang)
						tts.save(filename)
						#self._rate = 24000
						print "Play with Google"

					if(self._ttsengine == "watson"):

						self.ttsWatson.save(filename, (self._text))

						print "Play with Watson"

					if(self._ttsengine == "pico"):
						
						if (self._lang == "en"):
							lang = 'en-US'
						else:
							lang = 'fr-FR'

						filename_temp = filename_temp.replace(".mp3", ".wav")
						filename = filename.replace(".mp3", ".wav")
						print filename	
						cmd = 'pico2wave -l=' + lang + ' -w=' + filename + ' "' + self._text + '"' +  ' || echo "No .wav file created"'
						subprocess.call(cmd, shell=True)
						#self._rate = 16000
						print "Play with Pico"

					
					print "nouvelle entrée"
					new = (self._text.encode('utf-8'), filename_temp)
					print new
					w = csv.writer(file)
					w.writerow(new)
					self._filename = filename
					print "FIN GENERATION"

					
	@property
	def language(self):
		return self._lang
	@language.setter
	def language(self, lang):
		print "Now, I speak " + lang
		lang.encode('utf-8')
		self._lang = lang

		if(self._ttsengine == "watson"):
			self.ttsWatson.set_spoken_language(lang)


	@property
	def tts_engine(self):
			return self._ttsengine
	@tts_engine.setter
	def tts_engine(self, engine):
			
			engine.encode('utf-8')
			self._ttsengine = engine 

			if(engine == "google"):
				self._rate = 24000
			if(engine == "watson"):
				self._rate = 22050
			if(engine == "pico"):
				self._rate = 16000

			print "Now, my TTS engine is: " + engine + " and the bitrate is: " + str(self._rate)