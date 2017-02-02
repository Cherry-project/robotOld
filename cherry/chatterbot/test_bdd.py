#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Script permettant de récupérer les messages laissés sur le site web 


from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from numpy import *
from matplotlib.pyplot import *
from datetime import *


def RechercheFichiers():

	# Helper class to convert a DynamoDB item to JSON.
	class DecimalEncoder(json.JSONEncoder):
	    def default(self, o):
	        if isinstance(o, decimal.Decimal):
	            if o % 1 > 0:
	                return float(o)
	            else:
	                return int(o)
	        return super(DecimalEncoder, self).default(o)

	dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

	table = dynamodb.Table('Contents')

	response = table.query(
	    KeyConditionExpression=Key('target').eq('enfant2@gmail.com')
	)

	j=0
	date2 = array([])
	url2 = array([])
	titre = array([])
	descriptions = array([])
	messages = array([])
	for i in response['Items']:

		start_indice = i['realname'].find(".txt")
		if( start_indice != -1):

			nom =i['realname'][0:start_indice]
			date1 =i['start']
			url = i['name']
			url = "http://localhost/New/Uploads/" + url

			titre1 = i['title']
			descriptions1 = i['description']

			description2 = np.append(descriptions,descriptions1)
			today = date.today()
			now = datetime.now()



			if(int(date1[0:4])==today.year and int(date1[5:7])== today.month and int(date1[8:10]) == today.day and int(date1[11:13]) <= now.hour and int(date1[14:16]) <= now.minute):

				print("NOM TITRE : " + titre1 + "DATE" + date1)

				date2 = np.append(date2,date1)
				titre = np.append(titre,titre1)
				url2 = np.append(url2,url)
				j = j+1
				print(j)




	print(titre)

	if(j==1):

		msg = "Tu as reçu" + str(j) + "message aujourd'hui, nommé, " + str(titre[0]) + ". Souhaites-tu l'écouter ?"

	if(j==0):

		msg = "Tu n'as pas reçu de message aujourd'hui."

	if(j>1):

		print(titre[0])
		msg = "Tu as reçu " + str(j) + " messages aujourd'hui. Le premier s'appelle " + str(titre[0]) +", "
		print(msg)

		for k in range(j-1):
			print("nombre message =" + str(k+2))

			msg_suivant = "Le " + str(k+3) +"ieme s'appelle " + str(titre[k+1]) + ", "
			messages = np.append(messages,msg_suivant)
			print(messages)
			msg = msg + messages[k]

		msg = msg + "lequel souhaites tu écouter ?"


	print(msg)
	fichier = open("/home/thib/Documents/Cherry/pyector/src/reponse.txt", "w+")
	fichier.write(msg)
	fichier.close()

	return (url2,j)






