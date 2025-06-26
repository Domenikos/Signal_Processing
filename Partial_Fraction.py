#!/usr/bin/env python3
'''
    Partial Fraction Expansion of a Rational Fraction of Polynominals
'''
from scipy import signal
def read_and_process_input():
    """Reads an input array of numbers in the format "3/4" or "-2.3" and processes them.

    Returns:
        A list of processed numbers.
    """

    input_array = input("Enter the array of numbers (separated by spaces): ")
    numbers = input_array.split()

    processed_numbers = []
    for number in numbers:
        try:
            if '/' in number:
                numerator, denominator = map(int, number.split('/'))
                processed_number = numerator / denominator
            else:
                processed_number = float(number)
        except (ValueError, ZeroDivisionError):
            print(f"Invalid number format: {number}")
        else:
            processed_numbers.append(processed_number)
        

    return processed_numbers

print("***Partial Fraction Expansion for the z-transform in Rational Fraction Form***")
print('Enter denominator a array as a_0 a_1 a_2')
a = read_and_process_input()
print('Enter numerator b array as b_0 b_1 b_2')
b = read_and_process_input()
r, p, k = signal.residuez(b,a)
print(fr"a coefficients = {a}")
print(fr"b coefficients = {b}")
print('Partial Fraction Parameters')
print(fr"residues = {r}")
print(fr"poles = {p}")
print(fr"direct terms = {k}")
