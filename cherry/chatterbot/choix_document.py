#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Script permettant de récupérer des fichiers textes et de les lire depuis la base de donnée du site web 

import sys
import os
import urllib
import urllib2

reponse = "/home/thib/Documents/Cherry/pyector/src/reponse.txt " #Chemin vers un fichier texte qui contiendra la réponse lue par pico2wave
pico = 'sh ~/Documents/Cherry/pico.sh' #Chemin vers le script pico, qui lance pico2wave

def ChoixDocument(reponse,urls,j):

	nombre = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

	if(reponse == "je veux écouter le 1er"):

		response=urllib2.urlopen(urls[0])
		htmlSource = response.read()
		response.close()
		fichier = open(reponse, "w+")
		fichier.write(htmlSource)
		fichier.close()
		os.system('sh ~/Documents/Cherry/pico.sh')

	for i in nombre:

		print(i)

		if(reponse == "je veux écouter le " + str(i) + "e"):

			print(i)
			print(str(urls[i]))
			response=urllib2.urlopen(urls[i])
			htmlSource = response.read()
			response.close()
			fichier = open(reponse, "w+")
			fichier.write(htmlSource)
			fichier.close()
			os.system(pico)

	if(j ==1):
		if(reponse == "oui") or (reponse == "oui je veux l'écouter") or (reponse == "yes") or (reponse == "oui je veux bien"):

			response=urllib2.urlopen(urls[0])
			htmlSource = response.read()
			response.close()
			fichier = open(reponse, "w+")
			fichier.write(htmlSource)
			fichier.close()
			os.system(pico)

		if(reponse == "Non"):

			print(non)

	if(j==0):

		print(non)






