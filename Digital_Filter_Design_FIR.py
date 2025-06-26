'''
    FIR Digital Filter Design
'''

#import math
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def pow2db(P) :
    '''Convert power to dB'''
    return 10*np.log10(P)

# Lowpass Filter - Window Design

ntaps = 33
fc = 0.4
a = 1
Freq_edges = [0, fc, fc+.025, 1]
Band_Amplitudes = [1, 1, 0, 0]
Fs = 2
Window_Hamming = 'hamming'
Window_Boxcar = 'boxcar'
b_Hamming = signal.firwin2(ntaps,Freq_edges, Band_Amplitudes, window = Window_Hamming, fs = Fs)
b_Boxcar = signal.firwin2(ntaps,Freq_edges, Band_Amplitudes, window = Window_Boxcar, fs = Fs)
n = list(range(ntaps))
freq, h_Hamming = signal.freqz(b_Hamming, a, fs=Fs)
freq, h_Boxcar = signal.freqz(b_Boxcar, a, fs=Fs)
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(n,b_Hamming, label='Hamming')
plt.stem(n,b_Boxcar, linefmt='r-', markerfmt='rD', label = 'Boxcar')
plt.grid()
plt.xlabel('n')
plt.ylabel('h(n)')
plt.legend()
plt.title(rf'Filter Impulse Response, (ntaps = {ntaps})')
plt.subplot(212)
plt.plot(freq,(abs(h_Hamming)), label='Hamming')
plt.plot(freq,(abs(h_Boxcar)), label='Boxcar')
plt.grid()
plt.xlabel('Relative Frequency')
plt.ylabel('|H(f)|')
plt.legend()
plt.title(rf'Frequency Response, ($f_c$ = {fc})')
plt.tight_layout()
# Phase Response
plt.figure()
plt.plot(freq,np.unwrap(np.angle(h_Hamming)), label='Hamming')
plt.plot(freq,np.unwrap(np.angle(h_Boxcar)), label='Boxcar')
plt.grid()
plt.legend()
plt.xlabel('Relative Frequency')
plt.ylabel(r'$\Theta(f)$, radians')
plt.title('Phase Response')
plt.show()

# FIR - Least Squares Design
b_LS = signal.firls(ntaps,Freq_edges, Band_Amplitudes, weight=[10,1], fs = Fs)
freq, h_LS = signal.freqz(b_LS, a, fs=Fs)
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(n,b_Hamming, label='Hamming')
plt.stem(n,b_LS, linefmt='r-', markerfmt='rD', label='Least Squares')
plt.grid()
plt.xlabel('n')
plt.ylabel('h(n)')
plt.legend()
plt.title(rf'Filter Impulse Response, (ntaps = {ntaps})')
plt.subplot(212)
plt.plot(freq,(abs(h_Hamming)), label='Hamming')
plt.plot(freq,(abs(h_LS)), label='Least Squares')
plt.grid()
plt.xlabel('Relative Frequency')
plt.ylabel('|H(f)|')
plt.legend()
plt.title(rf'Frequency Response, ($f_c$ = {fc})')
plt.tight_layout()
plt.show()
