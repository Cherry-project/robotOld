#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *
import json
import time
import numpy
import time
import pypot.primitive 
from pypot.vrep import from_vrep
from poppytools.primitive.basic import StandPosition
import pypot.robot

def sinus(ampl,t,freq=0.5, phase=0, offset=0):
    pi = numpy.pi
    return ampl * numpy.sin(freq * 2.0 * pi * t + phase * pi / 180.0 ) + offset

class SimpleBodyBeats(pypot.primitive.LoopPrimitive):
    '''
    Simple primitive to make Poppy shake its booty following a given beat rate in bpm.

    '''
    def __init__(self, poppy_robot, bpm, motion_amplitude=10):
        pypot.primitive.LoopPrimitive.__init__(self, poppy_robot, 50)

        self.poppy_robot = poppy_robot
        self._bpm = bpm
        self.amplitude = motion_amplitude
        self.frequency = bpm / 60.0
        self.pi = numpy.pi


        for m in self.poppy_robot.motors:
            m.moving_speed = 50.0


    def update(self):
        t = self.elapsed_time
        amp = self._amplitude
        freq = self.frequency

        self.poppy_robot.head_y.goal_position = sinus(amp / 2.0, t, freq)
        self.poppy_robot.head_z.goal_position = sinus(amp / 2.0, t, freq / 2.0)

        self.poppy_robot.bust_x.goal_position = sinus(amp / 6.0, t, freq / 2.0) + sinus(amp / 6.0, t, freq / 4.0)
        self.poppy_robot.abs_x.goal_position = - sinus(amp / 8.0, t, freq / 4.0) + sinus(amp / 6.0, t, freq / 4.0)

        self.poppy_robot.l_shoulder_y.goal_position = sinus(amp / 3.0, t, freq / 2.0)
        self.poppy_robot.r_shoulder_y.goal_position = - sinus(amp / 3.0, t, freq / 2.0)

        self.poppy_robot.r_elbow_y.goal_position = sinus(amp / 2.0, t, freq, offset=-20)
        self.poppy_robot.l_elbow_y.goal_position = sinus(amp / 2.0, t, freq / 2.0, offset=-20)


    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self, new_bpm):
        '''
        Permits to change the beat rate while the motion is performing
        '''
        self._bpm = new_bpm
        self.frequency = self._bpm / 60.0

    @property
    def amplitude(self):
        return self._amplitude

    @amplitude.setter
    def amplitude(self, new_amp):
        self._amplitude = new_amp



#############
# 	GIVEN	#
#############
@given(u'Poppy s\'initialise')
def step_impl(context):
    context.poppy.start_sync()


#############
#	THEN	#
#############

@then(u'Attente de {value}s')
def step_impl(context, value):
    time.sleep(int(float((value))))

#Not working
@then(u'Poppy se relache')
def step_impl(context):
	context.poppy.goto_position({'r_hip_z': -2,
					'l_hip_z': 2,
					'r_hip_x': -2,
					'l_hip_x': 2,
					'l_shoulder_x': 10,
					'r_shoulder_x': -10,
					'l_shoulder_y': 10,
					'r_shoulder_y': 10,
					'l_elbow_y': -20,
					'r_elbow_y': -20,
					'l_ankle_y': -4,
					'r_ankle_y': -4,
					'abs_y': -4,
					'head_y': 0,
					'head_z':0},
					3,
					wait=True)


##############
#    WHEN    #
##############

@when(u'Poppy tourne la tête à gauche de "{value}"')
def step_impl(context, value):
    context.poppy.head_z.goal_position = int(value)

@when(u'Poppy tourne la tête à droite de "{value}"')
def step_impl(context, value):
    context.poppy.head_z.goal_position = -int(value)

@when(u'Poppy bouge son épaule gauche de "{value}"')
def step_impl(context, value):
	context.poppy.l_shoulder_x.goal_position = int(value)

@when(u'Poppy fait bonjour')
def step_impl(context):
	center_position = -90
	context.poppy.l_arm_z.goal_position = 90
	t0 = time.time()
	amp = 30
	freq = 0.5
	context.poppy.l_shoulder_x.goal_position = 180
	context.poppy.l_elbow_y.goal_position = center_position
	time.sleep(1)

	while True:
	    t = time.time() - t0

	    if t > 10:
	        break
	    pos = amp * numpy.sin(2 * numpy.pi * freq * t) + center_position
	    context.poppy.l_elbow_y.goal_position = pos 
	    time.sleep(0.02)

@when(u'Poppy fait non')
def step_impl(context):
	center_position = 0
	context.poppy.head_z.goal_position = 90
	t0 = time.time()
	amp = 40
	freq = 0.7
	context.poppy.head_z.goal_position = center_position
	time.sleep(1)

	while True:
	    t = time.time() - t0

	    if t > 7:
	        break
	    pos = amp * numpy.sin(2 * numpy.pi * freq * t) + center_position
	    context.poppy.head_z.goal_position = pos 
	    time.sleep(0.02)
	context.poppy.head_z.goal_position = center_position

@when(u'Poppy fait oui')
def step_impl(context):
	center_position = 25
	context.poppy.head_y.goal_position = 90
	t0 = time.time()
	amp = 40
	freq = 0.7
	context.poppy.head_y.goal_position = center_position
	time.sleep(1)

	while True:
	    t = time.time() - t0
	    if t > 7:
	        break
	    pos = amp * numpy.sin(2 * numpy.pi * freq * t) + center_position
	    context.poppy.head_y.goal_position = pos 
	    time.sleep(0.02)
	context.poppy.head_y.goal_position = center_position

@when(u'Poppy danse')
def step_impl(context):
	# context.poppy.attach_primitive(StandPosition(context.poppy),'stand')
	# context.poppy.stand.start()
	# context.poppy.stand.wait_to_stop()	
 #    Create dancing primitive
	bpm = 100
	context.poppy.attach_primitive(SimpleBodyBeats(context.poppy, bpm), 'beats' )
	context.poppy.beats.start()
	while True:
		try:
			time.sleep(1)

		except KeyboardInterrupt:
			context.poppy.beats.stop()
			context.poppy.stand.start()
			context.poppy.stand.wait_to_stop()
			break


@when(u'test')
def test(context):
    context.poppy.l_shoulder_x.goal_position = 180




