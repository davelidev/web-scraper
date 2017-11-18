import math


# DESIGN RECIPE EXAMPLES
def get_radius(area):
    '''(float) -> float
    Returns the radius of a circle given its area
    REQ: area >= 0

    >>> get_radius(100)
    5.641895835477563
    >>> get_radius(0)
    0.0
    '''
    #area = pi * r^2, so re-arrange
    #r^2 = area/pi. r = square root of area/pi
    #so first calcualte area/pi
    r_squared = area/math.pi
    #then use math's built in square root calculator to find
    #the radius
    radius = math.sqrt(r_squared)
    return radius


def get_area(radius):
    '''(float) -> float
    Return the area of a circle given its radius
    REQ: radius >= 0

    >>> get_area(10)
    314.1592653589793
    >>> get_area(0)
    0.0
    '''
    #calculate a value for pi
    pi = math.pi
    #square the radius
    r_squared = radius * radius
    #calculate the area (area = pi * r^2)
    area = pi * r_squared
    return area


def can_i_drive(age, have_license):
    '''(int, bool) -> bool
    Return True iff age is greater than or equal to 16 (the age that
    people are allowed to drive in Canada), and have_license (whether
    or not the person has a driving license) is True.
    REQ: age >=0

    >>> can_i_drive(5, False)
    False
    >>> can_i_drive(55, True)
    True
    '''
    return (age >= 16) and (have_license)

