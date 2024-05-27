# Program to  Multiply all numbers in the list

list1 = eval(input("Enter a list: "))

def list_product(list1):
    total = 1
    for item in list1:
        total*=item

    return total

result1  = list_product(list1)

print(f"Product of the entered list is {result1}")


# Anothr Simple way (using built in sum function)

import math
def list_product1(list1):
    total = math.prod(list1)
    return total

result2  = list_product1(list1)
print(f"Product of the entered list is {result2}")
