'''
    DFT Symmetry Property
    Real x(n) => Real X(k) is even, X(k) = X(N-k) 
                 Imaginary X(k) is odd, X(k) = -X(N-k)
    Versions:
        Python 3.12.3
        NumPy  1.26.4
        SciPy  1.11.4
        Matplotlib 3.6.3
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Symmetry Re[x(n)] -> Re[X(k)] is even and Im[X(k)] is odd
x = np.random.randint(-4,4,size=7)
#x = np.array([1, 2, 3, 4])
#x = np.array([0, -1, 2, 1, 1, 2, -1])  # Even sequence
#x = np.array([0, -1, 2, 1, -1, -2, 1])  # Odd sequence
#x = np.array([0, 1, 2, 0, -2, -1])
N = len(x)
n = list(range(N))
# FFT 
X = fft.fft(x)
# Parseval's Theorem, Energy/Power in index domain = energy/power in frequency domain
E_x = x @ x
E_x = np.round(E_x, 3)
E_X = X @ np.conjugate(X) / N
E_X = np.round(E_X, 3)
# Display sequences
plt.figure()
plt.stem(n,x)
plt.grid()
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title(rf'Real Sequence, N = {N}, $E_x$ = {E_x}')
plt.figure(figsize=(6,8))
plt.subplot(211)
plt.stem(n,np.real(X))
plt.axvline(x=N/2,ls='--',color='r')
plt.grid()
plt.ylabel('Re[X(k)]')
plt.title(rf'X(k) Real Values are Even, X(k) = X(N-k), $E_X$ = {E_X}')
plt.subplot(212)
plt.stem(n,np.imag(X))
plt.axvline(x=N/2,ls='--',color='r')
plt.grid()
plt.xlabel('k')
plt.ylabel('Im[X(k)]')
plt.title('X(k) Imaginary Values are Odd, X(k) = -X(N-k)')
plt.show()
