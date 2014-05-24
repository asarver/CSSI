# Names ducklings in "Make way for Ducklings"
#
# Names are Jack, Kack, Lack, Mack,
# Nack, Ouack, Pack, and Quack
#
# Program prints out all names of ducklings using prefixes "JKLMNOPQ"
# and the suffix "ack"
#
# Program has to be fixed for Ouack and Quack

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print letter + "u" + suffix
    else:
        print letter + suffix


def fullname(first, last):
    return first + ' ' + last

def fullname2(first, last):
    return '%s %s' % (first, last)
