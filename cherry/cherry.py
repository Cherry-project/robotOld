import numpy
import os

from functools import partial

from poppy.creatures import AbstractPoppyCreature

from attach_primitive import attach_primitives



class Cherry(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        robot._primitive_manager._filter = partial(numpy.sum, axis=0)
        
        
        #cls._name = "cherry" # Doesn't work, i have to find why
        name = "cherry"

        if False:
            cls.vrep_hack(robot)
        for m in robot.motors:
            m.compliant_behavior = 'dummy'
            m.goto_behavior = 'minjerk'
            m.moving_speed = 70
        

        for m in robot.motors:
            m.compliant = False
            m.goal_position = 0

        for m in robot.head:
            m.compliant = True

        try:
			attach_primitives(robot)
        except:
		    print "Cannot add primitives"
		
        try:
		    robot.test_gtts.start()
        except:
		    print "Something goes wrong with gTTS"
		
        try:
		    robot.send_ip.start(name)
        except:
		    print "Unable to send ip to the server"
