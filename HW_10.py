'''
    Homework 10
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 2
# 10.1 (a) Running average filter y(n) = (x(n) + x(n-1) + x(n-2))/3
a = 3
b =[1, 1, 1]
freq, h = signal.freqz(b, a, fs=fs)
plt.plot(freq,abs(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.title('Running Average Filter, h(n) =(x(n) + x(n-1) + x(n-2))/3')
# 10.1 (b) Improved running average filter h(n) =(x(n) + 2x(n-1) + x(n-2))/4
a = 4
b = [1, 2, 1]
freq, h = signal.freqz(b, a, fs=fs)
plt.figure()
plt.plot(freq,abs(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.title('Improved Running Average Filter, h(n) =(x(n) + 2x(n-1) + x(n-2))/4')
# 10.1 (c) High-pass Filter
# h(n) =(x(n) - 2x(n-1) + x(n-2))/4
a = 4
b = [1, -2, 1]
freq, h = signal.freqz(b, a, fs=fs)
plt.figure()
plt.plot(freq,abs(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.title('High-pass Filter, h(n) =(x(n) - 2x(n-1) + x(n-2))/4')
# 10.1 (d) Comb Filter
# h(n) =(x(n) + x(n-4))
a = 2
b = [1, 0, 0, 0, 1]
freq, h = signal.freqz(b, a, fs=fs)
plt.figure()
plt.plot(freq,abs(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.title('Feedforward Comb Filter')
# 10,1 (e) Differentiator Filter
# h(n) =(x(n) - x(n-1))
a = 2
b = [1, -1]
freq, h = signal.freqz(b, a, fs=fs)
plt.figure()
plt.plot(freq,abs(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.title('Differentiator Filter, h(n) =(x(n) - x(n-1))')
plt.show()

## 10.2 Resonator
#  H(z) = b0 /(1 - 2r cos w0 z^-1 + r^2 z^-2)
w0 = np.pi/4
r = 0.98 
b0 = 1
a1 = [1, -2*r*np.cos(w0), r**2]
freq, h = signal.freqz(b0, a1, fs=fs)
plt.figure()
plt.plot(freq,abs(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.title(r'Resonator, $H(z) = b_0 /(1 - 2r\ cos \omega_0 z^{-1} + r^2 z^{-2})$,'+fr' r={r}')
## 10.3 FIR Notch filter
#  H(z) = (1 - 2r cos w0 z^-1 + r^2 z^-2)
w0 = np.pi/4
a2 = 1
b2 = [1, -2*np.cos(w0), 1]
freq, h = signal.freqz(b2, a2, fs=fs)
plt.figure()
plt.plot(freq,abs(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.title(r'FIR Notch Filter, $H(z) = (1 - 2 cos \omega_0 z^{-1} + z^{-2})$')
## 10.4 IIR Notch Filter 
b0 = (1 + r**2 + 2*r*np.cos(w0))/(2 + 2*np.cos(w0))
b3 = b0*np.array(b2)
a3 = np.array(a1)
freq, h = signal.freqz(b3, a3, fs=fs)
plt.figure()
plt.plot(freq,abs(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.title(fr'IIR 2nd Order Notch Filter (Normalized), r = {r}')
# Phase
plt.figure()
plt.plot(freq,np.angle(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel(r'$\Theta(f)$ (rad)')
plt.title(fr'IIR 2nd Order Notch Filter (Normalized), r = {r}')
plt.show()

# Cascade 2nd Notch Filter
w1 = 3*np.pi/4
b4 = np.array([1, -2*np.cos(w1), 1])
b0 = (1 + r**2 + 2*r*np.cos(w1))/(2 + 2*np.cos(w1))
b4 = b0*b4
a4 = np.array([1, -2*r*np.cos(w1), r**2])
freq, h = signal.freqz(b4, a4, fs=fs)
plt.figure()
plt.plot(freq,abs(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.title(fr'IIR 2nd Order Notch Filter (Normalized), r = {r}')
plt.show()

b = np.polymul(b3,b4)
a = np.polymul(a3,a4)
freq, h = signal.freqz(b, a, fs=fs)
plt.figure()
plt.plot(freq,abs(h))
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.title(fr'IIR Cascaded Notch Filters (Normalized), r = {r}')
plt.show()
