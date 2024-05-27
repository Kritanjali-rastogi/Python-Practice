# Program to Count occurrences of an element in a list

list1 = eval(input("Enter a list: "))

element = input("Enter a element whose occurance you want to ckeck: ")

def occurance_check(list1,element):
    A = list1.count(element)
    return A

result = occurance_check(list1,element)

print(f"{element} occurs {result} times in the list")