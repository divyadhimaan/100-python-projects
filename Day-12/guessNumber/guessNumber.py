import random
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def generate_number():
    """Generates a random number between 1 and 100"""
    return random.randint(1,101)

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def make_guess(attempts, number):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            return
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        

def play():
    print(logo)
    print("Welcom to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = generate_number()
    print(f"Pssst, the correct answer is {number}")

    attempts = set_difficulty()
    
    make_guess(attempts, number)

play()

