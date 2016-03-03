#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from pypot.vrep import from_vrep


class virtual_robot:
    """A class to initialize and make primitive on the virtual robot"""
    def __init__(self, test):
        self.test = test
        
        
    def init(self):
        with open('../../utils/poppy_config.json') as f:            
                poppy_config = json.load(f)
        scene_path = '../../utils/poppy-standing2.ttt'
        self.poppy = from_vrep(poppy_config,'127.0.0.1', 19997, scene_path)
        # poppy.start_sync()
        # for m in poppy.motors:
        #   m.compliant = False
        