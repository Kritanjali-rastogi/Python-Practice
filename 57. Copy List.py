# Program to Cloning or Copying a list


list1 = eval(input("Enter a list: "))

def list_copy(list1):
    list2 = list1.copy()
    A = id(list1)
    B = id(list2)
    return A, B

a = list_copy(list1)

print(f"Memory of lists: {a}")