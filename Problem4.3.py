'''
    Problem 4.3 - impulse and step response
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define the system 
num = [1, 0, 0]     # z^2 (numerator)
den = [1, -1, 0.5]  # z^2 - z + 0.5 (denominator)
dt = 1              # Sampling time

# Compute the impulse response
n, h = signal.dimpulse((num, den, dt))

# Plot the impulse response
plt.stem(n, h[0], label ="Impulse Response")
plt.xlabel('n (Time)')
plt.ylabel('Amplitude')
plt.grid()

# Create a discrete-time system representation
#system = signal.dlti(num, den, dt)
sys = signal.TransferFunction(num,den,dt=1)

# Calculate the step response
n, y = signal.dstep(sys)

# Plot the step response
plt.step(n, y[0],'r',where='post',label ="Step Response")
#plt.plot(t,y[0],'r',label ="Step Response")
#plt.stairs(t, y[0],label ="Step Response")
plt.title('Step and Impulse Response')
plt.xlim((0,20))
plt.legend()

# Impulse response from equation
h1 = (np.sqrt(2))**(1-n) * np.cos(np.pi*n/4 - np.pi/4)
plt.figure()
plt.stem(n,h1)
plt.xlabel('n')
plt.ylabel('h(n)')
plt.xlim((0,20))
plt.grid()
plt.title(r'$h(n)=(\sqrt{2})^{(1-n)} cos(\pi n/4 - \pi/4) u(n)$')
plt.show()
