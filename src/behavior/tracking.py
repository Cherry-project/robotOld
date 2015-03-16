import numpy
import time


import pypot.primitive

class TrackingBehave(pypot.primitive.LoopPrimitive):

    
    def __init__(self, robot):
        pypot.primitive.LoopPrimitive.__init__(self, robot)
        self.coordx
        self.coordy
        self.presenty
        self.presentz
        #Résolution caméra
        self.resx = 640
        self.resy = 480
        self.middlex = resx/2
        self.middley = resy/2
        #bande acceptable ~10% ?
        self.seuilx=30
        self.seuily=25


    def setup(self):
        robot = self.robot

        self.robot.head_y.compliant = False
        self.robot.head_z.compliant = False 

    def teardown(self):
        robot = self.robot
        self.robot.normal_behave.start()

    def update(self):
        #traitement nécessaire de coordx et coordy?

        self.presenty = self.robot.head_y.present_position
        self.presentz = self.robot.head_z.present_position

        #si le visage est trop à gauche
        if (self.middlex-self.coordx)>self.seuilx
            #si visage pas trop tourné
            if (self.presentz>-90)
                #bouger de 10° gauche
                self.robot.head_z.goto_position(self.presentz-10, 1, wait=False)
        #else si trop à droite
        else if (self.coordx-self.middlex)>self.seuilx
            #si visage pas trop tourné
            if (self.presentz<90)
                #bouger de 10° droite
                self.robot.head_z.goto_position(self.presentz+10, 1, wait=False)

        #si trop haut
        if (self.middley-self.coordy)>self.seuily
            #si visage pas trop tourné
            if (self.presenty>-35)
                #bouger de 10° haut
                self.robot.head_y.goto_position(self.presenty-10, 1, wait=False)
        #else si trop à droite
        else if (self.coordy-self.middley)>self.seuily
            #si visage pas trop tourné
            if (self.presenty<5)
                #bouger de 10° bas
                self.robot.head_y.goto_position(self.presenty+10, 1, wait=False)
        
