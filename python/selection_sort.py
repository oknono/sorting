# Implementation of the selection sort algorithm
# Go through list left to right. Swap current element
# with the minimum element in the remaining list, if this element
# is larger then the current element

def selection_sort(S):
    for index in range(len(S) - 1):
	print S
        current_element = S[index]
        min_element = min(S[index+1:])
        min_index = S.index(min_element)
        if min_element < current_element:
            S[index] = min_element
            S[min_index] = current_element
    print S	    
    return S

if __name__ == "__main__":
    test_list = [10, 3, 4, 2, 81, 23, 0, 15, 100, 99]
    selection_sort(test_list)
