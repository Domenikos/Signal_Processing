'''
    Periodic Trigonometric Discrete-Time Signals 
    in index/time and frequency domains
    x(n) = cos(2 pi n k / N)  where k/N is a rational fraction
'''
import numpy as np
from numpy.fft import fft, fftshift, fftfreq
import matplotlib.pyplot as plt

def graphit(x,yaxis_str,title_it):
    '''Display a discrete-time signal'''
    n = np.arange(0,len(x))
    plt.figure()
    plt.stem(n,x)
    plt.xlim(-1,2*N)
    plt.grid()
    plt.xlabel('$n$')
    plt.ylabel(yaxis_str)
    plt.xticks(np.arange(0,2*N,2))
    plt.title(title_it)

def graphfreqmag(y,yaxis_str,title_str):
    '''Display the magnitude of the frequency content of a discrete-time signal'''
    Y = fftshift(fft(y))/len(y)
    F = fftshift(fftfreq(len(Y)))
    plt.figure()
    plt.stem(F,abs(Y))
    plt.grid()
    plt.xlabel('$F = k/N$')
    plt.ylabel(yaxis_str)
    plt.title(title_str)

k1, N = 3, 10
Fn = k1/N            # |Fn| <= 1/2 required
n = np.arange(0,2*N)
w = 2*np.pi*Fn
x1 = np.cos(w*n)
title_str = f'$x_1(n) = cos(2\pi\,n\,k/N), k_1 = {k1}, N = {N}$'
graphit(x1,'$x_1(n)$',title_str)

# Frequency Distribution
yaxis_str = '$|X_1(F)|$'
title_str = 'Frequency Content'
graphfreqmag(x1,yaxis_str,title_str)


# Sum of two periodic signals
k2 = 1
Fn1 = k2/N
w1 = 2*np.pi*Fn1
x2 = 2*np.cos(w1*n)
y = x2+x1
title_str = f'$y(n) = cos(2\pi\,n\,k1/N) + 2cos(2\pi\,n\,k2/N), k_1 = {k1}, k_2 = {k2}, N = {N}$'
graphit(y,'$y(n)$',title_str)

# Frequency Distribution
yaxis_str = '$|Y(F)|$'
title_str = 'Frequency Content Sum of Periodic Signals'
graphfreqmag(y,yaxis_str,title_str)

# Modulation
y = x2*x1
# Frequency Distribution
yaxis_str = '$|Y(F)|$'
title_str = f'$Modulation\, Frequency\, Response, k_1 = {k1},\, k_2 = {k2}$'
graphfreqmag(y,yaxis_str,title_str)

plt.show()