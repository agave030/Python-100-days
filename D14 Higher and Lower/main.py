import art
from game_data import data
from random import choice


def random_choice():
    """Return a random choice of data"""
    return choice(data)


def print_statement(a, b):
    """Print function for compare A and against B"""
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")
    # print(a['follower_count'], b['follower_count'])


def compare(a_followers, b_followers):
    """Compare the follower_counts"""
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if (a_followers > b_followers and guess == 'a') or (a_followers < b_followers and guess == 'b'):
            return True
        else:
            return False


# Initialization
print(art.logo)
score = 0
keep_playing = True

# For avoiding A and B are the same
A = random_choice()
B = random_choice()
if A == B:
    B = random_choice()

# Use keep_playing as the flag and print the first statement
while keep_playing:
    print_statement(A, B)
    # Use compare function as the flag.
    # If the user guesses right, it'll return True and keep going the while loop.
    # Also, add the score and replace A with B and generate a new B
    while compare(A['follower_count'], B['follower_count']):
        score += 1
        A = B
        B = random_choice()
        print(f"You're right. Current score: {score}")
        print_statement(A, B)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        keep_playing = False
