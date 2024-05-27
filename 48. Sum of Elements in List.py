# Program to find sum of elements in list

list1 = eval(input("Enter a list: "))

def list_sum(list1):
    total = 0
    for item in list1:
        total+=item

    return total

result1  = list_sum(list1)

print(f"Sum of the entered list is {result1}")


# Anothr Simple way (using built in sum function)

def list_sum1(list1):
    total = sum(list1)
    return total

result2  = list_sum1(list1)
print(f"Sum of the entered list is {result2}")