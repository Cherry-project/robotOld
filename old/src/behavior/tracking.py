#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import time


import pypot.primitive

class TrackingBehave(pypot.primitive.LoopPrimitive):

    #coord donnees par camera
    
    
    
    def __init__(self, robot, camera, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot,freq)

        coordx=0
        coordy=0
        #angle but
        goaly=0
        goalz=0
        #camera
        resx=640.0
        resy=480.0
        anglex=160.0
        angley=160.0
        self.middlex=resx/2
        self.middley=resy/2

        self.focale = 424.0
        self.gain = 0.4

        mesz = 0
        mesy = 0

        self.position_z = 0
        self.position_y = 30

        counter=0

        self._camera = camera
        self._robot = robot
        print "init ok"       


    def setup(self):

        self._robot.head_y.compliant = False
        self._robot.head_z.compliant = False

        self._robot.head_z.moving_speed=60
        self._robot.head_y.moving_speed=30

    def teardown(self):
        robot = self.robot
        #self.robot.normal_behave.start()

    def update(self):

        if (self._camera.isSomebody==True) :

            mesz = np.arctan(((self.middlex) - self._camera.xPosition)/self.focale)
            mesz = mesz * 180/np.pi


            mesy = np.arctan(((self.middley) - self._camera.yPosition)/self.focale)
            mesy = mesy * 180/np.pi


            self.position_z = self.robot.head_z.present_position
            self.position_y = self.robot.head_y.present_position

            goalz = self.position_z + mesz*self.gain
            goaly = self.position_y - mesy*self.gain

            tol = 1.0

            if((self.position_z + tol) >= goalz >= (self.position_z - tol)):
                self.robot.head_z.goal_position=self.position_z

            else :
                self.robot.head_z.goal_position=goalz

            if((self.position_y + tol) >= goaly >= (self.position_y - tol)):
                self.robot.head_y.goal_position=self.position_y

            else :
                self.robot.head_y.goal_position=goaly


        else :
            self.robot.head_z.goal_position=self.position_z
            self.robot.head_y.goal_position=self.position_y
        """ Ancien code
        camera = self.camera

        if (camera.isSomebody==True) :

            self.counter=0
            #traitement necessaire de coordx et coordy?
            goalz=(self.anglex/self.resx)*(self.middlex-camera.xPosition)+self.robot.head_z.present_position
            goaly=(self.angley/self.resy)*(camera.yPosition-self.middley)+self.robot.head_y.present_position

            # self.robot.head_z.goto_position(goalz, 3, wait=False)
            # self.robot.head_y.goto_position(goaly, 3, wait=True)
            self.robot.head_z.moving_speed=30
            self.robot.head_y.moving_speed=30
            self.robot.head_z.goal_position=goalz
            self.robot.head_y.goal_position=goaly
            time.sleep(0.5)
        else :
            self.counter+=1
            if (self.counter>6) :
                self.robot.head_z.moving_speed=30
                self.robot.head_y.moving_speed=30
                self.robot.head_z.goal_position=0
                self.robot.head_y.goal_position=0
        """
        