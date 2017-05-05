#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:32:24 2017

@author: gdebat
"""

import json
import pypot
import time

from pypot.vrep import from_vrep
from poppy.creatures import PoppyTorso
#from cherry import Cherry
from STT_google import STT_google
from chatterbot import sendToChatterbot
#from textToSpeech.TTS_test import TTS_test


poppy = PoppyTorso(simulator='vrep')
#sp=Speak(poppy, text="Non vous n'avez pas souri!")
sp=STT_google(poppy, state='normal')
sp.run()
print "ok"

# poppy = PoppyTorso(simulator='vrep')
# #sp=Speak(poppy, text="Non vous n'avez pas souri!")
# sp=TTS_test(poppy, text='Bonjour', lang= 'fr', ttsengine='google')
# sp.run()
# print "ok"

