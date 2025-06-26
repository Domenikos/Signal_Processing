'''
    Lowpass Filter Example
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.fft

def mag2db(P) :
    '''Convert magnitude to dB'''
    return 20*np.log10(P)

# Low-pass Filter
ntaps = 29
fc = 0.5
tband = 0.1
F = [0, fc, fc+tband, 1]
G = [1, 1, 0, 0]
#b = signal.firls(ntaps,bands = [0, fc, fc+0.2, 1],desired = [1, 1, 0, 0])
#b = signal.firwin(ntaps, fc)
b = signal.firwin2(numtaps=ntaps,freq=F, gain=G,fs=2)
#b = signal.remez(ntaps,[0, fc, fc+0.2, 1],[1, 0],fs=2)
plt.figure()
n = list(range(len(b)))
plt.stem(b)
plt.grid()
plt.xlabel('n')
plt.ylabel('h(n)')
plt.title(rf'Impulse Response Lowpass Filter, ntaps = {ntaps}')
a = 1
fs = 2
freq, h = signal.freqz(b, a, fs=fs)
plt.figure()
plt.plot(freq,mag2db(abs(h)))
plt.grid()
plt.xlabel('Normalized frequency')
plt.ylabel('|H(f)| (dB)')
#plt.title(rf'Frequency Response, fc = {fc}, ntaps = {ntaps}')
plt.title('Frequency Response')
plt.figure()
plt.plot(freq,np.unwrap(np.angle((h))))
plt.grid()
plt.xlabel('Normalized frequency')
plt.ylabel(r'$\Theta(f)$')
plt.title(rf'Phase, fc = {fc}')

plt.show()
