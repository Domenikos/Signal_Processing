'''
    Power of Discrete-Time Signals
'''
import numpy as np
import matplotlib.pyplot as plt

def signal_power(x):
    '''
    Power of signal
       Px = (1/N) sum (x^2)
    '''
    return (x @ x)/len(x)

t = np.linspace(0,1,100,endpoint=False)
f0 = 3
A = 4
x = A*np.sin(2*np.pi*f0*t)

plt.plot(t,x)
plt.ylabel('x(t)')
plt.xlabel('t (sec)')
plt.grid(True)
plt.title(fr'Signal power = {signal_power(x)}')
plt.show()
