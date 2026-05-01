import random
days = ["Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"]

num = random.randint(1, 7)
print("Number:", num)
print("Day:", days[num - 1])
