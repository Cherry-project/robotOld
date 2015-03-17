import numpy
import time


import pypot.primitive

class TrackingBehave(pypot.primitive.LoopPrimitive):

    #coord donnees par camera
    coordx=0
    coordy=0
    #angle actuel
    presenty=0
    presentz=0
    #angle but
    goaly=0
    goalz=0
    #camera
    resx=640.0
    resy=480.0
    anglex=160.0
    angley=160.0
    middlex=resx/2
    middley=resy/2
    seuilx=10
    seuily=10
    
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
        #self.robot.normal_behave.start()

    def update(self):
        #traitement necessaire de coordx et coordy?
        goalz=(self.anglex/self.resx)*(self.middlex-self.coordx)+self.robot.head_z.present_position
        goaly=(self.angley/self.resy)*(self.coordy-self.middley)+self.robot.head_y.present_position

        # self.robot.head_z.goto_position(goalz, 3, wait=False)
        # self.robot.head_y.goto_position(goaly, 3, wait=True)
        self.robot.head_z.moving_speed=30
        self.robot.head_y.moving_speed=30
        self.robot.head_z.goal_position=goalz
        self.robot.head_y.goal_position=goaly


        #time.sleep(2)

        #self.presenty = self.robot.head_y.present_position
        #self.presentz = self.robot.head_z.present_position

        # #si le visage est trop a gauche
        # if (self.middlex-self.coordx)>self.seuilx :
        #     #si visage pas trop tourne
        #     if (self.presentz>-70) :
        #         #bouger de 10d gauche
        #         self.robot.head_z.goto_position(self.presentz+10, 1, wait=True)
        # #else si trop a droite
        # elif (self.coordx-self.middlex)>self.seuilx :
        #     #si visage pas trop tourne
        #     if (self.presentz<70) :
        #         #bouger de 10d droite
        #         self.robot.head_z.goto_position(self.presentz-10, 1, wait=True)

        # #si trop haut
        # if (self.middley-self.coordy)>self.seuily :
        #     #si visage pas trop tourne
        #     if (self.presenty>-10) :
        #         #bouger de 10d haut
        #         self.robot.head_y.goto_position(self.presenty-10, 1, wait=True)
        # #else si trop bas
        # elif (self.coordy-self.middley)>self.seuily :
        #     #si visage pas trop tourne
        #     if (self.presenty<20) :
        #         #bouger de 10d bas
        #         self.robot.head_y.goto_position(self.presenty+10, 1, wait=True)
        
