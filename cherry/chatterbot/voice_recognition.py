#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Reconnaissance de la voix par Google Speech Recognition


import sys
import os
import speech_recognition as sr
import urllib2
import urllib
from test_bdd import RechercheFichiers


def voice_recognition():

	
	print "Start Listening!"
	# obtain audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.adjust_for_ambient_noise(source)
		print("Say something!")
		audio = r.listen(source)
	# recognize speech using Google Speech Recognition

	try:
			    # for testing purposes, we're just using the default API key
			    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
			    # instead of `r.recognize_google(audio)`
		print("Google Speech Recognition thinks you said " + r.recognize_google(audio,language='FR'))
			
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		voice_recognition()

		return 0 
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))


	msg = r.recognize_google(audio,language='FR').encode("utf-8")
	print(msg)

	return(msg)
