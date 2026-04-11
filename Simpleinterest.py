P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
T = float(input("Enter time: "))

SI = (P * R * T) / 100
A = P + SI

print("Simple Interest:", SI)
print("Total Amount:", A)
