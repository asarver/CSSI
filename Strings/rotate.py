# return a string where each letter in original
# is shifted by a certain amount of places
#

def rotate_word(original, shift):
    rot = ""
    for c in original:
        rot += rotate_letter(c, shift)
    return rot
        


def rotate_letter(letter, shift):
    decimal = ord(letter)
    shifted = decimal + shift
    # check for value inside the ascii character range
    max_ascii = ord('~')
    min_ascii = ord(' ')
    ascii_range = max_ascii - min_ascii + 1
    if shifted > max_ascii:
        shifted -= ascii_range
    elif shifted < min_ascii:
        shifted += ascii_range
    return chr(shifted)

def test_rotate_letter():
    if rotate_letter(' ', -1) != '~' or rotate_letter('~', 1) != ' ':
        print "rotate_letter is buggy!"
    
