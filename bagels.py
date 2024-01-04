#!/usr/bin/env python3
import random

NUM_DIGITS = 3 
MAX_GUESSES = 10 #you can increase the number of trials. But that will be too easy

def main():
    print("*****************WELCOME TO BAGELS*********************")
    while True:
        secretNumber = getSecretNumber()
        print('I have a number in mind.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess %{}: '.format(numGuesses))
                guess = input('> ')
                
                clues = getClues(guess, secretNumber)
                print(clues)
                numGuesses += 1
                
                if guess == secretNumber:
                    break #means you are correct
                if numGuesses > MAX_GUESSES:
                    print('You ran out of guesses.')
                    print('The answer was {}.'.format(secretNumber))
        
        print('Do you want to play again?')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNumber():
    numbers = list('0123456789')
    random.shuffle(numbers) 
    
    secretNumber = ''
    for i in range(NUM_DIGITS):
        secretNumber += str(numbers[i])
    return secretNumber

def getClues(guess, secretNumber):
    if guess == secretNumber:
        return 'Bim! YOU ARE A WINNER! YOU GOT IT!'
    
    clues = [] 
    
    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues.append('Fermi')
        elif guess[i] in secretNumber:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' #there are no correct digits at all
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
    