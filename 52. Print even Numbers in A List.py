# Program to print even numbers in a list

list1 = eval(input("Enter a list: "))

def even_numbers(list1):
    result = []

    for num in list1:
        if num%2==0:
            result.append(num)

    return result


a = even_numbers(list1)
print(f"The even numbers in {list1} are {a}")
