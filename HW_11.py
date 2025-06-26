'''
    Homework 11
'''
import numpy as np
import matplotlib.pyplot as plt
#from scipy import signal
import scipy.fft

# 
x = [0,1,2,3,-1,-1,-1,-1]
X = scipy.fft.fft(x)
plt.figure()
n = list(range(len(x)))
plt.stem(n,x)
plt.grid()
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Index Domain Sequence')
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(n,np.real(X))
plt.grid()
plt.ylabel('Re[X(k)]')
plt.title('Real DFT')
plt.subplot(212)
plt.stem(n,np.imag(X))
plt.grid()
plt.xlabel('k')
plt.ylabel('Im[X(k)]')
plt.title('Imaginary DFT(x)')

# 11.2 DFT[cos] and DFT[sin]
N = 8
k0 = 3
n = np.array(list(range(N)))
x = np.cos(2*np.pi*k0*n/N)
X = scipy.fft.fft(x)
plt.figure()
plt.stem(n,x)
plt.grid()
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Index Domain Sequence')
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(n,np.real(X))
plt.grid()
plt.ylabel('Re[X(k)]')
plt.title('Real DFT')
plt.subplot(212)
plt.stem(n,np.imag(X))
plt.grid()
plt.xlabel('k')
plt.ylabel('Im[X(k)]')
plt.title('Imaginary DFT(x)')
#
x = np.sin(2*np.pi*k0*n/N)
X = scipy.fft.fft(x)
plt.figure()
plt.stem(n,x)
plt.grid()
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Index Domain Sequence')
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(n,np.real(X))
plt.grid()
plt.ylabel('Re[X(k)]')
plt.title('Real DFT')
plt.subplot(212)
plt.stem(n,np.imag(X))
plt.grid()
plt.xlabel('k')
plt.ylabel('Im[X(k)]')
plt.title('Imaginary DFT(x)')

plt.show()

# Convolution
# Aperiodic Convolution
x1 = np.array([1, -2, -1, 2])
x2 = np.array([4, 3, 2, 1])

y = np.convolve(x1, x2)
n = list(range(len(y)))
plt.figure()
plt.stem(n,y)
plt.grid()
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title(r'Aperiodic Convolution, $y(n) = x_1(n) * x_2(n)$')
# Circular Convolution
#x1 = np.array([1, -2, -1, 2, 0, 0, 0])
#x2 = np.array([4, 3, 2, 1, 0, 0, 0])

Y = scipy.fft.fft(x1) * scipy.fft.fft(x2)
y = scipy.fft.ifft(Y)
y = np.real(y)
n = list(range(len(x1)))
plt.figure(figsize=(6,8))
plt.subplot(311)
plt.stem(n,x1)
plt.grid()
plt.title(r'Circular Convolution, $y(n) = x_1(n) \circ x_2(n)$')
#plt.xlabel('n')
plt.ylabel('$x_1(n)$')
plt.subplot(312)
plt.stem(n,x2)
plt.grid()
#plt.xlabel('n')
plt.ylabel('$x_2(n)$')
plt.subplot(313)
plt.stem(n,y)
plt.grid()
plt.xlabel('n')
plt.ylabel('y(n)')

plt.show()
