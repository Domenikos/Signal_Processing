'''
    Uniform Quantization Demonstration
'''
import numpy as np
import matplotlib.pyplot as plt

def uniform_quantize(signal, num_bits, signal_min, signal_max):
    """
    Performs uniform quantization on a given signal.

    Args:
        signal (np.ndarray): The input analog signal (numpy array).
        num_bits (int): The number of bits for quantization. This determines
                        the number of quantization levels (2^num_bits).
        signal_min (float): The minimum value of the signal's range.
        signal_max (float): The maximum value of the signal's range.

    Returns:
        np.ndarray: The quantized signal.
        np.ndarray: The quantization levels.
    """
    # Calculate the number of quantization levels
    num_levels = 2**num_bits

    # Calculate the step size (quantization step)
    # The range is divided by (num_levels - 1) to account for num_levels discrete steps
    # For example, 2 bits give 4 levels (0, 1, 2, 3), needing 3 steps.
    step_size = (signal_max - signal_min) / (num_levels - 1) if num_levels > 1 else 1

    # Clamp the signal values to the defined range to avoid out-of-range issues
    # during quantization, especially if the signal exceeds signal_min or signal_max.
    clamped_signal = np.clip(signal, signal_min, signal_max)

    # Map the signal values to integer indices from 0 to num_levels - 1
    # This involves shifting the signal so signal_min becomes 0, scaling it
    # by the inverse of the step size, and then rounding to the nearest integer.
    quantized_indices = np.round((clamped_signal - signal_min) / step_size)

    # Convert the integer indices back to the actual quantization levels
    quantized_signal = quantized_indices * step_size + signal_min

    # Generate the actual quantization levels for plotting
    levels = np.linspace(signal_min, signal_max, num_levels)

    return quantized_signal, levels

# --- Main demonstration ---
if __name__ == "__main__":
    # 1. Generate a continuous signal (sine wave)
    time = np.linspace(0, 1.0, 1000)
    analog_signal = 2 * np.sin(2*np.pi*time) + 1 # Sine wave with amplitude 2, shifted up by 1

    # Determine the actual min/max of the analog signal for the quantization range
    # It's good practice to base the quantization range on the actual signal's range
    # or a known desired range. Here, we'll use the signal's min/max.
    signal_min = np.min(analog_signal)
    signal_max = np.max(analog_signal)

    #print(f"Original Signal Range: [{signal_min:.2f}, {signal_max:.2f}]")

    # 2. Define quantization parameters
    num_bits_to_test = [1, 2, 3, 4] # Test with different numbers of bits

    plt.figure(figsize=(12, 8))
    plt.suptitle("Uniform Quantization Demonstration", fontsize=16)

    for i, num_bits in enumerate(num_bits_to_test):
        # 3. Perform uniform quantization
        quantized_signal, quantization_levels = uniform_quantize(
            analog_signal, num_bits, signal_min, signal_max
        )
        num_levels = 2**num_bits
        snr = 6.02 * num_bits + 1.76 # SNR in dB for uniform quantization

        #print(f"\nQuantizing with {num_bits} bits ({num_levels} levels):")
        step_size = (signal_max - signal_min) / (num_levels - 1) if num_levels > 1 else 1
        #print(f"  Number of Levels: {num_levels}")
        #print(f"  Signal Min: {signal_min:.2f}, Signal Max: {signal_max:.2f}")
        #print(f"  Quantization Levels: {quantization_levels}")
        #print(f"  Quantized Signal Range: [{np.min(quantized_signal):.2f}, {np.max(quantized_signal):.2f}]")
        #print(f"  Quantization Step Size: {step_size:.4f}")
        #print(f"  Step Size: {(signal_max - signal_min) / (num_levels - 1) if num_levels > 1 else 'N/A' :.4f}")

        # 4. Visualize the results
        plt.subplot(len(num_bits_to_test), 1, i + 1)
        plt.plot(time, analog_signal, label="Original Analog Signal", color='blue', alpha=0.7)
        plt.step(time, quantized_signal, where='mid', label=f"Quantized Signal ({num_bits} bits)", color='red', linestyle='--')

        # Plot quantization levels as horizontal lines
        for level in quantization_levels:
            plt.axhline(y=level, color='gray', linestyle=':', alpha=0.5, linewidth=0.7)

        plt.title(f'{num_bits} Bits Quantization ({num_levels} Levels), Step Size: {step_size:.4f}, SQNR = {snr:.2f} dB')
        plt.xlabel("Time (sec)")
        plt.ylabel("Amplitude")
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.96]) # Adjust layout to prevent suptitle overlap
    plt.show()

