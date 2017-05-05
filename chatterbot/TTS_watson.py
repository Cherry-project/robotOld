#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib2
import sys
import copy
import urllib
import pyaudio
import time

syn_parameters = {
    'text': '',
    'voice': 'fr-FR_ReneeVoice',
    'download': True,
    'accept': 'audio/wav'
}

def main():
    # Get the text
    chaine = ""
    tab = sys.argv[1].split("_");
    for i in tab :
      chaine+=i+" "
    text = chaine.decode("cp1252")
    print text

    # Synthesize it
    s = synthesize(text)
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2),channels=1,rate=22050,output=True)
    stream.write(s)
    
    print "fini"
    # Write it to a `f.ogg` file, overwriting it if it exists
    # with open('f.ogg', 'wb+') as f:
    #     f.write(s.content)
    stream.stop_stream()
    stream.close()
    p.terminate()

def synthesize(text):
    # Don't modify the original object
    parameters = copy.copy(syn_parameters)
    
    # Set the text
    parameters['text'] = text.encode("utf-8")

    # Request foo!

    #r = requests.get('https://text-to-speech-demo.mybluemix.net/api/synthesize?' + urlencode(parameters))
    r = urllib2.urlopen('https://text-to-speech-demo.mybluemix.net/api/synthesize?'+ urllib.urlencode(parameters))

    return r.read()

if __name__ == '__main__':
    # watsontts was called directly
    main()