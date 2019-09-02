# 4.3 REVERSE BITS - Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned integer consisting
# of the bits of the input in reverse order. For example, if the input is (1110000000000001), 
# the output should be (1000000000000111).

from test_framework import generic_test


def reverse_bits(x):
    y = 0
    for i in range(0,64):
        y |= ((x >> i) & 1) << 63 - i
    return y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
