import random
import time
# What size sets/arrays are we going to test?
SIZES_TO_CHECK = (10, 100, 1000, 10000, 100000, 1000000)
# How many times will we check?
TIMES_TO_CHECK = 1000


def time_func(func, data):
    '''(function,list of float) -> float

    Return the time taken to run func with data as its parameter

    '''
    start = time.time()
    func(data)
    end = time.time()
    return end-start


def check_membership(my_container):
    '''(list or set) -> NoneType

    Generate NUM_ELEMENTS random values, and check their membership in
    my_container
    '''
    for i in range(TIMES_TO_CHECK):
        rand_val = random.random()
        useless_bool = rand_val in my_container

# run the loop once for each size of list/set
for sample_size in SIZES_TO_CHECK:
    # create a list and a set that will hold lots of random values
    big_list = []
    big_set = set()

    # fill both the list and the set with random values
    for count in range(sample_size):
        rand_val = random.random()
        big_list.append(rand_val)
        big_set.add(rand_val)

    # use the time_func function to see how long check_membership
    # takes for each of the containers
    list_time = time_func(check_membership, big_list)
    set_time = time_func(check_membership, big_set)

    print(len(big_list), len(big_set))
    print(list_time, set_time)
