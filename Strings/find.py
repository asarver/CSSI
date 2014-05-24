# Finds a letter in a given word
#
# The function takes three arguments, a word,
# a letter it has to find, and an index where it
# should start looking.
#
# Example find(word, letter, index)
# find(banana, b, 0)
# returns index 0

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1
