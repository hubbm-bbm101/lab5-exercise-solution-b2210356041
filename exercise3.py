import random

def guess(random_number):
    user_guess = int(input())

    if user_guess < random_number:
        print("Increase your guess.")
        guess(random_number)
    elif user_guess > random_number:
        print("Decrease your guess.")
        guess(random_number)
    else:
        print("Success!")

random_number = random.randint(0, 100)
guess(random_number)