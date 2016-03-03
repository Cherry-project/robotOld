import numpy
import os

from functools import partial

from poppy.creatures import AbstractPoppyCreature

from .attach_primitive import attach_primitives



class Cherry(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        robot._primitive_manager._filter = partial(numpy.sum, axis=0)

        if False:
            cls.vrep_hack(robot)
        for m in robot.motors:
            m.compliant_behavior = 'dummy'
            m.goto_behavior = 'minjerk'
            m.moving_speed = 70
        

        attach_primitives(robot)
