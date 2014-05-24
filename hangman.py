# Hangman
#
# Use a random number generator to pull a value from a pre-loaded
# dictionary. User enters an amount of wrong attempts they have,
# and the user will continue to guess letters until they run out of
# attempts or they guess the word.

import random

def getWords(): # creates dictionary
    
    unix_words = "C:\Documents and Settings\googleuser\My Documents\Downloads\unix-words"
    wordfile = open(unix_words)
    counter = 0
    csdict = dict()
    for word in wordfile:
        word = word.replace('\n', '')
        csdict[word] = counter
        counter += 1
    return csdict
    


def startHangman(wrongAttempts): # calls basic functions to play hangman

    hiddenWord = createWord()
    print "Welcome to hangman!"
    print "I am thinking of a word. Guess the letters in the word!"
    print "You have " + str(wrongAttempts) + " mistakes left. Letters used: none."
    guessedWord = ''
    lettersGuessed = ''

    lengthOfWord = len(hiddenWord)
    # print lengthOfWord          # test
    # print hiddenWord            # test

    while lengthOfWord > 0:
        # print lengthOfWord, guessedWord               # test
        guessedWord += '-'
        lengthOfWord -= 1

    print "Word so far: " + guessedWord
    print
    
    while wrongAttempts > 0 and guessedWord.find('-') >= 0:
        result = askUserForLetter(guessedWord, hiddenWord, lettersGuessed)
        guessedWord = result[0]
        lettersGuessed += result[1] + ' '

        if result[2] == True:
            print "Correct! You have " + str(wrongAttempts) + " left. Letters used: " + lettersGuessed
            print "Word so far: " + guessedWord
        else:
            wrongAttempts -= 1
            print "Wrong! You have " + str(wrongAttempts) + " left. Letters used: " + lettersGuessed
            print "Word so far: " + guessedWord

    if guessedWord.find('-') < 0:
        print "You won!"
    else:
        print "You lost! The word was " + hiddenWord + "."
        print "Better luck next time!"



def createWord(): # creates random word by accessing a generated random number
    
        myDict = getWords()
        endIndex = len(myDict) - 1
        randNum = random.randint(0, endIndex)
        hiddenWord = reverseLookup(myDict, randNum)
        return hiddenWord


def reverseLookup(dictionary, valueToSearch):

    index = 0
    myListOfPossibleWords = ['']
    for eachWord in dictionary:
        if dictionary[eachWord] == valueToSearch:
            myListOfPossibleWords[index] = eachWord
            index += 1
    randomIndexNumber = random.randint(0,len(myListOfPossibleWords) - 1)
    return myListOfPossibleWords[randomIndexNumber]
        


def askUserForLetter(guessedWord, hiddenWord, lettersUsed):
    letterGuessed = raw_input("Next Letter? ")

    return isLetterRight(hiddenWord, guessedWord, letterGuessed, lettersUsed)



def isLetterRight(hiddenWord, guessedWord, letterGuessed, lettersUsed): 
        
    foundLetter = False
    index = 0
    newWord = ''

    letterGuessed = checkLetterValidity(letterGuessed, lettersUsed)
    
    while index < len(hiddenWord):
        if hiddenWord[index] == letterGuessed:
            newWord += letterGuessed
            foundLetter = True
        else:
            newWord += guessedWord[index]
            
        index += 1
        
    return newWord, letterGuessed, foundLetter, lettersUsed



def checkLetterValidity(letterGuessed, lettersUsed):
    validity = False
    while validity == False:
        
        if len(letterGuessed) > 1:
            print "Only one letter!"    
        elif ord(letterGuessed) < ord('a') or ord(letterGuessed) > ord('z'):
            print "This is not a real letter!"
        elif lettersUsed.find(letterGuessed) >= 0:
            print "You've already used this letter!"
        else:
            validity = True

        if validity == False:
            letterGuessed = raw_input("Try again. ")

    return letterGuessed
