def is_leap_year(year):
    ''' (int) -> bool
    Return True iff the year is a leap year.
    Leap years are years with 366 days, which occur once every 4 years
    (starting with year 4). Years that are divisible by 100 are not
    leap years, except if they are divisible by 400.
    REQ: 0 < year < 10000

    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2016)
    True
    >>> is_leap_year(2017)
    False
    '''

    # to be a leap year, the year must be divisible by 4
    isLeapYear = (year % 4 == 0)
    # but it can't be divisible by 100
    isLeapYear = isLeapYear and (year % 100 != 0)
    # but we make a special exception for years that are divisible
    # by 400
    isLeapYear = isLeapYear or (year % 400 == 0)

    return isLeapYear


year = int(input("input a year: "))
print("Is Year", year, "a leap year?", is_leap_year(year))
