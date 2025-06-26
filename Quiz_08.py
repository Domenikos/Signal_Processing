'''
    Quiz 08
    Versions:
        Python 3.12.3
        NumPy  1.26.4
        SciPy  1.11.4
        Matplotlib 3.6.3
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 2
# First Order Differeniator y(n) = x(n) - x(n-1)
a = 1
b =[1, -1]
freq, h = signal.freqz(b, a, fs=fs)
plt.plot(freq,abs(h),label='Approximate')
y = (1.175/0.4)*freq
plt.plot(freq,y,label='Ideal')
plt.ylim(-0.05,2.05)
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.legend()
plt.title('First Order Differentiator Filter, h(n) =(x(n) - x(n-1))')
# Second Order Differentiator y(n) = x(n) - x(n-2)
plt.figure()
a = 1
b =[1, 0, -1]
freq, h = signal.freqz(b, a, fs=fs)
plt.plot(freq,abs(h),label='Approximate')
y = (1.186/0.2)*freq
plt.plot(freq,y,label='Ideal')
plt.ylim(-0.05,2.05)
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.legend()
plt.title('Second Order Differentiator Filter, h(n) =(x(n) - x(n-2))')
# Second Order Differentiator with pole at -0.75; y(n) = -0.75y(n-1) + x(n) - x(n-2)
plt.figure()
a1 = 0.75
a = [1, a1]
b =[1, 0, -1]
freq, h = signal.freqz(b, a, fs=fs)
plt.plot(freq,abs(h),label='Approximate')
y = (1.34/0.4)*freq
plt.plot(freq,y,label='Ideal')
plt.ylim(-0.05,2.05)
plt.grid()
plt.xlabel('frequency')
plt.ylabel('|H(f)|')
plt.legend()
plt.title(r'$2^{nd}\ order\ with\ pole, H(z) = (1 - z^{-2})/(1 +$'+rf'{a1}'+r'$ z^{-1})$')
plt.show()
