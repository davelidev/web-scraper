def calc(op1, op2, oper):
    '''
    (obj, obj, obj) -> obj
    Simulates a calculator by geting two numbers and one operation

    >>> calc(10, 20, "+")
    30
    >>> calc(10, 20, "&")
    'Wrong Operator'
    >>> calc(10, "a", "+")
    'Wrong Input'
    '''

    # Check for the correctness of the type
    op1_type = (type(op1) is float) or (type(op1) is int)    op2_type = (type(op2) is float) or (type(op2) is int)
    oper_type = (type(oper) is str)
    # apply the given operator to the given operands
    if (not(op1_type and op2_type and oper_type)):
        result = "wrong input type"
    elif oper == '+':
        result = op1 + op2
    elif oper == '-':
        result = op1 - op2
    elif oper == '*':
        result = op1 * op2
    elif oper == '/':
        result = op1 / op2
    elif oper == '//':
        result = op1 // op2
    elif oper == '**':
        result = op1 ** op2
    elif oper == '%':
        result = op1 % op2
    else:
        result = "Wrong Operator"

    return result
