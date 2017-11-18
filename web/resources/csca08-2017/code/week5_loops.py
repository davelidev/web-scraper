import doctest


def letter_nums(input_str):
    '''(str) -> str

    Returns a string representing the letters of input_str along with the
    index of each letter (starting from 1)

    >>> letter_nums('Hello')
    '1=H2=e3=l4=l5=o'
    >>> letter_nums('Brian')
    '1=B2=r3=i4=a5=n'
    '''

    # complete the function using a while loop (uncomment to use)
    '''
    res = ""
    count = 0
    # keep looping until we've added one item per letter of the input
    while(count < len(input_str)):
        # add the index (which will be 1 greater than the number of times
        # we've looped
        res += str(count +1)
        res += "="
        # add the count-th letter of the input string
        res += input_str[count]
        # we have to increment the count ourselves
        count +=1
    return res
    '''

    # complete the function using an elemental for loop (uncomment to use)
    '''
    res = ""
    index = 0
    # loop once for each letter in the input string
    for next_letter in input_str:
        # add the index (which we will need to keep track of ourselves, since
        # the elemental for loop doesn't let us know where we are in the list)
        res += str(index + 1)
        res += "="
        # add the letter. Note that we don't need to retrieve it, because
        # the elemental for loop takes care of that for us
        res += next_letter
        # we have to keep track of the index ourselves
        index += 1
    return res
    '''

    # complete the function using an indexed for loop
    res = ""
    # loop through the indices of the letters in the input string
    for index in range(0, len(input_str)):
        # add the index, which will be updated for us
        res += str(index + 1)
        res += "="
        # add the letter, since we have the index, it's fairly easy to retrieve
        res += input_str[index]
    return res

if(__name__ == "__main__"):
    # print the output of the doctest, so we know we've passed
    # print(doctest.testmod())
    # or just run doctest, and then we only see output if there's a problem
    doctest.testmod()

    print(letter_nums("Test Sentence"))

    # SOME LOOP PRACTICE
    my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    # ELEMENTAL FOR LOOP: Print the elements of a list
    for element in my_list:
        print(element, end=' ')
    print("All done!")

    # INDEXED FOR LOOP: Print the elements of a list
    for index in range(0, len(my_list)):
        print(my_list[index], end=' ')
    print ("That's all of 'em")

    # WHILE LOOP: prompt a user until they say "Stop"
    response = ""
    while(response != "Stop!"):
        response = input("Type something (say 'Stop!' to exit):")
    print("Have a nice day")

    # A FEW OTHER FUN LOOPS

    # PRINT A LIST BACKWARDS
    # first reverse the list
    my_list.reverse()
    # now just loop through it normally
    for element in my_list:
        print(element, end=' ')
    print("Yup, that's backwards")
    # should probably turn the list back around in case anyone else
    # needs to use it
    my_list.reverse()

    # Here's a much more efficient way (can you see why?)
    # print each element by its index, starting at the end and working towards
    # the front
    for index in range(len(my_list) - 1, -1, -1):
        print(my_list[index], end=' ')
    print("That's backwards too...")

    # print out every other element in the list
    # to print out the alternate elements, we just have to set our skip to be
    # 2 when we're creating our range
    # Try to do this with one of the other types of loops... it's not easy
    for index in range(0, len(my_list), 2):
        print(my_list[index], end=' ')
    print("skipping elements is easy if you use the right type of loop")
