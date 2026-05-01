income = float(input("Enter income: "))

if income <= 8350:
    tax = income * 0.10
elif income <= 33950:
    tax = 835 + (income - 8350) * 0.15
else:
    tax = 4677.5 + (income - 33950) * 0.25

print("Tax =", tax)
