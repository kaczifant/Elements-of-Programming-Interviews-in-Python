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
