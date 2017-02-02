import sys
from cherry import Cherry
import time

poppy = Cherry()

poppy.speak.sentence_to_say = sys.argv[1]
poppy.speak.start()

time.sleep(4)
