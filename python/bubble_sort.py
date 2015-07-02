# go trough list list left to right
# If element right is smaller then current element
# swap element and proceed to next pair
# keep running through the list until all elements are sorted

def bubblesort(some_list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True	
        for index in range(len(some_list)-1):
            current = some_list[index]
            next = some_list[index + 1]
            if current > next:
                is_sorted = False
                some_list[index] = next
                some_list[index + 1] = current
            print some_list
    return some_list

if __name__ == "__main__":
    test_list = [10, 3, 4, 2, 81, 23, 0, 15, 100, 99]
    print "Bubblesort of [10, 3, 4, 2, 81, 23, 0, 15, 100, 99] is {0}".format(bubblesort(test_list))
