import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 20, endpoint=False)
y = np.cos(-x**2/6.0)
f_fft = signal.resample(y, 100)
f_poly = signal.resample_poly(y, 100, 20)
xnew = np.linspace(0, 10, 100, endpoint=False)

plt.plot(xnew, f_fft, 'b.-', xnew, f_poly, 'r.-')
plt.plot(x, y, 'ko-')
plt.plot(10, y[0], 'bo', 10, 0., 'ro')  # boundaries
plt.grid()
plt.legend(['resample', 'resamp_poly', 'data'], loc='best')
plt.title('Resampling Example (from SciPy Manual)')
plt.show()
