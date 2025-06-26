'''
    FIR Lowpass Filter
'''
import numpy as np
#from scipy.signal import firwin
import scipy.signal as sig
import matplotlib.pyplot as plt

# Sampling frequency
fs = 12
# Cutoff frequency
fc = 0.6

# Order of the filter (adjust as needed)
order = 48
M1 = order + 1

# Design the FIR lowpass filter
h1 = sig.firwin(M1, fc / (fs / 2), window='hann')

f, H1 = sig.freqz(h1,[1], fs = fs)
plt.plot(f, 20*np.log10(np.abs(H1)),label = f'M = {M1} Type I')
plt.grid()
plt.xlabel('Frequency f cycles/year')
plt.ylabel('|H(f)| (dB)')
plt.legend()
plt.title(f'FIR (Window Method), fc = {fc} cycles/year')
plt.show()
