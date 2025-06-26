'''
    Homework 12.2
'''
import numpy as np
import matplotlib.pyplot as plt
#from scipy import signal
from scipy.fft import fft

# Problem 12.2 (a)
N = 10
n = np.arange(0,N)
k = n
x_1 = np.pad([1], (0, N-1))
X_1 = fft(x_1)
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(n,x_1)
plt.grid()
plt.xlabel('n')
plt.ylabel(r'$x_1(n)$')
plt.title(rf'$x_1(n) = \delta(n), N = {N}$')
plt.subplot(212)
plt.stem(k,np.real(X_1),label='Real')
plt.stem(k+0.2,np.imag(X_1),linefmt='r-', markerfmt='ro',label='Imaginary')
plt.grid()
plt.legend()
plt.ylabel(r'$X_1(k) = DFT[x_1(n)]$')
plt.xlabel('k')
plt.tight_layout()

# Problem 12.2 (e)
N = 10
k0 = 3
n = np.arange(0,N)
k = n
x_1 = np.cos(2*np.pi*k0*n/N)
X_1 = fft(x_1) / N
x_2 = np.sin(2*np.pi*k0*n/N)
X_2 = fft(x_2) / N
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(n,x_1)
plt.grid()
plt.xlabel('n')
plt.ylabel(r'$x_1(n)$')
plt.title(rf'$x_1(n) = cos(2 \pi k_0 n/N), k_0 = {k0}, N = {N}$')
plt.subplot(212)
plt.stem(k,np.real(X_1),label='Real')
plt.stem(k+0.2,np.imag(X_1),linefmt='r-', markerfmt='ro',label='Imaginary')
plt.grid()
plt.legend()
plt.ylabel(r'$X_1(k) = DFT[x_1(n)]$')
plt.xlabel('k')
plt.tight_layout()
# Problem 12.2 (f)
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(n,x_2)
plt.grid()
plt.xlabel('n')
plt.ylabel(r'$x_2(n)$')
plt.title(rf'$x_2(n) = sin(2 \pi k_0 n/N), k_0 = {k0}, N = {N}$')
plt.subplot(212)
plt.stem(k,np.real(X_2),label='Real')
plt.stem(k+0.2,np.imag(X_2),linefmt='r-', markerfmt='ro',label='Imaginary')
plt.grid()
plt.legend()
plt.ylabel(r'$X_2(k) = DFT[x_2(n)]$')
plt.xlabel('k')
plt.tight_layout()

plt.show()
