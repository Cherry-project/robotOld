import pypot.primitive
import json
import requests

import pypot.primitive

class Rest(pypot.primitive.Primitive):

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

		for m in self.robot.motors:
			m.compliant = False
			m.goal_position = 0

		for m in self.robot.head:
			m.compliant = True

	# function that is call once the run function has ended
	def teardown(self):
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
