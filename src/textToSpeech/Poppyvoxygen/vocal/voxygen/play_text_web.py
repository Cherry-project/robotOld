import sys
text ="je m'appelle poppy"
file = open("/home/odroid/Downloads/vocal/voxygen/txt/mateo_text_from_web.txt", "w")
file.write(text)
file.close()

import subprocess
cmd_line = "python /home/odroid/Downloads/vocal/voxygen/play_text.py /home/odroid/Downloads/vocal/voxygen/txt/mateo_text_from_web.txt" 
subprocess.call(cmd_line, shell=True)
#return text

