import time
from poppy.creatures import PoppyHumanoid
from cherry import Cherry

cherry = Cherry()
cherry.setup()

cherry.robot.right_hand_mouv_behave.start()

time.sleep(15)
