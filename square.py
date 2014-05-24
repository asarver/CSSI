# square.py

import sys # contains system related stuff

def square(x):
    return x * x


if __name___ = "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        print square(int(sys.argv[1]))
    else:
        print 'usage:', sys.argv[0], 'number'


def newsquares(n):
    """return a list of the first n squares"""
    # list comprehensions
    return [x * x for x in range(n)]

def between(a, b, c):
    """return true if a < b < c"""
    return a < b and b < c

u2 = map(between, [1,2,3,4,5], [2,3,4,5,6], [3, 4, 5, 6, 7])

def getletter(index, string):
    """return the index letter of string"""
    return string[i]
