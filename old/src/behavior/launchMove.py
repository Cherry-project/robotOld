import time
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


class LaunchMove(pypot.primitive.Primitive):
    def __init__(self, robot):
            pypot.primitive.Primitive.__init__(self, robot)
            self._robot = robot
        

    def start(self, move):
            self._move  = move
            pypot.primitive.Primitive.start(self)


    def run(self):
        
            with open(self._move) as f:
                m = Move.load(f)
                self._robot.compliant = False

            move_player = MovePlayer(self._robot, m)
            move_player.start()

