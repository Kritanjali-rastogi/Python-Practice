# program to swap two variables

print("Let's swap two variable")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def swap(a,b):
    return b,a

result = swap(a,b)

print(f"The swap of {a},{b} is {result}")
    
    
