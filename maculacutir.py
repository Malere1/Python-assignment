principal_amount= float(input("Enter the principal amount : "))
intereat_rate = float(input("Enter the annual interest rate : "))
duration = float(input("Enter hte duration in years : "))


r = (interest_rate / 100) /12

n = (duration * 12)

sum = float(1 + r)
first_result = float(sum ** n)
second_result = first_result * r

third_result = first_result -1

fourth_result = second_result / third_result

monthly_payment = principal_amount * fourth_result

print("Your Monthly Payment is : ", monthly_payment)
