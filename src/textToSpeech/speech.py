#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pypot.primitive
#import mp3play
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer

from gtts import gTTS

from subprocess import call

class Speech(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._text = "Bonjour ! Je m'appelle Cherry. Je suis là pour t'aider durant ton séjour."
        self._move = "../src/moveRecorded/speech.move"

    def run(self):

        poppy = self.robot

        for m in poppy.motors:
            m.compliant = False

        filename = '../utils/temp.mp3'
        
        with open(self._move) as f :

            m = Move.load(f)

        tts = gTTS(self._text, lang='fr')
        tts.save(filename)
        call(["play", '../utils/temp.mp3'])
