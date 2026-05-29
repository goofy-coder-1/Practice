import random

Num_digits = 3
Max_guesses = 10

def main():
    print('''Bagels is a number guessing game
          1. Pico means one number is correct but in the wrong position
          2. Fermi means one number is correct and in the right position
          3. Bagels means no number is correct''')
       
    while True:
        secretNum = getSecretNum()
        print("I have thought of a number.")
        print("You have {} guesses to get it right", format(Max_guesses))

        numGuesses = 1
        while numGuesses <= Max_guesses:
            guess = ''
            