# quadratic equation solver
#
# given three constants, a, b, and c,
# for the quadratic equation ax^2 + bx + c
# return the two roots of the equation
# as a tuple
#
# Example: quad(1, 3, -4) => (1, -4)

import math


def quad(a, b, c): #dummy implementation
    return 1, -4


def quadratic(a, b, c): #actual formula
    disc_squared = b** 2 - 4 * a * c
    # this is where to check for impossible sqrt calculations
    if disc_squared < 0:
        print "negative arguments to square root"
    elif disc_squared == 0:
        print "it's zero"
    else:
        disc = math.sqrt(disc_squared)
        one = (-b + disc) / (2 * a)
        two = (-b - disc) / (2 * a)
        return one, two
