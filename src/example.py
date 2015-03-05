from poppy.creatures import PoppyHumanoid
from cherry import Cherry

cherry = Cherry()
cherry.setup()

cherry.robot.yes_behave.start()
cherry.robot.yes_behave.wait_to_stop()