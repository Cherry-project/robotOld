#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pypot.robot
import requests
import json


class SendIp(pypot.primitive.Primitive):
        
        
    properties = pypot.primitive.Primitive.properties + ['ip_controller']

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        with open("/home/poppy/resources/ip.txt", "U") as ip_file:
            self._ip = ip_file.readline().replace('\n', '')

        print self._ip


    def start(self, name):
        ip = self._ip

        print "on lance la requète :)"
        print "http://"+ip+"/setup?id="+name
        
        try: 
            requests.get("http://"+ip+"/setup?id="+name)
        except:
            print "requète échoué"


    @property
    def ip_controller(self):
        return self._ip


    @ip_controller.setter
    def ip_controller(self, dict_ip):
        print dict_ip

        self._ip = dict_ip.get("ip_controller")
        print self._ip
        #mettre l'ip dans le fichier
        with open("/home/poppy/resources/ip.txt", "w") as ip_file:
            ip_file.write(self._ip)
