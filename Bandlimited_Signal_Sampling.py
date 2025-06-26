'''
    Sampling a Bandlimited Signal
'''
import numpy as np
import matplotlib.pyplot as plt

def dsb_sc_modulate(message, carrier_freq, fs):
    """Modulate a message onto a carrier frequency using DSB-SC.
    
    Parameters:
    message (ndarray): The message signal to be modulated.
    carrier_freq (float): The frequency of the carrier signal.
    fs (float): The sample rate of the signals.
    
    Returns:
    ndarray: The modulated signal.
    """
    t = np.arange(len(message)) / fs
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    modulated = message * carrier
    return modulated

def dsb_sc_demodulate(modulated, carrier_freq, fs):
    """Demodulate a DSB-SC modulated signal.
    
    Parameters:
    modulated (ndarray): The modulated signal.
    carrier_freq (float): The frequency of the carrier signal.
    fs (float): The sample rate of the signals.
    
    Returns:
    ndarray: The demodulated message signal.
    """
    t = np.arange(len(modulated)) / fs
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    demodulated = modulated * carrier
    return demodulated

# Set the parameters
fs = 1000  # Sample rate (samples/second)
carrier_freq = 50  # Carrier frequency (Hz)
message_freq = 10  # Message frequency (Hz)
duration = 1  # Duration of signal (seconds)

# Generate the message signal
t = np.arange(duration * fs) / fs
message = np.sin(2 * np.pi * message_freq * t)

# Modulate the message onto the carrier
modulated = dsb_sc_modulate(message, carrier_freq, fs)

# Demodulate the modulated signal to recover the message
demodulated = dsb_sc_demodulate(modulated, carrier_freq, fs)

# Plot the signals
plt.figure()
plt.plot(t, message, label='Message')


plt.plot(t, modulated, label='Modulated')


plt.plot(t, demodulated, label='Demodulated')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
