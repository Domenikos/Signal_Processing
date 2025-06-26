'''
This script defines a function to plot the pole-zero map of a discrete-time system given
its transfer function coefficients. 
It uses the `scipy.signal.tf2zpk` function to convert the transfer function coefficients
into zeros, poles, and gain, and then plots these on a complex plane.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

def plot_pole_zero(b, a):
    """
    Plots the pole-zero map for a given z-transform transfer function.

    Args:
        b (array_like): Numerator (feedforward) coefficients of the transfer function.
        a (array_like): Denominator (feedback) coefficients of the transfer function.
        Numerator and denominator should be in terms of positive powers of z.
    """
    zeros, poles, gain = tf2zpk(b, a)

    plt.figure()
    plt.plot(poles.real, poles.imag, 'x', markersize=10, label='Poles')
    plt.plot(zeros.real, zeros.imag, 'o', markersize=10, label='Zeros')

    # Plot the unit circle
    theta = np.linspace(0, 2 * np.pi, 100)
    plt.plot(np.cos(theta), np.sin(theta), 'k--', label='Unit Circle')

    plt.xlabel('Real Part', fontsize=12)
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    plt.ylabel('Imaginary Part', fontsize=12)
    plt.title('Pole-Zero Map of z-Transform', fontsize=14)
    plt.grid(True)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axis('equal') # Ensure equal scaling for x and y axes
    plt.legend()
    plt.show()

# Example Usage:
# Define coefficients for a system with H(z) = (1 - 0.5z^-1) / (1 - 0.8z^-1 + 0.6z^-2)
# In terms of positive powers of z: H(z) = (z^2 - 0.5z + 0) / (z^2 - 0.8z + 0.6)
# So, numerator b = [1, -0.5, 0] and denominator a = [1, -0.8, 0.6]
b_coeffs = np.array([1, -0.5, 0])
a_coeffs = np.array([1, -0.8, 0.6])

plot_pole_zero(b_coeffs, a_coeffs)
