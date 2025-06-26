'''
    Homework 08
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Problem 8.2
x = np.array([0,1,2,3])
n = list(range(4))
N = len(x)
Px = (x @ x)/N          # Power of x index domain
plt.stem(n,x)
plt.grid()
plt.xlabel('n')
plt.ylabel(r'$x(n)$')
plt.title(rf'Sequence, Power = {Px}')
# DTFS Magnitude
X = fft(x)
ck = X/N
print(ck)
ck_mag = abs(ck)
Pck = ck_mag @ ck_mag
k = n
plt.figure()
plt.stem(k,ck_mag)
plt.grid()
plt.xlabel('k')
plt.ylabel(r'$|c_k|$')
plt.title(rf'DTFS Magnitude, Power = {Pck}')
# DTFS Phase
theta = np.angle(ck)
plt.figure()
plt.stem(k,theta)
plt.grid()
plt.xlabel('k')
plt.ylabel(r'$|\theta_k|$ (rad)')
plt.title('DTFS Phase')
plt.show()
# Problem 8.3
n = np.arange(0,10)
y = np.cos(3*np.pi*n/5)
plt.figure()
plt.stem(n,y)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid()
plt.title(r'$cos(3 \pi n/5)$')
Y = fft(y)/len(y)
ck = abs(Y)
Pck = ck @ ck
plt.figure()
plt.stem(n,ck)
plt.xlabel('k')
plt.ylabel(r'$|c_k|$')
plt.grid()
plt.title(rf'DTFS Coefficients, Power = {Pck}')
plt.show()
