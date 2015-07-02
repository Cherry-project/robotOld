# Poppy : read an text and play
# aoss ./baratinoo -i utf8 fichier.txt -o wav output.wav baratinoo.cfg
# aoss ./baratinoo -i utf8 fichier.txt -o ecoute baratinoo.cfg

import sys

#catch the input text file
#for input_text_file in sys.argv: 1

install_dir="/home/odroid/Downloads/vocal/voxygen/"

input_text_file = str(sys.argv[1])
print input_text_file

output_file = install_dir+"tmpwav/output_mateo.wav"
silence_file = install_dir+"silence/silence_700ms.wav"
cmd_speak = install_dir+"baratinoo"
cfg_speak = install_dir+"baratinoo.cfg"

from subprocess import call
print "##############################    Starts reading and playing TEXT"

call([cmd_speak,"-i", "utf8",input_text_file,"-o","wav",output_file, cfg_speak])
call(["aoss", "cvlc",silence_file,output_file,"--play-and-exit","--no-video"])


print('############################                    ##################################');
print('############################  END PLAYING TEXT  ##################################');
print('############################                    ##################################');
print " "

