# Program to find smallest number in a list

list1 = eval(input("Enter a list: "))

def largest_num1(list1):
    largest = list1[0]

    for i in list1:
        if i >= largest:
            largest = i
    
    return largest

result1 = largest_num1(list1)
print(f"The largest item in the list is {result1}") 

def largest_num2(list1):
    largest = max(list1)
    return largest

result2  = largest_num2(list1)

print(f"The largest item in the list is {result2}")