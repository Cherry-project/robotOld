#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0

from __future__ import division

import argparse
import collections
import contextlib
import functools
import logging
import re
import signal
import sys
import time

import google.auth
import google.auth.transport.grpc
import google.auth.transport.requests
from google.cloud.proto.speech.v1beta1 import cloud_speech_pb2
from google.rpc import code_pb2
import grpc
import pyaudio
from six.moves import queue

import sys
import os
import pypot
import urllib2
import urllib
import pyttsx
import string
import speech
import speech_recognition as sr
from test_bdd import RechercheFichiers
from voice_recognition import voice_recognition
from chatterbot import sendToChatterbot
from choix_document import ChoixDocument
from ReponseRobot import ReponseRobot
from pygsr import Pygsr
from gtts import gTTS
import pypot.primitive
import pyglet
import time
import pygame.mixer
from random import randint 
import copy


# Seconds you have to wrap up your utterance
WRAP_IT_UP_SECS = 15
SECS_OVERLAP = 1

syn_parameters = {
    'text': '',
    'voice': 'fr-FR_ReneeVoice',
    'download': True,
    'accept': 'audio/wav'
}

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

# The Speech API has a streaming limit of 60 seconds of audio*, so keep the
# connection alive for that long, plus some more to give the API time to figure
# out the transcription.
# * https://g.co/cloud/speech/limits#content
DEADLINE_SECS = 60 * 3 + 5
SPEECH_SCOPE = 'https://www.googleapis.com/auth/cloud-platform'

class STT_google(pypot.primitive.Primitive):
    
    properties = pypot.primitive.Primitive.properties + ['listen_state']

    def __init__(self, robot, state = 'normal', ttsengine='watson'):
        pypot.primitive.Primitive.__init__(self, robot)
        self._state = state
        self._robot = robot
        self._ttsengine = ttsengine
        self._engine=pyttsx.init()
        #self.ttsWatson = TtsWatson('9ab9e322-6ac9-4d11-a93f-10c19667a013', 'G4QF16oBGpIC', 'fr-FR_ReneeVoice')
        # self.ttsWatson = TtsWatson('c7b754a7-30af-478b-ad09-50d6599fee4a', '4PiXRAE4QPpU', 'fr-FR_ReneeVoice')

          
    def start(self):
        pypot.primitive.Primitive.start(self)

    def run(self):
        
        while(self._state == 'normal'):
            # obtain audio from the microphone
            # r = sr.Recognizer()
            # with sr.Microphone() as source:
            #     audio = r.adjust_for_ambient_noise(source)
            #     print("Say something!")
            #     audio = r.listen(source)
            # # recognize speech using Google Speech Recognition
            # msg= ""
            # try:
            #             # for testing purposes, we're just using the default API key
            #             # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            #             # instead of `r.recognize_google(audio)`
            #     msg = r.recognize_google(audio,language='FR').encode("utf-8")        
            #     print("Google Speech Recognition thinks you said " + msg)
                    
            # except sr.UnknownValueError:
            #     print("Google Speech Recognition could not understand audio")
            #     #voice_recognition()
            #     #return 0 
            # except sr.RequestError as e:
            #     print("Could not request results from Google Speech Recognition service; {0}".format(e))


            # #msg = r.recognize_google(audio,language='FR').encode("utf-8")
            # #print "Message " + msg
            print "You can speak"
            msg = main()
            print "You said : "+msg
            print type(msg)
            if msg != "None":
                msg = msg.encode('utf-8')
                params = urllib.urlencode({'msg':msg})
                print type(msg)
                print "\nUtilisateur : " + msg.decode('utf-8')

                print str("J'envois la requête")
                #urllib2.urlopen('http://localhost:8080/chatterbot',params)
                response = sendToChatterbot(msg);
                
                
                #requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                response = response.encode('utf-8')
                print type(response)
                

                # while pygame.mixer.music.get_busy():
                #     time.sleep(0.1)

                # pygame.mixer.quit()
                # time.sleep(0.2)
                # os.remove(filename) #remove temperory file

                #engine = pyttsx.init('sapi5')
                if "&quot;" in response :
                    response = response.replace("&quot;"," ")
                if "&apos;" in response :
                    response = response.replace("&apos;"," ")
                print "\n Bot : "+response
                # engine = self._engine
                # engine.setProperty('rate', 150)
                # engine.say(response)
                # engine.runAndWait()

                # methode avec la biblio ttswatson
                # pour une raison inconnue ne marche pas couplé à google
                #self.ttsWatson.play(response)

                # methode en appelant la demo de watson sur le net

                s = synthesize(response)
                p = pyaudio.PyAudio()
                stream = p.open(format=p.get_format_from_width(2),channels=1,rate=22050,output=True)
                stream.write(s)


                print "Requête délivrée"
                msg = ""
            else:
                print "Pas de message"

    @property
    def listen_state(self):
        return self._state

    @listen_state.setter
    def listen_state(self, state):
        print "Set parameter to: " + state
        self._state= state

