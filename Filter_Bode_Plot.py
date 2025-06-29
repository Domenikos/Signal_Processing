'''
    Display Filter Magnitude and Phase Response
'''
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
b = signal.firwin(40, 0.5, window=('kaiser', 8))
#b = np.array([1,2,1])/4
a = 1
w, h = signal.freqz(b,a)
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid(True)
ax2.axis('tight')
plt.show()
