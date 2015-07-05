# Swap element and proceed to next pair
# Keep running through the list until all elements are sorted

def bubble_sort(S):
    is_sorted = False
    while not is_sorted:
        is_sorted = True	
        for index in range(len(S)-1):
            print S
            current = S[index]
            next = S[index + 1]
            if current > next:
                is_sorted = False
                S[index] = next
                S[index + 1] = current
    return S

if __name__ == "__main__":
    test_list = [10, 3, 4, 2, 81, 23, 0, 15, 100, 99]
    bubblesort(test_list)
