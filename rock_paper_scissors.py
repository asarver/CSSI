# rock scissors paper
#
# judge a rock scissors paper contest
#
# one? rock
# two? scissors
# One wins!

def rps():
    playerOne = raw_input("Player one, what is your name? ")
    playerTwo = raw_input("Player two, what is your name? ")
    
    one = raw_input(playerOne + ", rock, paper, or scissors? ")
    while one != "rock" and one != "scissors" and one != "paper":
        print "Error. Please retry."
        one = raw_input(playerOne + ", rock, paper, or scissors? ")
    
    two = raw_input(playerTwo + ", rock, paper, or scissors? ")
    while two != "rock" and two != "paper" and two != "scissors":
        print "Error. Please retry."
        two = raw_input(playerTwo + ", rock paper, or scissors? ")
    
    if one == two:
        print "It's a tie!"
    elif one.lower() == "rock" and two.lower() == "scissors":
        print playerOne + " wins!"
    elif one.lower() == "rock" and two.lower() == "paper":
        print playerTwo + " wins!"
    elif one.lower() == "scissors" and two.lower() == "rock":
        print playerTwo + " wins!"
    elif one.lower() == "scissors" and two.lower() == "paper":
        print playerOne + " wins!"
    elif one.lower() == "paper" and two.lower() == "rock":
        print playerOne + " wins!"
    else:
        print playerTwo + " wins!"
