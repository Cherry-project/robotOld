#!/usr/bin/env python
# coding: utf-8

import socket
from gtts import gTTS
import pygame
from pygame import mixer
import os

tts = gTTS(text="Je vous écoute", lang='fr')
tts.save("google.mp3")
