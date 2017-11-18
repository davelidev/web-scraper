x = (1, 2, 3, 4, 5)
print(type(x))
print(x)
print(x[0])
# x[0] = 1 <-- this would cause an error

brian = ("Brian", "Harrington", "brian.harrington@utsc.utoronto.ca", 1234)
nick = ("Nick", "Cheng", "nick@utsc.utoronto.ca", 1)
(first_name, last_name, e_mail, id_num) = brian
print(first_name, last_name, e_mail, id_num)
(first_name, last_name, e_mail, id_num) = nick
print(first_name, last_name, e_mail, id_num)

# great for swapping variables around:

# old way
x = "X"
y = "Y"
temp = x
x = y
y = temp
print("x = ", x, "y = ", y)

# with tuples
x = "X"
y = "Y"
(x, y) = (y, x)
print("x = ", x, "y = ", y)

# also great for returning more than one thing from a function


def uppers_lowers(input_str):
    '''(str) -> (str, str)

    Return a tuple where the first element is all of the upper case letters
    in input_str and the second is all of the lower case letters.

    >>> uppers_lowers("HeLLo mY NAME is Brian")
    ('HLLYNAMEB', 'eomisrian')
    '''

    uppers = ""
    lowers = ""
    # loop over each letter in the input string
    for next_letter in input_str:
        # if the char is an upper case letter, add it to the upper string
        if(next_letter.isupper()):
            uppers += next_letter
        # if the char is a lower case letter, add it to the lower string
        elif(next_letter.islower()):
            lowers += next_letter
        # if the character is anything else, just ignore it
    return (uppers, lowers)
