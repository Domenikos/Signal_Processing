'''
    Aliasing Demonstration
'''
import numpy as np
import matplotlib.pyplot as plt

# Define the original signal
f_original = 5  # Frequency of the original signal (Hz)
fs = 200  # Sampling frequency (Hz)
t = np.arange(0, 1+1/fs, 1/fs)  # Time vector

# Generate the original signal
original_signal = np.sin(2 * np.pi * f_original * t)

# Undersample the signal
fs_undersampled = 4  # Undersampled sampling frequency (Hz)
t_undersampled = np.arange(0, 1+1/fs, 1/fs_undersampled)
undersampled_signal = np.sin(2 * np.pi * f_original * t_undersampled)

# Plot the signals
plt.figure(figsize=(10, 6))
plt.plot(t, original_signal, label=f'Original Signal ({f_original} Hz)')
plt.plot(t_undersampled, undersampled_signal, 'ro-', 
         label=f'Undersampled Signal (fs = {fs_undersampled} Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Aliasing Demonstration')
plt.legend(loc='upper right')
plt.grid()
plt.show()