# 5.1 THE DUTCH NATIONAL FLAG PROBLEM
# Write a program that takes an array A and an index i into A, and rearranges the elements such
# that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot,
# followed by elements greater than the pivot.

import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    for i in range(len(A)):
        if A[i] >= pivot:
            j = i + 1
            swap = False
            while not swap and j < len(A):
                if A[j] < pivot:
                    A[i], A[j] = A[j], A[i]
                    swap = True
                else:
                    j += 1
            
            if swap == False:
                k = i + 1
                while not swap and k < len(A):
                    if A[i] > pivot and A[k] == pivot:
                        A[i], A[k] = A[k], A[i]
                        swap = True
                    else:
                        k += 1
                    
    return A

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
