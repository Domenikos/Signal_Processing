'''
    Example periodic cos sequences
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-16,16)
N = 8
w0 = np.pi/N
y = np.cos(w0 * n)
plt.stem(n,y)
plt.grid()
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title(f'cos(($\pi$/{N}) n)')

# Double the frequency
N = 4
w0 = np.pi/N
y = np.cos(w0 * n)
plt.figure()
plt.stem(n,y)
plt.grid()
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title(f'cos(($\pi$/{N}) n)')
plt.show()
