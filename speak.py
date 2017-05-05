import threading
import pypot.primitive


from voice import *


class SayFR(pypot.primitive.Primitive):
	def start(self,text):
		threading.Thread(target=lambda:Voice.go(text=text,lang='fr')).start()


class SayEN(pypot.primitive.Primitive):
	def start(self,text):
		threading.Thread(target=lambda:Voice.go(text,lang='en')).start()


class SayES(pypot.primitive.Primitive):
	def start(self,text):
		threading.Thread(target=lambda:Voice.go(text,lang='es')).start()


class SayDE(pypot.primitive.Primitive):
	def start(self,text):
		threading.Thread(target=lambda:Voice.go(text,lang='de')).start()



