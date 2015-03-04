import numpy
import json
import time

# from pypot.vrep import from_vrep
from init import virtual_robot

#TO DO : Changer en chemin absolu
def init():
    with open('../../utils/poppy_config.json') as f:            
            poppy_config = json.load(f)
    scene_path = '../../utils/poppy-standing2.ttt'
    poppy = from_vrep(poppy_config,'127.0.0.1', 19997, scene_path)
    # poppy.start_sync()
    # for m in poppy.motors:
    #   m.compliant = False
    return poppy

def run(robot):
    center_position = 25
    robot.head_y.goal_position = 90
    t0 = time.time()
    amp = 45
    freq = 0.4
    robot.head_y.goal_position = center_position
    print "0"
    robot.head_z.goal_position = 0
    time.sleep(2)
##    print "90"
##    robot.head_z.goal_position = 90
##    time.sleep(5)
##    print "45"
##    robot.head_z.goal_position = 45
##    time.sleep(5)
##    print "-45"
##    robot.head_z.goal_position = -45
##    time.sleep(5)

    while True:
        t = time.time() - t0
        if t > 6:
            break
        pos = amp * numpy.sin(2 * numpy.pi * freq * t) 
        robot.head_z.goal_position = pos 
        time.sleep(0.02)
    robot.head_z.goal_position = 0
    time.sleep(2)

if __name__ ==  "__main__":
    print "debut du test"
    poppy = virtual_robot("coucou")
    print poppy.test
    poppy.init()
    print poppy.test
    print "fin de l'init"
    run(poppy.poppy)
    print "ok"
