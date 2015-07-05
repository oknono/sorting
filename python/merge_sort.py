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
    print S
    return S

def merge_sort(some_list):
    if len(some_list) < 2 :
        return some_list
    else:
        s1 = some_list[ :int(math.floor(len(some_list))) / 2 ]
        s2 = some_list[int(math.floor(len(some_list))) / 2 : ]
        #print s1
        #print s2
        merge_sort(s1)
        merge_sort(s2) 
        return merge(s1, s2, some_list)

if __name__ == "__main__":
    test_list = [10, 3, 4, 2, 81, 23, 0, 15, 100, 99]
    print "selection sort of [10, 3, 4, 2, 81, 23, 0, 15, 100, 99] is {0}".format(merge_sort(test_list))
