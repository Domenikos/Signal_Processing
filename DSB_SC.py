import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import math

def modulate_dsb_sc(message_signal, carrier_freq, fs):
    """Modulates the message signal using DSB-SC modulation."""
    t = np.arange(0, len(message_signal) / fs, 1 / fs)
    carrier_signal = np.cos(2 * np.pi * carrier_freq * t)
    modulated_signal = message_signal * carrier_signal
    return modulated_signal

def demodulate_dsb_sc(modulated_signal, carrier_freq, fs, cutoff_freq):
    """Demodulates the DSB-SC modulated signal - coherent demodulation."""
    t = np.arange(0, len(modulated_signal) / fs, 1 / fs)
    carrier_signal = np.cos(2 * np.pi * carrier_freq * t)
    demodulated_signal = modulated_signal * carrier_signal

    # Low-pass filtering to recover the message signal
    b, a = sig.butter(6, cutoff_freq / (0.5 * fs), btype='low')
    recovered_message = sig.lfilter(b, a, demodulated_signal)
    return recovered_message

def next_power_of_2(x):
    '''Return the next power of 2 greater than x'''
    return 1 if x == 0 else 2**(math.ceil(math.log(x,2)))

# Example usage
if __name__ == "__main__":
    fs = 1000  # Sampling frequency
    fcutoff = 10    # Cutoff frequency for demodulation LP filter
    t = np.arange(0, 10, 1 / fs)  # Time vector
    message_signal = np.sin(2 * np.pi * 5 * t)  # Message signal (5 Hz sine wave)
    carrier_freq = 100  # Carrier frequency (100 Hz)

    modulated = modulate_dsb_sc(message_signal, carrier_freq, fs)
    demodulated = demodulate_dsb_sc(modulated, carrier_freq, fs, fcutoff)

    nseg = len(t)/5
    nfft = next_power_of_2(nseg)

    f, Pxx = sig.welch(modulated, fs=fs, window = 'hann', nperseg = nseg, 
                       noverlap = nseg/2, nfft = nfft )

    # Plotting Signals
    plt.plot(t[0:999], message_signal[0:999], label = 'message')
    plt.plot(t[0:999], modulated[0:999], label = 'modulated')
    plt.plot(t[0:999], demodulated[0:999], label = 'demoduled')
    plt.grid()
    plt.xlabel('t (sec)')
    plt.ylabel('magnitude')
    plt.legend()
    plt.title('Double Sideband Suppressed Carrier (DSB-SC)')
    #plt.show()

    # Plot Modulated Signal Spectrum
    plt.figure()
    plt.plot(f, 10*np.log10(Pxx))
    plt.xlabel('frequency (Hz)')
    plt.ylabel('Pxx(f)')
    plt.grid()
    plt.ylim((-50, 10))
    plt.title('DSB-SC Power Spectral Density')
    plt.show()
   