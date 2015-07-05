# implementation of insertion sort
# Go through list from left to right
# Check current element with next element
# If next element is smaller, swap the two
# Keep checking the "next element" with element on the left
# Until element left is bigger

def insertion_sort(S):
    for index in range(1, len(S)):
        current = S[index]
        check = index
        while check > 0 and S[check-1] > current:
            S[check] = S[check-1]
            check -= 1
        S[check ]= current
        print S
    return S

if __name__ == "__main__":
    test_list = [10, 3, 4, 2, 81, 23, 0, 15, 100, 99]
    print insertion_sort(test_list)
