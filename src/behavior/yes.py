import numpy
import json
import time

from pypot.vrep import from_vrep


#TO DO : Changer en chemin absolu
def init():
	with open('../../utils/poppy_config.json') as f:			
		poppy_config = json.load(f)
	scene_path = '../../utils/poppy-standing2.ttt'
	poppy = from_vrep(poppy_config,'127.0.0.1', 19997, scene_path)
	# poppy.start_sync()
	# for m in poppy.motors:
	# 	m.compliant = False
	return poppy

def run(robot):
	center_position = 25
	robot.head_y.goal_position = 90
	t0 = time.time()
	amp = 40
	freq = 0.7
	robot.head_y.goal_position = center_position
	time.sleep(1)

	while True:
		t = time.time() - t0
		if t > 7:
			break
		pos = amp * numpy.sin(2 * numpy.pi * freq * t) + center_position
		robot.head_y.goal_position = pos 
		time.sleep(0.02)
	robot.head_y.goal_position = center_position

if __name__ ==  "__main__":
	print "debut du test"
	poppy = init()
	print "fin de l'init"
	run(poppy)
	print "ok"