from art import logo, vs
from game_data import data
import random
from replit import clear


def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if user is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display Art
print(logo)
score = 0
game_over = False
account_b = random.choice(data)

# Make the game repeatable
while game_over == False:

    # Make the account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"\n\nCompare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check is user is correct
    ## Get follower counts for each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # CLear screen between rounds
    clear()
    print(logo)

    # Give user feedback on their guess
    ## Score keeping
    if is_correct:
        score += 1
        print(f"Correct. Current score is {score}")
    else:
        game_over = True
        print(f"Wrong. Final score is {score}")




