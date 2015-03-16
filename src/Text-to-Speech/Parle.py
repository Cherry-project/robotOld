import pyglet
from gtts import gTTS

# !!!!! Attention a n'utiliser que des caracteres ASCII, meme pour le speech du robot !!!!

tts = gTTS(text='Bonjour,', lang='fr')
tts.save("Speech.mp3")   # cree le mp3

music = pyglet.media.load('Speech.mp3', streaming=False) 
music.play()  #lit le mp3

def exiter(dt):
    pyglet.app.exit()
pyglet.clock.schedule_once(exiter, music.duration)  #arrete la boucle a la fin du mp3

pyglet.app.run()  #lance la boucle
#______________NOM DE LA PERSONNE____________________________
tts = gTTS(text='Maximilien', lang='fr')
tts.save("Speech.mp3")  

music = pyglet.media.load('Speech.mp3', streaming=False) 
music.play() 

def exiter(dt):
    pyglet.app.exit()
pyglet.clock.schedule_once(exiter, music.duration)

pyglet.app.run()
#__________________________________________
tts = gTTS(text='Comment vas-tu ? Regarde comme je parle bien.', lang='fr')
tts.save("Speech.mp3")

music = pyglet.media.load('Speech.mp3', streaming=False) 
music.play()

def exiter(dt):
    pyglet.app.exit()
pyglet.clock.schedule_once(exiter, music.duration)

pyglet.app.run()

