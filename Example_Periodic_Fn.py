'''
    Example of a Periodic Trigonometric Function
    x(n) = cos(2 pi n k / N)
    x(n) = x(n + N) -- requirement for a periodic discrete-time signal
'''
import numpy as np
import matplotlib.pyplot as plt

def graphit(n,x,yaxis_str,title_it):
    plt.figure()
    plt.stem(n,x)
    plt.xlim(-1,2*N)
    plt.grid()
    plt.xlabel('n')
    plt.ylabel(yaxis_str)
    plt.xticks(np.arange(0,2*N,2))
    plt.title(title_it)

k, N = 1, 10
Fn = k/N            # |Fn| <= 1/2 required
n = np.arange(0,2*N)
#n = np.linspace(0,2*N,2*N,endpoint=False)
w = 2*np.pi*Fn
x = np.cos(w*n)
title_str = f'$x(n) = cos(2\pi\,n\,k/N), k = {k}, N = {N}$'
graphit(n,x,'$x(n)$',title_str)
plt.show()
