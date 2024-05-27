# Program to print odd numbers in a List

list1 = eval(input("Enter a list: "))

def odd_numbers(list1):
    result = []

    for num in list1:
        if num%2!=0:
            result.append(num)

    return result


a = odd_numbers(list1)
print(f"The odd numbers in {list1} are {a}")