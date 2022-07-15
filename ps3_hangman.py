# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    flag = False
    for l in secretWord:
        if l in lettersGuessed:
            flag = True
        else:
            return False
    
    return flag

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    for l in secretWord:
      if l in lettersGuessed:
        guessedWord += l
      else:
        guessedWord += '_ '
    
    return guessedWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = list(string.ascii_lowercase)
    copy = availableLetters[::]
    for l in availableLetters:
      if l in lettersGuessed:
        copy.remove(l)
      
    return ''.join(copy)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")

    numOfGuesses = 8
    lettersGuessed = []

    while not isWordGuessed(secretWord, lettersGuessed):
      print("You have " + str(numOfGuesses) + " guesses left.")
      print("Available Letters: " + getAvailableLetters(lettersGuessed))
      userInput = input("Please guess a letter: ")

      if userInput in lettersGuessed:
        print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
      elif userInput in secretWord:
        lettersGuessed += userInput
        print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
      elif userInput not in secretWord:
        lettersGuessed += userInput
        numOfGuesses -= 1
        print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
      
      print("-----------")

      if numOfGuesses == 0:
        print("Sorry, you ran out of guesses. The word was " + secretWord)
        break

    if isWordGuessed(secretWord, lettersGuessed):
      print("Congratulations, you won!")
         
# Driver Code.
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
