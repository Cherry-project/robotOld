import pyglet
from gtts import gTTS

tts = gTTS(text='Bonjour, je suis poppy le robot open source', lang='fr')
tts.save("Speech.mp3")

music = pyglet.media.load('Speech.mp3', streaming=False) 
music.play()
pyglet.app.run()

