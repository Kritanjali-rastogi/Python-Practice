# Program to find largest element in an array

array = eval(input("Enter the array type with brackets: "))

def largest(array):
    return max(array)

result = largest(array)

print(f"The largest element in {array} is {result}")
