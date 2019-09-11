# 6.1 INTERCONVERT STRINGS AND INTEGERS
# Implement an integer to string conversion function, and a string to integer conversison function.
# Your code should handle negative integers. You cannot use library functions like int in Python.

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    minus = False
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    string = ''
    if x < 0:
        minus = True
        x = x * -1
    if x == 0:
        return '0'
    else:
        while x != 0:
            mod_10 = x % 10
            x = (x - mod_10)//10
            string += chars[mod_10]
    if minus:
        return '-' + string[::-1]
    return string[::-1]


def string_to_int(s):
    num = 0
    num_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    if '-' in s:
        tens = len(s) - 2
        for char in s:
            if char in num_dict:
                num += num_dict[char] * (10 ** tens)
                tens -= 1
        return num * -1
    else:
        tens = len(s) - 1
        for char in s:
            if char in num_dict:
                num += num_dict[char] * (10 ** tens)
                tens -= 1
        return num


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
