#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:33:35 2021

https://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.signal.TransferFunction.bode.html

@author: cgreco
"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

zeta = 0.05
s1 = signal.lti([100], [1, 20*zeta, 100])
w = np.logspace(-1,3)
w, mag, phase = s1.bode(w, n=100)

plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.grid()
plt.xlabel('$\omega$ (rad/sec)')
plt.ylabel('|H($\omega$)| (dB)')
plt.title('Magnitude Response')
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.grid()
plt.xlabel('$\omega$ (rad/sec)')
plt.ylabel('$\phi(\omega)$ (deg)')
plt.title('Phase Response')
plt.show()
