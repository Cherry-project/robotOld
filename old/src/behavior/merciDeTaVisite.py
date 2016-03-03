import time
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


class MerciDeTaVisite(pypot.primitive.Primitive):
    def __init__(self, robot):
            pypot.primitive.Primitive.__init__(self, robot)
            self._robot = robot
        

    def start(self):
            
            pypot.primitive.Primitive.start(self)

    def run(self):
     
                move = '\home\poppy\resources\move\merciDeTaVisite.move'
        
                with open(move) as f:
                    m = Move.load(f)
                    
                self._robot.compliant = False
                
                speak.start("Maintenant il faut laisser la place aux autres, c’était bien sympa, je te remercie pour ta visite ! Je t’invite à remplir ce questionnaire, ça va beaucoup aider mes amis." )
                
                move_player = MovePlayer(self._robot, m)
                move_player.start()