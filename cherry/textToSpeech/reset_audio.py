#!/usr/bin/env python)
# -*- coding: utf-8 -*-

import time
import sys
import os
import csv
import pypot.primitive


def create_new_csv(fname):

	os.remove(fname)

	file = open(fname, "wb")
	writer = csv.writer(file)
	#print "Fichier ok"
	writer.writerow (('text','file'))
	file.close()

def remove_audio_files(path):
	
	for root,dirs,files in os.walk(path):
		print files
		for currentFile in files:
			print "processing file: " + currentFile
			exts = ('.mp3', '.wav')
			if any(currentFile.lower().endswith(ext) for ext in exts):
				#print os.path.join(root, currentFile)
				os.remove(os.path.join(root, currentFile))


class ResetAudio(pypot.primitive.Primitive):

	def __init__(self, robot):
		
			pypot.primitive.Primitive.__init__(self, robot)
			self.fname= '/home/poppy/resources/test/list_KO.csv' 
			self.path = '/home/poppy/resources/test/'

	def start(self):

			pypot.primitive.Primitive.start(self)

	def run(self):

		remove_audio_files(self.path)
		create_new_csv(self.fname)
