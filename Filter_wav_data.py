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
#plt.show()

# Display Power Spectral Density of Signal with Noise
Fs = 44100
NFFT = 8192
nseg = 8192
f, Pxx = signal.welch(normalized_data[:,0],fs=Fs,window='hann',nperseg=nseg,
    noverlap=nseg/2,nfft=NFFT,detrend='linear',return_onesided=True,scaling='density')
plt.figure(figsize=(9,6))
plt.plot(f,pow2db(Pxx))
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel(r'$P_{XX}\ (V^2 / Hz)\ dB$')
plt.title('PSD: Signal with Noise')
#plt.show()

# Design a Lowpass Filter to remove noise
Fc = 5000
a = 1
ntaps = 127
Freq_edges = [0, Fc, Fc+800, Fs/2]
Band_Amplitudes = [1, 1, 0, 0]
#b = signal.firwin2(ntaps,Freq_edges, Band_Amplitudes, window = 'hamming', fs = Fs)
b = signal.firls(ntaps,Freq_edges, Band_Amplitudes, fs = Fs)
freq, H = signal.freqz(b, a, fs=Fs)
plt.figure()
plt.plot(freq, pow2db(abs(H)))
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel('|H(f)|')
plt.title('Filter Frequency Response')
# plt.show()
filtered_sig = signal.oaconvolve(normalized_data[:,0], b)     # filter must be FIR
f, Pxx_filtered = signal.welch(filtered_sig,fs=Fs,window='hann',nperseg=nseg,
    noverlap=nseg/2,nfft=NFFT,detrend='linear',return_onesided=True,scaling='density')
plt.figure(figsize=(9,6))
plt.plot(f,pow2db(Pxx), label='Unfiltered')
plt.plot(f,pow2db(Pxx_filtered), label='Filtered')
plt.grid()
plt.xlabel('Frequency (Hz)')
plt.ylabel(r'$P_{XX}\ (V^2 / Hz)\ dB$')
plt.legend()
plt.title('PSD: Filtered and Signal with Noise')
plt.show()
