# Program to Check if a Number is Odd or Even

print("Let's check if the a number is odd or even")

num = float(input("Enter a number: "))

def check(num):
    if num%2 ==0:
        return "Even"
    else:
        return "Odd"
    
result = check(num)

print(f"{num}: {result} number ")