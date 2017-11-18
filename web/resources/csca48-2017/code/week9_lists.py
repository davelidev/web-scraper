def nr_sum(L):
    ## non recursive version of sum
    total = 0
    for next_item in L:
        total += next_item
    return total

def np1_sum(L):
    ## recursive n + 1 version of sum
    # Base case: if the list is empty, the answer is 0
    if(len(L) == 0):
        result = 0
    # Recursive decomposition: add the first item to the sum of the
    # rest of the items (use recursion to find the sum of the rest
    # of the items
    else:
        first_item = L[0]
        rest = L[1:]
        # get the sum of items 1 - end
        sum_rest = np1_sum(rest)
        # the sum of the items in this list is the first item, plus
        # the sum of the rest
        result = first_item + sum_rest
    return result

def dc_sum(L):
    ## divide and conquer version of sum
    # Base case: if the list is empty, the answer is 0
    if(L == []):
        result = 0
    # Base case #2: if the list has a single element, the answer is that
    # element
    elif(len(L) == 1):
        result = L[0]
    # Recursive decomposition: divide the list in half, use
    # recursion to find the sum of the two halves, add them
    # together to get our result
    else:
        # divide the list in half
        mid = len(L) // 2 # <- integer division, always gives an int back
        left_half = L[:mid]
        right_half = L[mid:]
        # get the sum of the two halves (recursively)
        left_sum = dc_sum(left_half)
        right_sum = dc_sum(right_half)
        # the sum of the items in this list is the sum of the items in
        # the two halves
        result = left_sum + right_sum
    return result

if(__name__ == "__main__"):
    L = [1, 2, 3, 4, 5, 6, 7]
    assert(nr_sum(L) == 28)
    assert(np1_sum(L) == 28)
    assert(dc_sum(L) == 28)
