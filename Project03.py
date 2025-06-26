'''
    Filter Audio File to Remove Noise
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

def pow2db(P) :
    '''Convert power to dB'''
    return 10*np.log10(P)

Fs, data = wavfile.read(filename="/home/cgreco/Music/Bach/BachAddedNoise.wav")
#print(samplerate)
#print(data[:,0])
N = len(data)
t = np.arange(N) / Fs
normalized_data = data / (2**15)

plt.figure(figsize=(9,6))
plt.subplot(211)
plt.plot(t, normalized_data[:,0])   # channel 1
plt.grid()
plt.ylabel('Normalized Amplitude Channel 1')
plt.title(rf'Bach Minuet in G Major with Noise (Channels 1 & 2), N={N} samples')
plt.subplot(212)
plt.plot(t, normalized_data[:,1])   # channel 2
plt.grid()
plt.ylabel('Normalized Amplitude Channel 2')
plt.xlabel('time (sec)')
plt.tight_layout()
plt.show()
