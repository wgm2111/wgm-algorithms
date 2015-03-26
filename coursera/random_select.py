 
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

import numpy as np
from numpy.random import shuffle, randint
from profilehooks import profile




# Define a funciton to get the pivot
def get_pivot_random_item(a):
    "Pick a random item"
    N = len(a)
    ipivot = randint(N)
    return ipivot, a[ipivot]

def get_pivot_first_item(a):
    "Pick the first item"
    return 0, a[0]

def get_pivot_middle_item(a):
    "Pick the middle item"
    i = a.size//2 if a.size>=2 else 0
    return i, a[i]

# Define my pivot sort
def get_pivot_sort(ipivot, a):
    ""
    count_lepivot = 0           # counter for placing pivot
    apivot = a[ipivot]          # store the pivot quicker than lookup

    for i, ai in enumerate(a):
        if ipivot == i:         # update the pivot index 
            ipivot = count_lepivot
        if ai <= apivot:        # move ai to end of lepivotsection
            a[i] = a[count_lepivot] 
            a[count_lepivot] = ai 
            count_lepivot += 1
    else:                       # move pivot to the end of lepivotsection
        ipivotfinal = count_lepivot - 1
        a[ipivot] = a[ipivotfinal]
        a[ipivotfinal] = apivot
    return ipivotfinal, a
            
def get_istat(istat, a, get_pivot):
    ""
    assert (istat <= (a.size-1)) 
    assert (istat>=0)           # for sanity

    # select a pivot
    ipivot, apivot = get_pivot(a) 

    # sort (partially) around the pivot
    ipivot, a = get_pivot_sort(ipivot, a)
    
    # Get the ith statistic
    if ipivot == istat:
        astat = a[ipivot]
    elif ipivot > istat:
        astat = get_istat(istat, a[:ipivot], get_pivot)
    elif ipivot < istat:
        istatnew = istat - (ipivot+1)
        astat = get_istat(istatnew, a[(ipivot+1):], get_pivot)

    # return 
    return astat
    



# Define quick sort routines with specific choices for the pivot_method
@profile
def selection_random(istat, a):
    "New call for profiling to work"
    return get_istat(istat, a, get_pivot_random_item)
@profile
def selection_first(istat, a):
    "New call for profiling to work"
    return get_istat(istat, a, get_pivot_first_item)
@profile
def selection_middle(istat, a):
    "New call for profiling to work"
    return get_istat(istat, a, get_pivot_middle_item)



# self test and performance profile
if __name__ == "__main__":




    # Make a shuffled list of the integers from 0 to N-1
    N = 8
    istat = 3
    a = np.arange(N)
    shuffle(a)
    msg = "Tyring the simple case of getting the {}th smallest element in the array {}."
    print(msg.format(istat, a))
    msg =  "\tRandom pivot selection returned, {}."
    print(msg.format(selection_random(istat, copy(a))))
    msg =  "\tFirst pivot selection returned,  {}."
    print(msg.format(selection_first(istat, copy(a))))
    msg =  "\tMiddle pivot selection returned, {}."
    print(msg.format(selection_middle(istat, copy(a))))
    
    
    # Make a shuffled list of the integers from 0 to N-1
    M = 500                       # different numbers
    N = 1500                     # numbers in the list
    Ntimes = 15                  # repeated samples
    

    msg = "Profiling test:"
    msg +="select the {}the smallest element in an array of {} integers.  Repeat {} times."
    print(msg.format(istat, N, M, Ntimes))
    
    for n in range(Ntimes):    
        istat = randint(M)
        a = np.array([i//(N//M) for i in range(N)])
        a = np.array([i//(N//M) for i in range(N)])
        a = a[-1::-1]
        # shuffle(a)


        # Try the sorting routines out on copies 
        arandom = copy(a)
        arandom = selection_random(istat, a)

        afirst = copy(a)
        afirst = selection_first(istat, a)

        amiddle = copy(a)
        amiddle = selection_middle(istat, a)
