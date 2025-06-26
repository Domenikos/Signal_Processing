'''
    Application of Low-pass FIR filter
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# FIR low-pass filter (firwin)
M1 = 15     # numtaps, Type 1
fs = 10.    # sampling frequency
fc = 2.     # cutoff frequency
h1 = signal.firwin(M1, fc, window = 'hann', pass_zero = 'lowpass', fs = fs)
f, H1 = signal.freqz(h1,[1], fs = fs)
plt.plot(f, 20*np.log10(np.abs(H1)),label = rf'M = {M1} Type I')
plt.grid()
plt.xlabel('Frequency f/fs')
plt.ylabel('|H(f)| (dB)')
plt.legend()
plt.title(rf'FIR (Window Method), Fc = {fc}')

n = np.arange(-5,42)
# input discrete-time rectangular pulse
x = np.heaviside(n,1) - np.heaviside(n-7,1)

y1 = signal.lfilter(h1,[1],x)   # forward filtering
y2 = signal.filtfilt(h1,[1],x)  # forward and reverse filtering

plt.figure()
plt.stem(n,x, label='Input, x(n)')
plt.stem(n,y1, markerfmt = 'ro', linefmt='r-', label='Output, y(n)')
plt.xlim((-5,20))
plt.xlabel('n')
plt.ylabel('Filter Input and Output')
plt.grid()
plt.legend()
plt.title('FIR Lowpass Filter Response')

plt.figure()
plt.stem(n,x, label='Input, x(n)')
plt.stem(n,y2, markerfmt = 'ro', linefmt='r-', label='Output, y(n)')
plt.xlim((-5,20))
plt.xlabel('n')
plt.ylabel('Filter Input and Output')
plt.grid()
plt.legend()
plt.title('FIR Lowpass Foward and Reverse Filter Response')

plt.show()
