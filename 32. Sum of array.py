# Program to find sum of array

array = eval(input("Enter the array type with brackets: "))

def sum_return(array):
    sum = 0
    for i in array:
        sum +=i

    return sum

result = sum_return(array)

print(f"The sum of elements in {array} is {result}")



