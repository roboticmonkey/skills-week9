#Sorting
#start 2:30pm - break: 245pm, start 300 - 316pm

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    # print lst
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1 ]:
                lst[j], lst[j + 1 ] = lst[j+1], lst[j]
    # print lst
    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    results = []

    while len(list1) > 0 or len(list2) > 0:
        if list1 == []:
            results.append(list2.pop(0))
        elif list2 == []:
            results.append(list1.pop(0))
        elif list1[0] < list2[0]:
            results.append(list1.pop(0))
        else:
            results.append(list2.pop(0))
    return results
    # pass


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    
    if len(lst) < 2:
        return lst

    mid = int(len(lst) /2)
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    results = []

    while len(lst1) >0 or len(lst2) > 0:
        if lst1 == []:
            results.append(lst2.pop(0))
        elif lst2 == []:
            results.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            results.append(lst1.pop(0))
        else:
            results.append(lst2.pop(0))
    return results
    pass




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print