def make_channel(host):
    """Creates a secure channel with auth credentials from the environment."""
    # Grab application default credentials from the environment
    credentials, _ = google.auth.default(scopes=[SPEECH_SCOPE])

    # Create a secure channel using the credentials.
    http_request = google.auth.transport.requests.Request()

    return google.auth.transport.grpc.secure_authorized_channel(
        credentials, http_request, host)


def _audio_data_generator(buff, overlap_buffer):
    """A generator that yields all available data in the given buffer.
    Args:
        buff (Queue): A Queue where each element is a chunk of data.
        overlap_buffer (deque): a ring buffer for storing trailing data chunks
    Yields:
        bytes: A chunk of data that is the aggregate of all chunks of data in
        `buff`. The function will block until at least one data chunk is
        available.
    """
    if overlap_buffer:
        yield b''.join(overlap_buffer)
        overlap_buffer.clear()

    while True:
        # Use a blocking get() to ensure there's at least one chunk of data.
        data = [buff.get()]

        # Now consume whatever other data's still buffered.
        while True:
            try:
                data.append(buff.get(block=False))
            except queue.Empty:
                break

        # `None` in the buffer signals that we should stop generating. Put the
        # data back into the buffer for the next generator.
        if None in data:
            data.remove(None)
            if data:
                buff.put(b''.join(data))
            break
        else:
            overlap_buffer.extend(data)

        yield b''.join(data)


def _fill_buffer(buff, in_data, frame_count, time_info, status_flags):
    """Continuously collect data from the audio stream, into the buffer."""
    buff.put(in_data)
    return None, pyaudio.paContinue


# [START audio_stream]
@contextlib.contextmanager
def record_audio(rate, chunk):
    """Opens a recording stream in a context manager."""
    # Create a thread-safe buffer of audio data
    buff = queue.Queue()

    audio_interface = pyaudio.PyAudio()
    audio_stream = audio_interface.open(
        format=pyaudio.paInt16,
        # The API currently only supports 1-channel (mono) audio
        # https://goo.gl/z757pE
        channels=1, rate=rate,
        input=True, frames_per_buffer=chunk,
        # Run the audio stream asynchronously to fill the buffer object.
        # This is necessary so that the input device's buffer doesn't overflow
        # while the calling thread makes network requests, etc.
        stream_callback=functools.partial(_fill_buffer, buff),
    )

    yield buff

    audio_stream.stop_stream()
    audio_stream.close()
    # Signal the _audio_data_generator to finish
    buff.put(None)
    audio_interface.terminate()
# [END audio_stream]


