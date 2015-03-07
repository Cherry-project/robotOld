import time
from poppy.creatures import PoppyHumanoid
from cherry import Cherry

cherry = Cherry()
cherry.setup()

cherry.robot.show_right_behave.start()

time.sleep(15)
