'''
    Quiz 10: Distinguish between Adjacent Frequency Components
'''

import math
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

fs = 7500           # sampling frequency
T = 10              # signal duration
N = fs * T          # total number of data values in the sequence
f1 = 1200           # message one frequency
f2 = 1260           # message two frequency
nseg = 512          # number of data values in each segment

def next_power_of_2(x):
    '''Return the next power of 2 greater than x'''
    return 1 if x == 0 else 2**(math.ceil(math.log(x,2)))

t = np.arange(0, T, 1 / fs)                 # Time vector
sig_noise = np.random.normal(0,1,N)         # Add a little noise
x = np.sin(2 * np.pi * f1 * t) + np.cos(2 * np.pi * f2 * t) + sig_noise

nfft = next_power_of_2(nseg)

f, Pxx = sig.welch(x, fs=fs, window = 'hamming', nperseg = nseg,
                       noverlap = nseg/2, nfft = nfft )

# Plotting Signals
plt.plot(t[0:999], x[0:999], label = 'Signal')
plt.grid()
plt.xlabel('time (sec)')
plt.ylabel('x(t)')
plt.title('Signal with Noise')

plt.figure()
plt.plot(f, 10*np.log10(Pxx))
plt.xlabel('frequency (Hz)')
plt.ylabel(r'$P_{xx}(f)\ (V^2 / Hz)$')
plt.grid()
#plt.ylim((-50, 10))
plt.title(rf'Power Spectral Density, $f_1 = {f1}, f_2 = {f2}$')
plt.show()
