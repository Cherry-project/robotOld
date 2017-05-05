#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import httplib,urllib
import urllib2
import requests

def getResponseFromChatterbot(response):
	start = response.index("Bot :")
	end = 0
	start=start+5
	# if "Bot: <IGNORER>" in response:
	# 	start = response.index("Bot : <IGNORER>")
	# # 	start = start+15
	# if "Bot: <IGNO" not in response:
	# 	start = response.index("Bot : <IGNORER>")
	# 	start = start+5

	# if response.index("<NOREUT>") == 1 :
	# 	end = response.index("<NOREUT>")
	# TODO
	if "<NOREUT>" not in response:
		end = response.index("<form method")
	try:
		result = response[start:end]
	except Exception :
		result = 'Je ne comprends pas désolé'
	#print "normal : "+result
	#print "utf8 : "+result.decode("utf-8")
	#print "normal : "+result
	return result

def sendToChatterbot(msg):
	sauveInput=""
	var=""
	varTemp=""
	cerveau="AR.txt"
	vraiesvars=""
	nom=""
	noReut=""
	rappel=""

	
	print "chaine :"+msg
	#msg=msg.decode('utf8')
	#print str(msg)
	#msg=u'ça va'
	#print msg
	url="http://127.0.0.1/Genesis/chatterbot23.php"
	msg=msg.decode('utf8')

	USER_AGENT = "Mozilla/5.0"
	urlParameters="vartemp="+varTemp+ "&cerveau=" + cerveau + "&vraiesvars=" + vraiesvars + "&nom=" + nom + "&noreut=" + noReut + "&var=" + var + "&usersay=" + msg + "&sauveinput=" + sauveInput + "&rappel=" +rappel
	#params=urllib.urlencode ({'vartemp=':varTemp,'&cerveau=':cerveau,"&vraiesvars=":vraiesvars,"&nom=":nom,"&noreut=":noReut,"&var=":var,"&usersay=":msg,"&sauveinput=":sauveInput,"&rappel=":rappel})
	params={'vartemp':varTemp,'cerveau':cerveau,"vraiesvars":vraiesvars,"nom":nom,"noreut":noReut,"var":var,"usersay":msg,"sauveinput":sauveInput,"rappel":rappel}
	#data = urllib.urlencode(params)
	# Send HTTP POST request
	r = requests.post("http://127.0.0.1/Genesis/chatterbot23.php", data=params)
	#print(r.text)
	# req = urllib2.Request(url, data)
	# response = urllib2.urlopen(req)
	# html = response.read()
	test = getResponseFromChatterbot(r.text)
	return test



	
		









