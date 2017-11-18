def binary_search(L, s):
    '''(list) -> bool
    Return True iff s is an element of L
    REQ: L must be a sorted list
    '''
    # BASE CASE: If L is empty, it's not in the list
    if(len(L) == 0):
        result = False
    # RECURSIVE DECOMP: Pick the middle element, if we found
    # what we're looking for, great. If not, then we've at
    # least cut the list in half
    else:
        # get the middle element of the list
        mid_index = len(L) // 2
        mid_element = L[mid_index]
        # if we found it, then we can stop
        if(mid_element == s):
            result = True
        # if we didn't find it, then see whether we need to continue searching
        # in the left side of the list, or the right
        elif(mid_element < s):
            result = binary_search(L[mid_index + 1:], s)
        else:
            result = binary_search(L[: mid_index], s)

    return result


def binary_search2(L, s):
    '''(list of float) -> int
    Return the index of s in the list L, or -1 if s is not in L
    REQ: L must be a sorted list
    '''

    # BASE CASE: If L is empty, return -1
    if(L == []):
        result = -1
    else:
        # GENERAL CASE
        # get the middle value of L, if it's larger than s, then s must be in
        # the first half of the list, so call binary_search on the first half,
        # otherwise, call it on the second half of L, if it's equal to s, then
        # we've found s and we can stop
        mid_index = len(L)//2
        mid = L[mid_index]
        if(mid == s):
            # found it. return its index
            result = (mid_index)
        elif(mid > s):
            # if s is in L, it must be in the first half of the list
            # so just perform a binary search on the first half of the list
            # and return that search's result
            result = binary_search2(L[0:mid_index], s)
        else:
            # if s is in L, it must be in the latter half of the list
            # so perform a binary search on the latter half of the list,
            # however, this time, if we do get a result, we have to return
            # its offset from our current midpoint
            result = binary_search2(L[mid_index+1:], s)
            # if we didn't find it, just pass on the -1, but if we did
            # we have to add the index in the right list to the index of
            # our middle element to get its index in our list
            if(result != -1):
                result = result + mid_index + 1
    return result
