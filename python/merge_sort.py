# implementation of mergesort algorithm
# divide and conquer - recursive call
import math

def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j]= S1[i]
            i += 1
        else:
            S[i+j]= S2[j]
            j += 1
    print "S is {0}".format(S)
    return S

def merge_sort(S):
    length = len(S)
    half = int(math.floor(length)) / 2
    if length < 2 :
        return S
    else:
        S1 = S[ :half]
        S2 = S[half: ]
	print "S1 is {0}, S2 is {1}".format(S1, S2)
        merge_sort(S1)
        merge_sort(S2) 
        return merge(S1, S2, S)

if __name__ == "__main__":
    test_list = [10, 3, 4, 2, 81, 23, 0, 15, 100, 99]
    merge_sort(test_list)
