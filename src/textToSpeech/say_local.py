#!/usr/bin/env python
# -*- coding: utf-8 -*-

#librairies annexes
import httplib, urllib

import StringIO
import wave
import time
import pymedia.audio.sound as sound

import sys

#librairies liées au robot poppy
import pypot.primitive
import pypot.robot

class maryclient:

    def __init__(self):

        self.host = "127.0.0.1"
        self.port = 59125 # 80 ou 8080
        self.input_type = "TEXT"
        self.output_type = "AUDIO"
        self.audio = "WAVE_FILE"
        self.locale = "fr"
        self.voice = "upmc-pierre"

    def set_host(self, a_host):
        """Set the host for the TTS server."""
        self.host = a_host

    def get_host(self):
        """Get the host for the TTS server."""
        self.host

    def set_port(self, a_port):
        """Set the port for the TTS server."""
        self.port = a_port

    def get_port(self):
        """Get the port for the TTS server."""
        self.port

    def set_input_type(self, type):
        """Set the type of input being 
           supplied to the TTS server
           (such as 'TEXT')."""
        self.input_type = type

    def get_input_type(self):
        """Get the type of input being 
           supplied to the TTS server
           (such as 'TEXT')."""
        self.input_type

    def set_output_type(self, type):
        """Set the type of input being 
           supplied to the TTS server
           (such as 'AUDIO')."""
        self.output_type = type

    def get_output_type(self):
        """Get the type of input being 
           supplied to the TTS server
           (such as "AUDIO")."""
        self.output_type

    def set_locale(self, a_locale):
        """Set the locale
           (such as "en_US")."""
        self.locale = a_locale

    def get_locale(self):
        """Get the locale
           (such as "en_US")."""
        self.locale

    def set_audio(self, audio_type):
        """Set the audio type for playback
           (such as "WAVE_FILE")."""
        self.audio = audio_type

    def get_audio(self):
        """Get the audio type for playback
           (such as "WAVE_FILE")."""
        self.audio

    def set_voice(self, a_voice):
        """Set the voice to speak with
           (such as "dfki-prudence-hsmm")."""
        self.voice = a_voice

    def get_voice(self):
        """Get the voice to speak with
           (such as "dfki-prudence-hsmm")."""
        self.voice

    def generate(self, message):
        """Given a message in message,
           return a response in the appropriate
           format."""
        raw_params = {"INPUT_TEXT": message,
                "INPUT_TYPE": self.input_type,
                "OUTPUT_TYPE": self.output_type,
                "LOCALE": self.locale,
                "AUDIO": self.audio,
                "VOICE": self.voice,
                }
        params = urllib.urlencode(raw_params)
        headers = {}

        # Open connection to self.host, self.port.
        #print('ouverture connection')
        conn = httplib.HTTPConnection(self.host, self.port)

        conn.set_debuglevel(5)
        
        #print('envoi requete')
        conn.request("POST", "/process", params, headers)
        #print('recuperation de la reponse')
        response = conn.getresponse()
        #print('renvoi de la reponse')
        #if response.status != 200:
            #print response.getheaders()
            #raise RuntimeError("{0}: {1}".format(response.status, response.reason))
        return response.read()


#définition de la classe pour dire un texte passé en paramètre
class Say_local(pypot.primitive.Primitive):

	def __init__(self, robot):
		pypot.primitive.Primitive.__init__(self, robot)

		self._robot = robot

		#texte par défaut
		self._text = 'Bonjour je m\'appelle poppy'

		print('init voice ok')

	def start(self, text):

		self._text = text

		pypot.primitive.Primitive.start(self)

	def run(self):

		client = maryclient()

		client.set_locale("fr")

		client.set_voice("upmc-pierre")

		#print('generation du son')

		the_sound = client.generate(self._text) #"Bonjour je m'appelle clément")

		#print('lecture du son')
		buf = StringIO.StringIO(the_sound)
		f = wave.open(buf, 'rb')
		sampleRate = f.getframerate()
		channels = f.getnchannels()
		format = sound.AFMT_S16_LE

		snd = sound.Output(sampleRate, channels, format)
		s = f.readframes(300000)
		snd.play(s)

		while snd.isPlaying():time.sleep(0.05)

