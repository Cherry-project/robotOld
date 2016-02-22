import time
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


class QuiJeSuis(pypot.primitive.Primitive):
    def __init__(self, robot):
            pypot.primitive.Primitive.__init__(self, robot)
            self._robot = robot
        

    def start(self):
            
            pypot.primitive.Primitive.start(self)

    def run(self):
     
                move = '\home\poppy\resources\move\quiJeSuis.move'
        
                with open(move) as f:
                    m = Move.load(f)
                    
                self._robot.compliant = False
                
                speak.start("Sais-tu qui je suis ?" )
                
                move_player = MovePlayer(self._robot, m)
                move_player.start()
