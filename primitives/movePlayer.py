import time
import requests
import json

import pypot.primitive
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


class PlayMove(pypot.primitive.Primitive):

	# Add an argument to the first init call
	def __init__(self, robot, movement=None):
		# save the argument
		self.move  = movement
		self.robot = robot

		# call agin the init function but in a way the primitive
		pypot.primitive.Primitive.__init__(self,robot)

	# main function that is call when the start method is launch
	def run(self):
		try:
			self.robot.upper_body_idle_motion.stop()
			self.robot.torso_idle_motion.stop()
			# self.robot.head_idle_motion.stop()
		except:
			pass
		else:
			pass
		finally:
			pass

		# initialize the time variable
		t =time.time()

		# find the right move 
		with open("./moves/"+self.move+".move") as f:
			m = Move.load(f) # chargement du .move

		# start the move
		movey = MovePlayer(self.robot, m)
		movey.start()

		#time to start the move
		el = time.time() - t

		# taking into account the movement time in itself (pos_number * framerate)
		md = movey.duration()-0.3
		time.sleep(md) # sleeping the wanted duration
		# print 'Primitive ', self.move, ' finished in ', el+md, 'secondes.' 


	# function that is call once the run function has ended
	def teardown(self):
		try:
			self.robot.upper_body_idle_motion.start()
			self.robot.torso_idle_motion.start()
			# self.robot.head_idle_motion.start()
		except:
			pass
		else:
			pass
		finally:
			pass

		# load the configuration file that give the server addr and port for requests 
		json_data = open('./config/conf.json')
		data = json.load(json_data)
		json_data.close()

		# we need the server addr+port and the robot name so the server know which robot has ended his move
		ip = data['server']['addr']
		port = data['server']['port']
		name = data['robot']['name']

		# create the url for the request
		url = "http://"+str(ip)+":"+str(port)+"/robot/behavefinished/"

		# send the post with the robot name request to the server
		try: 
			requests.post(url, data = {'id':str(name)})
		except:
			# print "Request error"
			pass
		else:
			# print "Request sent !"
			pass
		finally:
			pass






