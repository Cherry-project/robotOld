import numpy
import time


import pypot.primitive

class TrackingBehave(pypot.primitive.LoopPrimitive):

    #coord donnees par camera
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
    middlex=resx/2
    middley=resy/2

    counter=0
    
    
    def __init__(self, robot, camera, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot,freq)
        self.camera = camera

        print "init ok"       


    def setup(self):
        robot = self.robot

        self.robot.head_y.compliant = False
        self.robot.head_z.compliant = False 

    def teardown(self):
        robot = self.robot
        #self.robot.normal_behave.start()

    def update(self):

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


        
