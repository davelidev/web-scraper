# function to determine whether
# a given string is a palindrome.
def is_palindrome(s):
    ''' (str) -> bool

    Return True iff s is a palindrome.

    >>> is_palindrome("")
    >>> True
    >>> is_palindrome("radar")
    >>> True
    >>> is_palindrome("nick")
    >>> False
    '''

    # strings of length 1 or less are palindromes
    if len(s) <= 1:
        result = True

    else:
        # check first and last symbol, and rest of string
        result = (s[0] == s[-1]) and is_palindrome(s[1:-1])

    return result


# function to determine whether
# a given string is a near palindrome.
# Uses is_palindrome.
def is_near_palindrome1(s):
    ''' (str) -> bool

    Return True iff s is a near palindrome.

    >>> is_near_palindrome1("radar")
    >>> True
    >>> is_near_palindrome1("naval")
    >>> True
    >>> is_near_palindrome1("nick")
    >>> False
    '''

    # if s is empty
    if not s:
        result = True

    # if first and last symbol are equal
    elif s[0] == s[-1]:
        # check if rest of string is a near palindrome
        result = is_near_palindrome1(s[1:-1])

    # else first and last symbol are different
    else:
        # check if rest of string is a palindrome
        result = is_palindrome(s[1:-1])

    return result


# Solution using a helper function.
def is_palindrome_helper(s, d):
    ''' (str, int) -> bool

    Return True iff s is within d changes of
     being a palindrome.
    REQ: d >= 0.

    >>> is_palindrome_helper("radar", 0)
    >>> True
    >>> is_palindrome_helper("naval", 1)
    >>> True
    >>> is_palindrome_helper("palindrome", 4)
    >>> False
    >>> is_palindrome_helper("palindrome", 5)
    >>> True
    '''

    # if s is empty
    if not s:
        result = True

    # first and last symbol are equal
    elif s[0] == s[-1]:
        # check rest of string
        result = is_palindrome_helper(s[1:-1], d)

    # if first and last symbol are different and
    # distance is positive
    elif d > 0:
        # check rest of string for distance minus 1
        result = is_palindrome_helper(s[1:-1], d-1)

    else:
        result = False

    return result


# Uses above helper function.
def is_near_palindrome2(s):
    ''' (str) -> bool

    Return True iff s is a near palindrome.

    >>> is_near_palindrome2("radar")
    >>> True
    >>> is_near_palindrome2("naval")
    >>> True
    >>> is_near_palindrome2("nick")
    >>> False
    '''

    return is_palindrome_helper(s, 1)


# Uses python's default argument values to
# add helper without separate function.
def is_near_palindrome3(s, d=1):
    ''' (str, int) -> bool

    Return True iff s is within d changes of
     being a palindrome.
    REQ: d >= 0.

    >>> is_near_palindrome3("naval", 1)
    >>> True
    >>> is_near_palindrome3("naval")
    >>> True
    >>> is_near_palindrome3("palindrome", 4)
    >>> False
    >>> is_near_palindrome3("palindrome", 5)
    >>> True
    '''

    # if s is empty
    if not s:
        result = True

    elif s[0] == s[-1]:
        result = is_near_palindrome3(s[1:-1], d)

    elif d > 0:
        result = is_near_palindrome3(s[1:-1], d-1)

    else:
        result = False

    return result
