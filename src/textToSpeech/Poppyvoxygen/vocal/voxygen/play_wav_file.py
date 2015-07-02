# Poppy plays an audio file 
import sys

install_dir="/home/odroid/Downloads/vocal/voxygen/"

#catch the sleep time amount
for arg in sys.argv: 1

from subprocess import call

print "##############################    Starts reading WAV"

input_file = arg

silence_file = install_dir+"silence/silence_700ms.wav"

call(["aoss", "cvlc",silence_file,arg,"--play-and-exit","--no-video"])

print('############################                    ##################################');
print('############################  END READING WAV   ##################################');
print('############################                    ##################################');
print " "

