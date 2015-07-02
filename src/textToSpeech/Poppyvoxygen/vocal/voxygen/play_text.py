# Poppy : read an text and play
# aoss ./baratinoo -i utf8 fichier.txt -o wav output.wav baratinoo.cfg
# aoss ./baratinoo -i utf8 fichier.txt -o ecoute baratinoo.cfg

import sys

#catch the input text file
for arg in sys.argv: 1

install_dir="/home/odroid/Downloads/vocal/voxygen/"

input_text = arg
print input_text

output_file = install_dir+"tmpwav/output_mateo_from_web.wav"
input_text_file= install_dir+"txt/txt_from_web.txt"
silence_file = install_dir+"silence/silence_700ms.wav"
cmd_speak = install_dir+"baratinoo"
cfg_speak = install_dir+"baratinoo.cfg"

from subprocess import call
print "##############################    Starts reading and playing TEXT"

# write the text to a file before reading it
file = open(input_text_file, "w")
file.write(input_text)
file.close()

call([cmd_speak,"-i", "utf8",input_text_file,"-o","wav",output_file, cfg_speak])
call(["aoss", "cvlc",silence_file,output_file,"--play-and-exit","--no-video"])


print('############################                    ##################################');
print('############################  END PLAYING TEXT  ##################################');
print('############################                    ##################################');
print " "

