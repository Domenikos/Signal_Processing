'''
    Design a Low-pass FIR filter and convert to a high-pass filter
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# FIR low-pass filter (firwin)
M1 = 15     # numtaps, Type 1
fs = 10.    # sampling frequency
fc = 2.     # cutoff frequency
h1 = signal.firwin(M1, fc, window = 'hann', pass_zero = True, fs = fs)
f, H1 = signal.freqz(h1,[1], fs = fs)
plt.plot(f/fs, 20*np.log10(np.abs(H1)),label = rf'M = {M1} Lowpass')
plt.grid()
plt.xlabel('Frequency f/fs')
plt.ylabel('|H(f)| (dB)')
plt.legend()
plt.title(rf'FIR (Window Method), Fc = {fc}')

# Shift 180 by negating the odd coefficients
n = np.arange(len(h1))
#print(n)
#print(h1)
h2 = (-1)**n * h1
f, H2 = signal.freqz(h2,[1], fs = fs)
#print(h2)
plt.plot(f/fs, 20*np.log10(np.abs(H2)),label = rf'M = {M1} Highpass')
plt.grid()
plt.xlabel('Frequency f/fs')
plt.ylabel('|H(f)| (dB)')
plt.legend()
plt.grid()
plt.title(rf'FIR (Window Method), Fc = {fc}')

plt.show()
