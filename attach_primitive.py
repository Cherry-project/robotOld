import os
import glob

# Perpetual Movement
from primitives.idle import UpperBodyIdleMotion, HeadIdleMotion, TorsoIdleMotion

# Play Movement
from primitives.movePlayer import PlayMove

from primitives.rest import Rest
from primitives.off  import Off

# Attach all primitive to the robot.
def attach_primitives(robot, isCamera=True):

    # loop to attach all .move config file 
    os.chdir('./moves')
    for file in glob.glob("*.move"):
        print(file)
        move_name = os.path.splitext(file)[0]
        robot.attach_primitive(PlayMove(robot,movement=move_name),move_name)

    os.chdir('../')

    # Attach Perpetual Movement
    robot.attach_primitive(UpperBodyIdleMotion(robot, 50), 'upper_body_idle_motion')
    robot.attach_primitive(HeadIdleMotion(robot, 50), 'head_idle_motion')
    robot.attach_primitive(TorsoIdleMotion(robot, 50), 'torso_idle_motion')

    robot.attach_primitive(Rest(robot), 'rest')
    robot.attach_primitive(Off(robot), 'off')






