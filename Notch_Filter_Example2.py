'''
    Notch Filter Example2
    Base on:
    https://www.geeksforgeeks.org/design-an-iir-notch-filter-to-denoise-signal-using-python/
    Added FIR Notch filter for comparison.
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

# Design a IIR notch filter using signal.iirnotch
b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, samp_freq)
 
# Compute magnitude response of the designed IIR notch filter
freq, h = signal.freqz(b_notch, a_notch, fs=samp_freq)
 
# Plot magnitude response of the filter
fig = plt.figure(figsize=(8, 6))
plt.plot(freq, 20 * np.log10(abs(h)),'r', label='Notch filter', linewidth='2')
plt.xlabel('Frequency [Hz]', fontsize=14)
plt.ylabel('Magnitude [dB]', fontsize=14)
plt.title(fr'IIR Notch Filter, Q = {quality_factor}, $f_0$ = {notch_freq} Hz',
           fontsize=14)
plt.grid()
plt.figure(figsize=(8,6))
plt.plot(freq,np.unwrap(np.angle(h)),'r', label='Notch filter', linewidth='2')
plt.xlabel('Frequency [Hz]', fontsize=14)
plt.ylabel('Phase [radians]', fontsize=14)
plt.title(fr'IIR Notch Filter, Q = {quality_factor}, $f_0$ = {notch_freq} Hz',
           fontsize=14)
plt.grid()

# Create and view signal that is a mixture of two different frequencies
f1 = 35  # Frequency of 1st signal in Hz
f2 = 60  # Frequency of 2nd signal in Hz
# Set time vector
n = np.linspace(0, 1, 1000)  # Generate 1000 sample sequence in 1 sec
 
# Generate the signal containing f1 and f2 with random noise
#noisySignal = np.sin(2*np.pi*15*n) + np.sin(2*np.pi*50*n) + \
#    np.random.normal(0, .1, 1000)*0.3
noisySignal = (np.sin(2*np.pi*f1*n) + np.sin(2*np.pi*f2*n) + 
               np.random.randn(1000)*0.0005)

# Plotting
fig = plt.figure(figsize=(8, 8))
plt.subplot(311)
plt.plot(n, noisySignal, color='r', linewidth=2)
plt.grid()
plt.xlabel('Time', fontsize=14)
plt.ylabel('Magnitude', fontsize=14)
plt.title('Noisy Signal (random and sine wave noise)', fontsize=14)
 
# Apply IIR notch filter to the noisy signal using signal.filtfilt
outputSignal = signal.filtfilt(b_notch, a_notch, noisySignal)
# Apply FIR notch filter to the signal
outputFIR = signal.filtfilt(b_FIR,a_FIR, noisySignal)
 
# Plot FIR notch-filtered version of signal
plt.subplot(312)
# Plot output signal of notch filter
plt.plot(n, outputFIR)
plt.grid()
plt.xlabel('Time', fontsize=14)
plt.ylabel('Magnitude', fontsize=14)
plt.title('FIR Notch Filtered Output Signal', fontsize=14)
plt.subplots_adjust(hspace=0.5)

plt.subplot(313)
# Plot IIR notch-filtered version of signal
plt.plot(n, outputSignal)
plt.grid()
plt.xlabel('Time', fontsize=14)
plt.ylabel('Magnitude', fontsize=14)
plt.title('IIR Notch Filtered Output Signal', fontsize=14)
plt.subplots_adjust(hspace=0.5)

fig.tight_layout()
plt.show()
