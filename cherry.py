import numpy
import os
import glob
import threading
import time
import requests
import json

from pypot.server.httpserver import HTTPRobotServer

from pypot.server.zmqserver import ZMQRobotServer

from pypot.creatures import AbstractPoppyCreature

from attach_primitive import attach_primitives

from pypot.robot import from_json

from pypot.primitive.move import MoveRecorder

from primitives.movePlayer import PlayMove

from speak import *

from voice import Voice


class Cherry(AbstractPoppyCreature):
         
    @classmethod
    def setup(cls):

        print "Robot setup started :"

        json_data = open('./config/conf.json')
        data = json.load(json_data)
        json_data.close()

        port = data['robot']['port']
        name = data['robot']['name']

        try:
            cls.robot = from_json('config/torso.json')
        except Exception as e:
            try:
                cls.robot = from_json('config/torso.json')
            except Exception as e:
                raise
            else:
                print "Robot configuration successful !"
            finally:
                pass
            raise
        else:
            print "Robot configuration successful !"

        # Attach Gtts
        try:
            cls.robot.attach_primitive(SayFR(cls.robot), 'say_fr')
            cls.robot.attach_primitive(SayEN(cls.robot), 'say_en')
            cls.robot.attach_primitive(SayES(cls.robot), 'say_es')
            cls.robot.attach_primitive(SayDE(cls.robot), 'say_de')

        except Exception as e:
            print "Something goes wrong with gTTS"
            raise
        else:
            print "gTTS attached successfully"

        print "Starting motors configuration"

        for m in cls.robot.motors:
            m.compliant_behavior = 'dummy'
            m.goto_behavior = 'minjerk'
            m.moving_speed = 80
        
        for m in cls.robot.motors:
            m.compliant = False
            m.goal_position = 0
            print m

        for m in cls.robot.head:
            m.compliant = True
        try:
            attach_primitives(cls.robot)
        except:
            print "Primitives not attached "
        else:
            print "Primitives attached successfully"       
        
        try:
            cls.robot.torso_idle_motion.start()
            cls.robot.upper_body_idle_motion.start()
            # cls.robot.head_idle_motion.start()
        except Exception as e:
            raise
        else:
            pass

        # Voice.silent(text="Setup done",lang='en')
        try:
            Voice.silent(text="Bonjour, je m'appelle "+name+", ravi de vous rencontrer.",lang='fr')
        except:
            print "WARNING : no response from google tts engine : Check internet connectivity"
        else:
            pass

        return cls.robot

    @classmethod
    def serve(cls):
        json_data = open('./config/conf.json')
        data = json.load(json_data)
        json_data.close()
        
        ip = data['robot']['addr']
        port = data['robot']['port']
        
        try:
            server = HTTPRobotServer(cls.robot, host=str(ip), port=str(port))
        except:
            print "Unable to create server object"
        else:
            print "Server configuration done"
            try:
                threading.Thread(target=lambda: server.run()).start()
            except:
                print "Unable to start server"
            else:
                print "server started successfully"
                # Voice.silent(text="Server working",lang='en')

    @classmethod
    def connect(cls):
        json_data = open('./config/conf.json')
        data = json.load(json_data)
        json_data.close()

        ip = data['server']['addr']
        port = data['server']['port']
        name = data['robot']['name']

        print "Starting to ping the server"

        response = os.system("ping -c 1 " + str(ip))
        if response != 0:
            while response != 0:
                response = os.system("ping -c 1 " + str(ip))
                time.sleep(5)

        url = "http://"+str(ip)+":"+str(port)+"/setup?id="+str(name)
        print url
        try: 
            requests.get(url)
        except:
            print "Request error"
        else:
            # Voice.silent(text="Connexion request sent",lang='en')
            pass

    
    @classmethod
    def learn(cls):
        move = MoveRecorder(cls.robot,100,cls.robot.motors)
        cls.robot.compliant = True
        raw_input("Press enter to start recording a Move.")
        
        for x in xrange(3,0,-1):
            print x
            time.sleep(1)

        move.start()
        raw_input("Press again to stop the recording.")
        move.stop()

        for m in cls.robot.motors:
            m.compliant = False
            m.goal_position = 0

        print "List of already taken primitives : "

        os.chdir('./moves')
        for file in glob.glob("*.move"):
            print(os.path.splitext(file)[0])
        os.chdir('../')

        move_name = raw_input("Enter the name of this sick move : ")
        move_name = move_name+".move"

        with open("./moves/"+move_name, 'w') as f:
            try:
                move.move.save(f)
            except:
                print "Unable to save this move, sorry"
            else:
                print "Move successfully saved !"
        try:
            cls.robot.attach_primitive(PlayMove(cls.robot,movement=move_name),move_name)
        except Exception as e:
            raise
        else:
            print "Move successfully attached to the robot !"
        finally:
            pass
            
    @classmethod
    def forget(cls,move_name):
        raw_input("Are you sure ? Press enter to delete this move")
        try:
            os.remove("./moves/"+move_name+".move")
        except Exception as e:
            raise
        else:
            print move_name+" successfully forgotten !"
        finally:
            pass

    @classmethod
    def exit(cls):
        print "Exiting Cherry server process"
        Voice.silent(text="Au revoir !",lang='fr')
        os.system("sudo kill `sudo lsof -t -i:8000`")




