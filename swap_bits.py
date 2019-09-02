# 4.2 SWAP BITS - Implement code that takes as input a 64-bit integer and swaps the bits at indices i and j.

from test_framework import generic_test


def swap_bits(x, i, j):
    i_th = (x & 1 << i) >> i
    j_th = (x & 1 << j) >> j
        
    if i_th != j_th:
        if i_th == 0:
            x = (x | (1 << i)) & ~(1 << j) 
        elif j_th == 0:
            x = (x | (1 << j)) & ~(1 << i)
        return x
    else:
        return x
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
