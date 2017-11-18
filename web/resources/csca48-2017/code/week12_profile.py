import random
import time
from week12_sort import *

def time_func(func,data):
    '''(function,list of number) -> number

    Return the time taken to run func with data as its parameter

    '''
    start = time.time()
    func(data)
    end = time.time()
    return end-start

def print_times(func_list,data):
    '''(list of function, list of number) -> NoneType

    Print the time taken to run each function in func_list on data

    '''
    for func in func_list:
        print((func.__name__).ljust(15),":",time_func(func,data))


def create_random_list(list_length):
    '''(int) -> list of number

    Return a list of list_length random numbers between (0,100)
    rounded to 2 significant digits

    '''
    result = []
    for count in range(0,list_length):
        result.append(round(random.random() * 100,2))
    return result


if(__name__ == '__main__'):
    func_list = [insertion_sort, selection_sort, quick_sort, merge_sort, builtin_sort]
    print("-- Small data")
    data = create_random_list(100)
    print_times(func_list,data)
    print("-- Medium data")
    data = create_random_list(1000)
    print_times(func_list,data)
    print("-- Large data")
    data = create_random_list(10000)
    print_times(func_list,data)



