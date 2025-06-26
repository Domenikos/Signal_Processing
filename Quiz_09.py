'''
    Quiz 09
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import linalg
import scipy.fft

X1 = [16,-8.8-2.84j, 0.22+0.18j, -0.5-0.87j, 0.07+0.42j, 0.07-0.42j, -0.5+0.87j, 0.22-0.18j, -8.8+2.84j]
x1 = scipy.fft.ifft(X1)
plt.figure()
n = list(range(len(x1)))
plt.stem(n,np.real(x1))
plt.grid()
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Input Real Value Sequence')
# DFT 
plt.figure(figsize=(6,8))
plt.subplot(211)
k = list(range(len(X1)))
plt.stem(k,np.real(X1))
plt.grid()
plt.ylabel('Re[X(k)]')
plt.title('Real DFT[x(n)]')
plt.subplot(212)
plt.stem(k,np.imag(X1))
plt.grid()
plt.xlabel('k')
plt.ylabel('Im[X(k)]')
plt.title('Imaginary DFT[x(n)]')
plt.tight_layout()
# Convolution
# Circular Convolution
x1 = np.array([-1,1,2])
x2 = np.array([1,-1,-2])
#y = scipy.fft.ifft(scipy.fft.fft(x1) * scipy.fft.fft(x2))
r = linalg.circulant(x1)
y = r @ x2

plt.figure(figsize=(6,9))
n = list(range(len(y)))
plt.subplot(311)
plt.stem(n,x1)
plt.grid()
plt.ylabel(r'$x_1(n)$')
plt.title(r'Circular Convolution, $y(n) = x_1(n) \circ x_2(n)$')
plt.subplot(312)
plt.stem(n,x2)
plt.grid()
plt.ylabel(r'$x_2(n)$')
plt.subplot(313)
plt.stem(n,np.real(y))
plt.grid()
plt.xlabel('n')
plt.ylabel('y(n)')
plt.tight_layout()

# Aperiodic vs Circular Convolution
x1 = np.random.randint(-7,7,size=4)
x2 = np.random.randint(-3,10,size=6)
y_aperiodic = np.convolve(x1,x2)

N = len(x1) + len(x2) - 1
n = list(range(N))
#xE1 = np.pad(x1, (0,N-len(x1)))
#xE2 = np.pad(x2, (0,N-len(x2)))
#y_circ = np.real(scipy.fft.ifft(scipy.fft.fft(xE1) * scipy.fft.fft(xE2)))
y_circ = signal.fftconvolve(x1,x2)      # Equivalent to about statements

plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(x1)
plt.grid()
plt.ylabel(r'$x_1(n)$')
plt.xlabel('n')
plt.title('Sequence for Convolution')
plt.subplot(212)
plt.stem(x2)
plt.grid()
plt.ylabel(r'$x_2(n)$')
plt.xlabel('n')
plt.tight_layout()
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(n,y_aperiodic)
plt.grid()
plt.ylabel('y(n)')
plt.title('Aperiodic Convolution')
plt.subplot(212)
plt.stem(n,y_circ)
plt.grid()
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Circular Convolution, Extended Sequences')
plt.tight_layout()
plt.show()
