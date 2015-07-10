#!/usr/bin/env python)
# -*- coding: utf-8 -*-

import time
import sys
import pypot.primitive
#import mp3play

from gtts import gTTS
from subprocess import call

class Speak(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._text = 'coucou'

    def start(self, text):

        self._text = text

        pypot.primitive.Primitive.start(self)


    def run(self):

        filename = '../utils/temp.mp3'

        tts = gTTS(self._text, lang='fr')
        tts.save(filename)
        call (['play', '../utils/temp.mp3'])
