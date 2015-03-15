 
# me: William G. K. Martin
# date: March 2015
# License: BSD
# 

"""
This module contains functions to count the number of inversions in a 
list in O(nlogn) operations.  It is based on recusion, like merge sort. 

Running as a script will print out a test case with a check against 
the known sorted array.  Also this print profile information after closing
the interactive propt. 

NOTES: Based on Coursera lectures on the design of algorithms (part 1). 

"""



# standard libraries
from __future__ import print_function, division
from random import shuffle
from profilehooks import profile



# Define the merge/split_count step
def csin(a, b):
    """
    Count split inversions and merge: 
    IN:  lists a anad b (sorted)
    OUT: count, absorted
    """
    ia, ib = 0, 0               # pointers to  a and b 
    Na, Nb = len(a), len(b)     # for knowing when to stop
    
    c = []                      # the sorted list
    inversion_count = 0         # counter for split inversions

    while (ia<Na) and (ib<Nb):
        if a[ia] <= b[ib]:
            c.append(a[ia])
            ia += 1
        else:
            c.append(b[ib])
            ib += 1
            inversion_count += Na - ia
    else:
        c += (a[ia:] + b[ib:])
        
    return inversion_count, c

# define the recursive call
@profile
def count_inversions(a):
    "The function to recursively call itself."
    Na = len(a)
    if Na==1: 
        return 0, a
    else:
        # split the list
        aleft = a[:Na//2]
        aright = a[Na//2:]

        # counting
        count_left, aleft = count_inversions(aleft)
        count_right, aright = count_inversions(aright)
        count_split, asorted = csin(aleft, aright) 
        return count_left + count_right + count_split, asorted

@profile
def brute_count_inversions(a):
    "Count inversions with a nested loop."
    Na = len(a)
    counter = 0
    for i in range(1,Na):
        for j in range(i):
            if a[i] <= a[j]:
                counter += 1
    return counter



# Quick testing
# --
if __name__ == "__main__":


    # Make a shuffled list of the integers from 0 to N-1
    N = 25
    Ntimes = 10
    a = range(N)
    shuffle(a)
    msg = "Tyring a simple case. The list is {}."
    print(msg.format(a))
    msg =  "\tBrute force: there are {} inversions"
    print(msg.format(brute_count_inversions(a)))

    msg = "\tRecursion: there are {} inversions."
    merge_count, asorted = count_inversions(a)
    print(msg.format(merge_count))
    msg = "\tMerge returned the sorted list, range(N):{}"
    merge_true = (sum([(_a!=_r) for _a, _r in zip(asorted, range(N))]) == 0)
    print(msg.format(merge_true))

    
    # Make a shuffled list of the integers from 0 to N-1
    N = 5000
    Ntimes = 5
    for n in range(Ntimes):    
        a = range(N)
        shuffle(a)
        # call the recusive function
        inversion_count, asorted = count_inversions(a)
        brute_count = brute_count_inversions(a)
