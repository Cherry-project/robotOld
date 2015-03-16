import time

import pypot.primitive
import mp3play

from gtts import gTTS


class Speak(pypot.primitive.Primitive):

    def __init__(self, robot):
        pypot.primitive.Primitive.__init__(self, robot)

        self._text = 'coucou'

    def start(self, text):

        self._text = text

        pypot.primitive.Primitive.start(self)


    def run(self):

        filename = '../utils/temp.mp3'

        tts = gTTS(self._text, lang='fr')
        tts.save(filename)

        mp3 = mp3play.load(filename)

        mp3.play()
        time.sleep(mp3.seconds() + 1)
        mp3.stop()