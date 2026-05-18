def prime_number(number):
    
    for number in range(2,(number//2) + 1):
               if number == 1:
                   return True 
         
               if(number % number == 0):
                   return False
     
   
    return True 
number = int(input("Enter a number: "))
print(prime_number(number))
