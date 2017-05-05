import requests
import json
from gtts import gTTS
import pygame
from HTMLParser import HTMLParser


class Voice(object):
	@classmethod
	def go(cls,text,lang):
		
		#print HTMLParser().unescape(text)
		# Proceed special caracteres
		tts = gTTS(HTMLParser().unescape(text), lang=lang)
		tts.save("./tmp/temp.mp3")
		
		pygame.mixer.init()
		pygame.mixer.music.load("./tmp/temp.mp3")
		pygame.mixer.music.play()

		while pygame.mixer.music.get_busy():
			pass
		# load the configuration file that give the server addr and port for requests 
		json_data = open('./config/conf.json')
		data = json.load(json_data)
		json_data.close()

		# we need the server addr+port and the robot name so the server know which robot has ended his move
		ip = data['server']['addr']
		port = data['server']['port']
		name = data['robot']['name']

		# create the url for the request
		url = "http://"+str(ip)+":"+str(port)+"/robot/speakfinished/"

		# send the post with the robot name request to the server
		try: 
			requests.post(url, data = {'id':str(name)})
		except:
			# print "Request error"
			pass
		else:
			pass
			# print "Request sent !"

	@classmethod
	def silent(cls,text,lang):
		tts = gTTS(text, lang=lang)
		tts.save("./tmp/temp.mp3")

		pygame.mixer.init()
		pygame.mixer.music.load("./tmp/temp.mp3")
		pygame.mixer.music.play()

		while pygame.mixer.music.get_busy():
			pass


