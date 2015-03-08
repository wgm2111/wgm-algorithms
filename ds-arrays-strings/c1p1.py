
# 
# Check a string array for repeats
# 


from string import letters


s1 = "abcedfZ"
s2 = "rob"
s3 = "bob"
s4 = letters


# Brute force
def repeats_brute(s):
    "Check for repeats by brute force"
    repeats = False
    for i, ci in enumerate(s):
        for j, cj in enumerate(s[(i+1):]):
            if ci==cj:
                repeats = True
    return repeats
    
def repeats_ascii(s):
    "Test for repeats assuming characters are ascii"

    # Quick check, there are max 128 unique characters 
    if len(s) > 128:
        return True

    # Slow check for shorter lists
    tally = 128*[False,]
    for c in s:
        if tally[ord(c)]:
            return True
        else:
            tally[ord(c)] = True

    return False                 # nothing found


if __name__=="__main__":
    
    def print_results(s):
        msg = "Does the string {0} have repeats? \n\tbrute says {1},\n\tascii says {2}."
        print(msg.format(s, repeats_brute(s), repeats_ascii(s)))
        
    slist = [s1, s2, s3, s4]
    [print_results(s) for s in slist]
