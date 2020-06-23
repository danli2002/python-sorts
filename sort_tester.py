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
    algorithms = ['insertion_sort', 'selection_sort']
    for algorithm in algorithms:
        arr = [random.randint(1, 1000) for _ in range(1000)]
        num_runs = 10
        time = time_sort_algorithm(algorithm, arr, num_runs)
        print(f'One run using {algorithm}: {time:.5f}s')