'''
    Pole-Zero Plot Discrete Time System
'''
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def pole_zero_plot(b,a):
    ''' Create a discrete-time pole-zero plot 
        b - coefficients for the positive exponent z polynominal of the numerator
        a - coefficients for the positive exponent z polynominal of the denominator
    '''
    z, p, k = signal.tf2zpk(b, a)
    # Plot the pole-zero map
    plt.figure(figsize=(6,6))   # make it a circle
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Zeros')
    plt.scatter(np.real(p), np.imag(p), marker='x', linewidth=2, s=45, label='Poles')
    plt.legend()
    plt.grid()
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title('Discrete-Time Pole-Zero Plot')
    # Add unit circle
    circle = plt.Circle((0, 0), 1, color='red', fill=False)
    plt.gca().add_patch(circle)
    plt.show()

#b = [1, 0.5]  # Numerator coefficients
#a = [1, -0.8]  # Denominator coefficients
b = [1, 0, 0, 0, 0, 0, 0, 0, 1]  # Numerator coefficients
a = [1, 2/3, 0, 0, 0, 0, 0, 0, 0]  # Denominator coefficients
#b = [1, 0, 0]
#a = [1, 1/6, -1/3]
pole_zero_plot(b,a)
