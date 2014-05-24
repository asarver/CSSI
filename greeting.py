# #Greeting
#
#input asking for full name
#
# Example
# "What is your first: Ashley
# "What is your last: Sarver
# "Hello Ashley Sarver"

def greeting():
    first = raw_input("What is your first name? ")
    last = raw_input("What is your last name? ")
    fullname = first + " " + last
    print "Hello " + fullname
