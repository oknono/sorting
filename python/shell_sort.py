# Implementation of shell sort

def shell_sort(S):
    step = len(S) / 2
    while step > 0:
    	print "-" * 40 
    	print"Step is {0}".format(step)
    	print "-" * 40 
        for start in range(step):
            sorting(S, start, step)
        step /= 2
    return S


def sorting(S, start, step):
    for i in range(start + step, len(S), step):
        current = S[i]
        pos = i
        while pos >= step and S[pos - step] > current:
            S[pos] = S[pos-step]
            pos = pos - step
        S[pos] = current
        print S
    return S


if __name__ == "__main__":
    test_list = [10, 3, 4, 2, 81, 23, 0, 15, 100, 99]
    print shell_sort(test_list)


