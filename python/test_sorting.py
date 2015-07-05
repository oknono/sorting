import random
from bubble_sort import *
from comb_sort import *
from insertion_sort import *
from merge_sort import *
from selection_sort import *
from shell_sort import *

values = range(1,10)
random.shuffle(values)
values[:]

print "List to be sorted is {0}".format(values)
print "-" * 30
print "Selection Sort"
print "-" * 30
values1 = values[:]
selection_sort(values1)
print "-" * 30
print "Insertion Sort"
print "-" * 30
values2 = values[:]
insertion_sort(values2)
print "-" * 30
print "Bubble Sort"
print "-" * 30
values3 = values[:]
bubble_sort(values3)
print "-" * 30
print "Comb Sort"
print "-" * 30
values4 = values[:]
comb_sort(values4)
print "-" * 30
print "Shell Sort"
print "-" * 30
values5 = values[:]
shell_sort(values5)
print "-" * 30
print "Merge Sort"
print "-" * 30
values6 = values[:]
merge_sort(values6)