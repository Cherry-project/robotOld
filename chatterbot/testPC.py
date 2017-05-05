#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Boucle permettant de tenir une conversation avec le robot

#pico = 'sh ~/Documents/Cherry/pico.sh' #Chemin vers le script pico, qui lance pico2wave

import sys
import os
import pypot
import urllib2
import urllib
import pyttsx
import string
import speech_recognition as sr
from chatterbot import sendToChatterbot
import pypot.primitive
from tts_watson.TtsWatson import TtsWatson 
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

while True :
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
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))


    #msg = r.recognize_google(audio,language='FR').encode("utf-8")
    #print "Message " + msg
	if msg:
		params = urllib.urlencode({'msg':msg})
		print "\nUtilisateur : " + msg
		print "J'envois la requête"
		#urllib2.urlopen('http://localhost:8080/chatterbot',params)
		response = sendToChatterbot(msg);
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
		print "\n Bot : "+response
		response = response.encode('utf-8')
		# engine = pyttsx.init()
		# engine.setProperty('rate', 150)
		# engine.say(response)
		# engine.runAndWait()
		ttsWatson = TtsWatson('c7b754a7-30af-478b-ad09-50d6599fee4a', '4PiXRAE4QPpU', 'fr-FR_ReneeVoice')
		ttsWatson.play(response)
		print "Requête délivrée"
		msg = ""
	else:
		print "Pas de message"
        
