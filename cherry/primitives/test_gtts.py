#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pypot.robot
import requests
import json

from gtts import gTTS

class TestGTTS(pypot.primitive.Primitive):
        
        
    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        


    def start(self):
        
        print "Test du service GTTS"
        
        
        try: 
            tts = gTTS("Bonjour", lang='fr')
        except:
            print "Echec de la requète. GTTS indisponible"
