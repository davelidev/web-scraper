# this question is about the immutability of global variables.
# your job is to get this program working by using memory model.


def readMark():
    '''(None) -> flaot
    This function returns a float representing a mark
    REQ : 0<= mark <=100
    >>> readMark()
    100
    >>> readMark()
    50

    '''    
    # read the mark    
    mark = float(input("please enter a mark:"))
    return mark


def readWeight():
    '''(None) -> int
    This function returns an int representing a weight for a mark
    REQ : 0<= weight <=100
    >>> readWeight()
    10
    >>> readWeight()
    5
    '''        
    # read the mark
    weight = int(input("please enter the weight:"))
    return weight

def totalMark(mark, weight):
    '''(float, int) -> float
    This function adds up the marks based on the given weight

    REQ : 0<= weight, mark <=100
    >>> totalMark(100, 5)
    5
    >>> totalMark(100, 10)
    15
    '''        
    
    # compute the final mark 
    a08_grade = a08_grade + (mark * (weight/100)) #runtime error
    return a08_grade

a08_grade = 0
    
the_mark = readMark()
the_weight = readWeight()
a08_grade = totalMark(the_mark, the_weight)
print("The total mark is:", a08_grade)
    
the_mark = readMark()
the_weight = readWeight()
a08_grade = totalMark(the_mark, the_weight)
print("The total mark is:", a08_grade)


