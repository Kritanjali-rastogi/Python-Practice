# Program to find smallest number in a list

list1 = eval(input("Enter a list: "))

def smallest_item(list1):
    smallest = list1[0]
    for item in list1:
        if item <= smallest:
            smallest = item

    return smallest

result1  = smallest_item(list1)

print(f"The smallest item in the list is {result1}")


def smallest_item1(list1):
    smallest = min(list1)
    return smallest

result2  = smallest_item1(list1)

print(f"The smallest item in the list is {result2}")
