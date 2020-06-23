'''
A simple program to time and test various sorting algorithms in Python
'''
import timeit
import random


def test_sort_algorithm(algorithm):
    """ Ensure that the provided algorithm correctly sorts arrays """
    arr = [random.randint(1, 1000) for _ in range(1000)]
    setup = f'from {algorithm} import {algorithm}'
    stmt = f'global sorted_arr; sorted_arr = {algorithm}({arr})'
    exec(setup)
    exec(stmt)
    return sorted(arr) == sorted_arr


def time_sort_algorithm(algorithm, array, num_runs):
    setup = f'from {algorithm} import {algorithm}'
    stmt = f'{algorithm}({array})'
    time = timeit.timeit(setup=setup, stmt=stmt, number=num_runs)
    return time / num_runs


if __name__ == '__main__':
    arr = [random.randint(1, 1000) for _ in range(1000)]
    print(test_sort_algorithm('insertion_sort'))
    num_runs = 1000
    time = time_sort_algorithm('insertion_sort', arr, num_runs)
    print(f'Time for one run: {time}')