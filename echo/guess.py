import random


def get_number(maxValue):
    """create a game state based on maxValue"""
    return random.randint(1, maxValue)

def check_guess(number, guess):
    """return WON, LOW, or HIGH"""
    if number == guess:
        return False, "you won."
    elif number < guess:
        return True, "too high."
    else:
        return True, "too low."

def one_turn(number, request):
    """return (playing, response) to the user's request"""
    if not request:
        return (False, "goodbye")
    else:
        return check_guess(number, int(request))
        
    
