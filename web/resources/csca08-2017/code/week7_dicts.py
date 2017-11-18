name_to_age = {'Alice': 35, 'Bob': 42, 'Carol': 21, 'David': 56, 'Ed': 7}
# note that we don't necessarily print in order
print(name_to_age)

# this won't work, because dictionaries aren't ordered
# name_to_age[1]

print("Alice is:", name_to_age['Alice'])
# this won't work, because there is not 'Fred' key
# print("Fred is:", name_to_age['Fred'])

print('Fred' in name_to_age)

# another approach
age = name_to_age.get('Ann')
print(age)
age = name_to_age.get('Fred')
print(age)
# we can specify a 2nd parameter for get, what to return if the first parameter
# isn't in the dictionary
age = name_to_age.get('Fred', -1)
print(age)

# dictionaries are mutable
name_to_age['Carol'] += 1  # Happy Birthday Carol!
print(name_to_age)

# can we get rid of an entry?
name_to_age['Bob'] = None
print(name_to_age)

# we can use the del operator
del name_to_age['Bob']
print(name_to_age)

# loop over keys in a list
for next_name in name_to_age:
    # once again, note that
    # we're not going in any specific order
    print(next_name, " is ", name_to_age[next_name], " years old")

# keys must be immutable types
my_dict = {}
# so this will work
my_dict['x'] = ['a', 'b', 'c']
# but this will crash
# my_dict[['a', 'b', 'c']] = 'x'

# there's a few interesting things we need to consider when making functions
# that mutate parameters, as well as funcitons that use sets/dictionaries
# when the order can't be guaranteed


def add_phone_number(name_to_phone, new_name, new_phone):
    '''(dict, str, str) -> NoneType
    Add a new entry to name_to_phones mapping new_name to new_phone
    over-writing any old mapping that new_name may have had previously

    >>> name_to_phone = {}
    >>> add_phone_number(name_to_phone, 'Alice', '555-1212')
    >>> name_to_phone == {'Alice': '555-1212'}
    True
    >>> name_to_phone = {'Alice': '111-1111', 'Bob': '222-2222'}
    >>> add_phone_number(name_to_phone, 'Carol', '333-3333')
    >>> name_to_phone == {'Alice': '111-1111', 'Bob': '222-2222',\
    'Carol': '333-3333'}
    True
    '''
    # the body of this function is really trivial, it's only here to show
    # how to format examples for dictionaries
    name_to_phone[new_name] = new_phone

if(__name__ == "__main__"):
    import doctest
    doctest.testmod()
