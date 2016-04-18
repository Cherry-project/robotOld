#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import time
import pypot.robot
from pypot.dynamixel import DxlIO

# You'll need to change this to the serial port of your USB2Dynamixel
serial_port = '/dev/ttyACM0'

# You'll need to change this to the ID of your servo 
servo_id = (51, 41, 33)

# Turn the LED on

class Diode(pypot.primitive.LoopPrimitive):

    def setup(self):
        dxl = DxlIO('/dev/ttyACM0')
        
        for id in servo_id:
            dxl.switch_led_on({id})

    def teardown(self):

        dxl = DxlIO('/dev/ttyACM0')

        for id in servo_id:
            dxl.switch_led_off({id})
