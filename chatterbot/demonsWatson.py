#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import httplib,urllib
import urllib2
import requests
import pyaudio
import shutil
import pygame
from pygame import mixer 
import urllib
import io
import numpy as np
import pyglet

# r = requests.get("http://demonstrateur-watson.eu-gb.mybluemix.net/api/v1/text-to-speech/synthetize/%22Bonjour%22/fr-FR_ReneeVoice", stream=True)
# with open("testraw.ogg", 'wb') as f:
#         r.raw.decode_content = True
#         shutil.copyfileobj(r.raw, f)
# f.close()

# pygame.mixer.init()
# pygame.mixer.music.load("testraw.ogg")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue

tone_out = array(r.raw.read(),dtype=int16)
bytestream = tone_out.tobytes()

pya = pyaudio.PyAudio()
stream = pya.open(format=pya.get_format_from_width(width=2), channels=1, rate=OUTPUT_SAMPLE_RATE, output=True)
stream.write(bytestream)
stream.stop_stream()
stream.close()

pya.terminate()


# r.raw.decode_content = True
# arr = np.fromstring(r.raw.read(10000), 'Int16')
# print arr

# bytes = map(ord, data)
# print bytes

# snd = sound.Output(44100, 2, 2)

# with open("testraw.ogg", 'rb') as f:
#         frames = f.read()
# ascii_data = frames.decode("ascii", errors="ignore")
# print ascii_data

# song = pyglet.media.load('thesong.ogg')
# song.play()
# pyglet.app.run()

# pyaud = pyaudio.PyAudio()
# srate=22050
# stream = pyaud.open(format = pyaud.get_format_from_width(2),
#                 channels = 1,
#                 rate = srate,
#                 output = True)

# stream.write(frames)
# stream.close()
# f.close()
# pyaud.terminate()


# u = urllib2.urlopen("http://demonstrateur-watson.eu-gb.mybluemix.net/api/v1/text-to-speech/synthetize/%22Bonjour%20Bordeaux%20!%22/fr-FR_ReneeVoice")
# data = u.read(8192)

# while data:
#     stream.write(data)
#     data = u.read(8192)



# p = pyaudio.PyAudio()
# stream = p.open(format=p.get_format_from_width(2),
#                 channels=1,
#                 rate=11025,
#                 output=True)
# chaine = ""
# for byte in bytes :
# 	chaine+=str(byte)+" "
# chaine = chaine[:1]
# print chaine
# stream.close()
# stream.terminate()

# def play_binary_audio(self, binary_audio):
#         p = pyaudio.PyAudio()
#         stream = p.open(format=p.get_format_from_width(2),
#                         channels=1,
#                         rate=22050,
#                         output=True)
#         stream.write(binary_audio) 
