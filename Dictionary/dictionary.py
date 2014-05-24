# Exercise One
#
# read words in words.txt and stores them as keys in a dictionary
# values don't matter

def getWords():
    unix_words = "C:\Documents and Settings\googleuser\My Documents\Downloads\unix-words"
    wordfile = open(unix_words)
    counter = 0
    csdict = dict()
    for word in wordfile:
       csdict[word] = counter
       counter += 1
    return csdict

    # for word in csdict: # test
    #    print word


        
# Exercise Two
#
# write histogram more efficiently using
# the get function

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d




# Exercise Three
#
# modify print_hist to print the keys
# and their values in alphabetical order

def print_hist(h):
    keys = h.keys()
    keys.sort()
    for word in keys:
        print word, h[word]




# Exercise Four
#
# modify reverse_lookup so that it builds
# and returns a list of all keys that map to v
# or an empy list if there are none

def reverse_lookup(d, v):
    index = 0
    myList = ['']
    for k in d:
        if d[k] == v:
            myList[index] = k
            index += 1
    return myList




# Exercise Five
#
# Read dictionary documentation method setdeafult and
# use it to write a more conscise version of invert_dict


