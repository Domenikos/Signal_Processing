#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:31:03 2019

@author: cgreco
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def plot_response(fs, w, h, title):
    plt.figure()
    plt.plot(0.5*fs*w/np.pi, 20*np.log10(np.abs(h)))
    plt.ylim(-60, 5)
    plt.xlim(0, 0.5*fs)
    plt.grid(True)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain (dB)')
    plt.title(title)

'''
This example shows a steep low pass transition according to
the small transition width and high filter order:
'''

# Low-pass filter design parameters

fs = 22050.0       # Sample rate, Hz
cutoff = 8000.0    # Desired cutoff frequency, Hz
trans_width = 250  # Width of transition from pass band to stop band, Hz
numtaps = 125      # Size of the FIR filter.
taps = signal.remez(numtaps, [0, cutoff, cutoff + trans_width, 0.5*fs], [1, 0], 
                    [1, 5], type = 'bandpass', fs=fs)
w, h = signal.freqz(taps, [1], worN=2000)
plot_response(fs, w, h, "Low-pass Filter")


# This example is a first order derivative filter

fs = 1000.0       # Sample rate, Hz
cutoff = 250.0    # Desired cutoff frequency, Hz
trans_width = 50.0  # Width of transition from pass band to stop band, Hz
numtaps = 40      # Size of the FIR filter.
taps = signal.remez(numtaps, [0, cutoff, cutoff + trans_width, 0.5*fs], [1, 0],
                    Hz=fs,type='differentiator')
w, h = signal.freqz(taps, [1], worN=2000)
#plot_response(fs, w, h, "Derivative Filter")
plt.figure()
plt.plot(0.5*fs*w/np.pi, (np.abs(h)))
plt.xlim(0, 0.5*fs)
plt.grid(True)
plt.xlabel('Frequency (Hz)')
plt.title('Low-Pass Differentiator Filter')

plt.show()
