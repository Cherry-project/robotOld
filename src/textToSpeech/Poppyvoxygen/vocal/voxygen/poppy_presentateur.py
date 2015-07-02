# Poppy presentateur
import sys

install_dir="/home/odroid/Downloads/vocal/voxygen/"
upload_done=install_dir+"tmpwav/upload.done"
output_file =install_dir+ "tmpwav/output.wav"
news_file = install_dir+"tmpwav/news.wav"
silence_file = install_dir+"silence/silence_700ms.wav"

#catch the sleep time amount
for arg in sys.argv: 1

from subprocess import call
call(["clear"])

import time
print "##############################    Start : %s" % time.ctime()

sleep_time = int(arg)

import os
while 1==1:
    if os.path.isfile(upload_done):
        call(["cp", output_file, news_file])
        print ('output.wav file backuped before reading the news')
        call(["rm", upload_done])

    while 1==1:

        call(["aoss", "cvlc",silence_file,news_file,"--play-and-exit","--no-video"])

        print('############################                    ##################################');
        print('############################  END READING NEWS  ##################################');
        print('############################                    ##################################');
	print "############################    Cycle ended at : %s" % time.ctime()
        print "############################    Start sleeping before next cycle in %i seconds" % sleep_time
        time.sleep( sleep_time ) # x seconds

        print "############################   "
        print "############################   "
        print "############################    Next cycle starts : %s" % time.ctime()
        print " "

        if os.path.isfile(upload_done):
            call(["cp", output_file, news_file])
            print ('A new file arrived! backuped before reading the news... GO ! ')
            print " "
            print "############################   "
            call(["rm", upload_done])

    else:
        print "############################  FILE Transfert not ready.. sleeping 20s "
        time.sleep( 20 )

