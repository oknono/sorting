# Implementation of quick sort
# divide and conquer
# Choose first element of list as a pivot

def quick_sort(S):
	print "-" * 25
	print "S is {0}".format(S)
	if len(S) < 2:
		return S
	else:
		pivot = S[-1]
		print "Pivot is {0}".format(pivot)
		L = quick_sort([x for x in S[:-1] if x < pivot])
		G = quick_sort([x for x in S[:-1] if x >= pivot])
		print "L is {0}".format(L)
		print "G is {0}".format(G)
		print "Result is {0}".format(L + [pivot] + G)
        return L + [pivot] + G

if __name__ == "__main__":
    test_list = [10, 3, 4, 2, 81, 23, 0, 3, 100, 99]
    quick_sort(test_list)