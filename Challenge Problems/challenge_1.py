# recursive function to find number
# in a sorted list
# and returns true if the number is found
# false if it wasn't
# and the number of times the list was searched
#
# Example find_recursive(3, [1,2,3,4,5,6])
# (True, 4)

# 12 [6,12,20,25]

def find_recursive(num, arr):
    if len(arr) == 0):
        return False, len(arr)
    if num > arr[len(arr) / 2):
        print num, arr[len(arr) / 2:]
        find_recursive(num, arr[len(arr) / 2:])
    if(num < arr[len(arr) / 2]):
        find_recursive(num, arr[:len(arr) / 2])
    if(num == arr[len(arr) / 2]):
        return True, len(arr)
    elif:
        return False, 
