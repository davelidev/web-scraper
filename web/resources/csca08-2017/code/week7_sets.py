x = {1, 2, 3}
print(x)
x = {1, 2, 1, 2, 3, 1, 3, 2, 1, 3, 2}
print(x)
x.add(3)
print(x)
x.add(4)
print(x)
x = {1, 2, 4, 3, 5, 6, 3, 1}
y = {3, 5, 1, 6, 2}
print(x.issubset(y))
print(x <= y)
print(y.issubset(x))
print(y.issubset(x))
x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(y.difference(x))

# x.add([1, 2, 3]) <-- can't do this (because lists are mutable)

print("---")
for element in x:
    print(element)

print("---")
for index in range(0, 8):
    print(index in x)


def unique_elements(input_list):
    '''(list) -> int

    Return the number of unique elements in input_list

    >>> unique_elements(['A', 'B', 1, 'B', 1, 'A', 1.0])
    3
    '''
    # an easier way to do it:
    # set_list = set(input_list)
    # return len(set_list)

    # this is a funny thing we have to do to create a new set (we'll see
    # why once we have dictionaries)
    elements_set = set()
    unique_count = 0
    # check each elmement in the list
    for next_element in input_list:
        # if we've found a new element, add it to our set of elements
        # and increase our unique elements counter
        if (not (next_element in elements_set)):
            elements_set.add(next_element)
            unique_count += 1
    return unique_count
