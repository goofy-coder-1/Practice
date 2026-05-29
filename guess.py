import random


def difficulty_level():
    while True:
        print("\nWhat difficulty level would you like?")
        print("[A] for normal\n[B] for intermediate\n[C] for hard")
        difficulty = input("Enter difficulty level: ").upper()
        
        match difficulty:
            case 'A':
                max_guess = 10
                bot_number = random.randint(1, 10)
                print(f"The number lies between 1 to 10. You have {max_guess} guesses!")
                return max_guess, bot_number # Hand values over and exit loop
                
            case 'B':
                max_guess = 5
                bot_number = random.randint(1, 50)
                print(f"The number lies between 1 to 50. You have {max_guess} guesses!")
                return max_guess, bot_number
                
            case 'C':
                max_guess = 3
                bot_number = random.randint(1, 100)
                print(f"The number lies between 1 to 100. You have {max_guess} guesses!")
                return max_guess, bot_number
                
            case _:
                print("Invalid choice! Please enter A, B, or C.")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Oops! That's not a valid number. Try again.")

allowed_guesses, target_number = difficulty_level()
guess_count = 0

while guess_count < allowed_guesses:
    current_guess = get_user_guess()
    guess_count += 1

    if current_guess == target_number:
        print(f"You guessed it in {guess_count} tries")
        break
    elif current_guess < target_number:
        print("Too low! Aim higher.")
    else:
        print("Too high! Aim lower.")

    print(f"Guesses remaining: {allowed_guesses - guess_count}\n")
else:
    print(f"Game Over! You ran out of guesses. The number was {target_number}.")