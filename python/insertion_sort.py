# implementation of insertion sort
# Go through list from left to right
# Check current element with next element
# If next element is smaller, swap the two
# Keep checking the "next element" with element on the left
# Until element left is bigger

def insertion_sort(some_list):
    for index in range(1, len(some_list)):
        current = some_list[index]
        check = index
        while check > 0 and some_list[check-1] > current:
            some_list[check] = some_list[check-1]
            check -= 1
        some_list[check] = current
        print some_list
    return some_list

if __name__ == "__main__":
    test_list = [10, 3, 4, 2, 81, 23, 0, 15, 100, 99]
    #print "insertion sort of [10, 3, 4, 2, 81, 23, 0, 15, 100, 99]", 
    #print "is {0}".format(insertion_sort(test_list))
    print insertion_sort(test_list)
