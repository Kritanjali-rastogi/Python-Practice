"""Program to Find Factorial of Number Using Recursion"""

user_input = int(input("Enter a number: "))

def fac_recursive(user_input):
    if user_input<=1:
        return 1
    
    else:
        
        return user_input * fac_recursive(user_input-1)
    
if user_input<=0:
    print("Enter a positive number")
else:
    print(fac_recursive(user_input)) 
        
