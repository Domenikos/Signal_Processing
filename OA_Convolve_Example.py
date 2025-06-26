'''
    Overlap-Add Convolution Method
    Recommended when one sequence is significantly longer than the other.
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
# Generate a White Gaussian noise signal
# Filter it with a FIR lowpass filter
fs = 2000
fc = 0.2                        # relative cut off frequency
N = 100000
T = N / fs
L_filter = 512
L_seg = 2048
t = np.linspace(0,T,N)

# Create signal and filter it
rng = np.random.default_rng()
sig = rng.standard_normal(N)
filt = signal.firwin2(L_filter, [0, fc, fc+ 0.0125, 1],[1,1,0,0])
fsig = signal.oaconvolve(sig, filt)     # filter must be FIR
fsig = fsig[L_filter-1:]        # Trim the front end of the output to the same length as the input

# Display the PSD for the original noise and the filtered sequences
plt.figure()
plt.subplot(211)
plt.plot(t,sig)
plt.grid()
plt.title('White Gaussian Noise')
plt.subplot(212)
plt.plot(t,fsig)
plt.xlabel('t (sec)')
plt.grid()
plt.title('Lowpass Filtered Noise')
plt.tight_layout()
# Display the frequency response for the original and filtered sequences
f, Psig = signal.welch(sig,fs=fs,window='hamming',nperseg=L_seg,
        nfft=2048,detrend='linear',return_onesided=True,scaling='density')
f, Pfsig = signal.welch(fsig,fs=fs,window='hamming',nperseg=L_seg,
        nfft=2048,detrend='linear',return_onesided=True,scaling='density')
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.plot(f, 10*np.log10(Psig))
plt.grid()
plt.ylim(-100,-20)
plt.ylabel(r'$P_{sig} (V^2 / Hz) (dB)$')
plt.title('Power Spectral Density (White Gaussian Noise)')
plt.subplot(212)
plt.plot(f, 10*np.log10(Pfsig))
plt.grid()
plt.ylim(-100,-20)
plt.xlabel('Frequency (Hz)')
plt.ylabel(r'$P_{fsig} (V^2 / Hz) (dB)$')
plt.title('Power Spectral Density (Lowpass Filtered Noise)')
plt.tight_layout()
plt.show()
