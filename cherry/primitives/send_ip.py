#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pypot.robot
import requests
import json


class SendIp(pypot.primitive.Primitive):
        
        
    def start(self, name):
        ip = "192.168.1.250"

        print "on lance la requète :)"
        print "http://"+ip+":8080/setup?id="+name
        
        try: 
            requests.get("http://"+ip+":8080/setup?id="+name)
        except:
            print "requète échoué"
