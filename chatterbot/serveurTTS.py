#!/usr/bin/env python
# coding: utf-8

import socket
from gtts import gTTS
import pygame
from pygame import mixer
import os

tts = gTTS(text="Bonjour", lang='fr')
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

i = 0
while True:
        socket.listen(10)
        client, address = socket.accept()
        print "{} connected".format( address )

        phrase = client.recv(255)
        if phrase != "":
                print phrase

                tts = gTTS(text=phrase.decode("cp1252"), lang='fr')
                tts.save("google"+str(i)+".mp3")
                pygame.mixer.init()
                pygame.mixer.music.load("google"+str(i)+".mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                	continue
                print "done playing"
                pygame.mixer.quit()
                if i > 0 :
                	os.remove("google"+str(i-1)+".mp3")
                i=i+1
print "Close"
client.close()
stock.close()