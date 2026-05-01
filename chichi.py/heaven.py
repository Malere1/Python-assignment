import random

secret = random.randint(1, 9)
guess = int(input("Guess number (1-9): "))

if guess == secret:
    print("Correct!")
else:
    print("Wrong. Number was", secret)
