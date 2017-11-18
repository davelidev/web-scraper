def mutator(input_list):
    '''(list) -> NoneType

    Change the first element in input_list into "X"
    REQ: len(input_list) > 0

    >>> test_list = [1, 2, 3]
    >>> mutator(test_list)
    >>> test_list == ["X", 2, 3]
    True
    '''
    # for advanced tracing version, replace with
    # input_list[0][0] = "X"
    input_list[0] = "X"


def cloner(input_list):
    '''(list) -> list

    Return a copy of input_list, but the first element set to "X"
    REQ: len(input_list) > 0

    >>> cloner([1, 2, 3])
    ['X', 2, 3]
    '''
    clone_list = input_list[:]
    # for advanced tracing version, replace with
    # clone_list[0][0] = "X"
    clone_list[0] = "X"
    return clone_list

my_list = [1, 2, 3, 4, 5]
alias_list = my_list
clone_list = my_list[:]

# at first, all of these seem to be the same
print(my_list)
print(alias_list)
print(clone_list)

# but what happens when we change the original list?
my_list[0] = 99

print(my_list)
print(alias_list)
print(clone_list)

# but be careful. Cloning only makes a SHALLOW copy

my_list = [1, [2, 3]]
alias_list = my_list
clone_list = my_list[:]

my_list[1][1] = 99

print(my_list)
print(alias_list)
print(clone_list)

x = [1, 2, 3]
y = mutator(x)
print(x, y)
x = [1, 2, 3]
y = cloner(x)
print(x, y)

# Advanced version
x = [[1, 2], 3]
y = mutator(x)
print(x, y)
x = [[1, 2], 3]
y = cloner(x)
print(x, y)
