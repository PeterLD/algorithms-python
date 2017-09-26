"""
Write a function that generates all possible combinations of 1 and 0 for n bits.
For example, if the function receives 2 as the number of bits,
it should produce the following 4 combinations: 00,01,10,11.
You cannot use any mathematical operators.
"""

def generate_binary_strings(n_bits):
    bits = ["0", "1"]
    binary_strings = []

    if n_bits == 0:
        return binary_strings

    if n_bits == 1:
        return bits

    for binary_string in generate_binary_strings(n_bits - 1):
        for bit in bits:
            binary_strings.append(binary_string + bit)

    return binary_strings
