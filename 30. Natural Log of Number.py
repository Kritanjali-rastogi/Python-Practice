# Program to calculate the natural logarithm of any number


num = float(input("Enter the number whose log you want to find: "))
            
import math

def calculate_log(num):
    L = math.log(num)
    return L

result = calculate_log(num)

print(f"The Log of {num} is {result}")