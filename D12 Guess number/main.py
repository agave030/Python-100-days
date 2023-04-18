#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

def times():
    """Choose the difficulty. easy = 10 times, hard = 5 times"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return 10
    else:
        return 5

def compare(guess, answer):
    """compare the guess and answer"""
    if guess > answer:
        print("Too high.\nGuess again.")
    elif guess < answer:
        print("Too low.\nGuess again")

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")


answer = randint(1, 100)
print(f"Pssst, the correct answer is {answer}")

keep_guessing = True
difficulty = times()
while keep_guessing:
    print(f"You have {difficulty} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
        keep_guessing = False
        print(f"You got it! The answer was {answer}.")
    else:
        difficulty -= 1
        if difficulty == 0:
            print("You've run out of guesses, you lose.")
            keep_guessing = False
        else:
            compare(guess, answer)
