#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Boucle permettant de tenir une conversation avec le robot

#pico = 'sh ~/Documents/Cherry/pico.sh' #Chemin vers le script pico, qui lance pico2wave

import sys
import os
import pypot
import urllib2
import urllib
import speech_recognition as sr
from test_bdd import RechercheFichiers
from voice_recognition import voice_recognition
from choix_document import ChoixDocument
from ReponseRobot import ReponseRobot

class Listen(pypot.primitive.Primitive):
    
    properties = pypot.primitive.Primitive.properties + ['listen_state']
    def __init__(self, robot, state = 'normal' ):
        pypot.primitive.Primitive.__init__(self, robot)
        self._state = state
        self._robot = robot

          
    def start(self):
        pypot.primitive.Primitive.start(self)
        
        #msg = voice_recognition()
        
        while(self._state == 'normal'):
            # obtain audio from the microphone
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                print("Say something!")
                audio = r.listen(source)
            # recognize speech using Google Speech Recognition
            msg= ""
            try:
                        # for testing purposes, we're just using the default API key
                        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                        # instead of `r.recognize_google(audio)`
                msg = r.recognize_google(audio,language='FR').encode("utf-8")        
                print("Google Speech Recognition thinks you said " + msg)
                    
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                #voice_recognition()
                #return 0 
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


            #msg = r.recognize_google(audio,language='FR').encode("utf-8")
            #print "Message " + msg
            if msg:
                params = urllib.urlencode({'msg':msg})
                print "J'envois la requête"
                urllib2.urlopen('http://localhost:8080/chatterbot',params)
                print "Requête délivrée"
                msg = ""
            else:
                print "Pas de message"
            
		
    @property
    def listen_state(self):
        return self._state

    @listen_state.setter
    def listen_state(self, state):
        print "Set parameter to: " + state
        self._state= state
