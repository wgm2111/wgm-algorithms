
# 
# Check if two strings are permutations of eachother
# 

from __future__ import print_function
from numpy import zeros

s1 = "spammaps"
s2 = "pamssmap"
s3 = "porkspam"
s4 = "completelydifferent"


def check_if_permutations(s1, s2):
    "Take two strings and return true if permutations"
    
    # quick
    L = len(s1)
    if not (L == len(s2)):
        return False

    # tally check
    tally1 = zeros(128, dtype='int')
    tally2 = zeros(128, dtype='int')
    for c1, c2 in zip(s1, s2):
        tally1[ord(c1)] += 1
        tally2[ord(c2)] += 1
    
    # Check if tallys are all equal
    are_permutations = (tally1 == tally2).all()
    return are_permutations


if __name__=="__main__":
    
    def print_results(s1, s2):
        msg = "The following strings are {0}permutations :\n\t{1}\n\t{2}"
        print(msg.format("" if check_if_permutations(s1, s2) else "not ", 
                         s1, s2))

    slist = [s1, s2, s3, s4]
    [print_results(_s1, _s2) for _s1 in slist for _s2 in slist]
