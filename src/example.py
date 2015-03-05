from poppy.creatures import PoppyHumanoid
from cherry import Cherry

cherry = Cherry()
cherry.setup()

cherry.robot.wave_behave.start()
cherry.robot.wave_behave.wait_to_stop()