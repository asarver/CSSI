#lists

def add_all(t):
    """Add all the numbers in t and return the sum"""
    total = 0
    for x in t:
        total += x
    return total

# Exercise 4

def is_anagram(s, t):
    """return True if s and t are anagrams"""
    u = list(s)
    v = list(t)
    return u.sort() == v.sort()
