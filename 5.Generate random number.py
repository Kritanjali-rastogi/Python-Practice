# Program to generate a random number

import random

print("Lets, print a random number between two number")

a= int(input("Enter the lower range: "))
b= int(input("Enter the higher range: "))

def random_number(a,b):
    number = random.randint(a,b)
    return number

result = random_number(a,b)
print(f"Random number between {a} and {b} is {result}")

# Another way:
#random_number = random.randrange(start, stop, step)
