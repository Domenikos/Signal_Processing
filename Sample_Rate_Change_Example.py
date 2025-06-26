'''
    Sample Rate Change

'''
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

Fs = 2000
N = 5000
f1 = 50
f2 = 200
t = np.arange(N) / Fs
x = np.cos(2*np.pi*f1*t) + np.cos(2*np.pi*f2*t)
plt.figure(figsize=(8,6))
plt.plot(t[300:400],x[300:400])
plt.grid()
plt.xlabel('t (sec)')
plt.ylabel('x(t)')
plt.title('Original Signal')

# Resample to 300 Hz, Fs1/Fs = 3/10
Fs1 = 300
x_resample = sig.resample_poly(x,up = 3, down = 20)
N1 = len(x_resample)
t1 = np.arange(N1) / Fs1

plt.figure(figsize=(8,6))
plt.plot(t1[90:120],x_resample[90:120])
plt.grid()
plt.xlabel('t (sec)')
plt.ylabel('x_resample(t)')
plt.title('Resampled Signal')

plt.show()
