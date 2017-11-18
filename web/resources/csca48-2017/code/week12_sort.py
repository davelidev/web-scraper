import random

def selection_sort(unsorted_list):
    '''(list of objects) -> list of objects
    Return a copy of unsorted_list, but sorted using the
    selection sort algorithm
    '''
    #make a copy of the unsorted list so that we can modify it without
    #changing the list passed in
    ul_copy = unsorted_list[:]
    #find the global max element in the list
    global_max = max(unsorted_list)
    sorted_list = []
    #keep looping until the unsorted list is empty
    while(len(ul_copy) > 0):
        #loop through the list to find the smallest element
        smallest = global_max
        smallest_index = 0
        for i in range(0,len(ul_copy)):
            if(ul_copy[i] < smallest):
                smallest = ul_copy[i]
                smallest_index = i
        #now that we've found the smallest element, remove it and append
        #it to the sorted list
        sorted_list.append(smallest)
        ul_copy = ul_copy[:smallest_index] + ul_copy[smallest_index + 1:]
    return sorted_list


def insertion_sort(unsorted_list):
    '''(list of objects) -> list of objects
    Return a copy of unsorted_list, but sorted using the
    insertion sort algorithm (in-place version)
    '''
    #our unsorted and sorted list (since we're doing to be doing the sort
    #in place
    us_list = unsorted_list[:]
    #the starting index of the sorted list
    sorted_index = len(us_list) - 1
    #loop until our whole list is sorted
    while(sorted_index > 0):
        #add the last element of our unsorted list into our sorted list
        #then move it along the sorted list until it's in the correct
        #position
        sorted_index -= 1
        new_item_index = sorted_index
        #move the new item to the right one place at a time until
        #it's in the correct position
        while((new_item_index < len(us_list) -1) and (us_list[new_item_index] > us_list[new_item_index + 1])):
            swap(us_list, new_item_index, new_item_index +1)
            new_item_index +=1
    return us_list

def swap(my_list, i, j):
    '''(list of objects, int, int) -> NoneType
    swap items i and j in my_list
    '''
    my_list[i], my_list[j] = my_list[j], my_list[i]

def quick_sort(unsorted_list):
    '''(list of objects) -> list of objects
    Return a copy of unsorted_list, sorted via the quicksort algorithm
    '''
    #Base Case: If we have an empty list, it must be sorted, so just
    #return it
    if(unsorted_list == []):
        result = []
    else:
        #Pick a pivot, and split the list into three components
        #those less than the pivot, those equal to the pivot
        #and those greater than the pivot
        pivot = random.choice(unsorted_list)
        lt_list = []
        gt_list = []
        eq_list = []
        for element in unsorted_list:
            if(element < pivot):
                lt_list.append(element)
            elif(element > pivot):
                gt_list.append(element)
            else:
                eq_list.append(element)
        #RD: Sort the less than and greater than lists recursively
        lt_list = quick_sort(lt_list)
        gt_list = quick_sort(gt_list)
        result = lt_list + eq_list + gt_list
    return result

def merge_sort(unsorted_list):
    '''(list of objects) -> list of objects Return a copy of unsorted_list
    sorted using the MergeSort algorithm
    '''
    #Base Case: an empty list is sorted, just return it
    if(unsorted_list == []):
        result = []
    #Base Case 2: a list with a single element is sorted, just return it
    #Question: How can we improve our base cases?
    elif(len(unsorted_list) == 1):
        result = unsorted_list
    else:
        midpoint = len(unsorted_list) //2
        #split the list into two smaller lists
        u1 = unsorted_list[:midpoint]
        u2 = unsorted_list[midpoint:]
        #recursively sort each list
        s1 = merge_sort(u1)
        s2 = merge_sort(u2)
        #merge the two sorted lists
        sorted_list = merge(s1,s2)
        result = sorted_list
    return result

def merge(s1, s2):
    '''(list of objects, list of objects) -> list of objets
    Merge sorted lists s1 and s2 into a single sorted list and return it
    '''
    #index1 and index2 will hold our current place in s1 and s2 respectively
    i1 = 0
    i2 = 0
    #loop through s1 and s2 comparing the current indicies, and moving
    #the greater element into the sorted list
    sorted_list = []
    while(i1 < len(s1) and i2 < len(s2)):
        if(s1[i1] < s2[i2]):
            sorted_list.append(s1[i1])
            i1 +=1
        else:
            sorted_list.append(s2[i2])
            i2 +=1
    #append the rest of whichever list has not been finished to the end of
    #the sorted list
    if(i1 < len(s1)):
        sorted_list += s1[i1:]
    else:
        sorted_list += s2[i2:]
    return sorted_list



def builtin_sort(L):
    '''Make the built-in sort in-place.'''
    L[:] = sorted(L)

