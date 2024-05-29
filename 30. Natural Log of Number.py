# Program to calculate the natural logarithm of any number


num = float(input("Enter the number whose log you want to find: "))
            
import math

def calculate_log(num):
    
    if num <=0:
        return None
    else:
        L = math.log(num)
        return L

result = calculate_log(num)

if result == None:
    print("Error: Natural logarithm is undefined for non-positive numbers.")
else:
    print(f"The Log of {num} is {result}")