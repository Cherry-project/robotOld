#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import urllib
import urllib2


reponse = "/home/thib/Documents/Cherry/pyector/src/reponse.txt" #Chemin vers un fichier texte contenant la réponse lue par pico2wave
def ReponseRobot(msg,sauveinput,var,vartemp,vraiesvar,nom,noreut):


		params = urllib.urlencode({'usersay':msg,'sauveinput':sauveinput,'var':var,'vartemp':vartemp,'cerveau':"AR.txt",'vraiesvar':vraiesvar,'nom':nom,'noreut':noreut})
		response=urllib2.urlopen('http://localhost/Genesis/chatterbot23.php',params)
		htmlSource = response.read()                            
		response.close()                                        
		

		start = htmlSource.find("Bot : ")
		if(htmlSource.find("Bot : <IGNORER>")!=-1):
		    start = htmlSource.find("Bot : <IGNORER>")
		    start = start +15
		if(htmlSource.find("Bot : <IGNO")==-1):
			start = start + 5
		if(htmlSource.find("Bot : <IGNORER><IGNORER>")!=-1):
			start = start + 26


		end = htmlSource.find("<form method")

		if(htmlSource.find("<NOREUT>")==1):
			end = htmlSource.find("<NOREUT>")
			print("tonpere")

		if(htmlSource.find("<NOREUT>")==-1):
			print("coucou")
			end = htmlSource.find("<form method")




		start2 = htmlSource.find("<INPUT NAME=\"var\" value=\"")
		start3 = htmlSource.find("<INPUT NAME=\"vartemp\" value=\"")
		start4 = htmlSource.find("<INPUT NAME=\"cerveau\" value=\"")
		start5 = htmlSource.find("<INPUT NAME=\"vraiesvars\" value=\"")
		start6 = htmlSource.find("<INPUT NAME=\"nom\" value=\"")
		start7 = htmlSource.find("<INPUT NAME=\"noreut\" value=\"")


		end2 = htmlSource.find("\" id=\"var")
		end3 = htmlSource.find("\" id=\"vartemp")
		end4 = htmlSource.find("\" id=\"cerveau")
		end5 = htmlSource.find("\" id=\"vraiesvar")
		end6 = htmlSource.find("\" id=\"nom")
		end7 = htmlSource.find("\" id=\"noreut")


		
		print (start,end,start2,start3,start4,start5,start6,start7,end2,end3,end4,end5,end6,end7)
		print (htmlSource[start:end])

		var = htmlSource[start2+25:end2]
		vartemp = htmlSource[start3+29:end3]
		vraiesvar = htmlSource[start5+25:end5]
		nom = htmlSource[start6+25:end6]
		noreut = htmlSource[start7+28:end7]

		fichier = open(reponse, "w+")
		fichier.write(htmlSource[start:end])
		fichier.close()

		print("sauve : " +sauveinput)
		print("var :"+ var)
		print("vartemp : "+vartemp)
		print("vraiesvar : "+vraiesvar)
		print("nom : "+nom)
		print("noreut : "+noreut)

		return(sauveinput, var,vartemp,vraiesvar,nom,noreut)
