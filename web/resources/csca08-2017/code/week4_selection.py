def grade_message(percent):
    '''(float) -> str

    Given a percent grade for a course, return an appropriate message with the
    following logic:
    0-40: You failed
    40-50: Almost
    50-60: You passed, but just barely
    60-85: You passed
    85-100: Excellent

    Numbers on the boundary always receive the message from the higher tier.
    If percent is not a valid percentage mark, return "Not a valid mark"

    # NOTE: Since we added the 'not a valid mark' comment, we don't actually
    # need any REQ statements, any integer will work just fine

    >>> grade_message(0)
    'You failed'
    >>> grade_message(100)
    'Excellent'
    >>> grade_message(105)
    'Not a valid mark'
    >>> grade_message(-3)
    'Not a valid mark'
    '''

    if(percent > 100):
        result = "Not a valid mark"
    elif(percent >= 85):
        result = "Excellent"
    elif(percent >= 60):
        result = "You passed"
    elif(percent >= 50):
        result = "You passed, but just barely"
    elif(percent >= 40):
        result = "Almost"
    elif(percent >= 0):
        result = "You failed"
    else:
        result = "Not a valid mark"

    return result

# here is a complete different approach, but there's a problem with it
# run doctest to see which cases fail, and then use the debugger to
# fix the problem


def grade_message2(percent):
    '''(float) -> str

    Given a percent grade for a course, return an appropriate message with the
    following logic:
    0-40: You failed
    40-50: Almost
    50-60: You passed, but just barely
    60-85: You passed
    85-100: Excellent

    Numbers on the boundary always receive the message from the higher tier.
    If percent is not a valid percentage mark, return "Not a valid mark"

    # NOTE: Since we added the 'not a valid mark' comment, we don't actually
    # need any REQ statements, any integer will work just fine

    >>> grade_message(0)
    'You failed'
    >>> grade_message(100)
    'Excellent'
    >>> grade_message(105)
    'Not a valid mark'
    >>> grade_message(-3)
    'Not a valid mark'
    '''

    # deal with invalid input
    if(percent > 100 or percent < 0):
        result = "Not a valid mark"
    else:
        # deal with the passing cases
        if(percent >= 50):
            # deal with excellent marks
            if(percent >= 85):
                result = "Excellent"
            # deal with barely passing marks
            if(percent < 60):
                result = "You passed, but just barely"
            # everyone else gets a generic message
            else:
                result = "You passed"

        # deal with the failing cases
        else:
            # deal with the almost passing cases
            if(percent >= 40):
                result = "Almost"
            # anyone else just gets a generic failure message
            else:
                result = "You failed"

    return result
