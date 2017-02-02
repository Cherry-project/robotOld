#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import speech_recognition as sr
import sys
import time
import re
from unidecode import unidecode
import pypot.primitive


class Listen(pypot.primitive.Primitive):
    
    properties = pypot.primitive.Primitive.properties + ['listen_state']
    def __init__(self, robot, state = 'normal' ):
        pypot.primitive.Primitive.__init__(self, robot)
        self._state = state
        self._robot = robot
        
          
    def start(self):
        pypot.primitive.Primitive.start(self)
        
    #def run(self):    
        
        poppy = self._robot
        state = self._state
        url_to_robot = 'http://192.168.1.100:8080/'
        
        # Recording
        r = sr.Recognizer()
        with sr.Microphone() as source:

            print("Say something!")
            audio = r.listen(source)

        text = "Je n'ai pas compris. Veuillez répetez"
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            text = r.recognize_google(audio, language='FR-fr')
            print("Google Speech Recognition thinks you said " + text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        print text
        
        if(state == "multi"):
            
            print "Je suis dans: " + state
            # if it's a number
            if re.search('\d+', text):
                multi_str = "http://127.0.0.1:8080/multi/answer?param=" + text
                requests.get(multi_str, timeout = 0.1)
                print "réponse"
                return 0
            
            # if it's not a string
            if (type(text) == str):
                #robot_speak("Ce n'est pas une chaine de caractère")
                #time.sleep(1)
                #requests.get('http://127.0.0.1:8080/robot/listen?state=on')
                requests.get('http://127.0.0.1:8080/http://127.0.0.1:8080/presentation?name=pascompris', timeout = 0.1)
                return 0
            
            if ((unidecode(u"stop") in unidecode(text))):

                print "Stop"
                # Stop
                requests.post('http://127.0.0.2:8888/primitive/listen/property/listen_state/value.json', 
                  data=json.dumps("normal"), 
                  headers={'content-type': 'application/json'})
                
                
                #speak
                requests.post(url_to_robot + 'primitive/speak/property/sentence_to_speak/value.json', data=json.dumps("Entendu, j'arrête de jouer"), headers={'content-type': 'application/json'})
                requests.get(url_to_robot + 'primitive/speak/start.json')
                
                #text_to_say = "Entendu, j'arrête de jouer"
                #poppy.speak.sentence_to_speak = text_to_say
                #poppy.speak.start()  
                
                time.sleep(3)
                
                pres_str = "http://127.0.0.1:8080/robot/wait?state=on"
                requests.get(pres_str, timeout = 0.1)
                
                #requests.get('http://127.0.0.1:8080/wait?state=on', timeout = 0.1)
                return 0
            
            elif ((unidecode(u"sais") in unidecode(text) and unidecode(u"pas") in unidecode(text))):
                
                requests.post(url_to_robot + 'primitive/speak/property/sentence_to_speak/value.json', data=json.dumps("Essaie, je suis sur que tu peux y arriver"), headers={'content-type': 'application/json'})
                requests.get(url_to_robot + 'primitive/speak/start.json')
                #text_to_say = "Essaie! Je suis sur que tu peux y arriver"
                #poppy.speak.sentence_to_speak = text_to_say
                #poppy.speak.start()
                
                pres_str = "http://127.0.0.1:8080/robot/wait?state=on"
                requests.get(pres_str, timeout = 0.1)
                
                #requests.get('http://127.0.0.1:8080/wait?state=on', timeout = 0.1)
                return 0
                
            else:
                #text_to_say = "Je n'ai pas compris"
                #poppy.speak.sentence_to_speak = text_to_say
                #poppy.speak.start()
                requests.get('http://127.0.0.1:8080/presentation?name=pascompris', timeout = 0.1)
                
                
                print "Pas compris"
                return 0
            
        elif ( state == "presentation"):
           
            print "Je suis dans: " + state
            
            # if it's not a string
            if (type(text) == str):
                requests.get('http://127.0.0.1:8080/robot/listen?state=on', timeout = 0.1)
                #robot_speak("Ce n'est pas une chaine de caractère")
                #time.sleep(1)
                #requests.get('http://127.0.0.1:8080/robot/listen?state=on')
                #text_to_say = "Je n'ai pas compris"
                #poppy.speak.sentence_to_speak = text_to_say
                #poppy.speak.start()
                
                return 0
            
            if ((unidecode(u"stop") in unidecode(text))):

                print "Stop"
                #text_to_say = "Entendu, j'arrête de présenter"
                #poppy.speak.sentence_to_speak = text_to_say
                #poppy.speak.start()
                self._state = "normal"
                pres_str = "http://127.0.0.1:8080/stop?presentation=off"
                #requests.get(pres_str)
                #print "Présentation arreté"
                
                time.sleep(5)
                requests.get('http://127.0.0.1:8080/robot/wait_behave?state=on', timeout = 0.1)
                return 0
                #requests.get('http://127.0.0.1:8080/wait?state=on', timeout = 0.1)
                
            else:
                requests.get('http://127.0.0.1:8080/robot/listen?state=on', timeout = 0.1)
                #text_to_say = "Je n'ai pas compris"
                #poppy.speak.sentence_to_speak = text_to_say
                #poppy.speak.start()
                
            
        

        elif ( state == "normal"):
            
            print "Je suis dans: " + state    
            # if it's not a string
            if (type(text) == str):
                #robot_speak("Ce n'est pas une chaine de caractère")
                time.sleep(1)
                #requests.get('http://127.0.0.1:8080/robot/wait?state=on')
                requests.get('http://127.0.0.1:8080/robot/wait_behave?state=on', timeout = 0.1)
                return 0


            if "Bonjour" in unidecode(text):
                # say bonjour
                #text_to_say = "Bonjour"
                #poppy.speak.sentence_to_speak = text_to_say
                #poppy.speak.start()
                pres_str = "http://127.0.0.1:8080/presentation?name=bonjour"
                requests.get(pres_str, timeout = 0.1)
                # Back to wait state
                #requests.get('http://127.0.0.1:8080/robot/wait?state=on', timeout = 0.1)
                print "Bonjour"
                return 0

            elif ((unidecode(u"revoir") in unidecode(text) or unidecode(u"présentation") in unidecode(text)) or ( unidecode(u"aurevoir") in unidecode(text))):
                print "Au revoir"
                pres_str = "http://127.0.0.1:8080/presentation?name=aurevoir"
                requests.get(pres_str, timeout = 0.1)
                return 0
       

            elif ((unidecode(u"présente") in unidecode(text) or unidecode(u"présentation") in unidecode(text)) and ( unidecode(u"Sogeti") in unidecode(text))):

                print "lancement de la présentation"

                pres_str = "http://127.0.0.1:8080/pesentation?name=sogeti"
                requests.get(pres_str, timeout = 0.1)
                return 0


            elif ((unidecode(u"présente") in unidecode(text) or unidecode(u"présentation") in unidecode(text)) and ( unidecode(u"prima") in unidecode(text))):

                print "lancement de la présentation"

                pres_str = "http://127.0.0.1:8080/presentation?name=prima"
                requests.get(pres_str, timeout = 0.1)
                return 0


            elif ((unidecode(u"présente") in unidecode(text))) and ( unidecode(u"projet") in unidecode(text)):

                print "lancement de la présentation"

                pres_str = "http://127.0.0.1:8080/presentation?name=cherry"
                requests.get(pres_str, timeout = 0.1)
                return 0


            elif (unidecode(u"jouer") in unidecode(text)and unidecode(u"multiplication") in unidecode(text)):
                print "Multi"
                requests.get('http://127.0.0.1:8080/multi/set?param', timeout = 0.1)
                return 0
                

            else:
                print "Pas compris"
                requests.get('http://127.0.0.1:8080/presentation?name=pascompris', timeout = 0.1)
                #requests.get('http://127.0.0.1:8080/robot/listen?state=on', timeout = 0.1)
                return 0
        
        elif(state == 'stop'):
            #requests.post(url_to_robot + 'primitive/speak/property/sentence_to_speak/value.json', data=json.dumps("Je passe en manuel"), headers={'content-type': 'application/json'})
            #requests.get(url_to_robot + 'primitive/speak/start.json')
            return 0
                
        else:
            requests.get('http://127.0.0.1:8080/presentation?name=pascompris', timeout = 0.1)
            print "Unknown state"
            return 0
            
    @property
    def listen_state(self):
        return self._state

    @listen_state.setter
    def listen_state(self, state):
        print "Set parameter to: " + state
        self._state= state

