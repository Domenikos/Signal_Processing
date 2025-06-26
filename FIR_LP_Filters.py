'''
    FIR Low-Pass Filters
'''
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# FIR low-pass filter (firwin)
M1 = 15     # numtaps, Type 1
fs = 1.0    # sampling frequency
fc = 0.2    # cutoff frequency
h1 = sig.firwin(M1, fc, window = 'hann', pass_zero = True, fs = 1.0)
f, H1 = sig.freqz(h1,[1], fs = fs)
plt.plot(f, 20*np.log10(np.abs(H1)),label = f'M = {M1} Type I')
M2 = 16     # Type 2
h2 = sig.firwin(M2, fc, window = 'hann', pass_zero = True, fs = 1.0)
f, H2 = sig.freqz(h2,[1], fs = fs)
plt.plot(f,20*np.log10(np.abs(H2)), label = f'M = {M2} Type II')
plt.grid()
plt.xlabel('Frequency f/fs')
plt.ylabel('|H(f)| (dB)')
plt.legend()
plt.title(f'FIR (Window Method), Fc = {fc}')
#plt.show()

# Impulse Responses Low-pass Filter (firwin)
plt.figure()
n1 = range(M1)
plt.stem(n1,h1,label=f'M = {M1} Type I')
n2 = range(M2)
plt.stem(n2,h2, markerfmt = 'ro', label = f'M = {M2} Type II')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid()
plt.legend()
plt.title('FIR (Window Method) Impulse Response')
#plt.show()

# FIR Low-Pass Filter (Equal Ripple, remez)
plt.figure()
bands = [0, fc, fc+0.115, 0.5]

h3 = sig.remez(M1, bands = bands, desired = [1,0], weight = [1,10],fs = fs)
f, H3 = sig.freqz(h3,[1], fs = fs)
plt.plot(f, 20*np.log10(np.abs(H1)),label = f'FIR Window, M = {M1}')
plt.plot(f, 20*np.log10(np.abs(H3)),label = f'FIR Remez, M = {M1}')
plt.grid()
plt.xlabel('Frequency f/fs')
plt.ylabel('|H(f)| (dB)')
plt.legend()
plt.title(f'FIR (Window vs Remez Method), Fc = {fc}')

#plt.show()

# Phase Response for FIR Low-Pass Filters
plt.figure()
plt.plot(f, np.unwrap(np.angle(H1)),label = f'FIR Window, M = {M1}')
plt.plot(f, np.unwrap(np.angle(H3)),label = f'FIR Remez, M = {M1}')
plt.grid()
plt.xlabel('Frequency f/fs')
plt.ylabel('Phase (radians)')
plt.legend()
plt.title(f'FIR (Window vs Remez Method), Fc = {fc}')
plt.show()
