'''
Python implementation of bubble sort

From brilliant.org:

Bubble sort is a comparison​-based algorithm that compares each pair of elements in an array and swaps 
them if they are out of order until the entire array is sorted. For each element in the list, the algorithm 
compares every pair of elements.

It's also horribly inefficient, although it is super simple to understand and implement
'''

def bubble_sort(li):
    swapped = True # boolean flag to break out of the loop if more sorting is unnecessary
    while swapped:
        swapped = False
        for i in range(len(li)):
            for j in range(len(li) - 1):
                if li[j] > li[j+1]:
                    li[j],li[j+1] = li[j+1],li[j] # swaps
                    swapped = True


if __name__ == '__main__':
    list = [4,3,2,1]
    bubble_sort(list)
    print(list)