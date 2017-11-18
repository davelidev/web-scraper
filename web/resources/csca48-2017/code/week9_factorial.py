def factorial(n):
    '''(int) -> int

    Return n! = n * (n-1) * (n-2) * .... 3 * 2 * 1

    REQ: n >= 0

    >>> factorial(0)
    1
    >>> factorial(10)
    3628800
    '''

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
