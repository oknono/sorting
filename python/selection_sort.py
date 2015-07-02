# Implementation of the selection sort algorithm
# Go through list left to right. Swap current element
# with the minimum element in the remaining list, if this element
# is larger then the current element

def selection_sort(some_list):
    for index in range(len(some_list) - 1):
        current_element = some_list[index]
        # print "current element is {0}".format(current_element)
        min_element = min(some_list[index+1:])
        # print "min element is {0}".format(min_element)
        min_index = some_list.index(min_element)
        # print "swapping {0} and {1}".format(current_element, min_element)
        if min_element < current_element:
            some_list[index] = min_element
            some_list[min_index] = current_element
    return some_list

if __name__ == "__main__":
    test_list = [10, 3, 4, 2, 81, 23, 0, 15]
    print "selection sort of [10, 3, 4, 2, 81, 23, 0, 15] is {0}".format(selection_sort(test_list))