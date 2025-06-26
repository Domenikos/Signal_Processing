#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""PyAudio Example: Play a wave file."""

import wave
import sys

import pyaudio

chunk = 1024
'''
if len(sys.argv) < 2:
    print(f'Plays a wave file. Usage: {sys.argv[0]} filename.wav')
    sys.exit(-1)

with wave.open(sys.argv[1], 'rb') as wf:
    # Instantiate PyAudio and initialize PortAudio system resources (1)
    p = pyaudio.PyAudio()

    # Open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    
    # read data  
    data = wf.readframes(chunk)  
  
    # Play samples from the wave file (3)
    while len(data := wf.readframes(chunk)):  # Requires Python 3.8+ for :=
        stream.write(data)

    # Close stream (4)
    stream.stop_stream()
    stream.close()

    # Release PortAudio system resources (5)
    p.terminate()
'''
#open a wav format music  
f = wave.open(r"/home/cgreco/Music/Bach/Bach_Minuet_in_G_major30sec.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
#read data  
data = f.readframes(chunk)
  
#play stream  
while data !='':  
    stream.write(data)  
    data = f.readframes(chunk)  
  
#stop stream  
stream.stop_stream()  
stream.close()  
  
#close PyAudio  
p.terminate() 
