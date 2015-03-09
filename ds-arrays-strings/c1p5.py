
# 
# Compress a string with repeated values  'abbbbbcc' -> 'a1b5c2' but only if it helps
# 



from profilehooks import profile

s1 = "aabbCCCCCaaDdDFFFFFFFggggggHHhhhhhh"
s1_out = "a2b2C5a2D1d1D1F7g6H2h6"
s2 = 100*"aabbCCCCCaaDdDFFFFFFFggggggHHhhhhhh"
s2_out = 100*"a2b2C5a2D1d1D1F7g6H2h6"



@profile
def compress_repeats_list(s):
    "Compress using concatenation.  Concatination is O(n)! so the algorithm is O(n**2)"

    # argument checking
    if len(s)==1:
        return None

    # Compute the compressed form
    L = len(s)
    N = 1 + L//2
    scomps = N * ['',]
    icomp = 0
    repeat_counter = 1
    # loop over pairs
    for cold, cnew in zip(s[:-1], s[1:]):
        if not (cold==cnew): # add a new entry to the compressed string
            scomps[icomp] = (cold + str(repeat_counter))
            repeat_counter = 1  # reset
            icomp += 1
            if icomp >= N:
                return None
        elif (cold==cnew):      # update repeat counter
            repeat_counter += 1
    else:                       # add the final match
        scomps[icomp] = cnew +str(repeat_counter)

    sout = ''.join(scomps)
    if L <= len(sout):
        return None
    
    # Return the compressed string 
    return sout


@profile
def compress_repeats_concatenation(s):
    "Compress using concatenation.  Concatination is O(n)! so the algorithm is O(n**2)"

    # argument checking
    if len(s)==1:
        return None

    # Compute the compressed form
    sout = ''
    repeat_counter = 1
    # loop over pairs
    for cold, cnew in zip(s[:-1], s[1:]):
        if not (cold==cnew): # add a new entry to the compressed string
            sout += (cold + str(repeat_counter))
            repeat_counter = 1
        elif (cold==cnew):      # update repeat counter
            repeat_counter += 1
        if len(sout)>=len(s):
            return None         # stop if the compressed string gets too big
    else:                       # add the final match
        sout += cnew + str(repeat_counter)
        if len(sout)>=len(s):
            return None
    # Return the compressed string 
    return sout




if __name__ == "__main__":
    
    
    slist = 500*[s1,]
    sout_list = 500*[s1_out,]
    
    for s, strue in zip(slist, sout_list):
        scomp = compress_repeats_concatenation(s)
        if len(s)<50:
            msg = "Compression with concatenation:\n\t{0}\n\t{1}"
            print(msg.format(s, scomp))
            msg = "The output should be, \n\t{0}"
            print(msg.format(strue))

    for s, strue in zip(slist, sout_list):
        scomp = compress_repeats_list(s)
        if len(s)<50:
            msg = "Compression with concatenation:\n\t{0}\n\t{1}"
            print(msg.format(s, scomp))
            msg = "The output should be, \n\t{0}"
            print(msg.format(strue))

        # msg = "Compression with Lists:\n\t{0}\n\t{1}"
        # # print(msg.format(s, scomp))
        # msg = "The output should be, \n\t{0}"
        # # print(msg.format(strue))
