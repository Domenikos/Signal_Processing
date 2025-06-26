#!/usr/bin/env python3
'''
    Partial Fraction Inverse
    Given r, p, and k find A and B
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

#p = [1/2, 1/4]
#r = [-1, 2]
#k = [0]
print("***Inverse Partial Fraction Expansion for the z-transform in Rational Fraction Form***")
print('Enter residuals r array as r_1 r_2 r_3 ...')
r = read_and_process_input()
print('Enter the poles p array as p_1 p_2 p_3 ...')
p = read_and_process_input()
print('Enter the direct terms k array as k_1 k_2 k_3 ...')
k = read_and_process_input()

b,a = signal.invres(r, p, k)
print(fr"residues = {r}")
print(fr"poles = {p}")
print(fr"direct terms = {k}")
print('Inverse Partial Fraction Parameters')
print(fr"a coefficients = {a}")
print(fr"b coefficients = {b}")
