 
# me: William G. K. Martin
# date: March 2015
# License: BSD
# 

"""
This module contains python implementation of the quick sort algorithm. 

PLAN: Running as a script will print out a test case with a check against 
the known sorted array.  Also this print profile information after closing
the interactive propt. 

Learning points: 
  REMEMBER THE BASE CASE!!!!

NOTES: Based on Coursera lectures on the design of algorithms (part 1). 

"""



# standard libraries
from __future__ import print_function, division
from copy import copy
from random import shuffle, randint
from profilehooks import profile




# Define a funciton to get the pivot
def get_pivot_random_item(a):
    "Pick a random item"
    N = len(a)
    ipivot = randint(0,N-1)
    return ipivot, a[ipivot]

def get_pivot_first_item(a):
    "Pick the first item"
    return 0, a[0]

def get_pivot_middle_item(a):
    "Pick the middle item"
    i = len(a)//2 if len(a)>=2 else 0
    return i, a[i]


# Define my quick sort algorithm
def my_quick_sort(a, pivot_method):
    "Quick sort a list in place.  Uses first element by default."

    # Base case  
    if len(a) <= 1: 
        return a

    # Choose the pivot
    ipivot, apivot = pivot_method(a)
    
    # order around the pivot
    count_under = 0
    for i, ai in enumerate(a):
        if i == ipivot:
            ipivotnew = count_under
        if ai <= apivot:
            a[i] = a[count_under]
            a[count_under] = ai
            count_under += 1
    else:
        count_under -= 1    
        a[ipivotnew] = a[count_under]
        a[count_under] = apivot
            
    # Call quick sort on the less and more lists
    aless = my_quick_sort(a[:count_under], pivot_method)
    amore = my_quick_sort(a[(count_under+1):], pivot_method)

    # return 
    return aless + [apivot,] + amore


# Define quick sort routines with specific choices for the pivot_method
@profile
def qs_random(a):
    "New call for profiling to work"
    return my_quick_sort(a, pivot_method=get_pivot_random_item)
@profile
def qs_first(a):
    "New call for profiling to work"
    return my_quick_sort(a, pivot_method=get_pivot_first_item)
@profile
def qs_middle(a):
    "New call for profiling to work"
    return my_quick_sort(a, pivot_method=get_pivot_middle_item)



# self test and performance profile
if __name__ == "__main__":
    
    
    # Make a shuffled list of the integers from 0 to N-1
    M = 5                       # different numbers
    N = 100                    # numbers in the list
    Ntimes = 14                 # repeated samples
    for n in range(Ntimes):    
        
        a = [i//(N//M) for i in range(N)]
        a = a[-1::-1]
        # shuffle(a)


        # Try the sorting routines out on copies 
        arandom = copy(a)
        arandom = qs_random(a)

        afirst = copy(a)
        afirst = qs_first(a)

        amiddle = copy(a)
        amiddle = qs_middle(a)

        # Check sorted
        msg = "For n = {} quick sort works: random {}, first {}, middle {}"

        randsorts = all([(l0<=l1) for l0, l1 in zip(arandom[:-1], arandom[1:])])
        firstsorts = all([(l0<=l1) for l0, l1 in zip(afirst[:-1], afirst[1:])])
        middlesorts = all([(l0<=l1) for l0, l1 in zip(amiddle[:-1], amiddle[1:])])
        print(msg.format(n, randsorts, firstsorts, middlesorts))
