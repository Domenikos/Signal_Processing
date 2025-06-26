'''
    Notch Filter
    FIR Notch filter.
    
'''
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Create/view notch filter
samp_freq = 1000  # Sample frequency (Hz)
notch_freq = 60.0  # Frequency to be removed from signal (Hz)
quality_factor = 20.0  # Quality factor

# FIR notch filter - zeros on unit circle, normalized to 0 dB at z = -1
#  H(z) = (1 - 2 cos w0 z^-1 + z^-2) / (2 + 2 cos w0)
w0 = np.pi*notch_freq/(samp_freq/2)
b_FIR = [1, -2*np.cos(w0), 1]
a_FIR = [2 + 2*np.cos(w0)]
freq, h = signal.freqz(b_FIR, a_FIR, fs=samp_freq)
fig = plt.figure(figsize=(8, 6))
# Plot magnitude response of the filter
plt.plot(freq, 20 * np.log10(abs(h)),'r', label='Notch filter', linewidth='2')
plt.xlabel('Frequency [Hz]', fontsize=14)
plt.ylabel('Magnitude [dB]', fontsize=14)
plt.title(fr'FIR Notch Filter, $f_0$ = {notch_freq} Hz', fontsize=14)
plt.grid()
plt.show()
