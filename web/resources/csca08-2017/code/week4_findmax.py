def find_max(num1, num2):
    '''(int, int) -> int
    Return the maximum of {num1, num2}
    REQ: num1 >= 0, num2 >=0

    >>> find_max(10, 12)
    12
    >>> find_max(12, 10)
    12
    '''
    # if A >= B, A + B + (A - B) = 2A
    # if B >= A, A + B + (B - A) = 2B
    # therefore, A + B + |A - B| = 2 * maximum of A and B
    max_times_2 = num1 + num2 + abs(num1 - num2)
    # so now we have a value that is twice the max of num1 and num2
    # all we have to do is divide it in half to get the max value
    result = max_times_2 / 2
    # one funny thing here... we know that since num1 and num2 are
    # integers, the max must be an integer. But since we divided
    # our value by 2, python automatically makes the result a float
    # (it's not smart enough to know it will always be a whole number)
    # so let's cast it back to integer
    result = int(result)
    return result
