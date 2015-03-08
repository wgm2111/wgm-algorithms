
# 
# Replace whitespaces with %20
# 

from array import array

"""
Using array have to assign slices with array slices.  Using an arbitrary sequance will 
raise an error. I have to make an array out of the string I'm using in the assignment.
"""


s = "spam eggs cheese and eggs" + 10*" "
carr = array('c', s)

def replace_spaces_array(carr):
    "Replace spaces with %20, ignore trailing spaces"
    
    # Count spaces
    spaces_left = 0
    for c in carr: 
        if c == " ": 
            spaces_left += 1
    
    # Shift or add %20 to build the new carray in place (left to right)
    on_tail = True              # starting on tail
    N = len(carr)
    for iold in range(N)[-1::-1]:
        inew = iold + 2 * spaces_left
        cold = carr[iold]
        if cold == " ":          # found a space in the old array
            spaces_left -= 1
            if on_tail: 
                pass
            elif not on_tail:
                carr[(inew-2):(inew+1)] = array('c', "%20")
        else:                   # found a non-space character in the old array
            on_tail=False
            carr[inew] = cold

    # return the modified array
    return carr

# Note some other options when in-place manipulation is not required
# --
def replace_spaces_after_strip(s):
    "Remove leading and trailing whitspaces"
    return "%20".join(s.strip(" ").split(" "))


if __name__ == "__main__":

    msg = "Transformation in-place with replace_spaces_array: \n\t'{0}'\n\t'{1}'"
    print(msg.format(s, "".join(replace_spaces_array(carr))))
    msg = "Transformation with replace_spaces_after_strip: \n\t'{0}'\n\t'{1}'"
    print(msg.format(s, replace_spaces_after_strip(s)))
