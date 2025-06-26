#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 06 20:37 2024
Karplus-Strong string synthesis simulates the hammered or plucked string

@author: cgreco
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

M = 10
N = 10000
a = 0.8
Fs = 100
mu = 0
sigma = 1.0

x = np.random.normal(mu, sigma, size=N)

y = np.empty(N)
'''
for i in range(0,N):
    if i >= M:
        y[i] = a*y[i-M] + x[i]
    else:
        y[i] = x[i]
'''
bcoef = np.array([1-a])
acoef = np.zeros(M+1)
acoef[0] = 1.0
acoef[M] = -a

# yi = signal.lfilter_zi(bcoef, acoef)
# y, _ = signal.lfilter(bcoef, acoef, x, zi = yi*x[0])
y = signal.lfilter(bcoef, acoef, x)
f, Pxx = signal.welch(x, Fs, window = 'hann', nperseg=250, nfft = 1024, scaling = 'density')
f, Pyy = signal.welch(y, Fs, window = 'hann', nperseg=250, nfft = 1024, scaling = 'density')

plt.plot(f, 10*np.log10(Pxx), label = 'S_x')
plt.plot(f, 10*np.log10(Pyy), linewidth = 2, label = 'S_y')
plt.xlabel('f (Hz)')
plt.ylabel('Magnitude (dB)')
plt.legend()
plt.title(f'Karpus-Strong, M = {M}, a = {a}')
plt.grid()
plt.show()