def request_stream(data_stream, rate, single_utterance=True):
    """Yields `StreamingRecognizeRequest`s constructed from a recording audio
    stream.
    Args:
        data_stream (generator): The raw audio data to send.
        rate (int): The sampling rate in hertz.
        interim_results (boolean): Whether to return intermediate results,
            before the transcription is finalized.
    """
    # The initial request must contain metadata about the stream, so the
    # server knows how to interpret it.
    recognition_config = cloud_speech_pb2.RecognitionConfig(
        # There are a bunch of config options you can specify. See
        # https://goo.gl/KPZn97 for the full list.
        encoding='LINEAR16',  # raw 16-bit signed LE samples
        sample_rate=rate,  # the rate in hertz
        # See http://g.co/cloud/speech/docs/languages
        # for a list of supported languages.
        language_code='fr-FR',  # a BCP-47 language tag
    )
    streaming_config = cloud_speech_pb2.StreamingRecognitionConfig(
        interim_results=single_utterance,
        config=recognition_config,
    )

    yield cloud_speech_pb2.StreamingRecognizeRequest(
        streaming_config=streaming_config)

    for data in data_stream:
        # Subsequent requests can all just have the content
        yield cloud_speech_pb2.StreamingRecognizeRequest(audio_content=data)


def listen_print_loop(
        recognize_stream, wrap_it_up_secs, buff, max_recog_secs=60):
    """Iterates through server responses and prints them.
    The recognize_stream passed is a generator that will block until a response
    is provided by the server. When the transcription response comes, print it.
    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    # What time should we switch to a new stream?
    time_to_switch = time.time() + max_recog_secs - wrap_it_up_secs
    graceful_exit = False
    num_chars_printed = 0
    for resp in recognize_stream:
        if resp.error.code != code_pb2.OK:
            raise RuntimeError('Server error: ' + resp.error.message)

        if not resp.results:
            if resp.endpointer_type is resp.END_OF_SPEECH and (
                    time.time() > time_to_switch):
                graceful_exit = True
                buff.put(None)
            continue

        # Display the top transcription
        result = resp.results[0]
        transcript = result.alternatives[0].transcript

        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        if result.is_final:
            recognize_stream.cancel()
            return transcript


def synthesize(text):
    # Don't modify the original object
    parameters = copy.copy(syn_parameters)
    # Set the text
    parameters['text'] = text

    # Request foo!

    #r = requests.get('https://text-to-speech-demo.mybluemix.net/api/synthesize?' + urlencode(parameters))
    r = urllib2.urlopen('https://text-to-speech-demo.mybluemix.net/api/synthesize?'+ urllib.urlencode(parameters))

    return r.read()

def main():
    service = cloud_speech_pb2.SpeechStub(
        make_channel('speech.googleapis.com'))

    # For streaming audio from the microphone, there are three threads.
    # First, a thread that collects audio data as it comes in
    with record_audio(RATE, CHUNK) as buff:
        # Second, a thread that sends requests with that data
        overlap_buffer = collections.deque(
            maxlen=int(SECS_OVERLAP * RATE / CHUNK))
        requests = request_stream(
            _audio_data_generator(buff, overlap_buffer), RATE)
        # Third, a thread that listens for transcription responses
        recognize_stream = service.StreamingRecognize(
            requests, DEADLINE_SECS)

        # Exit things cleanly on interrupt
        signal.signal(signal.SIGINT, lambda *_: recognize_stream.cancel())

        # Now, put the transcription responses to use.
        try:
            while True:
                testUtterance = listen_print_loop(recognize_stream, WRAP_IT_UP_SECS, buff)
                if testUtterance != "":
                    recognize_stream.cancel()
                    return testUtterance
                    break

                
                # Discard this stream and create a new one.
                # Note: calling .cancel() doesn't immediately raise an RpcError
                # - it only raises when the iterator's next() is requested
                recognize_stream.cancel()

                logging.debug('Starting new stream')
                requests = request_stream(_audio_data_generator(
                    buff, overlap_buffer), RATE)
                recognize_stream = service.StreamingRecognize(
                        requests, DEADLINE_SECS)

        except grpc.RpcError:
            # This happens because of the interrupt handler
            pass
