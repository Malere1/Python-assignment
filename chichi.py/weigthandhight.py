weight = float(input("Enter weight: "))

if weight <= 1:
    cost = 3.5
elif weight <= 3:
    cost = 5.5
elif weight <= 10:
    cost = 8.5
elif weight <= 20:
    cost = 10.5
else:
    cost = "Cannot ship"

print("Cost:", cost)
