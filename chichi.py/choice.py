import random

choices = ["Rock", "Paper", "Scissors"]

computer = random.randint(0, 2)
user = int(input("0=Rock, 1=Paper, 2=Scissors: "))

print("Computer:", choices[computer])
print("You:", choices[user])

if computer == user:
    print("Draw")
elif (user == 0 and computer == 2) or \
     (user == 1 and computer == 0) or \
     (user == 2 and computer == 1):
    print("You win")
else:
    print("Computer wins")
