from test_framework import generic_test


def closest_int_same_bit_count(x):
    for i in range(64):
		if 1 & (x >> i)  != 1 & (x >> (i + 1)):
            y = x ^ ((1 << i) | (1 << (i + 1)))
            return y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
