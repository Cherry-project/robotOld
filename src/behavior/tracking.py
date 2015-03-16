import numpy
import time


import pypot.primitive

class TrackingBehave(pypot.primitive.LoopPrimitive):

    coordx=0
    coordy=0
    presenty=0
    presentz=0
    resx=640
    resy=480
    middlex=resx/2
    middley=resy/2
    seuilx=30
    seuily=25
    
    def __init__(self, robot, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot,freq)       
        # #Resolution camera
        # self.resx = 640
        # self.resy = 480
        # self.middlex = resx/2
        # self.middley = resy/2
        # #bande acceptable ~10% ?
        # self.seuilx=30
        # self.seuily=25


    def setup(self):
        robot = self.robot

        self.robot.head_y.compliant = False
        self.robot.head_z.compliant = False 

    def teardown(self):
        robot = self.robot
        self.robot.normal_behave.start()

    def update(self):
        #traitement necessaire de coordx et coordy?

        self.presenty = self.robot.head_y.present_position
        self.presentz = self.robot.head_z.present_position

        #si le visage est trop a gauche
        if (self.middlex-self.coordx)>self.seuilx :
            #si visage pas trop tourne
            if (self.presentz>-90) :
                #bouger de 10d gauche
                self.robot.head_z.goto_position(self.presentz+10, 1, wait=False)
        #else si trop a droite
        elif (self.coordx-self.middlex)>self.seuilx :
            #si visage pas trop tourne
            if (self.presentz<90) :
                #bouger de 10d droite
                self.robot.head_z.goto_position(self.presentz-10, 1, wait=False)

        #si trop haut
        if (self.middley-self.coordy)>self.seuily :
            #si visage pas trop tourne
            if (self.presenty>-35) :
                #bouger de 10d haut
                self.robot.head_y.goto_position(self.presenty-10, 1, wait=False)
        #else si trop bas
        elif (self.coordy-self.middley)>self.seuily :
            #si visage pas trop tourne
            if (self.presenty<5) :
                #bouger de 10d bas
                self.robot.head_y.goto_position(self.presenty+10, 1, wait=False)
        
