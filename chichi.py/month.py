month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

days_in_month = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]

if month == 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    print("29 days")
else:
    print(days_in_month[month - 1], "days")
