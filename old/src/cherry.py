#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from pypot.vrep import from_vrep
from pypot.robot import from_json
from poppy.creatures import PoppyHumanoid

from attach_primitive import attach_primitives

#from vision.camera import Camera
#from vision.runLook import RunLook


class Cherry():
    # TODO : Voir avec pierre si Cherry() puis self.robot ou Cherry(PoppyTorso)

    def __init__(self, simulator=None, camera=False):
        """Constructeur de la classe Cherry

        Param :
        simulator -- Mettre simulator='vrep' si vous voulez utiliser Vrep (None par défault)
        camera -- Utilisation de la camera ou non (True par défault)
        
        """

        if simulator is not None:

            self.robot = PoppyHumanoid(simulator='vrep')
            self.isCamera = False

        
        else:
            # TODO : Changer avec robot = PoppyTorso()
            self.robot = from_json("../resource/mandatory/poppy_torso_config.json")
            self.robot.start_sync()

            for m in self.robot.motors:
                m.moving_speed = 60

            for m in self.robot.torso:
                m.compliant = False
            
            if camera:
                imagePath = "../utils/img/"
                cascadePath = "../utils/haarcascade_frontalface_default.xml"
                self.camera = Camera( self.robot, imagePath, cascadePath)
                self.isCamera = True
            else:
                self.isCamera = False




    def setup(self):
        """ Initialisation de Cherry.

        Attachements des primitives, initialisation de la camera si besoin
        """
        robot = self.robot

        for m in robot.motors:
            m.compliant_behavior = 'safe'
            m.goto_behavior = 'minjerk'

        attach_primitives(self, self.isCamera)

