#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from poppy.creatures import PoppyHumanoid
from cherry import Cherry

cherry = Cherry()
cherry.setup()

cherry.robot.bow_behave.start()

time.sleep(15)
