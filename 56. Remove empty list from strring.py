# Program to Remove empty List from List

list1 = eval(input("Enter a list: "))

def remove_empty(list1):
    for item in list1:
        if item == []:
            list1.remove(item)

    return list1

result = remove_empty(list1)

print(f"The updated list is {result}")