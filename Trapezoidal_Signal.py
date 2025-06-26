'''
    Trapezoidal Signal Generator
    This script generates a trapezoidal signal with specified parameters and plots it.
    It allows customization of the amplitude, rise time, plateau time, fall time, total time,
    and number of samples.
'''
import numpy as np
import matplotlib.pyplot as plt

def generate_trapezoidal_signal(
    amplitude,
    rise_time,
    plateau_time,
    fall_time,
    total_time,
    num_samples):
    """
    Generates a trapezoidal signal.

    Args:
        amplitude (float): The peak amplitude of the signal.
        rise_time (float): The time taken for the signal to rise from 0 to amplitude.
        plateau_time (float): The duration for which the signal stays at amplitude.
        fall_time (float): The time taken for the signal to fall from amplitude to 0.
        total_time (float): The total duration of the signal.
        num_samples (int): The number of samples in the signal.

    Returns:
        tuple: A tuple containing:
            - t (numpy.ndarray): Time vector.
            - signal (numpy.ndarray): Trapezoidal signal array.
    """

    if not (rise_time + plateau_time + fall_time <= total_time):
        print("Warning: The sum of rise_time, plateau_time, and fall_time exceeds total_time. Adjusting total_time.")
        total_time = rise_time + plateau_time + fall_time

    t = np.linspace(0, total_time, num_samples, endpoint=True)
    signal = np.zeros(num_samples)

    # Calculate segment end times
    t_rise_end = rise_time
    t_plateau_end = t_rise_end + plateau_time
    t_fall_end = t_plateau_end + fall_time

    for i, current_t in enumerate(t):
        if 0 <= current_t < t_rise_end:
            # Rising phase
            signal[i] = amplitude * (current_t / rise_time)
        elif t_rise_end <= current_t < t_plateau_end:
            # Plateau phase
            signal[i] = amplitude
        elif t_plateau_end <= current_t < t_fall_end:
            # Falling phase
            signal[i] = amplitude * (1 - (current_t - t_plateau_end) / fall_time)
        else:
            # Zero phase (before rise or after fall)
            signal[i] = 0

    return t, signal

# --- Example Usage ---
if __name__ == "__main__":
    # Define signal parameters
    amp = 1.0
    t_rise = 0.5
    t_plateau = 1.0
    t_fall = 0.7
    t_total = 3.0
    n_samples = 500

    # Generate the trapezoidal signal
    time, trapezoid_signal = generate_trapezoidal_signal(
        amplitude=amp,
        rise_time=t_rise,
        plateau_time=t_plateau,
        fall_time=t_fall,
        total_time=t_total,
        num_samples=n_samples
    )

    # Plot the signal
    plt.figure(figsize=(10, 6))
    plt.plot(time, trapezoid_signal, label='Trapezoidal Signal', color='blue')
    plt.title('Generated Trapezoidal Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.axvline(x=t_rise, color='r', linestyle='--', label='End of Rise')
    plt.axvline(x=t_rise + t_plateau, color='g', linestyle='--', label='End of Plateau')
    plt.axvline(x=t_rise + t_plateau + t_fall, color='purple', linestyle='--', label='End of Fall')
    plt.legend()
    plt.tight_layout()
    plt.show()
