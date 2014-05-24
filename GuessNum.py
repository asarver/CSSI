# guessing game
# guessee(100)
# I have a number between 1 and 100
# your guess? 23
# higher!
# your guess? 34
# correct
# >>>

import time
import random

def guessee(minVal, maxVal):
    randNum = random.randint(minVal, maxVal)
    # print randNum  / test that randNum is correct
    print "Guessing game:"
    print "Enter 'Quit' to end game."
    print
    print "Please enter a number " + str(minVal) + " through " + str(maxVal)
    guessOne = raw_input("What is your first guess? ")
    if guessOne == 'Quit':
        print "Goodbye!"
        return
    elif int(guessOne) == randNum:
        print "Correct!"
    else:
        while int(guessOne) != randNum:
            if int(guessOne) < randNum:
                print "Incorrect. Guess higher!"
                guessOne = raw_input("Guess again! ")
            else:
                print "Incorrect. Guess lower!"
                guessOne = raw_input("Guess again! ")
        print "Correct!"


def guesser(minVal, maxVal):
    randNum = random.randint(minVal, maxVal)
    print "Now it's my turn!"
    print "Enter 'Quit' to end game."
    print
    print "Time for me to guess. Is your number " + str(randNum)
    answer = raw_input("Yes, Higher, or Lower? ")
    if answer.lower() == "yes":
        print "I win!"
    else:
        comMin = minVal
        comMax = maxVal
        counter = 1
        while answer.lower() != "yes":
            
            if answer.lower() == "higher":
                comMin = randNum
                randNum = random.randint(comMin, comMax)
                counter += 1
                print "Is your number " + str(randNum)
                answer = raw_input("Yes, Higher, or Lower? ")
                
            else:
                
                comMax = randNum
                randNum = random.randint(comMin, comMax)
                counter += 1
                print "Is your number " + str(randNum)
                answer = raw_input("Yes, Higher, or Lower? ")
                
        print "It took me " + str(counter) + " times to beat you. I win!"




# think of  a number between 1 and 100
# I will think of one too, we will take turns guessing
# you guess 50
# too low I guess 23 higher
# your guess...

def game(minVal, maxVal):
    print "We're going to play a game."
    print "I am going to try and guess your number, while"
    print "you try and guess mine."
    print
    print "Alright, I'll pick a number between " + str(minVal) + " and " + str(maxVal) + "."
    print "You pick yours too."
    print
    print
    
    randCompNum = random.randint(minVal, maxVal)
    randCompGuess = random.randint(minVal, maxVal)
    time.sleep(2)
    
    print "I have my number. Is yours " + str(randCompGuess) + "?"
    print "Enter 'Quit' to end game."
    
    myAnswer = raw_input("Yes, higher, or lower? ")
    myGuess = raw_input("What is your guess? ")

    if myAnswer == 'Quit':
        return
    
    if myAnswer.lower() == "yes" and int(myGuess) == randCompNum:
        print "We win!"
        return
    
        
    compCounter = 1
    myCounter = 1

    if myAnswer.lower() == "higher":
        compMin = randCompGuess
        compMax = maxVal
    else:
        compMax = randCompGuess
        compMin = minVal
        
    while myAnswer.lower() != "yes" or int(myGuess) != randCompNum:
            
        if myAnswer.lower() != "yes":
            if myAnswer.lower() == "higher":
                compMin = randCompGuess
                randCompGuess = random.randint(compMin, compMax)
                compCounter += 1
                print "Is your number " + str(randCompGuess)
                myAnswer = raw_input("Yes, Higher, or Lower? ")
                
            else:
                compMax = randCompGuess
                randCompGuess = random.randint(compMin, compMax)
                compCounter += 1
                print "Is your number " + str(randCompGuess)
                myAnswer = raw_input("Yes, Higher, or Lower? ")
                
        if int(myGuess) != randCompNum:
            if int(myGuess) < randCompNum:
                myCounter += 1
                myGuess = raw_input("Incorrect. Guess higher! ")
            else:
                myCounter += 1
                myGuess = raw_input("Incorrect. Guess lower! ")
    print
    print "It took me " + str(compCounter) + " times to guess!"
    print "It took you " + str(myCounter) + " times to guess!"
    print
    if compCounter > myCounter:
        print "You win!"
    else:
        print "I win!"







        
