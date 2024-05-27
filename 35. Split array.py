# Program to Split the array and add the first part to the end

array = eval(input("Enter an array: "))

k = int(input("After how many values would you want to split the array? "))


def split(array,k):
    
    part1 = array[:k]
    part2 = array[k:]

    new_array = part2.copy()
    new_array.extend(part1)

    return new_array

result = split(array,k)

print(f"The resultant array is {result}")

