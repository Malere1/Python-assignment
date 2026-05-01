import random

num = random.randint(0, 9)

if num % 2 != 0:
    num += 1

print("Result:", num)
