import os
import poppytools
import json
import time 

from pypot.vrep import from_vrep
from poppytools.primitive.walking import WalkingGaitFromMat


with open("/Users/wyoc/Projects/Poppy/tests/poppy_config.json") as f:
    poppy_config = json.load(f)


scene_path = '/Users/wyoc/Projects/Poppy/tests/poppy-standing2.ttt'
poppy = from_vrep(poppy_config, '127.0.0.1', 19997, scene_path)


cpg_filename = os.path.join(os.path.dirname(poppytools.__file__), 'behavior', 'IROS_Normal_Gait.mat')
walk = WalkingGaitFromMat(poppy, cpg_filename)

walk.start()

# To give enough "time" to really start the walk
# And prevent the script to stop too soon. 
time.sleep(5)

