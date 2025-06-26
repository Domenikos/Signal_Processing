'''
    Notch Filter Example
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time vector
f0 = 60  # Frequency to remove
x = np.sin(2*np.pi*40*t) + np.sin(2*np.pi*f0*t)

# Design the notch filter
Q = 30  # Quality factor
b, a = signal.iirnotch(f0, Q, fs)

# Apply the notch filter
y = signal.filtfilt(b, a, x)

# Plot magnitude response of filter
w,h = signal.freqz(b,a)
plt.plot((fs/2)*w/np.pi,abs(h))
plt.grid()
plt.xlabel('frequency (Hz)')
plt.ylabel('$|H(\omega)|$')
plt.title('Notch Filter Magnitude Response')
plt.figure()
plt.plot((fs/2)*w/np.pi,np.unwrap(np.angle(h)))
plt.grid()
plt.xlabel('frequency (Hz)')
plt.ylabel('$\Theta(\omega)$ (radians)')
plt.title('Notch Filter Phase Response')


# Plot the results
plt.figure()
plt.plot(t, x, label='Original signal')
plt.plot(t, y, label='Filtered signal')
plt.grid()
plt.xlim([0,0.2])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.show()
