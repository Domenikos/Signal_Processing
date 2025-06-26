'''
    IIR Digital Filter Design
'''

#import math
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def pow2db(P) :
    '''Convert power to dB'''
    return 10*np.log10(P)

# Lowpass Filter - IIR 

ntaps = 33
order = 8
RS = 60
fc = 0.4
Freq_edges = [0, fc, fc+.025, 1]
Band_Amplitudes = [1, 1, 0, 0]
Fs = 2
b_Hamming = signal.firwin2(ntaps,Freq_edges, Band_Amplitudes, window = 'hamming', fs = Fs)
freq, h_FIR = signal.freqz(b_Hamming, 1, fs=Fs)
#b_IIR, a_IIR = signal.butter(order, fc, 'lowpass', fs=Fs)
b_IIR, a_IIR = signal.cheby2(order, RS, fc+0.1, 'lowpass')
freq, h_IIR = signal.freqz(b_IIR, a_IIR, fs=Fs)
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.plot(freq,(abs(h_FIR)), label = rf'Hamming FIR, taps = {ntaps}')
#plt.plot(freq,(abs(h_IIR)), label=rf'Butterworth IIR, order={order}')
plt.plot(freq,(abs(h_IIR)), label=rf'Chebyshev II IIR, order={order}')
plt.grid()
plt.xlabel('Relative Frequency')
plt.ylabel('|H(f)|')
plt.legend()
plt.title(rf'Frequency Response, ($f_c$ = {fc})')
plt.subplot(212)
plt.plot(freq,np.unwrap(np.angle(h_FIR)), label=rf'Hamming FIR, taps = {ntaps}')
#plt.plot(freq,np.unwrap(np.angle(h_IIR)), label=rf'Butterworth IIR, order={order}')
plt.plot(freq,np.unwrap(np.angle(h_IIR)), label=rf'Chebyshev II IIR, order={order}')
plt.grid()
plt.legend()
plt.xlabel('Relative Frequency')
plt.ylabel(r'$\Theta(f)$, radians')
plt.title('Phase Response')
plt.tight_layout()
plt.show()
