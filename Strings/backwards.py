# displays letters of a word backward
#
# function takes a string as an argument
# and displays the letters backward
# one per line
#
# Example: word: banana
#          result: ananab


def backwards(word):
    i = len(word)
    while i > 0:
        letter = word[i - 1]
        print letter,
        i -= 1
