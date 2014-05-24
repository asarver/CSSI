# counts how many times a letter appears
#
# function takes a string and letter argument
# and returns the amount of times the number
# returns
#
# Example word = banana, letter = a
# return 3

def counter(word, letter):
    counter = 0
    for l in word:
        if letter == l:
            counter += 1
    return counter

def find(word, letter, index):
    counter = 0
    while index < len(word):
        if word[index] == letter:
            counter += 1
        index += 1
    return counter
            
