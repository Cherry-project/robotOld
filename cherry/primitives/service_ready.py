#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pypot.robot
import requests
import json

class ServiceReady(pypot.primitive.LoopPrimitive):
    
    def setup(self):
        ip = "192.168.1.102"
        self._req = "http://"+ip+"/hello?state=on"

    def update(self):
        
        r = request.get("127.0.0.1:8080/primitive/rest_open_behave/list.json") 
        if r.status_code == 200:
            request.get(self._req)
            self.stop()
        else:
            pass
