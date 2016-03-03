import time
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


class ExplicationsPlus(pypot.primitive.Primitive):
    def __init__(self, robot):
            pypot.primitive.Primitive.__init__(self, robot)
            self._robot = robot
        

    def start(self):
            
            pypot.primitive.Primitive.start(self)

    def run(self):
     
                move = '\home\poppy\resources\move\explicationsPlus.move'
        
                with open(move) as f:
                    m = Move.load(f)
                    
                self._robot.compliant = False
                
                speak.start("Je serais là pour jouer avec les enfants, et pour les accompagner quand ils sont dans la chambre! Grace à moi ils pourront garder contact avec leur famille et leur amis!" )
                
                move_player = MovePlayer(self._robot, m)
                move_player.start()
