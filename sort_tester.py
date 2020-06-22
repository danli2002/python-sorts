'''
A simple program to time and test various sorting algorithms in Python
'''
import timeit
from . import  *


def test_sort_algorithm(algorithm, array, num_runs):
    setup = f'from __main__ import {algorithm}'
    stmt = f'{algorithm}({array})'

    time = timeit.timeit(setup=setup, stmt=stmt, number=num_runs)
    return time / num_runs

# test_sort_algorithm('insertion_sort')