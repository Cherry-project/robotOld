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
from tts_watson.TtsWatson import TtsWatson 
# import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning


#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# engine = pyttsx.init()
# engine.setProperty('rate', 150)
# engine.say(response)
# engine.runAndWait()
ttsWatson = TtsWatson('9ab9e322-6ac9-4d11-a93f-10c19667a013', 'G4QF16oBGpIC', 'fr-FR_ReneeVoice')
# chaine = ""
# tab = sys.argv[1].split("_");
# for i in tab :
# 	chaine+=i+" "
# ttsWatson.play(chaine.encode('utf-8'))
ttsWatson.play("Bonjour")